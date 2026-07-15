"""
AirHelp scraper para GangaViaje.
Reclamaciones por vuelos retrasados/cancelados. Comisión 15–16.6% vía TravelPayouts.
El servicio es gratuito para el pasajero — AirHelp cobra solo si gana la reclamación.
"""

import logging
from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_DEALS = [
    {
        "title":       "Reclama hasta 600€ por tu vuelo retrasado o cancelado",
        "description": "Si tu vuelo llegó tarde más de 3 horas, fue cancelado o te denegaron el embarque, tienes derecho a hasta 600€ de compensación. AirHelp gestiona la reclamación gratis — solo cobran si ganan.",
        "location":    "Todo el mundo",
        "sale_price":  0.0,
        "image_url":   "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.airhelp.com/es/",
        "category":    "internacional",
        "tipo":        "vuelo",
        "discount_pct": 0,
        "rating":      8.9,
        "reviews_count": 183000,
    },
    {
        "title":       "Compensación por vuelo cancelado — hasta 600€",
        "description": "Vuelo cancelado con menos de 14 días de antelación? Tienes derecho a compensación según el Reglamento CE 261/2004. AirHelp comprueba tu caso gratis en menos de 3 minutos.",
        "location":    "Europa",
        "sale_price":  0.0,
        "image_url":   "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.airhelp.com/es/cancelacion-vuelo/",
        "category":    "internacional",
        "tipo":        "vuelo",
        "discount_pct": 0,
        "rating":      8.9,
        "reviews_count": 183000,
    },
    {
        "title":       "Retraso de vuelo — comprueba si tienes derecho a 250–600€",
        "description": "Retraso de más de 3 horas en tu llegada? La ley europea te protege. AirHelp analiza tu caso, negocia con la aerolínea y te paga si gana. Proceso 100% online.",
        "location":    "Europa",
        "sale_price":  0.0,
        "image_url":   "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.airhelp.com/es/retraso-vuelo/",
        "category":    "internacional",
        "tipo":        "vuelo",
        "discount_pct": 0,
        "rating":      8.9,
        "reviews_count": 183000,
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 6) -> list[dict]:
    urls = list({d["search_url"] for d in _DEALS})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("AirHelp: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for d in _DEALS[:max_results]:
        aff_url = affiliate_map.get(d["search_url"])
        if not aff_url:
            continue
        deals.append({
            "title":          d["title"],
            "description":    d["description"],
            "location":       d["location"],
            "original_price": None,
            "sale_price":     d["sale_price"],
            "discount_pct":   d["discount_pct"],
            "image_url":      d["image_url"],
            "affiliate_url":  aff_url,
            "source":         "airhelp",
            "category":       d["category"],
            "tipo":           d["tipo"],
            "rating":         d["rating"],
            "reviews_count":  d["reviews_count"],
        })

    log.info(f"AirHelp: {len(deals)} deals con enlace de afiliado real")
    return deals
