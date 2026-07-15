"""
Airalo scraper para GangaViaje.
eSIMs de viaje — el marketplace de eSIMs más grande del mundo. Comisión 12% vía TravelPayouts.
"""

import logging
from scrapers.tp_links import to_affiliate_urls

log = logging.getLogger(__name__)

_ESIMS = [
    {
        "title":       "eSIM Europa — datos ilimitados para 30+ países",
        "description": "eSIM regional para toda Europa: actívala antes de salir y conectate al aterrizar sin cambiar de SIM. Compatible con iPhone XS+ y Android desde 2018. Desde 5€ la semana.",
        "location":    "Europa",
        "sale_price":  5.0,
        "image_url":   "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.airalo.com/europe-esim",
        "category":    "europa",
        "tipo":        "actividad",
        "discount_pct": 0,
        "rating":      9.2,
        "reviews_count": 340000,
    },
    {
        "title":       "eSIM Global — datos en más de 190 países",
        "description": "Una sola eSIM para todo el mundo. Ideal para viajeros frecuentes o rutas multi-destino. Sin permanencia, sin facturas por sorpresa, recarga desde la app en segundos.",
        "location":    "Todo el mundo",
        "sale_price":  9.0,
        "image_url":   "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.airalo.com/global-esim",
        "category":    "internacional",
        "tipo":        "actividad",
        "discount_pct": 0,
        "rating":      9.2,
        "reviews_count": 340000,
    },
    {
        "title":       "eSIM España — datos 4G/5G sin contrato",
        "description": "eSIM local para España con datos 4G/5G. Perfecta para turistas que visitan España o para completar tu plan nacional. Activación instantánea desde la app de Airalo.",
        "location":    "España",
        "sale_price":  4.5,
        "image_url":   "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.airalo.com/spain-esim",
        "category":    "espana",
        "tipo":        "actividad",
        "discount_pct": 0,
        "rating":      9.2,
        "reviews_count": 340000,
    },
    {
        "title":       "eSIM Japón — conectividad 5G para tu viaje",
        "description": "eSIM local para Japón con datos en red 5G. Sin cola en el aeropuerto, sin buscar tiendas. Actívala antes de salir y empieza a funcionar en cuanto aterrices en Tokio.",
        "location":    "Tokio",
        "sale_price":  6.0,
        "image_url":   "https://images.unsplash.com/photo-1528360983277-13d401cdc186?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.airalo.com/japan-esim",
        "category":    "internacional",
        "tipo":        "actividad",
        "discount_pct": 0,
        "rating":      9.2,
        "reviews_count": 340000,
    },
    {
        "title":       "eSIM Asia — datos en 13 países asiáticos",
        "description": "eSIM regional para Asia: Japón, Tailandia, Bali, Singapur, Vietnam y más. Una sola tarjeta para toda la ruta sin cambiar de SIM en cada país.",
        "location":    "Asia",
        "sale_price":  8.0,
        "image_url":   "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.airalo.com/asia-esim",
        "category":    "internacional",
        "tipo":        "actividad",
        "discount_pct": 0,
        "rating":      9.2,
        "reviews_count": 340000,
    },
    {
        "title":       "eSIM América — datos en EEUU, México y Latinoamérica",
        "description": "eSIM regional para todo el continente americano. Perfecta para viajes a Nueva York, Cancún, Buenos Aires o cualquier destino de las Américas. Desde 7€.",
        "location":    "América",
        "sale_price":  7.0,
        "image_url":   "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "search_url":  "https://www.airalo.com/americas-esim",
        "category":    "internacional",
        "tipo":        "actividad",
        "discount_pct": 0,
        "rating":      9.2,
        "reviews_count": 340000,
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    urls = list({d["search_url"] for d in _ESIMS})
    affiliate_map = to_affiliate_urls(urls)

    if not affiliate_map:
        log.info("Airalo: sin credenciales válidas de TravelPayouts, omitiendo")
        return []

    deals = []
    for d in _ESIMS[:max_results]:
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
            "source":         "airalo",
            "category":       d["category"],
            "tipo":           d["tipo"],
            "rating":         d["rating"],
            "reviews_count":  d["reviews_count"],
        })

    log.info(f"Airalo: {len(deals)} eSIMs con enlace de afiliado real")
    return deals
