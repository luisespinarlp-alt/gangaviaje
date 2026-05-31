"""
Booking scraper para GangaViaje.
Fuente 1: Chollometro RSS filtrado por Booking
Fuente 2: Demo deals con hoteles reales (fallback)
Cuando BOOKING_AFFILIATE_ID está en .env, los links generan comisión.
"""

import logging
import re
import ssl
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

import certifi

import config

log = logging.getLogger(__name__)

_UA  = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
_NS  = {
    "media":  "http://search.yahoo.com/mrss/",
    "pepper": "http://www.pepper.com/rss",
}

CATEGORY_MAP = {
    "viajes":        "espana",
    "hotel":         "espana",
    "hoteles":       "espana",
    "escapada":      "espana",
    "playa":         "playa",
    "rural":         "rural",
    "ciudad":        "ciudad",
    "europa":        "europa",
    "internacional": "internacional",
}


def _affiliate_url(path: str = "", search: str = "") -> str:
    aid = config.BOOKING_AFFILIATE_ID or "304142"
    label = "gangaviaje"
    if path:
        return f"https://www.booking.com{path}?aid={aid}&label={label}"
    query = urllib.parse.quote_plus(search[:80])
    return f"https://www.booking.com/search.es.html?ss={query}&aid={aid}&label={label}"


def _parse_price(price_str: str) -> float | None:
    try:
        cleaned = re.sub(r"[^\d,\.]", "", price_str).replace(",", ".")
        return round(float(cleaned), 2)
    except (ValueError, AttributeError):
        return None


def _from_chollometro(min_discount: int, max_results: int) -> list[dict]:
    ctx = ssl.create_default_context(cafile=certifi.where())
    req = urllib.request.Request(
        "https://www.chollometro.com/rss",
        headers={"User-Agent": _UA}
    )
    try:
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            content = r.read().decode("utf-8", errors="ignore")
    except Exception as e:
        log.warning(f"Chollometro RSS error: {e}")
        return []

    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        return []

    deals = []
    for item in root.findall(".//item"):
        if len(deals) >= max_results:
            break

        merchant = item.find("pepper:merchant", _NS)
        if merchant is None:
            continue
        merchant_name = merchant.get("name", "").lower()
        if "booking" not in merchant_name:
            continue

        price_str  = merchant.get("price", "")
        sale_price = _parse_price(price_str)
        if not sale_price:
            continue

        title   = item.findtext("title", "").strip()
        raw_cat = item.findtext("category", "viajes").lower()
        category = next((v for k, v in CATEGORY_MAP.items() if k in raw_cat), "espana")

        img_el    = item.find("media:content", _NS) or item.find("media:thumbnail", _NS)
        image_url = img_el.get("url", "") if img_el is not None else ""

        desc        = item.findtext("description", "")
        orig_match  = re.search(r"[Aa]ntes[:\s]+([0-9]+[,\.][0-9]+)\s*€", desc)
        orig_price  = _parse_price(orig_match.group(1)) if orig_match else None
        discount    = int((orig_price - sale_price) / orig_price * 100) if orig_price and orig_price > sale_price else 0

        location_match = re.search(r"—\s*(.+?)(?:\s*\d|\s*$)", title)
        location = location_match.group(1).strip() if location_match else ""

        deals.append({
            "title":          title,
            "description":    "",
            "location":       location,
            "original_price": orig_price,
            "sale_price":     sale_price,
            "discount_pct":   discount,
            "image_url":      image_url,
            "affiliate_url":  _affiliate_url(search=title),
            "source":         "booking",
            "category":       category,
            "rating":         0.0,
            "reviews_count":  0,
        })

    log.info(f"Chollometro Booking: {len(deals)} deals encontrados")
    return deals


