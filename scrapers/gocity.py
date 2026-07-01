"""
Go City scraper para GangaViaje.
Pases de atracciones (Explorer Pass y All-Inclusive Pass) con comisión 3.4-6% vía TravelPayouts.
Programa confirmado como "Available" en la cuenta de TravelPayouts.
"""

import logging

from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_PASES = [
    {
        "title":          "Go City Londres — Pase todo incluido para atracciones",
        "description":    "Accede a más de 80 atracciones de Londres con un solo pase: Tower of London, London Eye, Madame Tussauds y mucho más.",
        "location":       "Londres",
        "sale_price":     79.00,
        "image_url":      "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://gocity.com/london/en-us",
        "category":       "europa",
        "rating":         8.8,
        "reviews_count":  12400,
    },
    {
        "title":          "Go City Nueva York — Explorer Pass atracciones",
        "description":    "Elige entre las mejores atracciones de Nueva York: Empire State, crucero por la bahía, museos y tours. Un pase, total libertad.",
        "location":       "Nueva York",
        "sale_price":     89.00,
        "image_url":      "https://images.unsplash.com/photo-1485738422979-f5c462d49f74?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://gocity.com/new-york/en-us",
        "category":       "internacional",
        "rating":         9.0,
        "reviews_count":  18600,
    },
    {
        "title":          "Go City París — Pase de atracciones todo incluido",
        "description":    "Visita la Torre Eiffel, el Louvre, Versalles y más de 40 atracciones de París con un solo pase. Sin colas, sin sorpresas.",
        "location":       "París",
        "sale_price":     69.00,
        "image_url":      "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://gocity.com/paris/en-us",
        "category":       "europa",
        "rating":         8.9,
        "reviews_count":  9800,
    },
    {
        "title":          "Go City Barcelona — Explorer Pass atracciones",
        "description":    "Sagrada Família, Park Güell, Fundació Miró y más de 20 atracciones de Barcelona incluidas en un solo pase.",
        "location":       "Barcelona",
        "sale_price":     49.00,
        "image_url":      "https://images.unsplash.com/photo-1583779457094-ab6f77f7bf63?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://gocity.com/barcelona/en-us",
        "category":       "ciudad",
        "rating":         8.7,
        "reviews_count":  5200,
    },
    {
        "title":          "Go City Dubái — Pase todo incluido atracciones",
        "description":    "Burj Khalifa, Desert Safari, Dubai Frame y más de 40 experiencias únicas en Dubái con un solo pase Explorer.",
        "location":       "Dubái",
        "sale_price":     95.00,
        "image_url":      "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://gocity.com/dubai/en-us",
        "category":       "internacional",
        "rating":         9.1,
        "reviews_count":  7300,
    },
    {
        "title":          "Go City Roma — Explorer Pass atracciones",
        "description":    "Coliseo, Vaticano, Galería Borghese y más de 25 atracciones de Roma incluidas. Reserva online y salta la cola.",
        "location":       "Roma",
        "sale_price":     59.00,
        "image_url":      "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://gocity.com/rome/en-us",
        "category":       "europa",
        "rating":         8.9,
        "reviews_count":  6100,
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    urls = list({p["search_url"] for p in _PASES})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("Go City: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for p in _PASES[:max_results]:
        affiliate_url = affiliate_map.get(p["search_url"])
        if not affiliate_url:
            continue
        deals.append({
            "title":          p["title"],
            "description":    p["description"],
            "location":       p["location"],
            "original_price": None,
            "sale_price":     p["sale_price"],
            "discount_pct":   0,
            "image_url":      p["image_url"],
            "affiliate_url":  affiliate_url,
            "source":         "gocity",
            "category":       p["category"],
            "tipo":           "actividad",
            "rating":         p["rating"],
            "reviews_count":  p["reviews_count"],
        })

    log.info(f"Go City: {len(deals)} pases con enlace de afiliado real")
    return deals
