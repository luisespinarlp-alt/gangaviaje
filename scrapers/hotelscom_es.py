"""
Hotels.com Spain & Portugal (CJ advertiser 5275610) — deep-links manuales.
Sin feed de producto en CJ; se usan los enlaces de categoría con mayor EPC.
EPCs destacados: Apartamentos 184$/130$, Homepage 123$/106$, Ofertas 203$/210$.
"""

import logging
import config

log = logging.getLogger(__name__)

_PID = config.CJ_WEBSITE_ID


def _cj_url(link_id: int) -> str:
    return f"https://www.dpbolvw.net/click-{_PID}-{link_id}"


def fetch_deals(min_discount: int = 20, max_results: int = 10) -> list[dict]:
    if not config.CJ_WEBSITE_ID:
        log.info("Hotels.com ES: sin CJ_WEBSITE_ID configurado")
        return []

    deals = [
        {
            "title":          "Hotels.com: hasta un 25% de descuento en tu próxima estancia",
            "description":    "Encuentra las mejores ofertas de hoteles en todo el mundo. Cancela gratis en la mayoría de reservas y acumula noches para conseguir una gratis.",
            "location":       "Todo el mundo",
            "original_price": 180.0,
            "sale_price":     135.0,
            "discount_pct":   25,
            "image_url":      "https://images.unsplash.com/photo-1566073771259-6a8506099945?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _cj_url(15607216),
            "source":         "hotelscom_es",
            "category":       "internacional",
            "tipo":           "hotel",
            "rating":         8.8,
            "reviews_count":  0,
        },
        {
            "title":          "Apartamentos en Hotels.com — Los mejores precios garantizados",
            "description":    "Descubre apartamentos para todos los gustos y presupuestos. Ideal para familias y estancias largas. Cancelación gratuita disponible.",
            "location":       "Europa",
            "original_price": 220.0,
            "sale_price":     159.0,
            "discount_pct":   28,
            "image_url":      "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _cj_url(14360154),
            "source":         "hotelscom_es",
            "category":       "europa",
            "tipo":           "apartamento",
            "rating":         8.6,
            "reviews_count":  0,
        },
        {
            "title":          "Hoteles en España — Ofertas exclusivas en Hotels.com",
            "description":    "Los mejores hoteles de España a precios imbatibles. Madrid, Barcelona, Sevilla, Valencia y más destinos con descuentos especiales.",
            "location":       "España",
            "original_price": 160.0,
            "sale_price":     115.0,
            "discount_pct":   28,
            "image_url":      "https://images.unsplash.com/photo-1543783207-ec64e4d95325?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _cj_url(14051402),
            "source":         "hotelscom_es",
            "category":       "espana",
            "tipo":           "hotel",
            "rating":         8.7,
            "reviews_count":  0,
        },
        {
            "title":          "Villas de lujo — Hotels.com selección premium",
            "description":    "Escápate a una villa exclusiva con piscina privada. Las mejores villas en España, Portugal, Italia y otros destinos europeos.",
            "location":       "Europa",
            "original_price": 450.0,
            "sale_price":     320.0,
            "discount_pct":   29,
            "image_url":      "https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _cj_url(14360155),
            "source":         "hotelscom_es",
            "category":       "europa",
            "tipo":           "villa",
            "rating":         9.1,
            "reviews_count":  0,
        },
        {
            "title":          "Casas y pisos turísticos — Hotels.com",
            "description":    "Alójate como en casa en cualquier destino. Amplia selección de pisos y casas turísticas con todas las comodidades.",
            "location":       "España",
            "original_price": 195.0,
            "sale_price":     139.0,
            "discount_pct":   29,
            "image_url":      "https://images.unsplash.com/photo-1484154218962-a197022b5858?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _cj_url(14360156),
            "source":         "hotelscom_es",
            "category":       "espana",
            "tipo":           "apartamento",
            "rating":         8.5,
            "reviews_count":  0,
        },
        {
            "title":          "Hotels.com — Cancela gratis en la mayoría de hoteles",
            "description":    "Más de 500.000 propiedades en todo el mundo. Reserva con tranquilidad: cancelación gratuita en miles de hoteles.",
            "location":       "Todo el mundo",
            "original_price": 150.0,
            "sale_price":     105.0,
            "discount_pct":   30,
            "image_url":      "https://images.unsplash.com/photo-1455587734955-081b22074882?fm=jpg&q=80&w=800&auto=format&fit=crop",
            "affiliate_url":  _cj_url(13830074),
            "source":         "hotelscom_es",
            "category":       "internacional",
            "tipo":           "hotel",
            "rating":         8.9,
            "reviews_count":  0,
        },
    ]

    filtered = [d for d in deals if d["discount_pct"] >= min_discount]
    log.info(f"Hotels.com ES: {len(filtered)} ofertas")
    return filtered[:max_results]
