"""
GangaViaje — Web Flask de ofertas de viajes
"""

from datetime import datetime
from flask import Flask, render_template, abort, Response, request

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
    return render_template("index.html", grouped=grouped, stats=stats,
                           active_cat="todos", destinos=config.DESTINOS,
                           tipo_labels=config.TIPOS)


@app.route("/destino/<cat>")
def destino(cat: str):
    if cat not in config.DESTINOS:
        abort(404)
    grouped = database.get_deals_grouped(category=cat)
    stats = database.get_stats()
    return render_template("index.html", grouped=grouped, stats=stats,
                           active_cat=cat, destinos=config.DESTINOS,
                           cat_title=config.DESTINOS[cat], tipo_labels=config.TIPOS)


@app.route("/oferta/<int:deal_id>")
def oferta(deal_id: int):
    deal = database.get_deal(deal_id)
    if not deal:
        abort(404)
    return render_template("deal.html", deal=deal, destinos=config.DESTINOS)


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
    for key in config.DESTINOS:
        urls.append(f"<url><loc>{base}/destino/{key}</loc><changefreq>hourly</changefreq><priority>0.8</priority></url>")

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
