"""
Consulta la Google Search Console API (Search Analytics) usando el token
guardado por el flujo de autorización manual (ver ga_auth.py para el patrón).
Uso: python3 -m scripts.gsc_query [dias_atras] [query|page]
"""

import json
import os
import sys
import datetime

import requests

import config

TOKEN_PATH = os.path.join(os.path.dirname(__file__), "gsc_token.json")
SITE_URL = "https://gangaviaje.es/"


def _headers():
    with open(TOKEN_PATH) as f:
        tok = json.load(f)
    return {"Authorization": f"Bearer {tok['token']}", "Content-Type": "application/json"}


def query(days=90, dimensions=("date",), row_limit=100):
    end = datetime.date.today().isoformat()
    start = (datetime.date.today() - datetime.timedelta(days=days)).isoformat()
    url = f"https://www.googleapis.com/webmasters/v3/sites/{requests.utils.quote(SITE_URL, safe='')}/searchAnalytics/query"
    body = {"startDate": start, "endDate": end, "dimensions": list(dimensions), "rowLimit": row_limit}
    r = requests.post(url, headers=_headers(), json=body)
    r.raise_for_status()
    return r.json().get("rows", [])


if __name__ == "__main__":
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 90
    dim = sys.argv[2] if len(sys.argv) > 2 else "date"
    rows = query(days=days, dimensions=(dim,))
    rows.sort(key=lambda r: r["position"])
    tot_clicks = sum(r["clicks"] for r in rows)
    tot_impr = sum(r["impressions"] for r in rows)
    for r in rows:
        print(f"{r['keys'][0]:<50} impr={r['impressions']:<4} clicks={r['clicks']:<3} pos={round(r['position'], 1)}")
    print(f"\nTOTAL {days} días -> clicks={tot_clicks} impressions={tot_impr}")
