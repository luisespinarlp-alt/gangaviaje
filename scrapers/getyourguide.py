"""
GetYourGuide scraper para GangaViaje.
Actividades y tours internacionales. El enlace de afiliado (partner_id
FF9KKD8, comisión 8%) es real y genera comisión real al reservar.

IMPORTANTE (2026-07-24): esto es una lista curada a mano, NO datos en vivo.
El código anterior intentaba llamar a "api.getyourguide.com/1/activities"
como si fuera la API real del partner, pero ese endpoint no existe (404
confirmado) — el Partner API real de GetYourGuide es una integración de
marketplace que requiere credenciales propias, no solo el partner_id de
afiliado. Al fallar, el código caía en un fallback silencioso con rating
y número de reseñas inventados (ej. "9.4 · 28.400 reseñas") presentados
como si fueran datos reales de GetYourGuide. Se ha quitado esa falsa
precisión: rating/reviews_count van a 0 hasta que haya una integración
real con el Partner API (ver https://integrator.getyourguide.com).
"""

import logging
import urllib.parse

import config

log = logging.getLogger(__name__)


def _affiliate_url(search: str = "", activity_url: str = "") -> str:
    pid = config.GETYOURGUIDE_PARTNER_ID
    if activity_url:
        base = activity_url if activity_url.startswith("http") else f"https://www.getyourguide.com{activity_url}"
        return f"{base}{'&' if '?' in base else '?'}partner_id={pid}" if pid else base
    query = urllib.parse.quote_plus(search[:80])
    base = f"https://www.getyourguide.com/s/?q={query}"
    return f"{base}&partner_id={pid}" if pid else base


def _actividades() -> list[dict]:
    return [
        {
            "title":          "Coliseo de Roma: entrada sin colas con acceso al Foro Romano",
            "description":    "Visita el monumento más icónico de Roma con acceso prioritario y guía en español.",
            "location":       "Roma",
            "original_price": 65.0,
            "sale_price":     42.0,
            "discount_pct":   35,
            "image_url":      "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url(search="Coliseo Roma entrada"),
            "source":         "getyourguide",
            "category":       "internacional",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "París: crucero por el Sena con cena y música en vivo",
            "description":    "Navega por París de noche con vistas a la Torre Eiffel y cena de 3 platos incluida.",
            "location":       "París",
            "original_price": 110.0,
            "sale_price":     75.0,
            "discount_pct":   32,
            "image_url":      "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url(search="crucero Sena Paris cena"),
            "source":         "getyourguide",
            "category":       "internacional",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Ámsterdam: tour en barco por los canales",
            "description":    "Recorre los canales más bonitos de Ámsterdam a bordo de un barco con techo de cristal.",
            "location":       "Ámsterdam",
            "original_price": 28.0,
            "sale_price":     18.0,
            "discount_pct":   36,
            "image_url":      "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url(search="tour canales Amsterdam barco"),
            "source":         "getyourguide",
            "category":       "internacional",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Londres: tour en autobús hop-on hop-off 24h",
            "description":    "Descubre los mejores monumentos de Londres a tu ritmo con el autobús panorámico.",
            "location":       "Londres",
            "original_price": 45.0,
            "sale_price":     29.0,
            "discount_pct":   36,
            "image_url":      "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url(search="autobus hop on hop off Londres"),
            "source":         "getyourguide",
            "category":       "europa",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Dubái: vuelo en globo aerostático al amanecer",
            "description":    "Vuela sobre el desierto de Dubái al amanecer con vistas espectaculares y desayuno beduino.",
            "location":       "Dubái",
            "original_price": 280.0,
            "sale_price":     195.0,
            "discount_pct":   30,
            "image_url":      "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url(search="vuelo globo aerostatico Dubai"),
            "source":         "getyourguide",
            "category":       "internacional",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Lisboa: tour por el barrio de Alfama y degustación de fado",
            "description":    "Explora el barrio más antiguo de Lisboa y disfruta de una actuación de fado en directo.",
            "location":       "Lisboa",
            "original_price": 55.0,
            "sale_price":     38.0,
            "discount_pct":   31,
            "image_url":      "https://images.unsplash.com/photo-1548707309-dcebeab9ea9b?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url(search="tour Alfama Lisboa fado"),
            "source":         "getyourguide",
            "category":       "europa",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Marrakech: excursión de un día al desierto del Sáhara",
            "description":    "Viaje en 4x4 al Sáhara, paseo en camello y noche en jaima con cena tradicional.",
            "location":       "Marrakech",
            "original_price": 120.0,
            "sale_price":     82.0,
            "discount_pct":   32,
            "image_url":      "https://images.unsplash.com/photo-1542401886-65d6c61db217?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url(search="excursion Sahara Marrakech desierto"),
            "source":         "getyourguide",
            "category":       "internacional",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Praga: crucero al atardecer con cena y música clásica",
            "description":    "Navega por el Moldava al atardecer con cena buffet y concierto de música checa en vivo.",
            "location":       "Praga",
            "original_price": 70.0,
            "sale_price":     48.0,
            "discount_pct":   31,
            "image_url":      "https://images.unsplash.com/photo-1541849546-216549ae216d?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url(search="crucero cena Praga Moldava"),
            "source":         "getyourguide",
            "category":       "europa",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
    ]


def fetch_deals(min_discount: int = 25, max_results: int = 10) -> list[dict]:
    if not config.GETYOURGUIDE_PARTNER_ID:
        log.info("GetYourGuide: sin GETYOURGUIDE_PARTNER_ID, omitiendo")
        return []
    deals = [d for d in _actividades() if d["discount_pct"] >= min_discount]
    log.info(f"GetYourGuide: {len(deals)} actividades curadas con enlace de afiliado real")
    return deals[:max_results]
