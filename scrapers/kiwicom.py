"""
Kiwi.com scraper para GangaViaje.
Vuelos con comisión 3%, cookie 30 días vía TravelPayouts.
Programa confirmado como "Available" en la cuenta de TravelPayouts.
"""

import logging

from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_VUELOS = [
    {
        "title":          "Vuelos baratos desde Madrid",
        "description":    "Busca y compara vuelos baratos desde Madrid a cientos de destinos. Combinaciones únicas con precio garantizado.",
        "location":       "Madrid",
        "sale_price":     49.00,
        "image_url":      "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.kiwi.com/es/search/results/madrid-espana/cualquier-lugar/anytime/anytime",
        "category":       "espana",
        "rating":         8.3,
        "reviews_count":  0,
    },
    {
        "title":          "Vuelos baratos desde Barcelona",
        "description":    "Encuentra los mejores precios de vuelos desde Barcelona. Miles de combinaciones con escala optimizada.",
        "location":       "Barcelona",
        "sale_price":     45.00,
        "image_url":      "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.kiwi.com/es/search/results/barcelona-espana/cualquier-lugar/anytime/anytime",
        "category":       "espana",
        "rating":         8.3,
        "reviews_count":  0,
    },
    {
        "title":          "Vuelos baratos a Europa",
        "description":    "Descubre destinos europeos al mejor precio. Londres, París, Roma, Berlín y más desde aeropuertos españoles.",
        "location":       "Europa",
        "sale_price":     39.00,
        "image_url":      "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.kiwi.com/es/search/results/espana/europa/anytime/anytime",
        "category":       "europa",
        "rating":         8.3,
        "reviews_count":  0,
    },
    {
        "title":          "Vuelos baratos a Canarias",
        "description":    "Vuela a Tenerife, Gran Canaria, Lanzarote y Fuerteventura al mejor precio. Compara todas las aerolíneas.",
        "location":       "Canarias",
        "sale_price":     55.00,
        "image_url":      "https://images.unsplash.com/photo-1559827260-dc66d52bef19?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.kiwi.com/es/search/results/espana/islas-canarias-espana/anytime/anytime",
        "category":       "playa",
        "rating":         8.4,
        "reviews_count":  0,
    },
    {
        "title":          "Vuelos baratos a América",
        "description":    "Combina vuelos para conseguir el precio más bajo a Estados Unidos, México, Colombia y Latinoamérica.",
        "location":       "América",
        "sale_price":     299.00,
        "image_url":      "https://images.unsplash.com/photo-1485738422979-f5c462d49f74?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.kiwi.com/es/search/results/espana/norteamerica/anytime/anytime",
        "category":       "internacional",
        "rating":         8.2,
        "reviews_count":  0,
    },
    {
        "title":          "Vuelos baratos a Asia",
        "description":    "Los mejores precios a Tokio, Bangkok, Dubái, Singapur y más destinos de Asia con Kiwi.com.",
        "location":       "Asia",
        "sale_price":     349.00,
        "image_url":      "https://images.unsplash.com/photo-1480796927426-f609979314bd?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.kiwi.com/es/search/results/espana/asia/anytime/anytime",
        "category":       "internacional",
        "rating":         8.2,
        "reviews_count":  0,
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    urls = list({v["search_url"] for v in _VUELOS})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("Kiwi.com: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for v in _VUELOS[:max_results]:
        affiliate_url = affiliate_map.get(v["search_url"])
        if not affiliate_url:
            continue
        deals.append({
            "title":          v["title"],
            "description":    v["description"],
            "location":       v["location"],
            "original_price": None,
            "sale_price":     v["sale_price"],
            "discount_pct":   0,
            "image_url":      v["image_url"],
            "affiliate_url":  affiliate_url,
            "source":         "kiwicom",
            "category":       v["category"],
            "tipo":           "vuelo",
            "rating":         v["rating"],
            "reviews_count":  v["reviews_count"],
        })

    log.info(f"Kiwi.com: {len(deals)} vuelos con enlace de afiliado real")
    return deals
