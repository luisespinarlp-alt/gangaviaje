"""
Iberostar scraper para GangaViaje.
Hoteles de la cadena Iberostar con comisión real vía CJ Affiliate (5.8-8%).
Programa "IBEROSTAR EMEA & UK" confirmado activo en la cuenta de CJ.
Los enlaces usan el formato de deep-link real de CJ: dpbolvw.net/click-{PID}-{LID},
donde cada LID es un link concreto ya verificado en el panel de CJ (Campañas > Enlaces).
"""

import logging

import config

log = logging.getLogger(__name__)


def _cj_url(link_id: str) -> str:
    return f"https://www.dpbolvw.net/click-{config.CJ_WEBSITE_ID}-{link_id}"


# Hoteles/ofertas reales tomados del catálogo de enlaces de CJ para Iberostar EMEA & UK.
_HOTELES = [
    {
        "link_id":        "17308149",
        "title":          "Oferta verano 2026 en Canarias — hasta 30% de descuento",
        "description":    "Hoteles Iberostar en las Islas Canarias con hasta un 30% de descuento en la oferta de verano 2026.",
        "location":       "Islas Canarias",
        "original_price": 180.0,
        "sale_price":     126.0,
        "discount_pct":   30,
        "image_url":      "https://images.unsplash.com/photo-1559827260-dc66d52bef19?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "playa",
    },
    {
        "link_id":        "17235683",
        "title":          "Tu hotel en Montenegro — 20% de descuento garantizado",
        "description":    "Iberostar Waves Slavija en Budva, Montenegro, con 20% de descuento garantizado.",
        "location":       "Budva, Montenegro",
        "original_price": 140.0,
        "sale_price":     112.0,
        "discount_pct":   20,
        "image_url":      "https://images.unsplash.com/photo-1601244005535-a48d21d951ac?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "internacional",
    },
    {
        "link_id":        "17250295",
        "title":          "Iberostar Waves Ciudad Blanca",
        "description":    "Hotel Iberostar en primera línea de playa en Mallorca.",
        "location":       "Mallorca",
        "original_price": None,
        "sale_price":     145.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "playa",
    },
    {
        "link_id":        "17250292",
        "title":          "Iberostar Waves Bahía de Palma",
        "description":    "Hotel Iberostar frente al mar en la Bahía de Palma, Mallorca.",
        "location":       "Mallorca",
        "original_price": None,
        "sale_price":     130.0,
        "discount_pct":   0,
        "image_url":      "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category":       "playa",
    },
]


def fetch_deals(min_discount: int = 0, max_results: int = 10) -> list[dict]:
    if not config.CJ_WEBSITE_ID:
        log.info("Iberostar: sin CJ_WEBSITE_ID configurado, omitiendo")
        return []

    deals = []
    for h in _HOTELES[:max_results]:
        deals.append({
            "title":          h["title"],
            "description":    h["description"],
            "location":       h["location"],
            "original_price": h["original_price"],
            "sale_price":     h["sale_price"],
            "discount_pct":   h["discount_pct"],
            "image_url":      h["image_url"],
            "affiliate_url":  _cj_url(h["link_id"]),
            "source":         "iberostar",
            "category":       h["category"],
            "tipo":           "hotel",
            "rating":         0.0,
            "reviews_count":  0,
        })

    log.info(f"Iberostar: {len(deals)} hoteles con enlace de afiliado real")
    return deals
