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
from scrapers import airalo, airhelp, autoeurope, booking, booking_cee, booking_es, centauro, civitatis, economybookings, ekta, expedia, getyourguide, getrentacar, gocity, hotelscom, hotelscom_es, iberostar, kiwicom, kiwitaxi, kkday, klook, tiqets, travelpayouts, wegotrip

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
            "actividad": "🎯", "traslado": "🚕", "coche": "🚗", "vuelo": "✈️"}.get(tipo, "🎯")


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
    "booking_es":       "Booking.com",
    "centauro":         "Centauro",
    "hotelscom_es":     "Hotels.com",
    "kiwitaxi":         "Kiwitaxi",
    "getrentacar":      "GetRentacar",
    "kiwicom":          "Kiwi.com",
    "wegotrip":         "WeGoTrip",
    "kkday":            "KKday",
    "gocity":           "Go City",
    "airhelp":          "AirHelp",
    "airalo":           "Airalo",
    "ekta":             "EKTA",
}


def publish_deal(deal: dict) -> bool:
    deal_id  = deal["id"]
    deal_url = f"{config.BASE_URL}/oferta/{deal_id}"
    emoji    = _tipo_emoji(deal.get("tipo", "hotel"))
    src      = SOURCE_LABELS.get(deal.get("source"), "GangaViaje")
    tipo     = deal.get("tipo", "hotel")
    unidad   = {"actividad": "persona", "coche": "día", "vuelo": "trayecto"}.get(tipo, "noche")

    lines = [f"🏷️ <b>OFERTA DETECTADA</b>\n"]
    lines.append(f"{emoji} <b>{deal['title']}</b>")
    if deal.get("location"):
        lines.append(f"📍 {deal['location']}\n")
    else:
        lines.append("")

    if deal.get("original_price") and deal["original_price"] > deal["sale_price"]:
        saving = deal["original_price"] - deal["sale_price"]
        lines.append(f"<s>Antes: €{deal['original_price']:.0f}</s>")
        lines.append(f"💥 <b>€{deal['sale_price']:.0f}</b> por {unidad}")
        lines.append(f"✅ Ahorras <b>€{saving:.0f}</b> · {deal['discount_pct']}% descuento\n")
    else:
        lines.append(f"💥 <b>Desde €{deal['sale_price']:.0f}</b> por {unidad}\n")

    if deal.get("rating") and deal["rating"] > 0:
        label = "Excepcional" if deal["rating"] >= 9 else "Muy bueno" if deal["rating"] >= 8 else "Bueno"
        lines.append(f"⭐ {deal['rating']:.1f}/10 · {label}")

    lines.append(f"\n🔗 {src}  |  ⏰ <i>Oferta limitada</i>")
    text = "\n".join(lines)

    buttons = json.dumps({
        "inline_keyboard": [
            [{"text": f"🎫 Ver oferta completa", "url": deal_url}],
            [{"text": f"➡️ Reservar en {src}", "url": deal["affiliate_url"]}],
        ]
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
        sources.append((kiwitaxi, "Kiwitaxi"))
        sources.append((getrentacar, "GetRentacar"))
        sources.append((kiwicom, "Kiwi.com"))
        sources.append((wegotrip, "WeGoTrip"))
        sources.append((kkday, "KKday"))
        sources.append((gocity, "Go City"))
        sources.append((airhelp, "AirHelp"))
        sources.append((airalo, "Airalo"))
        sources.append((ekta, "EKTA"))
    if config.CJ_WEBSITE_ID:
        sources.append((iberostar, "Iberostar"))
        sources.append((expedia, "Expedia"))
        sources.append((booking_cee, "Booking.com CEE"))
        sources.append((booking_es, "Booking.com ES"))
        sources.append((centauro, "Centauro"))
        sources.append((hotelscom_es, "Hotels.com ES"))
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
            refreshed = 0
            for d in deals:
                if database.deal_exists(d["affiliate_url"]):
                    database.refresh_deal(d["affiliate_url"], d)
                    refreshed += 1
                else:
                    database.add_deal(d)
                    added += 1
            log.info(f"{name}: {len(deals)} scrapeados, {added} nuevos, {refreshed} actualizados")
            new_total += added
        except Exception as e:
            log.error(f"{name} scraper error: {e}")

    # 3. Publicar en Telegram los pendientes
    if config.TELEGRAM_BOT_TOKEN:
        pending = database.get_unpublished_deals()
        published = 0
        for deal in pending[:10]:  # máx 10 por ciclo
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
