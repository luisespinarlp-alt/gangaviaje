"""
GetRentacar.com scraper para GangaViaje.
Alquiler de coches con comisión 10%, cookie 90 días vía TravelPayouts.
Programa confirmado como "Available" en la cuenta de TravelPayouts.
"""

import logging

from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_COCHES = [
    {
        "title":          "Alquiler de coche en España — GetRentacar",
        "description":    "Compara y reserva el mejor precio de alquiler de coches en España. Sin cargos ocultos, cancelación gratuita.",
        "location":       "España",
        "sale_price":     24.00,
        "image_url":      "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://getrentacar.com/en/spain/",
        "category":       "espana",
        "rating":         8.5,
        "reviews_count":  0,
    },
    {
        "title":          "Alquiler de coche en Portugal — GetRentacar",
        "description":    "Las mejores ofertas de coches en Portugal. Lisboa, Oporto y Faro con precio garantizado.",
        "location":       "Portugal",
        "sale_price":     21.00,
        "image_url":      "https://images.unsplash.com/photo-1548707309-dcebeab9ea9b?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://getrentacar.com/en/portugal/",
        "category":       "europa",
        "rating":         8.4,
        "reviews_count":  0,
    },
    {
        "title":          "Alquiler de coche en Italia — GetRentacar",
        "description":    "Recorre Italia libremente. Roma, Milán, Florencia y Venecia con las mejores tarifas garantizadas.",
        "location":       "Italia",
        "sale_price":     28.00,
        "image_url":      "https://images.unsplash.com/photo-1529260830199-42c24126f198?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://getrentacar.com/en/italy/",
        "category":       "europa",
        "rating":         8.3,
        "reviews_count":  0,
    },
    {
        "title":          "Alquiler de coche en Francia — GetRentacar",
        "description":    "Explora Francia en coche. París, Niza, Lyon y más destinos con precio cerrado sin sorpresas.",
        "location":       "Francia",
        "sale_price":     29.00,
        "image_url":      "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://getrentacar.com/en/france/",
        "category":       "europa",
        "rating":         8.4,
        "reviews_count":  0,
    },
    {
        "title":          "Alquiler de coche en Grecia — GetRentacar",
        "description":    "Descubre Grecia a tu ritmo. Atenas, Tesalónica y las islas con el mejor precio de alquiler.",
        "location":       "Grecia",
        "sale_price":     19.00,
        "image_url":      "https://images.unsplash.com/photo-1555993539-1732b0258235?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://getrentacar.com/en/greece/",
        "category":       "europa",
        "rating":         8.5,
        "reviews_count":  0,
    },
    {
        "title":          "Alquiler de coche en Croacia — GetRentacar",
        "description":    "Recorre la costa croata en coche. Dubrovnik, Split y Zadar con tarifas exclusivas online.",
        "location":       "Croacia",
        "sale_price":     22.00,
        "image_url":      "https://images.unsplash.com/photo-1555990793-da11153b2473?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":     "https://getrentacar.com/en/croatia/",
        "category":       "europa",
        "rating":         8.6,
        "reviews_count":  0,
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    urls = list({c["search_url"] for c in _COCHES})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("GetRentacar: sin credenciales válidas de TravelPayouts, omitiendo")
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
            "source":         "getrentacar",
            "category":       c["category"],
            "tipo":           "coche",
            "rating":         c["rating"],
            "reviews_count":  c["reviews_count"],
        })

    log.info(f"GetRentacar: {len(deals)} coches con enlace de afiliado real")
    return deals
