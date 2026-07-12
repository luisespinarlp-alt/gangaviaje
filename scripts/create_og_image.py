"""Genera og-image.png de 1200x630 con branding de GangaViaje."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), "../static/img/og-image.png")
LOGO = os.path.join(os.path.dirname(__file__), "../static/img/logo_icon.png")

W, H = 1200, 630
CORAL = (232, 93, 80)
DARK  = (30, 30, 30)
WHITE = (255, 255, 255)
LIGHT = (255, 220, 216)

img  = Image.new("RGB", (W, H), DARK)
draw = ImageDraw.Draw(img)

# Fondo con gradiente manual (bandas horizontales de oscuro a ligeramente menos oscuro)
for y in range(H):
    t = y / H
    r = int(30 + 20 * t)
    g = int(30 + 10 * t)
    b = int(30 + 15 * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Franja coral izquierda
draw.rectangle([0, 0, 8, H], fill=CORAL)

# Acento coral decorativo arriba-derecha
draw.rectangle([W - 300, 0, W, 6], fill=CORAL)
draw.rectangle([W - 6, 0, W, H], fill=CORAL)

# Logo icono centrado-izquierda
try:
    icon = Image.open(LOGO).convert("RGBA")
    icon_h = 180
    icon_w = int(icon.width * icon_h / icon.height)
    icon = icon.resize((icon_w, icon_h), Image.LANCZOS)
    icon_x = 90
    icon_y = (H - icon_h) // 2 - 20
    img.paste(icon, (icon_x, icon_y), icon)
except Exception as e:
    print(f"Logo no disponible: {e}")
    icon_w = 0
    icon_x = 60

# Texto principal
text_x = icon_x + icon_w + 50 if icon_w else 120

try:
    font_big   = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 88)
    font_coral = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 88)
    font_tag   = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 34)
    font_sub   = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 30)
except:
    font_big = font_coral = font_tag = font_sub = ImageFont.load_default()

# "Ganga" en blanco + "Viaje.es" en coral
name_y = H // 2 - 70
draw.text((text_x, name_y), "Ganga", font=font_big, fill=WHITE)
ganga_w = draw.textlength("Ganga", font=font_big)
draw.text((text_x + ganga_w, name_y), "Viaje.es", font=font_coral, fill=CORAL)

# Tagline
tag_y = name_y + 105
draw.text((text_x, tag_y), "Las mejores ofertas de viajes", font=font_tag, fill=LIGHT)

# Línea separadora coral
draw.rectangle([text_x, tag_y - 14, text_x + 60, tag_y - 10], fill=CORAL)

# Sub-tagline
sub_y = tag_y + 52
draw.text((text_x, sub_y), "Vuelos · Hoteles · Actividades · Coches", font=font_sub, fill=(160, 160, 160))

img.save(OUT, "PNG", optimize=True)
print(f"OG image guardada en {OUT} ({W}x{H})")
