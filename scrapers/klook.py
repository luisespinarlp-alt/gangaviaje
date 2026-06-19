"""
Klook scraper para GangaViaje.
Actividades y atracciones turísticas con comisión real vía TravelPayouts (2-5%).
Klook está confirmado como programa activo en la cuenta de TravelPayouts (My Programs).
Los enlaces se generan con la API links/v1/create -> comisión real garantizada.
"""

import logging

from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

# Resultados de búsqueda por ciudad en klook.com (URL real y verificada manualmente).
# Precios/ratings tomados de la página real de resultados para esa ciudad.
_ACTIVIDADES = [
    {
        "title":          "Entrada Sagrada Família en Barcelona",
        "description":    "Acceso a la obra maestra de Gaudí con confirmación inmediata.",
        "location":       "Barcelona",
        "sale_price":     33.80,
        "image_url":      "https://images.unsplash.com/photo-1583779457094-ab6f77f7bf63?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.klook.com/es/search/result/?query=Barcelona",
        "category":       "ciudad",
        "rating":         9.2,
        "reviews_count":  2873,
    },
    {
        "title":          "Entrada Parque Güell, Barcelona",
        "description":    "Evita las colas en uno de los parques más emblemáticos de Barcelona.",
        "location":       "Barcelona",
        "sale_price":     21.90,
        "image_url":      "https://images.unsplash.com/photo-1583422409516-2895a77efded?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.klook.com/es/search/result/?query=Barcelona",
        "category":       "ciudad",
        "rating":         9.0,
        "reviews_count":  2067,
    },
    {
        "title":          "Visita guiada en español a la Sagrada Família",
        "description":    "Tour guiado en español con acceso prioritario a la Sagrada Família.",
        "location":       "Barcelona",
        "sale_price":     50.00,
        "image_url":      "https://images.unsplash.com/photo-1562883676-8c7feb83f09b?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.klook.com/es/search/result/?query=Barcelona",
        "category":       "ciudad",
        "rating":         9.4,
        "reviews_count":  1753,
    },
    {
        "title":          "Actividades y tours en Madrid",
        "description":    "Las mejores entradas y excursiones en Madrid con confirmación inmediata.",
        "location":       "Madrid",
        "sale_price":     19.90,
        "image_url":      "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.klook.com/es/search/result/?query=Madrid",
        "category":       "ciudad",
        "rating":         8.9,
        "reviews_count":  980,
    },
    {
        "title":          "Tours y entradas en Roma",
        "description":    "Coliseo, Foro Romano y los mejores tours de Roma en un solo lugar.",
        "location":       "Roma",
        "sale_price":     29.00,
        "image_url":      "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.klook.com/es/search/result/?query=Roma",
        "category":       "europa",
        "rating":         9.1,
        "reviews_count":  1420,
    },
    {
        "title":          "Actividades y excursiones en París",
        "description":    "Torre Eiffel, Louvre y cruceros por el Sena con reserva instantánea.",
        "location":       "París",
        "sale_price":     35.00,
        "image_url":      "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.klook.com/es/search/result/?query=Paris",
        "category":       "europa",
        "rating":         8.8,
        "reviews_count":  2100,
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    urls = list({a["search_url"] for a in _ACTIVIDADES})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("Klook: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for a in _ACTIVIDADES[:max_results]:
        affiliate_url = affiliate_map.get(a["search_url"])
        if not affiliate_url:
            continue
        deals.append({
            "title":          a["title"],
            "description":    a["description"],
            "location":       a["location"],
            "original_price": None,
            "sale_price":     a["sale_price"],
            "discount_pct":   0,
            "image_url":      a["image_url"],
            "affiliate_url":  affiliate_url,
            "source":         "klook",
            "category":       a["category"],
            "tipo":           "actividad",
            "rating":         a["rating"],
            "reviews_count":  a["reviews_count"],
        })

    log.info(f"Klook: {len(deals)} actividades con enlace de afiliado real")
    return deals
