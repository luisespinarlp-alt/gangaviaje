"""
Welcome Pickups scraper para GangaViaje.
Traslados aeropuerto con conductor profesional. Comisión 8–9% vía TravelPayouts.
Complementa Kiwitaxi con una marca muy reconocida en destinos turísticos europeos.
"""

import logging
from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_TRANSFERS = [
    {
        "title":       "Traslado aeropuerto Madrid — conductor privado sin esperas",
        "description": "Traslado privado del aeropuerto de Barajas al centro de Madrid con conductor profesional. Precio fijo sin sorpresas, seguimiento de vuelo en tiempo real y cancelación gratuita.",
        "location":    "Madrid",
        "sale_price":  29.0,
        "image_url":   "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.welcomepickups.com/transfers/spain/madrid/",
        "category":    "espana",
        "tipo":        "traslado",
        "discount_pct": 0,
        "rating":      9.3,
        "reviews_count": 85000,
    },
    {
        "title":       "Traslado aeropuerto Barcelona — sin taxímetro ni sorpresas",
        "description": "Traslado privado del aeropuerto de El Prat al centro de Barcelona. Precio cerrado desde la reserva, conductor puntual y cancelación gratuita hasta 24h antes.",
        "location":    "Barcelona",
        "sale_price":  35.0,
        "image_url":   "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.welcomepickups.com/transfers/spain/barcelona/",
        "category":    "espana",
        "tipo":        "traslado",
        "discount_pct": 0,
        "rating":      9.3,
        "reviews_count": 85000,
    },
    {
        "title":       "Traslado aeropuerto Lisboa — conductor privado desde 18€",
        "description": "Traslado privado del aeropuerto de Lisboa al centro o a cualquier dirección. Conductor que sigue tu vuelo en tiempo real — te espera aunque llegues tarde.",
        "location":    "Lisboa",
        "sale_price":  18.0,
        "image_url":   "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.welcomepickups.com/transfers/portugal/lisbon/",
        "category":    "europa",
        "tipo":        "traslado",
        "discount_pct": 0,
        "rating":      9.3,
        "reviews_count": 85000,
    },
    {
        "title":       "Traslado aeropuerto Atenas — sin negociar con taxistas",
        "description": "Traslado privado del aeropuerto de Atenas al Pireo, la Acrópolis o cualquier hotel. Precio fijo en euros — sin la negociación habitual con los taxis griegos.",
        "location":    "Atenas",
        "sale_price":  32.0,
        "image_url":   "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.welcomepickups.com/transfers/greece/athens/",
        "category":    "europa",
        "tipo":        "traslado",
        "discount_pct": 0,
        "rating":      9.3,
        "reviews_count": 85000,
    },
    {
        "title":       "Traslado aeropuerto Roma — Fiumicino o Ciampino al centro",
        "description": "Traslado privado desde el aeropuerto de Fiumicino o Ciampino al centro de Roma o a cualquier dirección. Evita el caos del Termini y las colas de taxi.",
        "location":    "Roma",
        "sale_price":  40.0,
        "image_url":   "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.welcomepickups.com/transfers/italy/rome/",
        "category":    "europa",
        "tipo":        "traslado",
        "discount_pct": 0,
        "rating":      9.3,
        "reviews_count": 85000,
    },
    {
        "title":       "Traslado aeropuerto Marrakech — desde el Menara al riad",
        "description": "Traslado privado del aeropuerto Menara al riad o hotel de la medina de Marrakech. Conductor puntual con cartel — evita la presión de los taxis al salir del aeropuerto.",
        "location":    "Marrakech",
        "sale_price":  12.0,
        "image_url":   "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.welcomepickups.com/transfers/morocco/marrakech/",
        "category":    "internacional",
        "tipo":        "traslado",
        "discount_pct": 0,
        "rating":      9.3,
        "reviews_count": 85000,
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    urls = list({d["search_url"] for d in _TRANSFERS})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("Welcome Pickups: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for d in _TRANSFERS[:max_results]:
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
            "source":         "welcomepickups",
            "category":       d["category"],
            "tipo":           d["tipo"],
            "rating":         d["rating"],
            "reviews_count":  d["reviews_count"],
        })

    log.info(f"Welcome Pickups: {len(deals)} traslados con enlace de afiliado real")
    return deals
