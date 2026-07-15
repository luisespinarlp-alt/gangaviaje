"""
Compensair scraper para GangaViaje.
Reclamaciones por vuelos retrasados/cancelados. Recompensa fija €5–12 vía TravelPayouts.
Complementa AirHelp — dos marcas de reclamación aumentan la cobertura.
"""

import logging
from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_DEALS = [
    {
        "title":       "Reclamación gratuita por vuelo retrasado — hasta 600€",
        "description": "¿Tu vuelo llegó tarde más de 3 horas? Compensair analiza tu caso gratis y reclama hasta 600€ a la aerolínea. Sin papeleo, 100% online. Solo cobran si ganan tu caso.",
        "location":    "Todo el mundo",
        "sale_price":  0.0,
        "image_url":   "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://compensair.com/es/",
        "category":    "internacional",
        "tipo":        "vuelo",
        "discount_pct": 0,
        "rating":      8.7,
        "reviews_count": 45000,
    },
    {
        "title":       "Vuelo cancelado — reclama tu compensación en 3 minutos",
        "description": "Vuelo cancelado con menos de 14 días de antelación? El Reglamento Europeo 261/2004 te protege. Compensair gestiona toda la reclamación por ti. Servicio gratuito si no hay compensación.",
        "location":    "Europa",
        "sale_price":  0.0,
        "image_url":   "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://compensair.com/es/",
        "category":    "internacional",
        "tipo":        "vuelo",
        "discount_pct": 0,
        "rating":      8.7,
        "reviews_count": 45000,
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 4) -> list[dict]:
    urls = list({d["search_url"] for d in _DEALS})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("Compensair: sin credenciales válidas de TravelPayouts, omitiendo")
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
            "source":         "compensair",
            "category":       d["category"],
            "tipo":           d["tipo"],
            "rating":         d["rating"],
            "reviews_count":  d["reviews_count"],
        })

    log.info(f"Compensair: {len(deals)} deals con enlace de afiliado real")
    return deals
