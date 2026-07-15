"""
EKTA scraper para GangaViaje.
Seguros de viaje — comisión 25% vía TravelPayouts. Una de las comisiones más altas del programa.
"""

import logging
from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_SEGUROS = [
    {
        "title":       "Seguro de viaje Europa — desde 15€ la semana",
        "description": "Seguro de viaje completo para Europa: asistencia médica hasta 30.000€, cancelación de viaje, pérdida de equipaje y retrasos. Contratación online en 2 minutos, cobertura inmediata.",
        "location":    "Europa",
        "sale_price":  15.0,
        "image_url":   "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://ekta.eu/",
        "category":    "europa",
        "tipo":        "actividad",
        "discount_pct": 0,
        "rating":      8.7,
        "reviews_count": 12000,
    },
    {
        "title":       "Seguro de viaje Mundial — cobertura en 180 países",
        "description": "Seguro de viaje internacional con asistencia médica de emergencia, evacuación médica, cancelación y robo. Cobertura en más de 180 países. Ideal para viajes a largo plazo o destinos fuera de Europa.",
        "location":    "Todo el mundo",
        "sale_price":  22.0,
        "image_url":   "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://ekta.eu/",
        "category":    "internacional",
        "tipo":        "actividad",
        "discount_pct": 0,
        "rating":      8.7,
        "reviews_count": 12000,
    },
    {
        "title":       "Seguro multivïaje anual — todos tus viajes del año",
        "description": "Un solo seguro para todos los viajes del año. Cobertura automática en cada salida sin necesidad de contratar por separado. Perfecto para viajeros frecuentes y escapadas de fin de semana.",
        "location":    "Europa",
        "sale_price":  89.0,
        "original_price": 140.0,
        "image_url":   "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://ekta.eu/",
        "category":    "internacional",
        "tipo":        "actividad",
        "discount_pct": 36,
        "rating":      8.7,
        "reviews_count": 12000,
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 6) -> list[dict]:
    urls = list({d["search_url"] for d in _SEGUROS})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("EKTA: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for d in _SEGUROS[:max_results]:
        aff_url = affiliate_map.get(d["search_url"])
        if not aff_url:
            continue
        deals.append({
            "title":          d["title"],
            "description":    d["description"],
            "location":       d["location"],
            "original_price": d.get("original_price"),
            "sale_price":     d["sale_price"],
            "discount_pct":   d["discount_pct"],
            "image_url":      d["image_url"],
            "affiliate_url":  aff_url,
            "source":         "ekta",
            "category":       d["category"],
            "tipo":           d["tipo"],
            "rating":         d["rating"],
            "reviews_count":  d["reviews_count"],
        })

    log.info(f"EKTA: {len(deals)} seguros con enlace de afiliado real")
    return deals
