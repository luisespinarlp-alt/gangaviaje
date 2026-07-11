"""
Booking.com (CEE) scraper para GangaViaje.
Programa "Booking.com Central and Eastern Europe" (advertiser 5096493) confirmado activo en CJ.
La Product Search API de CJ no tiene feed para este anunciante (igual que Expedia/Iberostar):
el catálogo de "Campañas > Enlaces" solo ofrece banners/enlaces de categoría, no hoteles
individuales. Se usan deep-links reales generados manualmente en CJ.
Los enlaces usan el formato de deep-link real de CJ: dpbolvw.net/click-{PID}-{LID}.
"""

import logging

import config

log = logging.getLogger(__name__)


def _cj_url(link_id: str) -> str:
    return f"https://www.dpbolvw.net/click-{config.CJ_WEBSITE_ID}-{link_id}"


# Enlaces reales tomados del catálogo de "Campañas > Enlaces" de CJ para Booking.com CEE.
_OFERTAS = [
    {
        "link_id":        "13386171",
        "title":          "Hoteles con cancelación gratuita",
        "description":    "Millones de alojamientos en todo el mundo, con cancelación gratuita en la mayoría de reservas.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     80.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "hotel",
    },
    {
        "link_id":        "17211504",
        "title":          "Descuentos exclusivos para miembros Genius",
        "description":    "Accede a precios rebajados y ventajas exclusivas en miles de hoteles con el programa Genius de Booking.com.",
        "location":       "España y resto del mundo",
        "original_price": 100.0,
        "sale_price":     80.0,
        "discount_pct":   20,
        "image_url":      "https://images.unsplash.com/photo-1566073771259-6a8506099945?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "hotel",
    },
    {
        "link_id":        "14312908",
        "title":          "Ofertas de viaje — las mejores del momento",
        "description":    "Las mejores rebajas en hoteles, apartamentos y casas vacacionales seleccionadas por Booking.com.",
        "location":       "Europa",
        "original_price": None,
        "sale_price":     65.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "europa",
        "tipo":           "apartamento",
    },
    {
        "link_id":        "17053224",
        "title":          "Vuelos baratos a todo el mundo",
        "description":    "Compara vuelos de cientos de aerolíneas y encuentra el mejor precio para tu próximo viaje.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     58.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "vuelo",
    },
    {
        "link_id":        "17122732",
        "title":          "Alquiler de coche con cancelación gratuita",
        "description":    "Compara precios de alquiler de coches en España y el extranjero con cancelación flexible.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     26.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1503376780353-7e6692767b70?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "coche",
    },
    {
        "link_id":        "17254616",
        "title":          "Entradas y tours sin colas",
        "description":    "Reserva entradas, tours y excursiones en los principales destinos turísticos con Booking.com.",
        "location":       "Europa",
        "original_price": None,
        "sale_price":     24.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "europa",
        "tipo":           "actividad",
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    if not config.CJ_WEBSITE_ID:
        log.info("Booking CEE: sin CJ_WEBSITE_ID configurado, omitiendo")
        return []

    deals = []
    for o in _OFERTAS[:max_results]:
        deals.append({
            "title":          o["title"],
            "description":    o["description"],
            "location":       o["location"],
            "original_price": o["original_price"],
            "sale_price":     o["sale_price"],
            "discount_pct":   o["discount_pct"],
            "image_url":      o["image_url"],
            "affiliate_url":  _cj_url(o["link_id"]),
            "source":         "booking_cee",
            "category":       o["category"],
            "tipo":           o["tipo"],
            "rating":         0.0,
            "reviews_count":  0,
        })

    log.info(f"Booking CEE: {len(deals)} ofertas con enlace de afiliado real")
    return deals
