"""
KKday scraper para GangaViaje.
Tours, actividades y experiencias con comisión 1%-5% vía TravelPayouts.
Programa confirmado como "Available" en la cuenta de TravelPayouts.
"""

import logging

from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_ACTIVIDADES = [
    {
        "title":          "Tours y actividades en Tokio — KKday",
        "description":    "Descubre Tokio con las mejores experiencias: visita al Monte Fuji, tour por Shibuya y mucho más.",
        "location":       "Tokio",
        "sale_price":     35.00,
        "image_url":      "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.kkday.com/es/city/tokyo",
        "category":       "internacional",
        "rating":         9.0,
        "reviews_count":  3400,
    },
    {
        "title":          "Tours y actividades en Bangkok — KKday",
        "description":    "Las mejores experiencias en Bangkok: templos, mercados flotantes y cocina tailandesa.",
        "location":       "Bangkok",
        "sale_price":     25.00,
        "image_url":      "https://images.unsplash.com/photo-1563492065599-3520f775eeed?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.kkday.com/es/city/bangkok",
        "category":       "internacional",
        "rating":         8.9,
        "reviews_count":  2800,
    },
    {
        "title":          "Tours y actividades en Dubái — KKday",
        "description":    "Vive Dubái al máximo: safari en desierto, Burj Khalifa y cruceros por la marina.",
        "location":       "Dubái",
        "sale_price":     45.00,
        "image_url":      "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.kkday.com/es/city/dubai",
        "category":       "internacional",
        "rating":         9.1,
        "reviews_count":  1900,
    },
    {
        "title":          "Tours y actividades en Singapur — KKday",
        "description":    "Explora Singapur con experiencias únicas: Gardens by the Bay, Sentosa y gastronomía local.",
        "location":       "Singapur",
        "sale_price":     30.00,
        "image_url":      "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.kkday.com/es/city/singapore",
        "category":       "internacional",
        "rating":         9.0,
        "reviews_count":  2200,
    },
    {
        "title":          "Tours y actividades en Seúl — KKday",
        "description":    "Descubre Seúl con los mejores tours: palacios, K-pop, gastronomía y tour nocturno.",
        "location":       "Seúl",
        "sale_price":     28.00,
        "image_url":      "https://images.unsplash.com/photo-1534274988757-a28bf1a57c17?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.kkday.com/es/city/seoul",
        "category":       "internacional",
        "rating":         8.8,
        "reviews_count":  1600,
    },
    {
        "title":          "Tours y actividades en Bali — KKday",
        "description":    "Las mejores experiencias en Bali: templos, arrozales, surf y excursiones al monte Agung.",
        "location":       "Bali",
        "sale_price":     22.00,
        "image_url":      "https://images.unsplash.com/photo-1537996194471-e657df975ab4?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://www.kkday.com/es/city/bali",
        "category":       "internacional",
        "rating":         9.2,
        "reviews_count":  4100,
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    urls = list({a["search_url"] for a in _ACTIVIDADES})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("KKday: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for a in _ACTIVIDADES[:max_results]:
        affiliate_url = affiliate_map.get(a["search_url"])
        if not affiliate_url:
            continue
        deals.append({
            "title":          a["title"],
            "description":    a["description"],
            "location":       a["location"],
            "original_price": None,
            "sale_price":     a["sale_price"],
            "discount_pct":   0,
            "image_url":      a["image_url"],
            "affiliate_url":  affiliate_url,
            "source":         "kkday",
            "category":       a["category"],
            "tipo":           "actividad",
            "rating":         a["rating"],
            "reviews_count":  a["reviews_count"],
        })

    log.info(f"KKday: {len(deals)} actividades con enlace de afiliado real")
    return deals
