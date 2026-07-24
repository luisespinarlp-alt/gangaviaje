"""
GangaViaje — Newsletter semanal vía Resend.
Añade suscriptores al segmento de Resend al apuntarse (add_contact) y
envía el resumen semanal de las mejores ofertas (send_weekly).
"""

import json
import logging
import ssl
import urllib.error
import urllib.request

import certifi

import config
import database

log = logging.getLogger(__name__)

_BASE = "https://api.resend.com"


def _req(method: str, path: str, payload: dict) -> dict | None:
    if not config.RESEND_API_KEY:
        return None
    ctx = ssl.create_default_context(cafile=certifi.where())
    req = urllib.request.Request(
        f"{_BASE}{path}", data=json.dumps(payload).encode(), method=method,
        headers={
            "Authorization": f"Bearer {config.RESEND_API_KEY}",
            "Content-Type": "application/json",
            # Sin esto Cloudflare bloquea el User-Agent por defecto de urllib con 403.
            "User-Agent": "gangaviaje-bot/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        log.warning(f"Resend {method} {path} → {e.code}: {e.read().decode()[:200]}")
        return None
    except Exception as e:
        log.warning(f"Resend {method} {path} error: {e}")
        return None


def add_contact(email: str) -> bool:
    """Añade un suscriptor al segmento de la newsletter en Resend. No falla el signup si Resend falla."""
    if not (config.RESEND_API_KEY and config.RESEND_SEGMENT_ID):
        return False
    resp = _req("POST", "/contacts", {
        "email": email,
        "unsubscribed": False,
        "segments": [{"id": config.RESEND_SEGMENT_ID}],
    })
    return bool(resp and resp.get("id"))


def _top_deals(limit: int = 8, n_live: int = 3) -> list[dict]:
    """Combina ofertas de precio en vivo (TravelPayouts, discount_pct=0 por diseño así que
    nunca aparecerían solo ordenando por descuento) con las mejores ofertas curadas por %."""
    live = database.get_deals(category=None, limit=200)
    live = [d for d in live if d.get("source") == "travelpayouts"][:n_live]
    live_ids = {d["id"] for d in live}

    curated_pool = database.get_deals(limit=200)
    curated: list[dict] = []
    per_source: dict[str, int] = {}
    for d in curated_pool:
        if d["id"] in live_ids or len(curated) >= limit - len(live):
            continue
        if per_source.get(d["source"], 0) >= 2:
            continue
        curated.append(d)
        per_source[d["source"]] = per_source.get(d["source"], 0) + 1

    return live + curated


def _deal_row(d: dict) -> str:
    url = f"{config.BASE_URL}/oferta/{d['id']}"
    precio_unidad = config.PRECIO_UNIDAD.get(d.get("tipo"), "")
    descuento = f'<span style="background:#fdecea;color:#c0392b;font-weight:700;font-size:12px;padding:3px 8px;border-radius:5px;margin-left:8px;">-{d["discount_pct"]}%</span>' if d.get("discount_pct") else ""
    img = d.get("image_url") or ""
    return f"""
    <tr>
      <td style="padding:0 0 16px 0;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FAF0E8;border-radius:12px;overflow:hidden;">
          <tr>
            <td width="120" style="padding:0;">
              <a href="{url}"><img src="{img}" width="120" height="120" style="display:block;object-fit:cover;width:120px;height:120px;" alt=""></a>
            </td>
            <td style="padding:14px 16px;vertical-align:top;">
              <a href="{url}" style="color:#1C1610;font-weight:700;font-size:15px;text-decoration:none;line-height:1.35;">{d['title']}</a><br>
              <span style="color:#888;font-size:12px;">📍 {d.get('location','')}</span><br>
              <span style="color:#C85A2A;font-weight:800;font-size:18px;">€{d['sale_price']:.0f}</span>
              <span style="color:#999;font-size:12px;">/{precio_unidad}</span>{descuento}
            </td>
          </tr>
        </table>
      </td>
    </tr>"""


def _build_html(deals: list[dict]) -> str:
    rows = "".join(_deal_row(d) for d in deals)
    return f"""<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;background:#F9F7F3;font-family:-apple-system,Helvetica,Arial,sans-serif;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F9F7F3;padding:24px 0;">
    <tr><td align="center">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">
        <tr><td style="padding:8px 8px 24px;text-align:center;">
          <span style="font-size:22px;font-weight:800;color:#1C1610;">Ganga<span style="color:#C85A2A;">Viaje</span></span>
        </td></tr>
        <tr><td style="padding:0 8px 20px;text-align:center;">
          <h1 style="font-size:20px;color:#1C1610;margin:0 0 6px;">🔥 Los chollos de esta semana</h1>
          <p style="color:#777;font-size:14px;margin:0;">Seleccionados a mano entre cientos de ofertas activas</p>
        </td></tr>
        <tr><td style="padding:0 8px;">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0">{rows}</table>
        </td></tr>
        <tr><td style="padding:20px 8px 8px;text-align:center;">
          <a href="{config.BASE_URL}/ofertas/vuelos" style="display:inline-block;background:#C85A2A;color:white;font-weight:700;font-size:14px;text-decoration:none;padding:12px 28px;border-radius:8px;">Ver todas las ofertas →</a>
        </td></tr>
        <tr><td style="padding:24px 8px 0;text-align:center;color:#aaa;font-size:11px;">
          <p>Recibes esto porque te suscribiste en gangaviaje.es.<br>
          {{{{{{RESEND_UNSUBSCRIBE_URL}}}}}}</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>"""


def send_weekly() -> dict:
    if not (config.RESEND_API_KEY and config.RESEND_SEGMENT_ID):
        log.info("Newsletter: sin RESEND_API_KEY/RESEND_SEGMENT_ID, omitiendo")
        return {"sent": False, "reason": "no config"}

    deals = _top_deals()
    if not deals:
        log.info("Newsletter: sin ofertas activas, omitiendo envío")
        return {"sent": False, "reason": "no deals"}

    html = _build_html(deals)
    resp = _req("POST", "/broadcasts", {
        "segment_id": config.RESEND_SEGMENT_ID,
        "from": config.RESEND_FROM,
        "subject": f"🔥 {len(deals)} chollos de viaje seleccionados esta semana",
        "html": html,
        "send": True,
    })
    if resp and resp.get("id"):
        log.info(f"Newsletter: broadcast enviado {resp['id']} con {len(deals)} ofertas")
        return {"sent": True, "broadcast_id": resp["id"], "deals": len(deals)}
    log.warning("Newsletter: fallo al crear/enviar el broadcast")
    return {"sent": False, "reason": "resend error"}
