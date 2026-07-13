"""
Centauro Rent a Car EU (CJ advertiser 5371583) — deep-links manuales.
Comisión: 6% sobre reserva. Sin feed de producto en CJ, solo enlaces de categoría.
"""

import logging
import config

log = logging.getLogger(__name__)

_PID = config.CJ_WEBSITE_ID


def _cj_url(link_id: int) -> str:
    return f"https://www.dpbolvw.net/click-{_PID}-{link_id}"


def fetch_deals(min_discount: int = 20, max_results: int = 10) -> list[dict]:
    if not config.CJ_WEBSITE_ID:
        log.info("Centauro: sin CJ_WEBSITE_ID configurado")
        return []

    deals = [
        {
            "title":          "Alquiler de coche en España — Mejores precios garantizados",
            "description":    "Alquila un coche en los principales aeropuertos y ciudades de España. Amplia flota, sin sorpresas, cancelación gratuita.",
            "location":       "España",
            "original_price": 35.0,
            "sale_price":     22.0,
            "discount_pct":   37,
            "image_url":      "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _cj_url(15165285),
            "source":         "centauro",
            "category":       "espana",
            "tipo":           "coche",
            "rating":         8.4,
            "reviews_count":  0,
        },
        {
            "title":          "Alquiler de coche en Portugal — Ofertas exclusivas",
            "description":    "Recorre Portugal en coche con las mejores tarifas. Recogida en Lisboa, Oporto y Faro. Incluye seguro básico.",
            "location":       "Portugal",
            "original_price": 33.0,
            "sale_price":     21.0,
            "discount_pct":   36,
            "image_url":      "https://images.unsplash.com/photo-1548707309-dcebeab9ea9b?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _cj_url(15725509),
            "source":         "centauro",
            "category":       "europa",
            "tipo":           "coche",
            "rating":         8.2,
            "reviews_count":  0,
        },
        {
            "title":          "Alquiler de coche en Italia — Desde los principales aeropuertos",
            "description":    "Explora Italia a tu ritmo. Recogida en Roma, Milán, Venecia y más de 50 puntos en todo el país.",
            "location":       "Italia",
            "original_price": 45.0,
            "sale_price":     29.0,
            "discount_pct":   36,
            "image_url":      "https://images.unsplash.com/photo-1529260830199-42c24126f198?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _cj_url(15165267),
            "source":         "centauro",
            "category":       "europa",
            "tipo":           "coche",
            "rating":         8.1,
            "reviews_count":  0,
        },
        {
            "title":          "Alquiler de coche en Francia — Las mejores tarifas",
            "description":    "Viaja por Francia con total libertad. Recogida en París, Niza, Lyon y otros destinos. Flota moderna y segura.",
            "location":       "Francia",
            "original_price": 48.0,
            "sale_price":     31.0,
            "discount_pct":   35,
            "image_url":      "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _cj_url(15725511),
            "source":         "centauro",
            "category":       "europa",
            "tipo":           "coche",
            "rating":         8.0,
            "reviews_count":  0,
        },
        {
            "title":          "Alquiler de coche en Alemania — Precio especial online",
            "description":    "Descubre Alemania en coche. Recogida en Berlín, Múnich, Frankfurt y más ciudades. Reserva ahora y ahorra.",
            "location":       "Alemania",
            "original_price": 46.0,
            "sale_price":     29.0,
            "discount_pct":   37,
            "image_url":      "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _cj_url(15725514),
            "source":         "centauro",
            "category":       "europa",
            "tipo":           "coche",
            "rating":         8.3,
            "reviews_count":  0,
        },
        {
            "title":          "Alquiler de coche en Europa — Compara y ahorra",
            "description":    "Las mejores tarifas de alquiler de coches en más de 100 destinos europeos. Sin cargos ocultos, cancelación flexible.",
            "location":       "Europa",
            "original_price": 42.0,
            "sale_price":     27.0,
            "discount_pct":   36,
            "image_url":      "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _cj_url(15735349),
            "source":         "centauro",
            "category":       "europa",
            "tipo":           "coche",
            "rating":         8.3,
            "reviews_count":  0,
        },
    ]

    filtered = [d for d in deals if d["discount_pct"] >= min_discount]
    log.info(f"Centauro: {len(filtered)} ofertas de coches")
    return filtered[:max_results]
