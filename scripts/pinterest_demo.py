"""
Script de demo para la solicitud de Standard Access de Pinterest.
Uso: python3 scripts/pinterest_demo.py <code>
El <code> se saca de la URL a la que redirige Pinterest tras autorizar
(https://www.gangaviaje.es/?code=XXXX), usando este enlace de autorización:

https://www.pinterest.com/oauth/?client_id=1586481&redirect_uri=https://www.gangaviaje.es/&response_type=code&scope=pins:read,pins:write,boards:read,boards:write

Este script hace, con salida clara para la grabación:
1. Intercambia el code por un access token real (llamada real a la API).
2. Crea un tablero de prueba.
3. Crea un pin de verdad en ese tablero, enlazando a una guía real de GangaViaje.
"""

import base64
import json
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import certifi

CLIENT_ID = "1586481"
CLIENT_SECRET = "2957af79143e3cbb029b0259c9483fbb13b8cf7a"
REDIRECT_URI = "https://www.gangaviaje.es/"
CTX = ssl.create_default_context(cafile=certifi.where())


def _req(method, url, token=None, body=None, auth_header=None):
    headers = {"User-Agent": "gangaviaje-bot/1.0", "Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if auth_header:
        headers["Authorization"] = auth_header
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = body.encode() if isinstance(body, str) else (json.dumps(body).encode() if body else None)
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=15, context=CTX) as r:
        return json.loads(r.read())


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 scripts/pinterest_demo.py <code>")
        sys.exit(1)
    code = sys.argv[1]

    print("=" * 60)
    print("PASO 1: Intercambiando el código de autorización por un access token real (Sandbox)")
    print("=" * 60)
    creds = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    body = urllib.parse.urlencode({
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    })
    token_data = _req("POST", "https://api-sandbox.pinterest.com/v5/oauth/token",
                       body=body, auth_header=f"Basic {creds}")
    token = token_data["access_token"]
    print(f"✅ Token obtenido correctamente. Scopes: {token_data['scope']}")
    time.sleep(1)

    print()
    print("=" * 60)
    print("PASO 2: Creando un tablero real vía la API de Pinterest")
    print("=" * 60)
    board = _req("POST", "https://api-sandbox.pinterest.com/v5/boards", token=token,
                 body={"name": "GangaViaje", "description": "Guías y ofertas de viaje"})
    print(f"✅ Tablero creado: '{board['name']}' (id: {board['id']})")
    time.sleep(1)

    print()
    print("=" * 60)
    print("PASO 3: Creando un Pin real vía la API de Pinterest")
    print("=" * 60)
    pin = _req("POST", "https://api-sandbox.pinterest.com/v5/pins", token=token, body={
        "board_id": board["id"],
        "title": "Marrakech: guía completa de viaje",
        "description": "5 cosas que no sabías de Marrakech antes de ir — guía gratis en GangaViaje",
        "link": "https://www.gangaviaje.es/blog/marrakech-que-ver-guia-completa",
        "media_source": {
            "source_type": "image_url",
            "url": "https://images.unsplash.com/photo-1489749798305-4fea3ae63d43?fm=jpg&q=80&w=800&auto=format&fit=crop",
        },
    })
    print(f"✅ Pin creado correctamente. id: {pin['id']}")
    print(f"   Link: {pin['link']}")
    print(f"   Creado en: {pin['created_at']}")
    print()
    print("=" * 60)
    print("DEMO COMPLETA: OAuth + creación de tablero + creación de pin, todo real.")
    print("=" * 60)


if __name__ == "__main__":
    main()
