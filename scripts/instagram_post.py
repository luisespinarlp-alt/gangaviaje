"""
Generador de imágenes para Instagram de GangaViaje.

Uso:
    python3 scripts/instagram_post.py

Estilo fijo:
- Caja blanca redondeada en la parte superior con texto oscuro
- Emoji grande centrado dentro de la caja (Apple Color Emoji)
- Pregunta en mayúsculas en 2 líneas (fuente HelveticaNeue Bold, tamaño 68)
- Subtítulo en coral con emoji (tamaño 38)
- Foto del destino visible en el centro
- Gradiente oscuro en la parte inferior
- "👉 GUÍA COMPLETA EN EL LINK" centrado en blanco
- URL del blog en gris claro
- "GangaViaje" bicolor (blanco + coral) centrado abajo

Tamaño de salida: 1080x1080px (cuadrado Instagram)
"""

import re
import sys
import urllib.request
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

CORAL  = (232, 93, 80)
WHITE  = (255, 255, 255)
DARK   = (30, 30, 30)
W, H   = 1080, 1080

BOLD_FONT   = "/System/Library/Fonts/HelveticaNeue.ttc"
MEDIUM_FONT = "/System/Library/Fonts/Helvetica.ttc"
EMOJI_FONT  = "/System/Library/Fonts/Apple Color Emoji.ttc"
OUTPUT_DIR  = Path("/Users/cex/Desktop/GangaViaje Instagram")
TMP_DIR     = Path("/tmp/ig_imgs")

EMOJI_PAT = re.compile(
    r'[\U00010000-\U0010ffff\U00002600-\U000027BF'
    r'\U0001F300-\U0001F9FF\U00002702-\U000027B0]'
)


def lf(path, size, idx=1):
    try:
        return ImageFont.truetype(path, size, index=idx)
    except Exception:
        return ImageFont.truetype(path, size)


def ef(size=40):
    for s in [size, 40, 36, 44, 32]:
        try:
            return ImageFont.truetype(EMOJI_FONT, s)
        except Exception:
            continue


def text_w(draw, text, tfont, efont):
    w = 0
    for part in re.split(EMOJI_PAT, text):
        if not part:
            continue
        f = efont if EMOJI_PAT.match(part) else tfont
        b = draw.textbbox((0, 0), part, font=f)
        w += b[2] - b[0] + 2
    return w


def draw_text_emoji(draw, x, y, text, tfont, efont, fill):
    cx = x
    for part in re.split(r'([\U00010000-\U0010ffff\U00002600-\U000027BF\U0001F300-\U0001F9FF\U00002702-\U000027B0])', text):
        if not part:
            continue
        if EMOJI_PAT.match(part):
            draw.text((cx, y - 4), part, font=efont, embedded_color=True)
            b = draw.textbbox((0, 0), part, font=efont)
            cx += b[2] - b[0] + 4
        else:
            draw.text((cx, y), part, font=tfont, fill=fill)
            b = draw.textbbox((0, 0), part, font=tfont)
            cx += b[2] - b[0]


def download_image(url, filename):
    TMP_DIR.mkdir(exist_ok=True)
    path = TMP_DIR / filename
    subprocess.run(["curl", "-s", "-L", url, "-o", str(path)], check=True)
    return path


