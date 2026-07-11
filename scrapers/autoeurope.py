"""
AutoEurope scraper para GangaViaje.
Alquiler de coches con comisión real vía TravelPayouts.
AutoEurope (EU,UK) está confirmado como programa "Available" en la cuenta de TravelPayouts
(nota: solo el dominio autoeurope.es está suscrito; autoeurope.com no).
URLs de ciudad verificadas directamente en autoeurope.es (HTTP 200 confirmado).
"""

import logging

from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_COCHES = [
    {
        "title":          "Alquiler de coche en Madrid",
        "description":    "Compara las mejores tarifas de alquiler de coche en Madrid, con cancelación gratuita.",
        "location":       "Madrid",
        "sale_price":     24.00,
        "image_url":      "https://images.unsplash.com/photo-1503376780353-7e6692767b70?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.autoeurope.es/alquiler-coches-madrid/",
        "category":       "ciudad",
    },
    {
        "title":          "Alquiler de coche en Barcelona",
        "description":    "Las mejores ofertas de alquiler de coche en Barcelona, comparando varias compañías a la vez.",
        "location":       "Barcelona",
        "sale_price":     22.00,
        "image_url":      "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.autoeurope.es/alquiler-coches-barcelona/",
        "category":       "ciudad",
    },
    {
        "title":          "Alquiler de coche en Málaga",
        "description":    "Coches de alquiler en el aeropuerto de Málaga y la Costa del Sol al mejor precio.",
        "location":       "Málaga",
        "sale_price":     19.00,
        "image_url":      "https://images.unsplash.com/photo-1559827260-dc66d52bef19?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.autoeurope.es/alquiler-coches-malaga/",
        "category":       "playa",
    },
    {
        "title":          "Alquiler de coche en Mallorca",
        "description":    "Recorre Mallorca a tu ritmo con un coche de alquiler reservado con antelación.",
        "location":       "Palma de Mallorca",
        "sale_price":     21.00,
        "image_url":      "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.autoeurope.es/alquiler-coches-palma-de-mallorca/",
        "category":       "playa",
    },
    {
        "title":          "Alquiler de coche en Tenerife",
        "description":    "Explora la isla de Tenerife con total libertad alquilando un coche con cancelación gratuita.",
        "location":       "Tenerife",
        "sale_price":     18.00,
        "image_url":      "https://images.unsplash.com/photo-1559827260-dc66d52bef19?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.autoeurope.es/alquiler-coches-tenerife/",
        "category":       "playa",
    },
    {
        "title":          "Alquiler de coche en Sevilla",
        "description":    "Coches de alquiler en Sevilla para descubrir Andalucía a tu ritmo.",
        "location":       "Sevilla",
        "sale_price":     20.00,
        "image_url":      "https://images.unsplash.com/photo-1503376780353-7e6692767b70?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.autoeurope.es/alquiler-coches-sevilla/",
        "category":       "ciudad",
    },
    {
        "title":          "Alquiler de coche en Roma",
        "description":    "Compara precios de alquiler de coche en Roma con varias compañías a la vez.",
        "location":       "Roma",
        "sale_price":     26.00,
        "image_url":      "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.autoeurope.es/alquiler-coches-roma/",
        "category":       "europa",
    },
    {
        "title":          "Alquiler de coche en París",
        "description":    "Encuentra el coche de alquiler más barato en París y alrededores.",
        "location":       "París",
        "sale_price":     28.00,
        "image_url":      "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.autoeurope.es/alquiler-coches-paris/",
        "category":       "europa",
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    urls = list({c["search_url"] for c in _COCHES})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("AutoEurope: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for c in _COCHES[:max_results]:
        affiliate_url = affiliate_map.get(c["search_url"])
        if not affiliate_url:
            continue
        deals.append({
            "title":          c["title"],
            "description":    c["description"],
            "location":       c["location"],
            "original_price": None,
            "sale_price":     c["sale_price"],
            "discount_pct":   0,
            "image_url":      c["image_url"],
            "affiliate_url":  affiliate_url,
            "source":         "autoeurope",
            "category":       c["category"],
            "tipo":           "coche",
            "rating":         0.0,
            "reviews_count":  0,
        })

    log.info(f"AutoEurope: {len(deals)} ofertas de coche con enlace de afiliado real")
    return deals
