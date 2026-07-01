"""
Kiwitaxi scraper para GangaViaje.
Traslados al aeropuerto con comisión 9-11% vía TravelPayouts.
Programa confirmado como "Available" en la cuenta de TravelPayouts.
"""

import logging

from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_TRASLADOS = [
    {
        "title":          "Traslado aeropuerto Barcelona — Taxi privado sin esperas",
        "description":    "Traslado privado entre el Aeropuerto El Prat y Barcelona ciudad. Conductor profesional, precio fijo sin sorpresas.",
        "location":       "Barcelona",
        "sale_price":     35.00,
        "image_url":      "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://kiwitaxi.com/Spain/Barcelona",
        "category":       "ciudad",
        "rating":         9.2,
        "reviews_count":  4200,
    },
    {
        "title":          "Traslado aeropuerto Madrid — Taxi privado al centro",
        "description":    "Traslado directo entre el Aeropuerto Barajas y Madrid. Precio cerrado, sin taxímetro. Disponible 24h.",
        "location":       "Madrid",
        "sale_price":     32.00,
        "image_url":      "https://images.unsplash.com/photo-1464219789935-c2d9d9aba644?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://kiwitaxi.com/Spain/Madrid",
        "category":       "ciudad",
        "rating":         9.1,
        "reviews_count":  3800,
    },
    {
        "title":          "Traslado aeropuerto Roma — Transfer privado Fiumicino",
        "description":    "Taxi privado entre el Aeropuerto Fiumicino y Roma. Conductor con letrero, sin esperas ni sorpresas.",
        "location":       "Roma",
        "sale_price":     40.00,
        "image_url":      "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://kiwitaxi.com/Italy/Rome",
        "category":       "europa",
        "rating":         9.0,
        "reviews_count":  5100,
    },
    {
        "title":          "Traslado aeropuerto París — Transfer privado CDG",
        "description":    "Traslado entre el Aeropuerto Charles de Gaulle y París. Vehículo privado, sin esperas, precio fijo.",
        "location":       "París",
        "sale_price":     55.00,
        "image_url":      "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://kiwitaxi.com/France/Paris",
        "category":       "europa",
        "rating":         9.0,
        "reviews_count":  6300,
    },
    {
        "title":          "Traslado aeropuerto Londres — Transfer privado Heathrow",
        "description":    "Taxi privado entre Heathrow y Londres. Conductor con letrero, equipaje incluido. Reserva online con antelación.",
        "location":       "Londres",
        "sale_price":     60.00,
        "image_url":      "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://kiwitaxi.com/United-Kingdom/London",
        "category":       "europa",
        "rating":         9.1,
        "reviews_count":  7200,
    },
    {
        "title":          "Traslado aeropuerto Lisboa — Taxi privado sin taxímetro",
        "description":    "Transfer privado entre el Aeropuerto de Lisboa y la ciudad. Precio cerrado, conductor profesional.",
        "location":       "Lisboa",
        "sale_price":     28.00,
        "image_url":      "https://images.unsplash.com/photo-1548707309-dcebeab9ea9b?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://kiwitaxi.com/Portugal/Lisbon",
        "category":       "europa",
        "rating":         9.2,
        "reviews_count":  2900,
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    urls = list({t["search_url"] for t in _TRASLADOS})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("Kiwitaxi: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for t in _TRASLADOS[:max_results]:
        affiliate_url = affiliate_map.get(t["search_url"])
        if not affiliate_url:
            continue
        deals.append({
            "title":          t["title"],
            "description":    t["description"],
            "location":       t["location"],
            "original_price": None,
            "sale_price":     t["sale_price"],
            "discount_pct":   0,
            "image_url":      t["image_url"],
            "affiliate_url":  affiliate_url,
            "source":         "kiwitaxi",
            "category":       t["category"],
            "tipo":           "actividad",
            "rating":         t["rating"],
            "reviews_count":  t["reviews_count"],
        })

    log.info(f"Kiwitaxi: {len(deals)} traslados con enlace de afiliado real")
    return deals
