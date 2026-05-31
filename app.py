"""
GangaViaje — Web Flask de ofertas de viajes
"""

import os
from flask import Flask, render_template, abort

import config
import database

app = Flask(__name__)
app.secret_key = config.FLASK_SECRET_KEY

database.init_db()

if os.getenv("VERCEL") == "1" and database.get_stats()["total"] == 0:
    from scrapers import booking
    for deal in booking.fetch_deals():
        if not database.deal_exists(deal["affiliate_url"]):
            database.add_deal(deal)


@app.route("/")
def index():
    deals = database.get_deals(limit=60)
    stats = database.get_stats()
    return render_template("index.html", deals=deals, stats=stats,
                           active_cat="todos", destinos=config.DESTINOS)


@app.route("/destino/<cat>")
def destino(cat: str):
    if cat not in config.DESTINOS:
        abort(404)
    deals = database.get_deals(category=cat, limit=60)
    stats = database.get_stats()
    return render_template("index.html", deals=deals, stats=stats,
                           active_cat=cat, destinos=config.DESTINOS,
                           cat_title=config.DESTINOS[cat])


@app.route("/oferta/<int:deal_id>")
def oferta(deal_id: int):
    deal = database.get_deal(deal_id)
    if not deal:
        abort(404)
    return render_template("deal.html", deal=deal, destinos=config.DESTINOS)


@app.errorhandler(404)
def not_found(e):
    return render_template("index.html", deals=[], stats={"total": 0, "today": 0},
                           active_cat="todos", destinos=config.DESTINOS), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=False)
