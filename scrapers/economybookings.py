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

# Economybookings no tiene URLs de búsqueda por ciudad verificadas (su buscador es un
# formulario), así que solo se ofrece UN deal genérico con el enlace real a la home
# -> evita mostrar varias tarjetas de "ciudad" que en realidad llevan todas al mismo sitio.
_COCHES = [
    {
        "title":         "Alquiler de coche barato en toda España",
        "description":   "Compara tarifas de alquiler de coche en cualquier ciudad de España, con cancelación gratuita y sin sorpresas en el precio.",
        "location":      "España",
        "sale_price":    16.0,
        "image_url":     "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":      "espana",
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
