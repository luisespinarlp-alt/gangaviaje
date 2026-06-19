"""
Economybookings scraper para GangaViaje.
Alquiler de coches con comisión real vía TravelPayouts (3-8%).
Economybookings está confirmado como programa activo en la cuenta de TravelPayouts.
No existe un deep-link verificado por ciudad (su buscador es un formulario, no URLs
por parámetros), así que todos los enlaces apuntan a la home real, comisionada vía
la API links/v1/create -> comisión real garantizada en cualquier reserva posterior.
"""

import logging

from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_HOME_URL = "https://www.economybookings.com/"

# Precios "desde" estimados a partir de tarifas habituales de alquiler de coche económico.
_COCHES = [
    {
        "title":         "Alquiler de coche en Barcelona",
        "description":   "Compara las mejores tarifas de alquiler de coche en Barcelona con cancelación gratuita.",
        "location":      "Barcelona",
        "sale_price":    19.0,
        "image_url":     "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":      "ciudad",
    },
    {
        "title":         "Alquiler de coche en Madrid",
        "description":   "Encuentra el coche de alquiler más barato en Madrid, sin sorpresas en el precio.",
        "location":      "Madrid",
        "sale_price":    18.0,
        "image_url":     "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":      "ciudad",
    },
    {
        "title":         "Alquiler de coche en Málaga",
        "description":   "Tarifas bajas para tu alquiler de coche en Málaga, ideal para la Costa del Sol.",
        "location":      "Málaga",
        "sale_price":    16.0,
        "image_url":     "https://images.unsplash.com/photo-1591018120414-83c5f0e7fe8e?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":      "playa",
    },
    {
        "title":         "Alquiler de coche en Palma de Mallorca",
        "description":   "Compara precios de alquiler de coche en Mallorca con seguro incluido.",
        "location":      "Palma de Mallorca",
        "sale_price":    21.0,
        "image_url":     "https://images.unsplash.com/photo-1562766591-80ba2f6feffb?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":      "playa",
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    affiliate_map = to_affiliate_urls([_HOME_URL])
    affiliate_url = affiliate_map.get(_HOME_URL)

    if not affiliate_url:
        log.info("Economybookings: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for c in _COCHES[:max_results]:
        deals.append({
            "title":          c["title"],
            "description":    c["description"],
            "location":       c["location"],
            "original_price": None,
            "sale_price":     c["sale_price"],
            "discount_pct":   0,
            "image_url":      c["image_url"],
            "affiliate_url":  affiliate_url,
            "source":         "economybookings",
            "category":       c["category"],
            "tipo":           "coche",
            "rating":         0.0,
            "reviews_count":  0,
        })

    log.info(f"Economybookings: {len(deals)} ofertas de coche con enlace de afiliado real")
    return deals
