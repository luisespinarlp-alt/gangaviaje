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


def _deep_url(destination: str) -> str:
    """Evergreen deep-link a búsqueda de ciudad en Booking.com ES."""
    import urllib.parse
    booking_url = f"https://www.booking.com/searchresults.es.html?ss={urllib.parse.quote(destination)}&lang=es"
    return f"https://www.anrdoezrs.net/click-{config.CJ_WEBSITE_ID}-15734352?url={urllib.parse.quote(booking_url)}"


_OFERTAS = [
    {
        "link_id":        "11891543",
        "title":          "Hoteles con cancelación gratuita",
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
        "title":          "Al menos 15% de descuento en estancias seleccionadas",
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
        "title":          "Descuentos exclusivos para miembros Genius",
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
        "title":          "Apartamentos y alojamientos únicos",
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
        "title":          "Vuelos baratos a todo el mundo — +500 aerolíneas",
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
        "title":          "Alquiler de coche — cancelación gratuita incluida",
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
        "title":          "Entradas y tours sin colas en los mejores destinos",
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

# Hoteles por ciudad usando deep-link Evergreen
_HOTELES_CIUDAD = [
    {
        "dest":           "Madrid",
        "title":          "Hoteles en Madrid",
        "sale_price":     75.0,
        "original_price": 95.0,
        "discount_pct":   21,
        "image_url":      "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "espana",
        "tipo":           "hotel",
    },
    {
        "dest":           "Barcelona",
        "title":          "Hoteles en Barcelona",
        "sale_price":     90.0,
        "original_price": 115.0,
        "discount_pct":   22,
        "image_url":      "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "espana",
        "tipo":           "hotel",
    },
    {
        "dest":           "Paris",
        "title":          "Hoteles en París",
        "sale_price":     110.0,
        "original_price": 140.0,
        "discount_pct":   21,
        "image_url":      "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "europa",
        "tipo":           "hotel",
    },
    {
        "dest":           "Rome",
        "title":          "Hoteles en Roma",
        "sale_price":     95.0,
        "original_price": 120.0,
        "discount_pct":   21,
        "image_url":      "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "europa",
        "tipo":           "hotel",
    },
    {
        "dest":           "Lisbon",
        "title":          "Hoteles en Lisboa",
        "sale_price":     70.0,
        "original_price": 90.0,
        "discount_pct":   22,
        "image_url":      "https://images.unsplash.com/photo-1548707309-dcebeab9ea9b?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "europa",
        "tipo":           "hotel",
    },
    {
        "dest":           "Amsterdam",
        "title":          "Hoteles en Ámsterdam",
        "sale_price":     105.0,
        "original_price": 135.0,
        "discount_pct":   22,
        "image_url":      "https://images.unsplash.com/photo-1459679749680-18eb1eb37418?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "europa",
        "tipo":           "hotel",
    },
    {
        "dest":           "Berlin",
        "title":          "Hoteles en Berlín",
        "sale_price":     80.0,
        "original_price": 100.0,
        "discount_pct":   20,
        "image_url":      "https://images.unsplash.com/photo-1560969184-10fe8719e047?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "europa",
        "tipo":           "hotel",
    },
    {
        "dest":           "Dubai",
        "title":          "Hoteles en Dubái",
        "sale_price":     120.0,
        "original_price": 155.0,
        "discount_pct":   23,
        "image_url":      "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
        "tipo":           "hotel",
    },
    {
        "dest":           "Malaga",
        "title":          "Hoteles en Málaga",
        "sale_price":     65.0,
        "original_price": 85.0,
        "discount_pct":   24,
        "image_url":      "https://images.unsplash.com/photo-1559827260-dc66d52bef19?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "espana",
        "tipo":           "hotel",
    },
    {
        "dest":           "Sevilla",
        "title":          "Hoteles en Sevilla",
        "sale_price":     70.0,
        "original_price": 90.0,
        "discount_pct":   22,
        "image_url":      "https://images.unsplash.com/photo-1503376780353-7e6692767b70?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "espana",
        "tipo":           "hotel",
    },
    {
        "dest":           "Valencia",
        "title":          "Hoteles en Valencia",
        "sale_price":     60.0,
        "original_price": 78.0,
        "discount_pct":   23,
        "image_url":      "https://images.unsplash.com/photo-1555881400-74d7acaacd8b?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "espana",
        "tipo":           "hotel",
    },
    {
        "dest":           "Prague",
        "title":          "Hoteles en Praga",
        "sale_price":     65.0,
        "original_price": 85.0,
        "discount_pct":   24,
        "image_url":      "https://images.unsplash.com/photo-1541849546-216549ae216d?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "europa",
        "tipo":           "hotel",
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 30) -> list[dict]:
    if not config.CJ_WEBSITE_ID:
        log.info("Booking ES: sin CJ_WEBSITE_ID configurado, omitiendo")
        return []

    deals = []

    # Ofertas generales
    for o in _OFERTAS:
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

    # Hoteles por ciudad con deep-link
    for h in _HOTELES_CIUDAD:
        if h["discount_pct"] >= min_discount:
            deals.append({
                "title":          h["title"],
                "description":    f"Encuentra el hotel perfecto en {h['dest']} con cancelación gratuita en la mayoría de opciones. Más de 2,3 millones de alojamientos disponibles.",
                "location":       h["dest"],
                "original_price": h["original_price"],
                "sale_price":     h["sale_price"],
                "discount_pct":   h["discount_pct"],
                "image_url":      h["image_url"],
                "affiliate_url":  _deep_url(h["dest"]),
                "source":         "booking_es",
                "category":       h["category"],
                "tipo":           h["tipo"],
                "rating":         0.0,
                "reviews_count":  0,
            })

    log.info(f"Booking ES: {len(deals)} ofertas ({len(_OFERTAS)} generales + {len(_HOTELES_CIUDAD)} hoteles ciudad)")
    return deals[:max_results]
