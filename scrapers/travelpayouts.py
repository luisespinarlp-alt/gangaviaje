"""
TravelPayouts scraper para GangaViaje.
Vuelos baratos vía la Data API de Aviasales (api.travelpayouts.com/v1/prices/cheap).
Cuando TRAVELPAYOUTS_TOKEN y TRAVELPAYOUTS_MARKER están en .env, se usan datos reales
y los links generan comisión. Sin token, usa demo deals con vuelos de ejemplo.
"""

import json
import logging
import ssl
import urllib.parse
import urllib.request

import certifi

import config

log = logging.getLogger(__name__)

_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

# Origen España → destinos populares con su categoría en la web
ORIGINS = ["MAD", "BCN", "VLC", "AGP", "PMI", "BIO", "SVQ"]

_ORIGIN_NAMES = {
    "MAD": "Madrid", "BCN": "Barcelona", "VLC": "Valencia", "AGP": "Málaga",
    "PMI": "Palma de Mallorca", "BIO": "Bilbao", "SVQ": "Sevilla",
}

DESTINATIONS = [
    ("PAR", "París",        "europa"),
    ("ROM", "Roma",         "europa"),
    ("LIS", "Lisboa",       "europa"),
    ("AMS", "Ámsterdam",    "europa"),
    ("LON", "Londres",      "europa"),
    ("BER", "Berlín",       "europa"),
    ("VIE", "Viena",        "europa"),
    ("PRG", "Praga",        "europa"),
    ("DUB", "Dublín",       "europa"),
    ("ATH", "Atenas",       "europa"),
    ("IST", "Estambul",     "internacional"),
    ("NYC", "Nueva York",   "internacional"),
    ("BKK", "Bangkok",      "internacional"),
    ("DXB", "Dubái",        "internacional"),
    ("RAK", "Marrakech",    "internacional"),
    ("CUN", "Cancún",       "internacional"),
    ("BRU", "Bruselas",     "europa"),
    ("BUD", "Budapest",     "europa"),
    ("MIL", "Milán",        "europa"),
    ("TYO", "Tokio",        "internacional"),
    ("MIA", "Miami",        "internacional"),
    ("BUE", "Buenos Aires", "internacional"),
    ("VCE", "Venecia",      "europa"),
]

_DEST_IMAGES = {
    "PAR": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "ROM": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "LIS": "https://images.unsplash.com/photo-1548707309-dcebeab9ea9b?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "AMS": "https://images.unsplash.com/photo-1576924542622-772281b13aa8?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "LON": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "BER": "https://images.unsplash.com/photo-1560969184-10fe8719e047?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "VIE": "https://images.unsplash.com/photo-1516550893923-42d28e5677af?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "PRG": "https://images.unsplash.com/photo-1541849546-216549ae216d?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "DUB": "https://images.unsplash.com/photo-1549918864-48ac978761a4?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "ATH": "https://images.unsplash.com/photo-1555993539-1732b0258235?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "IST": "https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "NYC": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "BKK": "https://images.unsplash.com/photo-1508009603885-50cf7c579365?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "DXB": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "RAK": "https://images.unsplash.com/photo-1542401886-65d6c61db217?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "CUN": "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "BRU": "https://images.unsplash.com/photo-1559113202-c916b8e44373?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "BUD": "https://images.unsplash.com/photo-1551867633-194f125bddfa?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "MIL": "https://images.unsplash.com/photo-1513581166391-887a96ddeafd?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "TYO": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "MIA": "https://images.unsplash.com/photo-1506966953602-c20cc11f75e3?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "BUE": "https://images.unsplash.com/photo-1589909202802-8f4aadce1849?fm=jpg&q=80&w=800&auto=format&fit=crop",
    "VCE": "https://images.unsplash.com/photo-1534113414509-0eec2bfb493f?fm=jpg&q=80&w=800&auto=format&fit=crop",
}


