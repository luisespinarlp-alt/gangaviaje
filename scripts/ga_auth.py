"""
Autorización OAuth para Google Analytics Data API.
Genera URL manualmente para evitar bugs de encoding.
"""
import json, os, sys, urllib.parse, secrets, hashlib, base64
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import config

TOKEN_PATH = os.path.join(os.path.dirname(__file__), "ga_token.json")

SCOPE = "https://www.googleapis.com/auth/analytics.readonly"
AUTH_URI = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URI = "https://oauth2.googleapis.com/token"
REDIRECT = "urn:ietf:wg:oauth:2.0:oob"

# Build auth URL manually
state = secrets.token_urlsafe(16)
params = {
    "client_id":     config.GA_OAUTH_CLIENT_ID,
    "redirect_uri":  REDIRECT,
    "response_type": "code",
    "scope":         SCOPE,
    "access_type":   "offline",
    "state":         state,
    "prompt":        "consent",
}
auth_url = AUTH_URI + "?" + urllib.parse.urlencode(params)
print("\nAbre esta URL en el navegador:")
print(auth_url)
print()
code = input("Pega aquí el código de autorización: ").strip()

# Exchange code for token
import urllib.request
data = urllib.parse.urlencode({
    "code":          code,
    "client_id":     config.GA_OAUTH_CLIENT_ID,
    "client_secret": config.GA_OAUTH_CLIENT_SECRET,
    "redirect_uri":  REDIRECT,
    "grant_type":    "authorization_code",
}).encode()

req = urllib.request.Request(TOKEN_URI, data=data, method="POST")
req.add_header("Content-Type", "application/x-www-form-urlencoded")
with urllib.request.urlopen(req) as r:
    token_data = json.loads(r.read())

# Save in format compatible with ga_query.py
import datetime
expiry = (datetime.datetime.utcnow() + datetime.timedelta(seconds=token_data["expires_in"])).isoformat() + "Z"
saved = {
    "token":         token_data["access_token"],
    "refresh_token": token_data.get("refresh_token"),
    "token_uri":     TOKEN_URI,
    "client_id":     config.GA_OAUTH_CLIENT_ID,
    "client_secret": config.GA_OAUTH_CLIENT_SECRET,
    "scopes":        [SCOPE],
    "expiry":        expiry,
}
with open(TOKEN_PATH, "w") as f:
    json.dump(saved, f, indent=2)

print(f"\nToken guardado OK. Expira: {expiry[:16]}")
