"""
GangaViaje — Web Flask de ofertas de viajes
"""

from datetime import datetime
import re
import time as _time
from flask import Flask, render_template, abort, Response, request, jsonify

import bot
import config
import database

app = Flask(__name__)
app.secret_key = config.FLASK_SECRET_KEY

database.init_db()

@app.context_processor
def inject_now():
    return {"now": datetime.utcnow()}

# Cache simple para datos de homepage (TTL: 5 minutos)
_cache: dict = {}
_CACHE_TTL = 300  # segundos

def _cache_get(key):
    entry = _cache.get(key)
    if entry and (_time.time() - entry["ts"]) < _CACHE_TTL:
        return entry["data"]
    return None

def _cache_set(key, data):
    _cache[key] = {"data": data, "ts": _time.time()}


_FEATURED_DESTINATIONS = [
    {"name": "Bali",       "guide": "que-ver-en-bali-guia-completa",
     "img": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?fm=jpg&q=80&w=400&auto=format&fit=crop"},
    {"name": "Maldivas",   "guide": "maldivas-guia-viaje-economico",
     "img": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?fm=jpg&q=80&w=400&auto=format&fit=crop"},
    {"name": "París",      "guide": "paris-tres-dias-itinerario",
     "img": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=400&auto=format&fit=crop"},
    {"name": "Nueva York", "guide": "que-ver-en-nueva-york-guia-completa",
     "img": "https://images.unsplash.com/photo-1485738422979-f5c462d49f74?fm=jpg&q=80&w=400&auto=format&fit=crop"},
    {"name": "Islandia",   "guide": "que-ver-en-islandia-guia-completa",
     "img": "https://images.unsplash.com/photo-1531366936337-7c912a4589a7?fm=jpg&q=80&w=400&auto=format&fit=crop"},
    {"name": "Tailandia",  "guide": "tailandia-islas-guia-koh-samui-phi-phi",
     "img": "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?fm=jpg&q=80&w=400&auto=format&fit=crop"},
    {"name": "Japón",      "guide": "japon-guia-viaje-completo",
     "img": "https://images.unsplash.com/photo-1528360983277-13d401cdc186?fm=jpg&q=80&w=400&auto=format&fit=crop"},
    {"name": "Roma",       "guide": "que-ver-en-roma-guia-completa",
     "img": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=400&auto=format&fit=crop"},
    {"name": "Tenerife",   "guide": "tenerife-que-hacer-guia-completa",
     "img": "https://images.unsplash.com/photo-1559827260-dc66d52bef19?fm=jpg&q=80&w=400&auto=format&fit=crop"},
    {"name": "Florencia",  "guide": "florencia-que-ver-en-dos-dias",
     "img": "https://images.unsplash.com/photo-1506929562872-bb421503ef21?fm=jpg&q=80&w=400&auto=format&fit=crop"},
]


@app.route("/")
def index():
    cached = _cache_get("homepage_v2")
    if cached:
        guides, consejos, featured_deals, stats = cached
    else:
        guides = database.get_posts(limit=6, exclude_category="consejos")
        consejos = database.get_posts(limit=6, category="consejos")
        featured_deals = database.get_deals(limit=4)
        stats = database.get_stats()
        _cache_set("homepage_v2", (guides, consejos, featured_deals, stats))
    return render_template(
        "home.html",
        guides=guides,
        consejos=consejos,
        featured_deals=featured_deals,
        stats=stats,
        featured_destinations=_FEATURED_DESTINATIONS,
    )


_TIPO_SEO = {
    "vuelos": {
        "titulo": "Ofertas de vuelos baratos",
        "desc":   "Encuentra vuelos baratos a Europa, América, Asia y más. Precios actualizados cada hora desde los principales aeropuertos españoles.",
        "faqs": [
            ("¿Cuándo es mejor reservar un vuelo barato?", "Lo ideal es reservar entre 6 y 8 semanas antes para vuelos europeos, y entre 2 y 4 meses antes para vuelos de larga distancia. Los martes y miércoles suelen tener precios más bajos."),
            ("¿Cuáles son las aerolíneas más baratas desde España?", "Ryanair, Vueling, EasyJet y Transavia son las principales low-cost. Para larga distancia, Norwegian e Iberia Express suelen tener las mejores ofertas."),
            ("¿Cómo sé si el precio del vuelo es una buena oferta?", "Compara siempre el precio con la media histórica del destino. En GangaViaje solo publicamos vuelos cuando detectamos precios significativamente por debajo de lo habitual."),
        ],
    },
    "hoteles": {
        "titulo": "Hoteles con descuento — Mejores ofertas",
        "desc":   "Los mejores hoteles con descuento en España y todo el mundo. Reserva con cancelación gratuita y ahorra hasta un 40% en tu alojamiento.",
        "faqs": [
            ("¿Cómo conseguir el mejor precio en hoteles?", "Reserva con antelación en temporada alta y en el último momento en temporada baja. Activa siempre la opción de cancelación gratuita para poder cambiar si aparece un precio mejor."),
            ("¿Es mejor reservar el hotel por la app o por la web?", "Las apps de Booking.com y Hotels.com a veces tienen descuentos exclusivos para app. Compara siempre con el precio de la web del hotel directamente."),
            ("¿Qué significa 'precio orientativo' en las ofertas?", "El precio mostrado es el precio base en el momento en que detectamos la oferta. El precio final depende de las fechas y disponibilidad al hacer la reserva."),
        ],
    },
    "actividades": {
        "titulo": "Actividades y tours con descuento",
        "desc":   "Tours guiados, entradas a monumentos, experiencias y actividades en los mejores destinos del mundo. Reserva online con cancelación gratuita.",
        "faqs": [
            ("¿Puedo cancelar una actividad reservada online?", "La mayoría de actividades ofrecen cancelación gratuita hasta 24-48 horas antes. Comprueba siempre las condiciones específicas de cada reserva."),
            ("¿Es mejor reservar actividades antes de llegar?", "Sí, especialmente en destinos muy visitados como Roma, París o Dubái. Las entradas a monumentos populares se agotan semanas antes en temporada alta."),
            ("¿Las actividades incluyen transporte?", "Depende de cada actividad. Muchos tours incluyen recogida en hotel. Lee la descripción completa antes de reservar."),
        ],
    },
    "coches": {
        "titulo": "Alquiler de coches baratos",
        "desc":   "Alquila un coche barato en más de 50.000 ubicaciones en todo el mundo. Cancelación gratuita, sin cargos ocultos, comparamos los mejores precios.",
        "faqs": [
            ("¿Qué documentos necesito para alquilar un coche?", "Carnet de conducir válido (con al menos 1-2 años de antigüedad según la empresa), DNI o pasaporte y tarjeta de crédito a nombre del conductor principal."),
            ("¿El seguro está incluido en el precio?", "Generalmente incluye seguro básico a terceros. El seguro a todo riesgo sin franquicia suele ser un extra. Lee bien las condiciones antes de reservar."),
            ("¿Puedo recoger el coche en un lugar y devolverlo en otro?", "Sí, la mayoría de empresas ofrecen 'one-way'. Puede tener un coste adicional, especialmente entre países distintos."),
        ],
    },
    "apartamentos": {
        "titulo": "Apartamentos y alojamientos con descuento",
        "desc":   "Apartamentos, villas y alojamientos únicos en todo el mundo. Más espacio, más privacidad y generalmente más económico que un hotel para estancias largas.",
        "faqs": [
            ("¿Cuándo es mejor un apartamento que un hotel?", "Para estancias de 3 o más días o para grupos. Tener cocina reduce el gasto en restaurantes y suele ser más barato por noche cuando se divide entre varias personas."),
            ("¿Los apartamentos incluyen servicio de limpieza?", "Varía mucho. Algunos incluyen limpieza diaria, otros solo al finalizar la estancia. Comprueba la descripción y las reseñas de otros viajeros."),
            ("¿Hay depósito de seguridad?", "Muchos apartamentos piden una fianza que se devuelve al finalizar la estancia sin incidencias. Se menciona siempre en la descripción de la oferta."),
        ],
    },
    "traslados": {
        "titulo": "Traslados aeropuerto baratos",
        "desc":   "Traslados privados y compartidos desde y hasta el aeropuerto en los principales destinos del mundo. Reserva con antelación y evita sorpresas.",
        "faqs": [
            ("¿Es mejor reservar el traslado antes o coger un taxi al llegar?", "Reservar online suele ser más barato y más seguro, especialmente de noche o en destinos donde los taxistas suelen cobrar de más a turistas."),
            ("¿Qué pasa si mi vuelo llega tarde?", "Los servicios de traslado monitorizan los vuelos. Si hay retraso, el conductor ajusta la hora de recogida sin coste adicional."),
            ("¿Traslado privado o compartido?", "El compartido es más barato pero puede tardar más (otras paradas). El privado es directo. Para grupos de 3 o más personas, el privado suele compensar económicamente."),
        ],
    },
}

@app.route("/ofertas/<tipo>")
def ofertas_tipo(tipo: str):
    if tipo not in _TIPO_SEO:
        abort(404)
    seo = _TIPO_SEO[tipo]
    tipo_db_map = {
        "vuelos": "vuelo", "hoteles": "hotel", "actividades": "actividad",
        "coches": "coche", "apartamentos": "apartamento", "traslados": "traslado",
    }
    tipo_db = tipo_db_map[tipo]
    cache_key = f"ofertas_{tipo}"
    cached = _cache_get(cache_key)
    if cached:
        deals, stats = cached
    else:
        import psycopg2.extras as _extras
        conn = database.get_conn()
        cur = conn.cursor(cursor_factory=_extras.RealDictCursor)
        cur.execute("SELECT * FROM deals WHERE active=1 AND tipo=%s ORDER BY discount_pct DESC, created_at DESC LIMIT 60", (tipo_db,))
        deals = [dict(r) for r in cur.fetchall()]
        cur.close(); conn.close()
        stats = database.get_stats()
        _cache_set(cache_key, (deals, stats))
    if not deals:
        abort(404)
    grouped = [(tipo_db, deals)]
    return render_template("index.html", grouped=grouped, stats=stats,
                           active_cat="todos", destinos=config.DESTINOS,
                           cat_title=seo["titulo"], tipo_labels=config.TIPOS,
                           seo_desc=seo["desc"], seo_faqs=seo["faqs"],
                           )


@app.route("/destino/<cat>")
def destino(cat: str):
    if cat not in config.DESTINOS:
        abort(404)
    grouped = database.get_deals_grouped(category=cat)
    stats = database.get_stats()
    return render_template("index.html", grouped=grouped, stats=stats,
                           active_cat=cat, destinos=config.DESTINOS,
                           cat_title=config.DESTINOS[cat], tipo_labels=config.TIPOS,
                           )


_SLUG_TO_CITY = {
    "paris": "París", "amsterdam": "Ámsterdam", "berlin": "Berlín",
    "dubai": "Dubái", "dublin": "Dublín", "cancun": "Cancún",
    "malaga": "Málaga", "almeria": "Almería", "cadiz": "Cádiz",
    "cordoba": "Córdoba", "murcia": "Murcia", "leon": "León",
    "espana": "España", "tokio": "Tokio", "milan": "Milán",
    "buenos-aires": "Buenos Aires", "marrakech": "Marrakech",
    "moscu": "Moscú", "munich": "Múnich", "zurich": "Zúrich",
    "bruselas": "Bruselas", "budapest": "Budapest", "praga": "Praga",
    "viena": "Viena", "roma": "Roma", "barcelona": "Barcelona",
    "madrid": "Madrid", "lisboa": "Lisboa", "bangkok": "Bangkok",
    "bali": "Bali", "singapur": "Singapur",
    "nueva-york": "Nueva York", "miami": "Miami", "canarias": "Canarias",
    "mallorca": "Mallorca", "ibiza": "Ibiza", "sevilla": "Sevilla",
    "granada": "Granada", "atenas": "Atenas", "estambul": "Estambul",
    "venecia": "Venecia", "florencia": "Florencia", "napoles": "Nápoles",
}

_CITY_IMAGES = {
    "barcelona": "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "madrid":    "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "paris":     "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "roma":      "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "lisboa":    "https://images.unsplash.com/photo-1548707309-dcebeab9ea9b?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "amsterdam": "https://images.unsplash.com/photo-1459679749680-18eb1eb37418?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "berlin":    "https://images.unsplash.com/photo-1560969184-10fe8719e047?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "dubai":     "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "bangkok":   "https://images.unsplash.com/photo-1528181304800-259b08848526?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "nueva-york":"https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "tokio":     "https://images.unsplash.com/photo-1528360983277-13d401cdc186?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "cancun":    "https://images.unsplash.com/photo-1510414842594-a61c69b5ae57?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "praga":     "https://images.unsplash.com/photo-1541849546-216549ae216d?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "viena":     "https://images.unsplash.com/photo-1516550893923-42d28e5677af?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "budapest":  "https://images.unsplash.com/photo-1551867633-194f125bddfa?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "atenas":    "https://images.unsplash.com/photo-1555993539-1732b0258235?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "estambul":  "https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "venecia":   "https://images.unsplash.com/photo-1514890547357-a9ee288728e0?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "bali":      "https://images.unsplash.com/photo-1537996194471-e657df975ab4?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "mallorca":  "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "sevilla":   "https://images.unsplash.com/photo-1503376780353-7e6692767b70?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "canarias":  "https://images.unsplash.com/photo-1559827260-dc66d52bef19?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "marrakech": "https://images.unsplash.com/photo-1542401886-65d6c61db217?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "dublin":    "https://images.unsplash.com/photo-1549918864-48ac978761a4?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "bruselas":  "https://images.unsplash.com/photo-1559113202-c916b8e44373?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "miami":     "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?fm=jpg&q=80&w=1200&auto=format&fit=crop",
}

@app.route("/ciudad/<name>")
def ciudad(name: str):
    cache_key = f"ciudad_{name}"
    cached = _cache_get(cache_key)
    if cached:
        grouped, stats = cached
    else:
        name_display = _SLUG_TO_CITY.get(name, name.replace("-", " ").title())
        grouped = database.get_deals_grouped_by_location(name_display)
        if not grouped:
            abort(404)
        stats = database.get_stats()
        _cache_set(cache_key, (grouped, stats))
    name_display = _SLUG_TO_CITY.get(name, name.replace("-", " ").title())
    city_image = _CITY_IMAGES.get(name, "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?fm=jpg&q=80&w=1200&auto=format&fit=crop")
    total = sum(len(items) for _, items in grouped)
    return render_template("ciudad.html", grouped=grouped, stats=stats,
                           city_name=name_display, city_slug=name,
                           city_image=city_image, total=total,
                           tipo_labels=config.TIPOS, destinos=config.DESTINOS)


@app.route("/oferta/<int:deal_id>")
def oferta(deal_id: int):
    deal = database.get_deal(deal_id)
    if not deal:
        abort(404)
    related = database.get_deals(category=deal.get("category", "europa"), limit=4)
    related = [d for d in related if d["id"] != deal_id][:3]
    return render_template("deal.html", deal=deal, destinos=config.DESTINOS, related=related)


@app.route("/blog")
def blog():
    posts = database.get_posts(limit=100)
    return render_template("blog_list.html", posts=posts, destinos=config.DESTINOS)


@app.route("/guias")
def guias():
    cat = request.args.get("cat")
    _titles = {"espana": "Guías de España", "europa": "Guías de Europa", "internacional": "Guías internacionales"}
    if cat and cat in _titles:
        posts = database.get_posts(limit=100, category=cat)
        page_title = _titles[cat]
    else:
        posts = database.get_posts(limit=100, exclude_category="consejos")
        page_title = "Guías de viaje"
    return render_template("blog_list.html", posts=posts, destinos=config.DESTINOS,
                           page_title=page_title, page_desc="Guías detalladas para cada destino",
                           active_cat=cat or "todos")


@app.route("/consejos")
def consejos():
    posts = database.get_posts(limit=100, category="consejos")
    return render_template("blog_list.html", posts=posts, destinos=config.DESTINOS,
                           page_title="GangaConsejos", page_desc="Trucos y consejos para viajar gastando menos")


_CITY_MAP = {
    "roma": ("Roma", "roma"), "paris": ("París", "paris"),
    "barcelona": ("Barcelona", "barcelona"), "madrid": ("Madrid", "madrid"),
    "venecia": ("Venecia", "venecia"), "tokio": ("Tokio", "tokio"),
    "budapest": ("Budapest", "budapest"), "bangkok": ("Bangkok", "bangkok"),
    "berlin": ("Berlín", "berlin"), "dubai": ("Dubái", "dubai"),
    "lisboa": ("Lisboa", "lisboa"), "amsterdam": ("Ámsterdam", "amsterdam"),
    "mallorca": ("Mallorca", "mallorca"), "sevilla": ("Sevilla", "sevilla"),
    "canarias": ("Canarias", "canarias"), "london": ("Londres", "londres"),
    "londres": ("Londres", "londres"), "bali": ("Bali", "bali"),
    "maldivas": ("Maldivas", "maldivas"), "japon": ("Tokio", "tokio"),
    "islandia": ("Islandia", "islandia"), "tailandia": ("Bangkok", "bangkok"),
    "florencia": ("Florencia", "florencia"), "tenerife": ("Tenerife", "canarias"),
    "nueva-york": ("Nueva York", "nueva-york"), "phuket": ("Phuket", "phuket"),
    "koh-samui": ("Koh Samui", "tailandia"), "phi-phi": ("Tailandia", "tailandia"),
    "toledo": ("Toledo", "toledo"), "salamanca": ("Salamanca", "salamanca"),
    "asturias": ("Asturias", "asturias"), "croacia": ("Dubrovnik", "croacia"),
    "dubrovnik": ("Dubrovnik", "croacia"), "sicilia": ("Sicilia", "sicilia"),
    "palermo": ("Palermo", "sicilia"), "georgia": ("Tbilisi", "georgia"),
    "tbilisi": ("Tbilisi", "georgia"), "ciudad-real": ("Ciudad Real", "ciudad-real"),
    "granada": ("Granada", "granada"), "ibiza": ("Ibiza", "ibiza"),
    "praga": ("Praga", "praga"), "viena": ("Viena", "viena"),
    "atenas": ("Atenas", "atenas"), "estambul": ("Estambul", "estambul"),
    "napoles": ("Nápoles", "napoles"), "marrakech": ("Marrakech", "marrakech"),
    "miami": ("Miami", "miami"), "cancun": ("Cancún", "cancun"),
    "singapur": ("Singapur", "singapur"), "bruselas": ("Bruselas", "bruselas"),
    "dublin": ("Dublín", "dublin"), "edimburgo": ("Edimburgo", "edimburgo"),
    "tokyo": ("Tokio", "tokio"), "mexico": ("Ciudad de México", "ciudad-de-mexico"),
    "buenos-aires": ("Buenos Aires", "buenos-aires"),
}

_SLUG_TO_TIPO = [
    ("vuelo", "vuelo"), ("traslado", "traslado"), ("aeropuerto", "traslado"),
    ("hotel", "hotel"), ("alojamiento", "hotel"), ("alquiler-coche", "coche"),
    ("coche", "coche"), ("actividad", "actividad"), ("tour", "actividad"),
]

def _extract_faq(html: str) -> list:
    """Extrae pares pregunta/respuesta de los H2 y el primer párrafo que les sigue."""
    if not html:
        return []
    blocks = re.split(r'<h2[^>]*>', html, flags=re.IGNORECASE)
    faq = []
    for block in blocks[1:]:  # El primer trozo es el texto antes del primer H2
        h2_match = re.match(r'(.*?)</h2>(.*)', block, re.DOTALL | re.IGNORECASE)
        if not h2_match:
            continue
        question = re.sub(r'<[^>]+>', '', h2_match.group(1)).strip()
        rest = h2_match.group(2)
        p_match = re.search(r'<p[^>]*>(.*?)</p>', rest, re.DOTALL | re.IGNORECASE)
        if not p_match:
            continue
        answer = re.sub(r'<[^>]+>', '', p_match.group(1)).strip()
        if len(question) > 8 and len(answer) > 25:
            faq.append({"q": question, "a": answer[:350]})
        if len(faq) == 5:
            break
    return faq


def _detect_city(slug: str):
    for keyword, (name, url_slug) in _CITY_MAP.items():
        if keyword in slug:
            return name, url_slug
    return None, None

def _detect_tipo(slug: str):
    for keyword, tipo in _SLUG_TO_TIPO:
        if keyword in slug:
            return tipo
    return None


@app.route("/blog/<slug>")
def blog_post(slug: str):
    post = database.get_post_by_slug(slug)
    if not post:
        abort(404)
    ciudad_name, ciudad_slug = _detect_city(post["slug"])
    if ciudad_name:
        related_deals = database.get_deals(location=ciudad_name, limit=4)
        related_label = f"Ofertas actuales para {ciudad_name}"
    else:
        tipo = _detect_tipo(post["slug"])
        if tipo:
            related_deals = database.get_deals(tipo=tipo, limit=4)
            related_label = f"Mejores ofertas de {config.TIPOS.get(tipo, tipo)}"
        else:
            related_deals = database.get_deals(limit=4)
            related_label = "Ofertas destacadas ahora mismo"
    faq_items = _extract_faq(post.get("content", ""))
    all_related = database.get_posts(limit=12, category=post["category"])
    related_posts = [p for p in all_related if p["slug"] != slug][:3]
    return render_template("blog_post.html", post=post, destinos=config.DESTINOS,
                           related_deals=related_deals, related_label=related_label,
                           ciudad_name=ciudad_name, ciudad_slug=ciudad_slug,
                           faq_items=faq_items, related_posts=related_posts)


@app.route("/newsletter", methods=["POST"])
def newsletter():
    import psycopg2
    email = (request.json or {}).get("email", "").strip().lower()
    if not email or "@" not in email or "." not in email:
        return jsonify({"ok": False, "msg": "Email no válido"}), 400
    try:
        conn = psycopg2.connect(config.DATABASE_URL)
        cur = conn.cursor()
        cur.execute("INSERT INTO newsletter_subscribers (email) VALUES (%s) ON CONFLICT (email) DO NOTHING", (email,))
        new = cur.rowcount > 0
        conn.commit()
        conn.close()
        msg = "¡Apuntado! Te enviaremos las mejores ofertas." if new else "Ya estás suscrito."
        return jsonify({"ok": True, "msg": msg})
    except Exception as e:
        return jsonify({"ok": False, "msg": "Error al guardar. Inténtalo de nuevo."}), 500


@app.route("/buscar")
def buscar():
    q = request.args.get("q", "").strip()
    results = database.search(q) if len(q) >= 2 else {"deals": [], "posts": []}
    return render_template("buscar.html", q=q, results=results, destinos=config.DESTINOS)


@app.route("/sobre-nosotros")
def sobre_nosotros():
    stats = database.get_stats()
    post_count = len(database.get_posts(limit=200))
    return render_template("about.html", destinos=config.DESTINOS,
                           stats=stats, post_count=post_count)


@app.route("/privacidad")
def privacidad():
    return render_template("privacy.html", destinos=config.DESTINOS)


@app.route("/sitemap.xml")
def sitemap():
    base = config.BASE_URL.rstrip("/")
    today = datetime.utcnow().strftime("%Y-%m-%d")
    urls = []

    # Páginas estáticas
    urls.append(f"<url><loc>{base}/</loc><changefreq>hourly</changefreq><priority>1.0</priority></url>")
    urls.append(f"<url><loc>{base}/sobre-nosotros</loc><changefreq>monthly</changefreq><priority>0.4</priority></url>")
    urls.append(f"<url><loc>{base}/privacidad</loc><changefreq>monthly</changefreq><priority>0.3</priority></url>")
    urls.append(f"<url><loc>{base}/blog</loc><changefreq>weekly</changefreq><priority>0.6</priority></url>")
    urls.append(f"<url><loc>{base}/guias</loc><changefreq>weekly</changefreq><priority>0.7</priority></url>")
    urls.append(f"<url><loc>{base}/consejos</loc><changefreq>weekly</changefreq><priority>0.7</priority></url>")
    for key in config.DESTINOS:
        urls.append(f"<url><loc>{base}/destino/{key}</loc><changefreq>hourly</changefreq><priority>0.8</priority></url>")
    # Páginas de ofertas por tipo
    for tipo_slug in ["vuelos", "hoteles", "actividades", "coches", "apartamentos", "traslados"]:
        urls.append(f"<url><loc>{base}/ofertas/{tipo_slug}</loc><changefreq>hourly</changefreq><priority>0.9</priority></url>")

    # Páginas de ciudad (generadas dinámicamente desde locations de deals activos)
    import psycopg2
    conn = psycopg2.connect(config.DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT location FROM deals WHERE active = 1 AND location != '' ORDER BY location")
    ciudades = [r[0] for r in cur.fetchall()]
    cur.close(); conn.close()
    for ciudad_name in ciudades:
        slug = ciudad_name.lower().replace(" ", "-").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
        urls.append(f"<url><loc>{base}/ciudad/{slug}</loc><changefreq>hourly</changefreq><priority>0.7</priority></url>")

    # Artículos del blog (con imagen y lastmod)
    for post in database.get_posts(limit=200):
        lastmod = post["created_at"].strftime("%Y-%m-%d") if post.get("created_at") else today
        img_tag = ""
        if post.get("image_url"):
            img_tag = (
                f'<image:image>'
                f'<image:loc>{post["image_url"]}</image:loc>'
                f'<image:title>{post["title"].replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")}</image:title>'
                f'</image:image>'
            )
        urls.append(
            f"<url><loc>{base}/blog/{post['slug']}</loc>"
            f"<lastmod>{lastmod}</lastmod>"
            f"<changefreq>monthly</changefreq><priority>0.8</priority>"
            f"{img_tag}</url>"
        )

    # Deals activos
    for deal in database.get_deals(limit=200):
        urls.append(
            f"<url><loc>{base}/oferta/{deal['id']}</loc>"
            f"<lastmod>{today}</lastmod>"
            f"<changefreq>daily</changefreq><priority>0.6</priority></url>"
        )

    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
           ' xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'
           + "".join(urls) + "</urlset>")
    return Response(xml, mimetype="application/xml")


@app.route("/api/cron")
def cron():
    if not config.CRON_SECRET or request.headers.get("Authorization") != f"Bearer {config.CRON_SECRET}":
        abort(401)
    bot.run_once()
    return {"ok": True, "stats": database.get_stats()}


@app.route("/robots.txt")
def robots():
    base = config.BASE_URL.rstrip("/")
    content = f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n"
    return Response(content, mimetype="text/plain")


@app.errorhandler(404)
def not_found(e):
    deals = database.get_deals(limit=6)
    return render_template("404.html", deals=deals), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=False)
