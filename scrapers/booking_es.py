"""
Booking.com ES scraper para GangaViaje.
Programa "Booking.com ES" (advertiser 4347393) — aprobado en CJ el 2026-07-08.
EPC 7 días: 18,49€ (hoteles), 25,75€ (coches). Comisión: 4% hoteles, 6% coches.
Deep-links reales de Campañas > Enlaces en CJ.
"""

import logging
import config

log = logging.getLogger(__name__)


def _cj_url(link_id: str) -> str:
    return f"https://www.dpbolvw.net/click-{config.CJ_WEBSITE_ID}-{link_id}"


_OFERTAS = [
    {
        "link_id":        "11891543",
        "title":          "Hoteles en Booking.com — Cancelación gratis en la mayoría",
        "description":    "Más de 2,3 millones de alojamientos en todo el mundo. Cancela gratis en la mayoría de reservas y paga en el hotel.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     85.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "hotel",
    },
    {
        "link_id":        "17259345",
        "title":          "Booking.com: al menos 15% de descuento en estancias seleccionadas",
        "description":    "Ofertas Getaway 2026: consigue al menos un 15% de descuento en una selección de hoteles. Válido hasta el 30 de septiembre de 2026.",
        "location":       "España y resto del mundo",
        "original_price": 120.0,
        "sale_price":     102.0,
        "discount_pct":   15,
        "image_url":      "https://images.unsplash.com/photo-1566073771259-6a8506099945?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "hotel",
    },
    {
        "link_id":        "17211509",
        "title":          "Booking.com Genius: descuentos exclusivos para miembros",
        "description":    "Accede a precios rebajados y ventajas como desayuno gratis y upgrade de habitación con el programa de fidelidad Genius.",
        "location":       "España y resto del mundo",
        "original_price": 100.0,
        "sale_price":     80.0,
        "discount_pct":   20,
        "image_url":      "https://images.unsplash.com/photo-1455587734955-081b22074882?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "hotel",
    },
    {
        "link_id":        "15734352",
        "title":          "Apartamentos y alojamientos únicos en Booking.com",
        "description":    "Desde apartamentos hasta casas en los árboles: encuentra el alojamiento perfecto para tu próximo viaje con Booking.com.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     70.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "apartamento",
    },
    {
        "link_id":        "17053226",
        "title":          "Vuelos baratos con Booking.com — +500 aerolíneas",
        "description":    "Compara vuelos de más de 500 aerolíneas en 10.000 destinos y encuentra el mejor precio para tu próximo viaje.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     65.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "vuelo",
    },
    {
        "link_id":        "17122734",
        "title":          "Alquiler de coche con Booking.com — +800 proveedores",
        "description":    "Compara precios de alquiler de coches en más de 50.000 ubicaciones con cancelación flexible y sin cargos ocultos.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     28.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1503376780353-7e6692767b70?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "coche",
    },
    {
        "link_id":        "17254651",
        "title":          "Atracciones y experiencias con Booking.com",
        "description":    "Entradas, tours y experiencias en más de 2.300 ciudades. Reserva sin complicaciones y cancela gratis.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     22.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "actividad",
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    if not config.CJ_WEBSITE_ID:
        log.info("Booking ES: sin CJ_WEBSITE_ID configurado, omitiendo")
        return []

    deals = []
    for o in _OFERTAS[:max_results]:
        if o["discount_pct"] >= min_discount or o["discount_pct"] == 0:
            deals.append({
                "title":          o["title"],
                "description":    o["description"],
                "location":       o["location"],
                "original_price": o["original_price"],
                "sale_price":     o["sale_price"],
                "discount_pct":   o["discount_pct"],
                "image_url":      o["image_url"],
                "affiliate_url":  _cj_url(o["link_id"]),
                "source":         "booking_es",
                "category":       o["category"],
                "tipo":           o["tipo"],
                "rating":         0.0,
                "reviews_count":  0,
            })

    log.info(f"Booking ES: {len(deals)} ofertas con enlace de afiliado real")
    return deals
