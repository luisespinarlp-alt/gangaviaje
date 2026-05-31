"""
GetYourGuide scraper para GangaViaje.
Actividades y tours internacionales con comisión del 8%.
Cuando GETYOURGUIDE_PARTNER_ID está en .env, los links generan comisión.
"""

import logging
import ssl
import json
import urllib.request
import urllib.parse

import certifi
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


def _demo_deals() -> list[dict]:
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
            "rating":         9.4,
            "reviews_count":  28400,
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
            "rating":         9.2,
            "reviews_count":  15600,
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
            "rating":         9.1,
            "reviews_count":  22300,
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
            "rating":         8.8,
            "reviews_count":  31200,
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
            "rating":         9.6,
            "reviews_count":  8900,
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
            "rating":         9.3,
            "reviews_count":  11400,
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
            "rating":         9.5,
            "reviews_count":  6700,
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
            "rating":         9.0,
            "reviews_count":  9200,
        },
    ]


def fetch_deals(min_discount: int = 25, max_results: int = 10) -> list[dict]:
    if not config.GETYOURGUIDE_PARTNER_ID:
        log.info("GetYourGuide: modo demo (sin GETYOURGUIDE_PARTNER_ID)")
        return _demo_deals()[:max_results]

    try:
        ctx = ssl.create_default_context(cafile=certifi.where())
        url = (f"https://api.getyourguide.com/1/activities"
               f"?currency=EUR&language=es&limit={max_results}"
               f"&partner_id={config.GETYOURGUIDE_PARTNER_ID}")
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
        })
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            data = json.loads(r.read())

        deals = []
        for item in data.get("data", {}).get("activities", []):
            price      = float(item.get("price", {}).get("values", {}).get("amount", 0))
            orig_price = float(item.get("original_price", {}).get("values", {}).get("amount", price))
            discount   = int((orig_price - price) / orig_price * 100) if orig_price > price else 0
            if discount < min_discount or not price:
                continue
            deals.append({
                "title":          item.get("title", ""),
                "description":    item.get("abstract", "")[:200],
                "location":       item.get("location", {}).get("city", ""),
                "original_price": orig_price,
                "sale_price":     price,
                "discount_pct":   discount,
                "image_url":      (item.get("pictures") or [{}])[0].get("url", ""),
                "affiliate_url":  _affiliate_url(activity_url=item.get("url", "")),
                "source":         "getyourguide",
                "category":       "internacional",
                "tipo":           "actividad",
                "rating":         float(item.get("overall_rating", {}).get("average", 0)),
                "reviews_count":  int(item.get("number_of_ratings", 0)),
            })
        log.info(f"GetYourGuide API: {len(deals)} actividades encontradas")
        return deals
    except Exception as e:
        log.warning(f"GetYourGuide API error: {e} — usando demo")
        return _demo_deals()[:max_results]
