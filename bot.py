"""
GangaViaje — Bot automático
Scrape Booking + Civitatis + GetYourGuide + TravelPayouts, publica en Telegram, expira deals viejos.
Se ejecuta vía Vercel Cron (endpoint /api/cron) en producción, o en bucle local con main().
"""

import json
import logging
import os
import ssl
import time
import urllib.parse
import urllib.request

import certifi

import config
import database
import pinterest as pinterest_publisher
from scrapers import autoeurope, booking, booking_cee, centauro, civitatis, economybookings, expedia, getyourguide, hotelscom, iberostar, klook, tiqets, travelpayouts

_handlers = [logging.StreamHandler()]
if os.getenv("VERCEL") != "1":
    _handlers.append(logging.FileHandler("bot.log"))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=_handlers,
)
log = logging.getLogger(__name__)


# ── Telegram ──────────────────────────────────────────────────────────────────

def _tg(method: str, payload: dict) -> bool:
    if not config.TELEGRAM_BOT_TOKEN:
        return False
    ctx  = ssl.create_default_context(cafile=certifi.where())
    url  = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/{method}"
    data = json.dumps(payload).encode("utf-8")
    req  = urllib.request.Request(url, data=data, method="POST",
                                  headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            return r.status == 200
    except Exception as e:
        log.warning(f"Telegram {method} error: {e}")
        return False


def _tipo_emoji(tipo: str) -> str:
    return {"hotel": "🏨", "apartamento": "🏠", "villa": "🏡",
            "actividad": "🎯", "coche": "🚗", "vuelo": "✈️"}.get(tipo, "🎯")


SOURCE_LABELS = {
    "booking":          "Booking",
    "civitatis":        "Civitatis",
    "getyourguide":     "GetYourGuide",
    "travelpayouts":    "Aviasales",
    "klook":            "Klook",
    "economybookings":  "Economybookings",
    "iberostar":        "Iberostar",
    "hotelscom":        "Hotels.com",
    "expedia":          "Expedia",
    "tiqets":           "Tiqets",
    "autoeurope":       "AutoEurope",
    "booking_cee":      "Booking.com",
    "centauro":         "Centauro",
}


def publish_deal(deal: dict) -> bool:
    deal_id = deal["id"]
    deal_url = f"{config.BASE_URL}/oferta/{deal_id}"
    emoji    = _tipo_emoji(deal.get("tipo", "hotel"))
    src      = SOURCE_LABELS.get(deal.get("source"), "GangaViaje")

    text = (
        f"{emoji} <b>{deal['title']}</b>\n"
        f"📍 {deal.get('location', '')}\n\n"
    )
    if deal.get("original_price") and deal["original_price"] > deal["sale_price"]:
        text += (
            f"<s>€{deal['original_price']:.0f}</s>  "
            f"<b>€{deal['sale_price']:.0f}</b>  "
            f"🔥 -{deal['discount_pct']}%\n\n"
        )
    else:
        text += f"💰 Desde <b>€{deal['sale_price']:.0f}</b>\n\n"

    if deal.get("rating") and deal["rating"] > 0:
        text += f"⭐ {deal['rating']:.1f}/10\n\n"

    text += f"🔗 Disponible en {src}"

    buttons = json.dumps({
        "inline_keyboard": [[
            {"text": "🌐 Ver oferta", "url": deal_url},
            {"text": "👉 Reservar", "url": deal["affiliate_url"]},
        ]]
    })

    payload = {
        "chat_id":      config.TELEGRAM_CHANNEL_ID,
        "parse_mode":   "HTML",
        "reply_markup": buttons,
    }

    if deal.get("image_url"):
        ok = _tg("sendPhoto", {**payload, "photo": deal["image_url"], "caption": text})
        if not ok:
            ok = _tg("sendMessage", {**payload, "text": text})
    else:
        ok = _tg("sendMessage", {**payload, "text": text})

    if ok:
        database.mark_published_telegram(deal_id)
        log.info(f"Telegram publicado: deal {deal_id} — {deal['title'][:50]}")
    return ok


# ── Ciclo principal ────────────────────────────────────────────────────────────

def run_once():
    log.info("=== GangaViaje bot — iniciando ciclo ===")

    # 1. Expirar deals viejos
    database.deactivate_old_deals(config.DEAL_EXPIRY_HOURS)

    # 2. Scrape fuentes — solo las que generan comisión real (afiliado confirmado)
    sources = [(travelpayouts, "TravelPayouts")]
    if config.TRAVELPAYOUTS_TOKEN and config.TRAVELPAYOUTS_TRS:
        sources.append((klook, "Klook"))
        sources.append((economybookings, "Economybookings"))
        sources.append((tiqets, "Tiqets"))
        sources.append((autoeurope, "AutoEurope"))
    if config.CJ_WEBSITE_ID:
        sources.append((iberostar, "Iberostar"))
        sources.append((expedia, "Expedia"))
        sources.append((booking_cee, "Booking.com CEE"))
        sources.append((centauro, "Centauro"))
    if config.CJ_PERSONAL_ACCESS_TOKEN and config.CJ_COMPANY_ID and config.CJ_WEBSITE_ID:
        sources.append((hotelscom, "Hotels.com"))
    if config.BOOKING_AFFILIATE_ID_CONFIRMED:
        sources.append((booking, "Booking"))
    if config.CIVITATIS_AFFILIATE_ID:
        sources.append((civitatis, "Civitatis"))
    if config.GETYOURGUIDE_PARTNER_ID:
        sources.append((getyourguide, "GetYourGuide"))

    new_total = 0
    for scraper, name in sources:
        try:
            deals = scraper.fetch_deals(
                min_discount=config.MIN_DISCOUNT_PCT,
                max_results=config.MAX_DEALS_PER_RUN,
            )
            added = 0
            for d in deals:
                if not database.deal_exists(d["affiliate_url"]):
                    database.add_deal(d)
                    added += 1
            log.info(f"{name}: {len(deals)} scrapeados, {added} nuevos")
            new_total += added
        except Exception as e:
            log.error(f"{name} scraper error: {e}")

    # 3. Publicar en Telegram los pendientes
    if config.TELEGRAM_BOT_TOKEN:
        pending = database.get_unpublished_deals()
        published = 0
        for deal in pending[:5]:  # máx 5 por ciclo para no saturar el canal
            if publish_deal(deal):
                published += 1
                time.sleep(2)  # pausa entre mensajes
        log.info(f"Telegram: {published} deals publicados")
    else:
        log.info("Telegram: sin token configurado, omitiendo publicación")

    # 4. Publicar en Pinterest los deals nuevos (máx 3 por ciclo)
    if config.PINTEREST_ACCESS_TOKEN:
        pending_pins = database.get_unpublished_deals()
        pinned = 0
        for deal in pending_pins[:3]:
            if pinterest_publisher.publish_pin(deal):
                pinned += 1
                time.sleep(3)
        log.info(f"Pinterest: {pinned} pins publicados")
    else:
        log.info("Pinterest: sin token configurado, omitiendo")

    stats = database.get_stats()
    log.info(f"BD: {stats['total']} deals activos, {stats['today']} de hoy")
    log.info("=== Ciclo completado ===")


def main():
    database.init_db()
    log.info(f"GangaViaje bot arrancado — intervalo {config.BOT_INTERVAL_SEC}s")

    while True:
        try:
            run_once()
        except Exception as e:
            log.error(f"Error en ciclo: {e}")
        time.sleep(config.BOT_INTERVAL_SEC)


if __name__ == "__main__":
    main()