def _affiliate_url(origin: str, destination: str, depart_date: str = "") -> str:
    marker = config.TRAVELPAYOUTS_MARKER
    params = {"origin_iata": origin, "destination_iata": destination, "currency": "eur"}
    if depart_date:
        params["depart_date"] = depart_date
    if marker:
        params["marker"] = marker
    return f"https://www.aviasales.com/search?{urllib.parse.urlencode(params)}"


def _demo_deals() -> list[dict]:
    demo = [
        ("MAD", "PAR", "París",     89.0,  "europa"),
        ("BCN", "ROM", "Roma",      75.0,  "europa"),
        ("MAD", "LIS", "Lisboa",    49.0,  "europa"),
        ("BCN", "AMS", "Ámsterdam", 95.0,  "europa"),
        ("MAD", "LON", "Londres",   69.0,  "europa"),
        ("BCN", "IST", "Estambul",  110.0, "internacional"),
        ("MAD", "NYC", "Nueva York", 340.0, "internacional"),
        ("BCN", "BKK", "Bangkok",   480.0, "internacional"),
    ]
    deals = []
    for origin, dest, name, price, category in demo:
        deals.append({
            "title":          f"Vuelo {('Madrid' if origin == 'MAD' else 'Barcelona')} → {name}",
            "description":    f"Vuelo ida y vuelta a {name} al mejor precio encontrado por Aviasales.",
            "location":       name,
            "original_price": None,
            "sale_price":     price,
            "discount_pct":   0,
            "image_url":      "",
            "affiliate_url":  _affiliate_url(origin, dest),
            "source":         "travelpayouts",
            "category":       category,
            "tipo":           "vuelo",
            "rating":         0.0,
            "reviews_count":  0,
        })
    return deals


def _fetch_cheapest(origin: str, destination: str) -> dict | None:
    params = {
        "origin": origin,
        "destination": destination,
        "currency": "eur",
        "token": config.TRAVELPAYOUTS_TOKEN,
    }
    url = f"https://api.travelpayouts.com/v1/prices/cheap?{urllib.parse.urlencode(params)}"
    ctx = ssl.create_default_context(cafile=certifi.where())
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    try:
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            data = json.loads(r.read().decode("utf-8"))
    except Exception as e:
        log.warning(f"TravelPayouts API error ({origin}->{destination}): {e}")
        return None

    if not data.get("success"):
        return None
    dest_data = data.get("data", {}).get(destination)
    if not dest_data:
        return None
    cheapest = min(dest_data.values(), key=lambda d: d.get("price", float("inf")))
    return cheapest


def fetch_deals(min_discount: int = 20, max_results: int = 10) -> list[dict]:
    if not config.TRAVELPAYOUTS_TOKEN:
        log.info("TravelPayouts: sin token configurado, usando demo")
        return _demo_deals()[:max_results]

    deals = []
    for origin in ORIGINS:
        for dest_code, dest_name, category in DESTINATIONS:
            if len(deals) >= max_results:
                break
            flight = _fetch_cheapest(origin, dest_code)
            if not flight:
                continue
            depart_date = (flight.get("departure_at") or "")[:10]
            deals.append({
                "title":          f"Vuelo {_ORIGIN_NAMES.get(origin, origin)} → {dest_name}",
                "description":    f"Vuelo encontrado por Aviasales con {flight.get('airline', '')} "
                                   f"({flight.get('number_of_changes', 0)} escalas).",
                "location":       dest_name,
                "original_price": None,
                "sale_price":     round(flight["price"], 2),
                "discount_pct":   0,
                "image_url":      _DEST_IMAGES.get(dest_code, ""),
                "affiliate_url":  _affiliate_url(origin, dest_code, depart_date),
                "source":         "travelpayouts",
                "category":       category,
                "tipo":           "vuelo",
                "rating":         0.0,
                "reviews_count":  0,
            })

    if not deals:
        log.info("TravelPayouts: sin resultados de la API, usando demo")
        return _demo_deals()[:max_results]

    log.info(f"TravelPayouts: {len(deals)} vuelos encontrados")
    return deals[:max_results]
