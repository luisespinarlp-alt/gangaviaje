"""
Hotels.com (global) scraper para GangaViaje, vía la Product Search API (GraphQL) de CJ Affiliate.
Programa "Hotels.com" (advertiser 1702763, distinto de "Hotels.com Spain & Portugal") tiene un
feed de cientos de miles de hoteles reales con comisión, incluyendo cadenas como Iberostar.

Solo genera deals cuando CJ aprueba la solicitud al programa: hasta entonces, la API devuelve
linkCode=null y este scraper no añade nada (no se publican ofertas sin comisión confirmada).
"""

import json
import logging
import ssl
import urllib.request

import certifi

import config

log = logging.getLogger(__name__)

_GRAPHQL_URL = "https://ads.api.cj.com/query"
_ADVERTISER_ID = "1702763"  # Hotels.com (global)

# Destinos españoles populares -> (término de búsqueda, categoría del sitio)
_DESTINOS = [
    ("Madrid hotel",    "Madrid",              "ciudad"),
    ("Barcelona hotel",  "Barcelona",          "ciudad"),
    ("Mallorca hotel",   "Mallorca",           "playa"),
    ("Tenerife hotel",   "Tenerife",           "playa"),
    ("Canarias hotel",   "Islas Canarias",     "playa"),
    ("Ibiza hotel",      "Ibiza",              "playa"),
    ("Malaga hotel",     "Málaga",             "playa"),
    ("Sevilla hotel",    "Sevilla",            "ciudad"),
]


def _graphql(query: str) -> dict:
    body = json.dumps({"query": query}).encode("utf-8")
    req = urllib.request.Request(
        _GRAPHQL_URL,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {config.CJ_PERSONAL_ACCESS_TOKEN}",
            "Content-Type": "application/json",
        },
    )
    ctx = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(req, timeout=15, context=ctx) as r:
        return json.loads(r.read().decode("utf-8"))


def _search(keywords: str, limit: int = 6) -> list[dict]:
    query = (
        '{ products(companyId: "%s", partnerIds: "%s", keywords: "%s", limit: %d) '
        '{ resultList { id title description imageLink price { amount currency } '
        'discountPercentage linkCode(pid: "%s") { clickUrl } } } }'
    ) % (config.CJ_COMPANY_ID, _ADVERTISER_ID, keywords, limit, config.CJ_WEBSITE_ID)

    data = _graphql(query)
    if "errors" in data:
        log.warning(f"Hotels.com GraphQL error ({keywords}): {data['errors']}")
        return []
    return data.get("data", {}).get("products", {}).get("resultList", []) or []


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    if not (config.CJ_PERSONAL_ACCESS_TOKEN and config.CJ_COMPANY_ID and config.CJ_WEBSITE_ID):
        log.info("Hotels.com: sin credenciales de CJ Product Search API, omitiendo")
        return []

    deals = []
    per_destino = max(1, max_results // len(_DESTINOS))

    for keywords, location, category in _DESTINOS:
        if len(deals) >= max_results:
            break
        try:
            products = _search(keywords, limit=per_destino + 4)
        except Exception as e:
            log.warning(f"Hotels.com: error buscando '{keywords}': {e}")
            continue

        added_aqui = 0
        for p in products:
            if added_aqui >= per_destino or len(deals) >= max_results:
                break

            link_code = p.get("linkCode")
            if not link_code or not link_code.get("clickUrl"):
                # Sin enlace de afiliado con comisión confirmada -> no se publica.
                continue

            price = p.get("price") or {}
            amount = float(price.get("amount") or 0)
            if amount <= 0:
                continue

            discount = p.get("discountPercentage") or 0
            if discount < min_discount and min_discount > 0:
                # Mantenemos los hoteles sin descuento explícito solo si no se exige mínimo.
                continue

            sale_price = round(amount, 2)
            original_price = round(sale_price / (1 - discount / 100), 2) if discount else None

            deals.append({
                "title":          p.get("title") or location,
                "description":    (p.get("description") or "")[:300],
                "location":       location,
                "original_price": original_price,
                "sale_price":     sale_price,
                "discount_pct":   int(discount),
                "image_url":      p.get("imageLink") or "",
                "affiliate_url":  link_code["clickUrl"],
                "source":         "hotelscom",
                "category":       category,
                "tipo":           "hotel",
                "rating":         0.0,
                "reviews_count":  0,
            })
            added_aqui += 1

    log.info(f"Hotels.com: {len(deals)} hoteles con enlace de afiliado real")
    return deals
