"""
WeGoTrip scraper para GangaViaje.
Audioguías y tours autoguiados con comisión 6.64%-41.5% vía TravelPayouts.
Programa confirmado como "Available" en la cuenta de TravelPayouts.
"""

import logging

from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_TOURS = [
    {
        "title":          "Audioguía del Coliseo de Roma — WeGoTrip",
        "description":    "Visita el Coliseo a tu ritmo con una audioguía interactiva en español. Sin guía fijo, sin horarios.",
        "location":       "Roma",
        "sale_price":     6.00,
        "image_url":      "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://wegotrip.com/en/italy/rome/",
        "category":       "europa",
        "rating":         9.1,
        "reviews_count":  1240,
    },
    {
        "title":          "Tour autoguiado por Barcelona — WeGoTrip",
        "description":    "Descubre el Barrio Gótico y el Born con una ruta interactiva en tu móvil. Sin esperas, sin grupo.",
        "location":       "Barcelona",
        "sale_price":     5.00,
        "image_url":      "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://wegotrip.com/en/spain/barcelona/",
        "category":       "ciudad",
        "rating":         8.9,
        "reviews_count":  870,
    },
    {
        "title":          "Audioguía del Louvre de París — WeGoTrip",
        "description":    "Visita el museo más grande del mundo a tu propio ritmo con una audioguía interactiva.",
        "location":       "París",
        "sale_price":     7.00,
        "image_url":      "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://wegotrip.com/en/france/paris/",
        "category":       "europa",
        "rating":         9.0,
        "reviews_count":  2100,
    },
    {
        "title":          "Tour autoguiado por Madrid — WeGoTrip",
        "description":    "Explora el Madrid de los Austrias y el Retiro con una ruta interactiva en español.",
        "location":       "Madrid",
        "sale_price":     5.00,
        "image_url":      "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://wegotrip.com/en/spain/madrid/",
        "category":       "ciudad",
        "rating":         8.8,
        "reviews_count":  560,
    },
    {
        "title":          "Audioguía del British Museum — WeGoTrip",
        "description":    "Recorre las salas más importantes del British Museum con una guía interactiva. Gratis entrar, la guía desde 6€.",
        "location":       "Londres",
        "sale_price":     6.00,
        "image_url":      "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://wegotrip.com/en/united-kingdom/london/",
        "category":       "europa",
        "rating":         8.9,
        "reviews_count":  980,
    },
    {
        "title":          "Tour autoguiado por Ámsterdam — WeGoTrip",
        "description":    "Descubre el centro histórico de Ámsterdam a tu ritmo con una audioguía interactiva en móvil.",
        "location":       "Ámsterdam",
        "sale_price":     5.00,
        "image_url":      "https://images.unsplash.com/photo-1459679749680-18eb1eb37418?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://wegotrip.com/en/netherlands/amsterdam/",
        "category":       "europa",
        "rating":         8.7,
        "reviews_count":  430,
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    urls = list({t["search_url"] for t in _TOURS})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("WeGoTrip: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for t in _TOURS[:max_results]:
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
            "source":         "wegotrip",
            "category":       t["category"],
            "tipo":           "actividad",
            "rating":         t["rating"],
            "reviews_count":  t["reviews_count"],
        })

    log.info(f"WeGoTrip: {len(deals)} tours con enlace de afiliado real")
    return deals
