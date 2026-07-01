"""
GangaViaje — Publicador de Pins en Pinterest.
Publica un Pin por cada deal nuevo en el tablero correspondiente según tipo.
Requiere PINTEREST_ACCESS_TOKEN con scope pins:write (disponible tras aprobación de trial).
"""

import json
import logging
import ssl
import urllib.request

import certifi
import config

log = logging.getLogger(__name__)

_BASE = "https://api.pinterest.com/v5"


def _req(method: str, path: str, payload: dict | None = None) -> dict | None:
    if not config.PINTEREST_ACCESS_TOKEN:
        return None
    ctx = ssl.create_default_context(cafile=certifi.where())
    url = f"{_BASE}{path}"
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {config.PINTEREST_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        log.warning(f"Pinterest {method} {path} → {e.code}: {body[:200]}")
        return None
    except Exception as e:
        log.warning(f"Pinterest {method} {path} error: {e}")
        return None


def get_board_ids() -> dict:
    """Devuelve {nombre_tablero: board_id} para todos los tableros de la cuenta."""
    resp = _req("GET", "/boards?page_size=25")
    if not resp:
        return {}
    return {b["name"]: b["id"] for b in resp.get("items", [])}


def publish_pin(deal: dict) -> bool:
    """
    Publica un pin en el tablero correspondiente al tipo del deal.
    Devuelve True si el pin se creó correctamente.
    """
    if not config.PINTEREST_ACCESS_TOKEN:
        log.info("Pinterest: sin token configurado, omitiendo")
        return False

    tipo = deal.get("tipo", "actividad")
    board_id = config.PINTEREST_BOARD_IDS.get(tipo) or config.PINTEREST_BOARD_OFERTAS
    if not board_id:
        log.warning(f"Pinterest: sin board_id para tipo '{tipo}', omitiendo pin")
        return False

    deal_url = f"{config.BASE_URL}/oferta/{deal['id']}"
    descuento = f" (-{deal['discount_pct']}%)" if deal.get("discount_pct") else ""
    precio = f"Desde €{deal['sale_price']:.0f}{descuento}"

    description = (
        f"{precio} · {deal.get('location', '')}\n"
        f"{deal.get('description', '')[:400]}\n\n"
        f"🔗 Ver oferta en GangaViaje"
    ).strip()

    payload = {
        "board_id": board_id,
        "title": deal["title"][:100],
        "description": description,
        "link": deal_url,
    }

    if deal.get("image_url"):
        payload["media_source"] = {
            "source_type": "image_url",
            "url": deal["image_url"],
        }

    resp = _req("POST", "/pins", payload)
    if resp and resp.get("id"):
        log.info(f"Pinterest pin creado: {resp['id']} — {deal['title'][:50]}")
        return True
    return False