def make_instagram_post(
    bg_path: str,
    icon: str,
    question_lines: list[str],
    subtitle: str,
    url_slug: str,
    output_name: str,
):
    """
    Genera una imagen profesional para Instagram de GangaViaje.

    Args:
        bg_path:        Ruta local a la imagen de fondo (ya descargada)
        icon:           Emoji grande para el centro de la caja blanca (ej: "✈️")
        question_lines: Lista de 1-2 strings para el título en mayúsculas (ej: ["¿QUÉ VER EN JAPÓN", "MÁS ALLÁ DE TOKIO?"])
        subtitle:       Texto con emoji para debajo del título (ej: "✈️ Kioto, Osaka e Hiroshima")
        url_slug:       Slug del post del blog (ej: "japon-mas-alla-de-tokio-kyoto-osaka-hiroshima")
        output_name:    Nombre del archivo de salida (ej: "ig_post6_japon.jpg")
    """
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Cargar y recortar foto de fondo a cuadrado
    bg = Image.open(bg_path).convert("RGB")
    bw, bh = bg.size
    side = min(bw, bh)
    bg = bg.crop(((bw-side)//2, (bh-side)//2, (bw+side)//2, (bh+side)//2))
    bg = bg.resize((W, H), Image.LANCZOS)
    img = bg.copy().convert("RGBA")

    # Gradiente oscuro en la parte inferior (72%-100%)
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    bs = int(H * 0.72)
    for y in range(bs, H):
        od.line([(0, y), (W, y)], fill=(15, 15, 15, int((y - bs) / (H - bs) * 220)))
    img = Image.alpha_composite(img, ov)
    draw = ImageDraw.Draw(img)

    # Fuentes
    fq   = lf(BOLD_FONT, 68, 1)
    fs   = lf(BOLD_FONT, 38, 1)
    fe40 = ef(40)
    fe34 = ef(34)
    fe36 = ef(36)
    fcta = lf(BOLD_FONT, 36, 1)
    furl = lf(MEDIUM_FONT, 27)
    fb   = lf(BOLD_FONT, 34, 1)

    # Calcular altura de la caja blanca
    qh = sum(
        draw.textbbox((0,0), l, font=fq)[3] - draw.textbbox((0,0), l, font=fq)[1] + 6
        for l in question_lines
    )
    sh = draw.textbbox((0,0), subtitle, font=fs)[3] - draw.textbbox((0,0), subtitle, font=fs)[1]
    box_h = 56 + qh + sh + 36
    pad = 28
    bx1, by1 = pad, pad
    bx2, by2 = W - pad, pad + box_h

    # Caja blanca redondeada
    draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=20, fill=(255, 255, 255, 242))

    # Emoji grande centrado
    ib = draw.textbbox((0, 0), icon, font=fe40)
    draw.text(((W - (ib[2]-ib[0])) // 2, by1 + 10), icon, font=fe40, embedded_color=True)

    # Líneas de pregunta centradas
    y = by1 + 62
    for line in question_lines:
        b = draw.textbbox((0, 0), line, font=fq)
        draw.text(((W - (b[2]-b[0])) // 2, y), line, font=fq, fill=DARK)
        y += b[3] - b[1] + 4

    # Subtítulo con emoji en coral
    sw = text_w(draw, subtitle, fs, fe34)
    draw_text_emoji(draw, (W - sw) // 2, y + 6, subtitle, fs, fe34, CORAL)

    # CTA inferior
    cy = int(H * 0.75)
    cta = "GUÍA COMPLETA EN EL LINK"
    cb = draw.textbbox((0, 0), cta, font=fcta)
    cw = cb[2] - cb[0]
    draw.text(((W - cw - 54) // 2, cy), "👉", font=fe36, embedded_color=True)
    draw.text(((W - cw) // 2 + 8, cy), cta, font=fcta, fill=WHITE)

    url_text = f"gangaviaje.es/blog/{url_slug}"
    ub = draw.textbbox((0, 0), url_text, font=furl)
    uw = ub[2] - ub[0]
    draw.text(((W - uw) // 2, cy + 50), url_text, font=furl, fill=(200, 200, 200))

    # "GangaViaje" bicolor
    b1, b2 = "Ganga", "Viaje"
    b1b = draw.textbbox((0, 0), b1, font=fb)
    b2b = draw.textbbox((0, 0), b2, font=fb)
    bx = (W - (b1b[2]-b1b[0]) - (b2b[2]-b2b[0])) // 2
    draw.text((bx, cy + 94), b1, font=fb, fill=WHITE)
    draw.text((bx + b1b[2]-b1b[0], cy + 94), b2, font=fb, fill=CORAL)

    output_path = OUTPUT_DIR / output_name
    img.convert("RGB").save(str(output_path), quality=95)
    print(f"✓ Guardado: {output_path}")
    return str(output_path)


# ──────────────────────────────────────────────
# EJEMPLO DE USO — modifica estos datos para
# generar nuevos posts
# ──────────────────────────────────────────────
if __name__ == "__main__":
    import subprocess

    posts = [
        {
            "bg_url":    "https://images.unsplash.com/photo-1528360983277-13d401cdc186?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file":   "japon.jpg",
            "icon":      "✈️",
            "question":  ["¿QUÉ VER EN JAPÓN", "MÁS ALLÁ DE TOKIO?"],
            "subtitle":  "✈️ Kioto, Osaka e Hiroshima",
            "slug":      "japon-mas-alla-de-tokio-kyoto-osaka-hiroshima",
            "output":    "ig_post6_japon.jpg",
        },
    ]

    for p in posts:
        bg_path = download_image(p["bg_url"], p["bg_file"])
        make_instagram_post(
            bg_path=str(bg_path),
            icon=p["icon"],
            question_lines=p["question"],
            subtitle=p["subtitle"],
            url_slug=p["slug"],
            output_name=p["output"],
        )
