"""
Autorización única para acceder a la Google Analytics Data API.
Ejecutar una sola vez: abre el navegador para conceder acceso con la cuenta
de Google que ya administra la propiedad GA4 de GangaViaje. Guarda un token
reutilizable en scripts/ga_token.json (no subir a git).
"""

import json
import os

from google_auth_oauthlib.flow import InstalledAppFlow

import config

SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]
TOKEN_PATH = os.path.join(os.path.dirname(__file__), "ga_token.json")


def main():
    client_config = {
        "installed": {
            "client_id": config.GA_OAUTH_CLIENT_ID,
            "client_secret": config.GA_OAUTH_CLIENT_SECRET,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost"],
        }
    }
    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    creds = flow.run_local_server(port=0, open_browser=False)

    with open(TOKEN_PATH, "w") as f:
        f.write(creds.to_json())

    print(f"Token guardado en {TOKEN_PATH}")


if __name__ == "__main__":
    main()
