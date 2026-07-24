"""
Civitatis scraper para GangaViaje.
Actividades, tours y excursiones en español con comisión del 6-8%.
Actualmente INACTIVO (falta CIVITATIS_AFFILIATE_ID en .env).

IMPORTANTE (2026-07-24): igual que se detectó en getyourguide.py, el
endpoint "api.civitatis.com/api/activities" que usaba esta fuente
devolvía 404 — no era un endpoint real. El acceso a datos en vivo de
Civitatis requiere pasar por su Portal de Partners
(connectivity.civitatis.com) y contacto directo
(partnerships@civitatis.com), no un endpoint público adivinado. Se ha
quitado ese intento de API rota; _demo_deals() ya no rellena
rating/reviews_count con cifras inventadas — son ejemplos curados con
enlace de afiliado real, no datos de reseñas en vivo de Civitatis.
"""

import logging

import config

log = logging.getLogger(__name__)


def _affiliate_url(path: str) -> str:
    aid = config.CIVITATIS_AFFILIATE_ID
    base = f"https://www.civitatis.com{path}"
    if aid:
        return f"{base}?aid={aid}"
    return base


def _demo_deals() -> list[dict]:
    return [
        {
            "title":          "Tour privado por la Sagrada Família con acceso sin colas",
            "description":    "Visita guiada en español a la obra maestra de Gaudí con guía experto y acceso preferente.",
            "location":       "Barcelona",
            "original_price": 89.0,
            "sale_price":     59.0,
            "discount_pct":   34,
            "image_url":      "https://images.unsplash.com/photo-1758471206484-0eaa2568320c?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url("/es/barcelona/visita-sagrada-familia/"),
            "source":         "civitatis",
            "category":       "ciudad",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Espectáculo de flamenco en Sevilla con bebida incluida",
            "description":    "Vive el flamenco auténtico en uno de los tablaos más reconocidos de Sevilla.",
            "location":       "Sevilla",
            "original_price": 55.0,
            "sale_price":     38.0,
            "discount_pct":   31,
            "image_url":      "https://images.unsplash.com/photo-1503757665727-92b48111c1a0?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url("/es/sevilla/espectaculo-flamenco/"),
            "source":         "civitatis",
            "category":       "ciudad",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Visita guiada a la Alhambra con Palacios Nazaríes",
            "description":    "Descubre la Alhambra con un guía local experto. Incluye acceso a los Palacios Nazaríes.",
            "location":       "Granada",
            "original_price": 75.0,
            "sale_price":     49.0,
            "discount_pct":   35,
            "image_url":      "https://images.unsplash.com/photo-1759434613657-422a87ff991a?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url("/es/granada/visita-alhambra-palacios-nazaries/"),
            "source":         "civitatis",
            "category":       "ciudad",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Tour por el Madrid de los Austrias y el Madrid de los Borbones",
            "description":    "Recorre los rincones más históricos de Madrid con un guía apasionado.",
            "location":       "Madrid",
            "original_price": 45.0,
            "sale_price":     29.0,
            "discount_pct":   36,
            "image_url":      "https://images.unsplash.com/photo-1543785734-4b6e564642f8?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url("/es/madrid/tour-madrid-austrias-borbones/"),
            "source":         "civitatis",
            "category":       "ciudad",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Excursión en catamarán por la costa de Mallorca con snorkel",
            "description":    "Navega por las calas más espectaculares de Mallorca. Comida y bebida incluidas.",
            "location":       "Mallorca",
            "original_price": 95.0,
            "sale_price":     65.0,
            "discount_pct":   32,
            "image_url":      "https://images.unsplash.com/photo-1562766591-80ba2f6feffb?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url("/es/mallorca/excursion-catamaran-snorkel/"),
            "source":         "civitatis",
            "category":       "playa",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Ticket Museu Picasso Barcelona — Sin colas",
            "description":    "Entrada directa al museo con la colección más completa de Picasso del mundo.",
            "location":       "Barcelona",
            "original_price": 35.0,
            "sale_price":     22.0,
            "discount_pct":   37,
            "image_url":      "https://images.unsplash.com/photo-1745186487192-09eccb385169?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url("/es/barcelona/entrada-museo-picasso/"),
            "source":         "civitatis",
            "category":       "ciudad",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Paseo en barco al atardecer por Ibiza",
            "description":    "Navega alrededor de la isla al atardecer con cócteles y música lounge.",
            "location":       "Ibiza",
            "original_price": 80.0,
            "sale_price":     55.0,
            "discount_pct":   31,
            "image_url":      "https://images.unsplash.com/photo-1662297260477-4bf319603002?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url("/es/ibiza/paseo-barco-atardecer/"),
            "source":         "civitatis",
            "category":       "playa",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
        {
            "title":          "Tour nocturno por el Barrio Gótico de Barcelona",
            "description":    "Descubre los secretos y leyendas del Barrio Gótico de noche con guía experto.",
            "location":       "Barcelona",
            "original_price": 40.0,
            "sale_price":     25.0,
            "discount_pct":   38,
            "image_url":      "https://images.unsplash.com/photo-1764107183244-0cef642a99a9?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _affiliate_url("/es/barcelona/tour-nocturno-barrio-gotico/"),
            "source":         "civitatis",
            "category":       "ciudad",
            "tipo":           "actividad",
            "rating":         0.0,
            "reviews_count":  0,
        },
    ]


def fetch_deals(min_discount: int = 25, max_results: int = 10) -> list[dict]:
    if not config.CIVITATIS_AFFILIATE_ID:
        log.info("Civitatis: sin CIVITATIS_AFFILIATE_ID, omitiendo")
        return []
    deals = [d for d in _demo_deals() if d["discount_pct"] >= min_discount]
    log.info(f"Civitatis: {len(deals)} actividades curadas con enlace de afiliado real")
    return deals[:max_results]
