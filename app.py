"""
GangaViaje — Web Flask de ofertas de viajes
"""

from datetime import datetime
from flask import Flask, render_template, abort, Response, request, jsonify

import bot
import config
import database

app = Flask(__name__)
app.secret_key = config.FLASK_SECRET_KEY

database.init_db()


@app.route("/")
def index():
    grouped = database.get_deals_grouped()
    stats = database.get_stats()
    recent_posts = database.get_posts(limit=3)
    return render_template("index.html", grouped=grouped, stats=stats,
                           active_cat="todos", destinos=config.DESTINOS,
                           tipo_labels=config.TIPOS, recent_posts=recent_posts)


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
    "bali": "Bali", "tokio": "Tokio", "singapur": "Singapur",
    "nueva-york": "Nueva York", "miami": "Miami", "canarias": "Canarias",
    "mallorca": "Mallorca", "ibiza": "Ibiza", "sevilla": "Sevilla",
    "granada": "Granada", "atenas": "Atenas", "estambul": "Estambul",
    "venecia": "Venecia", "florencia": "Florencia", "napoles": "Nápoles",
}

@app.route("/ciudad/<name>")
def ciudad(name: str):
    name_display = _SLUG_TO_CITY.get(name, name.replace("-", " ").title())
    grouped = database.get_deals_grouped_by_location(name_display)
    if not grouped:
        abort(404)
    stats = database.get_stats()
    return render_template("index.html", grouped=grouped, stats=stats,
                           active_cat="todos", destinos=config.DESTINOS,
                           cat_title=f"Ofertas en {name_display}",
                           tipo_labels=config.TIPOS)


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


@app.route("/sobre-nosotros")
def sobre_nosotros():
    return render_template("about.html", destinos=config.DESTINOS)


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
    return render_template("index.html", grouped=[], stats={"total": 0, "today": 0},
                           active_cat="todos", destinos=config.DESTINOS,
                           tipo_labels=config.TIPOS), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=False)
