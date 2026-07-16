"""
Radical Storage scraper para GangaViaje.
Consignas de equipaje en ciudades turísticas. Comisión ~15% vía TravelPayouts.
Complementa Welcome Pickups — el viajero deja las maletas y explora la ciudad.
"""

import logging
from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_CONSIGNAS = [
    {
        "title":        "Consigna de maletas en Madrid — guarda el equipaje y explora",
        "description":  "Deja tu equipaje en una consigna segura en el centro de Madrid y disfruta del día sin cargar con las maletas. Puntos en Sol, Atocha y barrio de Salamanca. Desde 5€/día.",
        "location":     "Madrid",
        "sale_price":   5.0,
        "search_url":   "https://radicalstorage.com/es/spain/madrid/",
        "category":     "espana",
        "tipo":         "actividad",
        "discount_pct": 0,
        "rating":       9.1,
        "reviews_count": 120000,
        "image_url":    "https://images.unsplash.com/photo-1553413077-190dd305871c?fm=jpg&q=80&w=800&auto=format&fit=crop",
    },
    {
        "title":        "Consigna de maletas en Barcelona — guarda el equipaje y disfruta",
        "description":  "Puntos de consigna seguros en el centro de Barcelona: Las Ramblas, Gràcia, Barceloneta. Guarda tu equipaje y aprovecha las horas antes del vuelo o después del check-out.",
        "location":     "Barcelona",
        "sale_price":   5.0,
        "search_url":   "https://radicalstorage.com/es/spain/barcelona/",
        "category":     "espana",
        "tipo":         "actividad",
        "discount_pct": 0,
        "rating":       9.1,
        "reviews_count": 120000,
        "image_url":    "https://images.unsplash.com/photo-1553413077-190dd305871c?fm=jpg&q=80&w=800&auto=format&fit=crop",
    },
    {
        "title":        "Consigna de maletas en Roma — sin cargar el equipaje por el Coliseo",
        "description":  "Guarda las maletas en una consigna certificada cerca del Coliseo, Termini o el Vaticano. Sigue explorando Roma con las manos libres. Precio fijo por bolsa, sin sorpresas.",
        "location":     "Roma",
        "sale_price":   6.0,
        "search_url":   "https://radicalstorage.com/es/italy/rome/",
        "category":     "europa",
        "tipo":         "actividad",
        "discount_pct": 0,
        "rating":       9.1,
        "reviews_count": 120000,
        "image_url":    "https://images.unsplash.com/photo-1553413077-190dd305871c?fm=jpg&q=80&w=800&auto=format&fit=crop",
    },
    {
        "title":        "Consigna de maletas en Lisboa — explora sin peso",
        "description":  "Puntos de consigna seguros en Lisboa: Alfama, Baixa y junto a la estación de Oriente. Deja el equipaje y sube a los tranvías de Lisboa sin preocupaciones. Desde 5€.",
        "location":     "Lisboa",
        "sale_price":   5.0,
        "search_url":   "https://radicalstorage.com/es/portugal/lisbon/",
        "category":     "europa",
        "tipo":         "actividad",
        "discount_pct": 0,
        "rating":       9.1,
        "reviews_count": 120000,
        "image_url":    "https://images.unsplash.com/photo-1553413077-190dd305871c?fm=jpg&q=80&w=800&auto=format&fit=crop",
    },
    {
        "title":        "Consigna de maletas en París — guarda el equipaje cerca de la Torre Eiffel",
        "description":  "Consignas seguras en el centro de París: cerca de la Torre Eiffel, el Louvre y Montmartre. Certificadas y aseguradas. Ideal para aprovechar el último día antes del vuelo.",
        "location":     "París",
        "sale_price":   6.0,
        "search_url":   "https://radicalstorage.com/es/france/paris/",
        "category":     "europa",
        "tipo":         "actividad",
        "discount_pct": 0,
        "rating":       9.1,
        "reviews_count": 120000,
        "image_url":    "https://images.unsplash.com/photo-1553413077-190dd305871c?fm=jpg&q=80&w=800&auto=format&fit=crop",
    },
    {
        "title":        "Consigna de maletas en Ámsterdam — explora los canales sin peso",
        "description":  "Guarda el equipaje en una consigna certificada cerca de la Estación Central o el barrio de los Museos. Recorre los canales de Ámsterdam con las manos libres desde 5€.",
        "location":     "Ámsterdam",
        "sale_price":   5.0,
        "search_url":   "https://radicalstorage.com/es/netherlands/amsterdam/",
        "category":     "europa",
        "tipo":         "actividad",
        "discount_pct": 0,
        "rating":       9.1,
        "reviews_count": 120000,
        "image_url":    "https://images.unsplash.com/photo-1553413077-190dd305871c?fm=jpg&q=80&w=800&auto=format&fit=crop",
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    urls = list({d["search_url"] for d in _CONSIGNAS})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("Radical Storage: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for d in _CONSIGNAS[:max_results]:
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
            "source":         "radicalstorage",
            "category":       d["category"],
            "tipo":           d["tipo"],
            "rating":         d["rating"],
            "reviews_count":  d["reviews_count"],
        })

    log.info(f"Radical Storage: {len(deals)} consignas con enlace de afiliado real")
    return deals
