"""
Iberia scraper para GangaViaje.
Programa "IBERIA EU" (advertiser 4455265) — aprobado en CJ el 2026-07-24.
Enlaces reales del catálogo CJ (Campañas > Enlaces), mercado España, sin banners.
Restricción del programa: no se permiten códigos de cupón, solo ofertas con precio
(p.ej. "Vuelos a Madrid desde 20€"), así que los precios aquí son de partida orientativos.
"""

import logging

import config

log = logging.getLogger(__name__)


def _cj_url(link_id: str, sid: str = None) -> str:
    """sid = CJ Sub ID opcional: no cambia el destino del enlace ni la comisión,
    solo distingue URLs en nuestra BD cuando varios destinos comparten el mismo
    link_id (p.ej. varias ciudades italianas apuntan a la única landing de Italia)."""
    url = f"https://www.dpbolvw.net/click-{config.CJ_WEBSITE_ID}-{link_id}"
    if sid:
        url += f"?sid={sid}"
    return url


_OFERTAS = [
    {
        "link_id":        "17327726",
        "title":          "Últimos días: Ofertas de Verano de Iberia",
        "description":    "Campaña de ofertas de verano con vuelos para julio y agosto. Promoción activa hasta el 30 de julio de 2026.",
        "location":       "España y Europa",
        "original_price": 55.0,
        "sale_price":     39.0,
        "discount_pct":   29,
        "image_url":      "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "espana",
    },
    {
        "link_id":        "15466012",
        "title":          "Vuelos con Iberia desde España",
        "description":    "Vuelos nacionales e internacionales con la aerolínea de bandera española. Encuentra tu mejor precio.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     35.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1569154941061-e231b4725ef1?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "espana",
    },
    {
        "link_id":        "15134741",
        "title":          "Ofertas Flash de Iberia",
        "description":    "Descuentos por tiempo limitado en una selección de rutas de Iberia.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     25.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1517479149777-5f3b1511d5ad?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
    },
    {
        "link_id":        "15382402",
        "title":          "Precios especiales Iberia",
        "description":    "Selección de precios especiales de Iberia para tu próximo viaje.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     45.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
    },
    {
        "link_id":        "17065680",
        "title":          "¿Dónde ir de vacaciones este verano? — vuelos Iberia",
        "description":    "Los mejores destinos de verano con vuelos Iberia: playas, ciudades y escapadas por Europa y el mundo.",
        "location":       "Europa e internacional",
        "original_price": None,
        "sale_price":     59.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1503220317375-aaad61436b1b?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "europa",
    },
    {
        "link_id":        "17289401",
        "title":          "Nueva ruta: Madrid–Monterrey (México)",
        "description":    "Iberia estrena ruta a Monterrey. Los pasajeros pueden hacer escala de 1 a 6 noches en Madrid sin coste adicional.",
        "location":       "Monterrey, México",
        "original_price": None,
        "sale_price":     450.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1518105779142-d975f22f1b0a?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
    },
    {
        "link_id":        "15217622",
        "title":          "Vuelos en clase Turista con Iberia",
        "description":    "Tarifas de clase Turista de Iberia a los principales destinos de Europa y el mundo.",
        "location":       "España y resto del mundo",
        "original_price": None,
        "sale_price":     49.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
    },
]


# Ofertas por destino: cada una enlaza a la página real de Iberia para ese
# país/ciudad en el catálogo de CJ (Campañas > Enlaces, advertiser 4455265).
# `location` = nombre exacto usado en _CITY_MAP de app.py, para que la oferta
# aparezca en el bloque "Ofertas actuales para <ciudad>" de esa guía de destino.
# Varias ciudades italianas comparten el mismo link_id porque Iberia solo
# tiene una página de aterrizaje para Italia en CJ, no una por ciudad.
_DESTINOS = [
    {"dest": "Madrid",           "link_id": "12245349", "sale_price": 29.0,  "category": "espana",
     "image_url": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?fm=jpg&q=80&w=800&auto=format&fit=crop",
     "note": "puente aéreo y conexiones frecuentes desde toda España y el extranjero al hub de la aerolínea en el aeropuerto de Barajas"},
    {"dest": "Nueva York",       "link_id": "13863711", "sale_price": 380.0, "category": "internacional",
     "image_url": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Roma",             "link_id": "12119547", "sale_price": 69.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Venecia",          "link_id": "12119547", "sale_price": 75.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1514890547357-a9ee288728e0?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Florencia",        "link_id": "12119547", "sale_price": 72.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1541370976299-4d24ebbc9077?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Nápoles",          "link_id": "12119547", "sale_price": 65.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Sicilia",          "link_id": "12119547", "sale_price": 79.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "París",            "link_id": "13017938", "sale_price": 59.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Bruselas",         "link_id": "12119526", "sale_price": 65.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1559113202-c916b8e44373?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Viena",            "link_id": "12119527", "sale_price": 85.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1516550893923-42d28e5677af?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Lisboa",           "link_id": "12119557", "sale_price": 49.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1548707309-dcebeab9ea9b?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Ámsterdam",        "link_id": "12119546", "sale_price": 75.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1459679749680-18eb1eb37418?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Berlín",           "link_id": "12119555", "sale_price": 69.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1560969184-10fe8719e047?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Dublín",           "link_id": "12119548", "sale_price": 89.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1549918864-48ac978761a4?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Praga",            "link_id": "12119552", "sale_price": 79.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1541849546-216549ae216d?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Atenas",           "link_id": "12119543", "sale_price": 95.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1555993539-1732b0258235?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Dubrovnik",        "link_id": "12119531", "sale_price": 99.0,  "category": "europa",
     "image_url": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Tokio",            "link_id": "12604307", "sale_price": 550.0, "category": "internacional",
     "image_url": "https://images.unsplash.com/photo-1528360983277-13d401cdc186?fm=jpg&q=80&w=800&auto=format&fit=crop"},
    {"dest": "Ciudad de México", "link_id": "13524303", "sale_price": 480.0, "category": "internacional",
     "image_url": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=800&auto=format&fit=crop"},
]


def fetch_deals(min_discount: int = 0, max_results: int = 30) -> list[dict]:
    if not config.CJ_WEBSITE_ID:
        log.info("Iberia: sin CJ_WEBSITE_ID configurado, omitiendo")
        return []

    deals = []

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
                "source":         "iberia",
                "category":       o["category"],
                "tipo":           "vuelo",
                "rating":         0.0,
                "reviews_count":  0,
            })

    for d in _DESTINOS:
        sid = d["dest"].lower().replace(" ", "-").replace("é", "e").replace("á", "a").replace("í", "i")
        deals.append({
            "title":          f"Vuelos a {d['dest']} con Iberia",
            "description":    d.get("note") or f"Vuela a {d['dest']} con Iberia. Compara fechas y encuentra tu mejor tarifa.",
            "location":       d["dest"],
            "original_price": None,
            "sale_price":     d["sale_price"],
            "discount_pct":   0,
            "image_url":      d["image_url"],
            "affiliate_url":  _cj_url(d["link_id"], sid=sid),
            "source":         "iberia",
            "category":       d["category"],
            "tipo":           "vuelo",
            "rating":         0.0,
            "reviews_count":  0,
        })

    log.info(f"Iberia: {len(deals)} ofertas ({len(_OFERTAS)} generales + {len(_DESTINOS)} por destino)")
    return deals[:max_results]
