"""
GangaViaje — Web Flask de ofertas de viajes
"""

from datetime import datetime
import time as _time
from flask import Flask, render_template, abort, Response, request, jsonify

import bot
import config
import database

app = Flask(__name__)
app.secret_key = config.FLASK_SECRET_KEY

database.init_db()

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


@app.route("/")
def index():
    cached = _cache_get("homepage")
    if cached:
        grouped, stats, recent_posts = cached
    else:
        grouped = database.get_deals_grouped()
        stats = database.get_stats()
        recent_posts = database.get_posts(limit=3)
        _cache_set("homepage", (grouped, stats, recent_posts))
    return render_template("index.html", grouped=grouped, stats=stats,
                           active_cat="todos", destinos=config.DESTINOS,
                           tipo_labels=config.TIPOS, recent_posts=recent_posts)


@app.route("/ofertas/<tipo>")
def ofertas_tipo(tipo: str):
    tipo_nombres = {
        "vuelos": ("vuelo", "Ofertas de vuelos baratos"),
        "hoteles": ("hotel", "Ofertas de hoteles con descuento"),
        "actividades": ("actividad", "Actividades y tours con descuento"),
        "coches": ("coche", "Alquiler de coches baratos"),
        "apartamentos": ("apartamento", "Apartamentos y alojamientos"),
        "traslados": ("traslado", "Traslados aeropuerto baratos"),
    }
    if tipo not in tipo_nombres:
        abort(404)
    tipo_db, titulo = tipo_nombres[tipo]
    conn = database.get_conn()
    cur = conn.cursor(cursor_factory=__import__('psycopg2').extras.RealDictCursor)
    cur.execute("SELECT * FROM deals WHERE active=1 AND tipo=%s ORDER BY discount_pct DESC, created_at DESC LIMIT 60", (tipo_db,))
    deals = [dict(r) for r in cur.fetchall()]
    cur.close(); conn.close()
    if not deals:
        abort(404)
    grouped = [(tipo_db, deals)]
    stats = database.get_stats()
    return render_template("index.html", grouped=grouped, stats=stats,
                           active_cat="todos", destinos=config.DESTINOS,
                           cat_title=titulo, tipo_labels=config.TIPOS)


@app.route("/destino/<cat>")
def destino(cat: str):
    if cat not in config.DESTINOS:
        abort(404)
    grouped = database.get_deals_grouped(category=cat)
    stats = database.get_stats()
    return render_template("index.html", grouped=grouped, stats=stats,
                           active_cat=cat, destinos=config.DESTINOS,
                           cat_title=config.DESTINOS[cat], tipo_labels=config.TIPOS)


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
    name_display = _SLUG_TO_CITY.get(name, name.replace("-", " ").title())
    grouped = database.get_deals_grouped_by_location(name_display)
    if not grouped:
        abort(404)
    stats = database.get_stats()
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


_CITY_MAP = {
    "roma": ("Roma", "roma"), "paris": ("París", "paris"),
    "barcelona": ("Barcelona", "barcelona"), "madrid": ("Madrid", "madrid"),
    "venecia": ("Venecia", "venecia"), "tokio": ("Tokio", "tokio"),
    "budapest": ("Budapest", "budapest"), "bangkok": ("Bangkok", "bangkok"),
    "berlin": ("Berlín", "berlin"), "dubai": ("Dubái", "dubai"),
    "lisboa": ("Lisboa", "lisboa"), "amsterdam": ("Ámsterdam", "amsterdam"),
    "mallorca": ("Mallorca", "mallorca"), "sevilla": ("Sevilla", "sevilla"),
    "canarias": ("Canarias", "canarias"), "london": ("Londres", "londres"),
    "londres": ("Londres", "londres"), "venecia": ("Venecia", "venecia"),
}

def _detect_city(slug: str):
    for keyword, (name, url_slug) in _CITY_MAP.items():
        if keyword in slug:
            return name, url_slug
    return None, None


@app.route("/blog/<slug>")
def blog_post(slug: str):
    post = database.get_post_by_slug(slug)
    if not post:
        abort(404)
    related_deals = database.get_deals(category=post["category"], limit=3)
    ciudad_name, ciudad_slug = _detect_city(post["slug"])
    return render_template("blog_post.html", post=post, destinos=config.DESTINOS,
                           related_deals=related_deals,
                           ciudad_name=ciudad_name, ciudad_slug=ciudad_slug)


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

    # Artículos del blog
    for post in database.get_posts(limit=100):
        urls.append(
            f"<url><loc>{base}/blog/{post['slug']}</loc>"
            f"<changefreq>monthly</changefreq><priority>0.5</priority></url>"
        )

    # Deals activos
    for deal in database.get_deals(limit=200):
        urls.append(
            f"<url><loc>{base}/oferta/{deal['id']}</loc>"
            f"<lastmod>{today}</lastmod>"
            f"<changefreq>daily</changefreq><priority>0.6</priority></url>"
        )

    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
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
