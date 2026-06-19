"""
Helper compartido: convierte URLs normales de marcas asociadas en TravelPayouts
en enlaces de afiliado reales y comisionados, vía la API links/v1/create.
https://support.travelpayouts.com/hc/en-us/articles/25289759198226
"""

import json
import logging
import ssl
import urllib.request

import certifi

import config

log = logging.getLogger(__name__)

_API_URL = "https://api.travelpayouts.com/links/v1/create"


def to_affiliate_urls(urls: list[str]) -> dict[str, str]:
    """Convierte una lista de URLs en enlaces de afiliado reales. Devuelve {url_original: url_afiliado}.
    Si la API falla o faltan credenciales, devuelve un dict vacío (sin comisión garantizada -> no usar)."""
    if not (config.TRAVELPAYOUTS_TOKEN and config.TRAVELPAYOUTS_MARKER and config.TRAVELPAYOUTS_TRS):
        return {}

    result: dict[str, str] = {}
    ctx = ssl.create_default_context(cafile=certifi.where())

    # Máximo 10 links por request según la documentación de la API
    for i in range(0, len(urls), 10):
        batch = urls[i:i + 10]
        body = json.dumps({
            "trs":     int(config.TRAVELPAYOUTS_TRS),
            "marker":  int(config.TRAVELPAYOUTS_MARKER),
            "shorten": False,
            "links":   [{"url": u} for u in batch],
        }).encode("utf-8")

        req = urllib.request.Request(
            _API_URL, data=body, method="POST",
            headers={
                "Content-Type":    "application/json",
                "X-Access-Token":  config.TRAVELPAYOUTS_TOKEN,
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
                data = json.loads(r.read().decode("utf-8"))
        except Exception as e:
            log.warning(f"tp_links API error: {e}")
            continue

        for item in data.get("result", {}).get("links", []):
            if item.get("code") != "success":
                log.warning(f"tp_links: link no convertido ({item.get('url')}): {item.get('message')}")
                continue
            partner_url = item.get("partner_url")
            if partner_url:
                result[item.get("url")] = partner_url

    return result
