import os
from dotenv import load_dotenv

load_dotenv()

# Booking
BOOKING_AFFILIATE_ID = os.getenv("BOOKING_AFFILIATE_ID", "")
# Poner en "true" solo cuando BOOKING_AFFILIATE_ID sea un ID de afiliado real confirmado
BOOKING_AFFILIATE_ID_CONFIRMED = os.getenv("BOOKING_AFFILIATE_ID_CONFIRMED", "").lower() == "true"

# Civitatis
CIVITATIS_AFFILIATE_ID = os.getenv("CIVITATIS_AFFILIATE_ID", "")

# GetYourGuide
GETYOURGUIDE_PARTNER_ID = os.getenv("GETYOURGUIDE_PARTNER_ID", "")

# CJ Affiliate (Commission Junction) — PID = ID de sitio web GangaViaje en CJ.
# Válido para todos los anunciantes aprobados en CJ (Iberostar, Hotels.com, etc.)
CJ_WEBSITE_ID = os.getenv("CJ_WEBSITE_ID", "")

# CJ Product Search API (GraphQL) — automatiza catálogos de anunciantes con feed de producto.
# CJ_COMPANY_ID = CID de publisher de GangaViaje en CJ (visible en members.cj.com, selector de cuenta).
CJ_PERSONAL_ACCESS_TOKEN = os.getenv("CJ_PERSONAL_ACCESS_TOKEN", "")
CJ_COMPANY_ID = os.getenv("CJ_COMPANY_ID", "")

# TravelPayouts (vuelos vía Aviasales Data API, y links/v1/create para otras marcas)
TRAVELPAYOUTS_TOKEN  = os.getenv("TRAVELPAYOUTS_TOKEN", "")
TRAVELPAYOUTS_MARKER = os.getenv("TRAVELPAYOUTS_MARKER", "")
TRAVELPAYOUTS_TRS    = os.getenv("TRAVELPAYOUTS_TRS", "")

# Base de datos (Supabase Postgres)
DATABASE_URL = os.getenv("DATABASE_URL", "")

# Cron (Vercel Cron Job -> /api/cron)
CRON_SECRET = os.getenv("CRON_SECRET", "")

# Telegram
TELEGRAM_BOT_TOKEN  = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID", "@gangaviaje")

# Web
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")
_vercel_url = os.getenv("VERCEL_URL", "")
BASE_URL = os.getenv("BASE_URL") or (f"https://{_vercel_url}" if _vercel_url else "http://localhost:5002")
PORT     = int(os.getenv("PORT", 5002))

# Bot
BOT_INTERVAL_SEC   = 3600
MAX_DEALS_PER_RUN  = 30
DEAL_EXPIRY_HOURS  = 48
MIN_DISCOUNT_PCT   = 20

DESTINOS = {
    "espana":        "España",
    "europa":        "Europa",
    "playa":         "Playa",
    "ciudad":        "Ciudad",
    "rural":         "Rural",
    "internacional": "Internacional",
}

TIPOS = {
    "hotel":       "Hoteles",
    "apartamento": "Apartamentos",
    "villa":       "Villas",
    "actividad":   "Atracciones",
    "coche":       "Coches",
    "vuelo":       "Vuelos",
}

# Orden en el que se agrupan las secciones automáticas de la web (solo se muestran las que tengan ofertas)
TIPO_ORDER = ["vuelo", "hotel", "apartamento", "villa", "actividad", "coche"]
