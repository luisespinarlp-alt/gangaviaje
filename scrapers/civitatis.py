"""
Civitatis scraper para GangaViaje.
Actividades, tours y excursiones en español con comisión del 6-8%.
Cuando CIVITATIS_AFFILIATE_ID está en .env, los links generan comisión.
"""

import logging
import ssl
import json
import urllib.request
import urllib.parse

import certifi
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
            "rating":         9.6,
            "reviews_count":  18420,
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
            "rating":         9.4,
            "reviews_count":  7230,
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
            "rating":         9.7,
            "reviews_count":  14800,
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
            "rating":         9.3,
            "reviews_count":  9650,
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
            "rating":         9.5,
            "reviews_count":  4310,
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
            "rating":         9.2,
            "reviews_count":  6780,
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
            "rating":         9.4,
            "reviews_count":  2890,
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
            "rating":         9.1,
            "reviews_count":  5120,
        },
    ]


def fetch_deals(min_discount: int = 25, max_results: int = 10) -> list[dict]:
    """Devuelve deals de Civitatis. Con API key usa la API real, si no usa demo."""
    if not config.CIVITATIS_AFFILIATE_ID:
        log.info("Civitatis: modo demo (sin CIVITATIS_AFFILIATE_ID)")
        return _demo_deals()[:max_results]

    # Con affiliate ID: API real de Civitatis
    try:
        ctx = ssl.create_default_context(cafile=certifi.where())
        url = (f"https://api.civitatis.com/api/activities"
               f"?lang=es&countryId=5&page=1&affiliateId={config.CIVITATIS_AFFILIATE_ID}")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            data = json.loads(r.read())

        deals = []
        for item in data.get("rows", [])[:max_results]:
            price      = float(item.get("price", 0))
            orig_price = float(item.get("originalPrice", price))
            discount   = int((orig_price - price) / orig_price * 100) if orig_price > price else 0
            if discount < min_discount:
                continue
            deals.append({
                "title":          item.get("name", ""),
                "description":    item.get("description", "")[:200],
                "location":       item.get("city", {}).get("name", ""),
                "original_price": orig_price,
                "sale_price":     price,
                "discount_pct":   discount,
                "image_url":      item.get("image", ""),
                "affiliate_url":  _affiliate_url(item.get("url", "/")),
                "source":         "civitatis",
                "category":       "ciudad",
                "tipo":           "actividad",
                "rating":         float(item.get("rating", 0)),
                "reviews_count":  int(item.get("numComments", 0)),
            })
        log.info(f"Civitatis API: {len(deals)} actividades encontradas")
        return deals
    except Exception as e:
        log.warning(f"Civitatis API error: {e} — usando demo")
        return _demo_deals()[:max_results]