def _demo_deals() -> list[dict]:
    aid = config.BOOKING_AFFILIATE_ID or "304142"
    label = "gangaviaje"

    return [
        # HOTELES
        {
            "title": "Hotel Arts Barcelona 5 estrellas", "location": "Barcelona",
            "original_price": 420.0, "sale_price": 249.0, "discount_pct": 41,
            "affiliate_url": f"https://www.booking.com/hotel/es/arts-barcelona.es.html?aid={aid}&label={label}",
            "source": "booking", "category": "ciudad", "tipo": "hotel", "rating": 9.2, "reviews_count": 4231,
            "description": "Hotel de lujo frente al mar en Barcelona con vistas espectaculares al Mediterráneo.",
            "image_url": "https://images.unsplash.com/photo-1745186487192-09eccb385169?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
        {
            "title": "Meliá Sevilla 4 estrellas", "location": "Sevilla",
            "original_price": 185.0, "sale_price": 99.0, "discount_pct": 46,
            "affiliate_url": f"https://www.booking.com/hotel/es/melia-sevilla.es.html?aid={aid}&label={label}",
            "source": "booking", "category": "ciudad", "tipo": "hotel", "rating": 8.5, "reviews_count": 2890,
            "description": "En el corazón de Sevilla, a pocos pasos de la Giralda y la Catedral.",
            "image_url": "https://images.unsplash.com/photo-1503757665727-92b48111c1a0?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
        {
            "title": "Hard Rock Hotel Ibiza 5 estrellas", "location": "Ibiza",
            "original_price": 550.0, "sale_price": 319.0, "discount_pct": 42,
            "affiliate_url": f"https://www.booking.com/hotel/es/hard-rock-hotel-ibiza.es.html?aid={aid}&label={label}",
            "source": "booking", "category": "playa", "tipo": "hotel", "rating": 8.9, "reviews_count": 6780,
            "description": "El hotel más icónico de Ibiza con piscina infinita y acceso a la playa.",
            "image_url": "https://images.unsplash.com/photo-1662297260477-4bf319603002?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
        {
            "title": "Parador de Granada 4 estrellas", "location": "Granada",
            "original_price": 380.0, "sale_price": 245.0, "discount_pct": 35,
            "affiliate_url": f"https://www.booking.com/hotel/es/parador-de-granada.es.html?aid={aid}&label={label}",
            "source": "booking", "category": "espana", "tipo": "hotel", "rating": 9.0, "reviews_count": 1870,
            "description": "Dentro del recinto de la Alhambra. Una experiencia histórica única en España.",
            "image_url": "https://images.unsplash.com/photo-1759434613657-422a87ff991a?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
        # APARTAMENTOS
        {
            "title": "Apartamento con vistas al mar en Barceloneta", "location": "Barcelona",
            "original_price": 180.0, "sale_price": 110.0, "discount_pct": 39,
            "affiliate_url": f"https://www.booking.com/searchresults.es.html?ss=Barceloneta&nflt=ht_id%3D201&aid={aid}&label={label}",
            "source": "booking", "category": "playa", "tipo": "apartamento", "rating": 8.7, "reviews_count": 320,
            "description": "Apartamento moderno completamente equipado a 2 minutos de la playa.",
            "image_url": "https://images.unsplash.com/photo-1562766591-80ba2f6feffb?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
        {
            "title": "Apartamento de lujo en Madrid Gran Vía", "location": "Madrid",
            "original_price": 150.0, "sale_price": 89.0, "discount_pct": 41,
            "affiliate_url": f"https://www.booking.com/searchresults.es.html?ss=Madrid+Gran+Via&nflt=ht_id%3D201&aid={aid}&label={label}",
            "source": "booking", "category": "ciudad", "tipo": "apartamento", "rating": 8.4, "reviews_count": 560,
            "description": "Apartamento moderno en el corazón de Madrid con todas las comodidades.",
            "image_url": "https://images.unsplash.com/photo-1543785734-4b6e564642f8?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
        # VILLAS
        {
            "title": "Villa con piscina privada en la Costa del Sol", "location": "Málaga",
            "original_price": 450.0, "sale_price": 279.0, "discount_pct": 38,
            "affiliate_url": f"https://www.booking.com/searchresults.es.html?ss=Costa+del+Sol&nflt=ht_id%3D213&aid={aid}&label={label}",
            "source": "booking", "category": "playa", "tipo": "villa", "rating": 9.1, "reviews_count": 145,
            "description": "Villa independiente con piscina y jardín privado a 500 metros de la playa.",
            "image_url": "https://images.unsplash.com/photo-1437650268498-5a0577e14e10?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
        {
            "title": "Casa rural en la Sierra de Gredos", "location": "Ávila",
            "original_price": 120.0, "sale_price": 75.0, "discount_pct": 37,
            "affiliate_url": f"https://www.booking.com/searchresults.es.html?ss=Sierra+de+Gredos&nflt=ht_id%3D220&aid={aid}&label={label}",
            "source": "booking", "category": "rural", "tipo": "villa", "rating": 9.3, "reviews_count": 89,
            "description": "Casa rural con chimenea, jardín y vistas privilegiadas a la sierra.",
            "image_url": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
        # ATRACCIONES
        {
            "title": "Visita guiada a la Sagrada Família con acceso preferente", "location": "Barcelona",
            "original_price": 65.0, "sale_price": 42.0, "discount_pct": 35,
            "affiliate_url": f"https://www.booking.com/attractions/searchresults/es/barcelona.es.html?aid={aid}&label={label}",
            "source": "booking", "category": "ciudad", "tipo": "actividad", "rating": 9.5, "reviews_count": 12400,
            "description": "Tour oficial con guía experto y acceso sin esperas a la obra maestra de Gaudí.",
            "image_url": "https://images.unsplash.com/photo-1758471206484-0eaa2568320c?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
        {
            "title": "Excursión en catamarán con snorkel en Menorca", "location": "Menorca",
            "original_price": 80.0, "sale_price": 49.0, "discount_pct": 39,
            "affiliate_url": f"https://www.booking.com/attractions/searchresults/es/menorca.es.html?aid={aid}&label={label}",
            "source": "booking", "category": "playa", "tipo": "actividad", "rating": 9.4, "reviews_count": 870,
            "description": "Excursión en catamarán con snorkel en calas cristalinas y comida incluida.",
            "image_url": "https://images.unsplash.com/photo-1562766591-80ba2f6feffb?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
        # COCHES
        {
            "title": "Alquiler de coche — Aeropuerto de Málaga, 7 días", "location": "Málaga",
            "original_price": 280.0, "sale_price": 159.0, "discount_pct": 43,
            "affiliate_url": f"https://www.booking.com/cars/index.es.html?pickup_airport=AGP&aid={aid}&label={label}",
            "source": "booking", "category": "espana", "tipo": "coche", "rating": 8.2, "reviews_count": 2300,
            "description": "Coche compacto con seguro a todo riesgo y kilometraje ilimitado incluido.",
            "image_url": "https://images.unsplash.com/photo-1543785734-4b6e564642f8?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
        {
            "title": "Alquiler de coche — Aeropuerto de Barcelona, 5 días", "location": "Barcelona",
            "original_price": 220.0, "sale_price": 129.0, "discount_pct": 41,
            "affiliate_url": f"https://www.booking.com/cars/index.es.html?pickup_airport=BCN&aid={aid}&label={label}",
            "source": "booking", "category": "ciudad", "tipo": "coche", "rating": 8.0, "reviews_count": 3100,
            "description": "Vehículo económico con cancelación gratuita hasta 48h antes.",
            "image_url": "https://images.unsplash.com/photo-1764107183244-0cef642a99a9?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
    ]


def fetch_deals(min_discount: int = 20, max_results: int = 10) -> list[dict]:
    deals = _from_chollometro(min_discount, max_results)
    if not deals:
        log.info("Booking: sin datos de Chollometro, usando demo")
        deals = _demo_deals()
    return deals[:max_results]
