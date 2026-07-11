"""
Expedia scraper para GangaViaje.
Programa "Expedia Spain" (advertiser 5289019) confirmado activo en la cuenta de CJ.
La Product Search API de CJ no tiene feed para este anunciante (igual que Iberostar),
así que se usan los deep-links reales generados manualmente en CJ (Campañas > Enlaces).
Los enlaces usan el formato de deep-link real de CJ: dpbolvw.net/click-{PID}-{LID}.
"""

import logging

import config

log = logging.getLogger(__name__)


def _cj_url(link_id: str) -> str:
    return f"https://www.dpbolvw.net/click-{config.CJ_WEBSITE_ID}-{link_id}"


# Enlaces reales tomados del catálogo de "Campañas > Enlaces" de CJ para Expedia Spain.
_OFERTAS = [
    {
        "link_id":        "15606975",
        "title":          "Ahorra un 25% (¡o más!) en la estancia de tus sueños",
        "description":    "Ofertas de hoteles con hasta un 25% de descuento en Expedia, válidas en miles de destinos.",
        "location":       "España y resto del mundo",
        "original_price": 160.0,
        "sale_price":     120.0,
        "discount_pct":   25,
        "image_url":      "https://images.unsplash.com/photo-1566073771259-6a8506099945?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "hotel",
    },
    {
        "link_id":        "13852544",
        "title":          "Hoteles con cancelación gratuita",
        "description":    "Miles de hoteles en España y el resto del mundo, con cancelación gratuita en la mayoría de reservas.",
        "location":       "España",
        "original_price": None,
        "sale_price":     85.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "espana",
        "tipo":           "hotel",
    },
    {
        "link_id":        "13852545",
        "title":          "Vuelos baratos a todo el mundo",
        "description":    "Compara vuelos de las principales aerolíneas y encuentra el mejor precio para tu próximo viaje.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     64.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "vuelo",
    },
    {
        "link_id":        "13852548",
        "title":          "Vuelo + Hotel — paquetes con descuento",
        "description":    "Reserva vuelo y hotel juntos en Expedia y ahorra frente a reservarlos por separado.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     180.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1488646953014-85cb44e25828?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "vuelo",
    },
    {
        "link_id":        "13852550",
        "title":          "Alquiler de coche — las mejores tarifas",
        "description":    "Compara precios de alquiler de coches en España y el extranjero con cancelación flexible.",
        "location":       "España",
        "original_price": None,
        "sale_price":     28.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1503376780353-7e6692767b70?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "espana",
        "tipo":           "coche",
    },
    {
        "link_id":        "13852552",
        "title":          "Alquileres vacacionales — apartamentos y villas",
        "description":    "Apartamentos y casas vacacionales en playa, ciudad o zona rural con reserva directa en Expedia.",
        "location":       "España",
        "original_price": None,
        "sale_price":     95.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "playa",
        "tipo":           "apartamento",
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    if not config.CJ_WEBSITE_ID:
        log.info("Expedia: sin CJ_WEBSITE_ID configurado, omitiendo")
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
            "source":         "expedia",
            "category":       o["category"],
            "tipo":           o["tipo"],
            "rating":         0.0,
            "reviews_count":  0,
        })

    log.info(f"Expedia: {len(deals)} ofertas con enlace de afiliado real")
    return deals
