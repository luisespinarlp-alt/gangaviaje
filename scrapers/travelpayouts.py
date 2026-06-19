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
]


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
                "image_url":      "",
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
