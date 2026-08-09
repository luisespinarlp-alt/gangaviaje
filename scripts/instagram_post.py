"""
Generador de imágenes Instagram — GangaViaje
Estética revista de viaje: foto a sangre + texto sobre gradiente oscuro.

FORMATOS:
1. make_instagram_post() — foto de destino a sangre, texto en la zona inferior
2. make_consejo_post()   — fondo oscuro limpio, lista de tips editorial
"""

import re
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

TERRACOTTA = (200, 90, 42)
WHITE      = (255, 255, 255)

W, H = 1080, 1080

BOLD_FONT   = "/System/Library/Fonts/HelveticaNeue.ttc"
MEDIUM_FONT = "/System/Library/Fonts/Helvetica.ttc"
EMOJI_FONT  = "/System/Library/Fonts/Apple Color Emoji.ttc"
OUTPUT_DIR  = Path("/Users/cex/Desktop/gangaviaje instagram")
TMP_DIR     = Path("/tmp/ig_imgs")

EMOJI_PAT = re.compile(
    r'[\U00010000-\U0010ffff\U00002600-\U000027BF'
    r'\U0001F300-\U0001F9FF\U00002702-\U000027B0]'
)
SPLIT_PAT = (
    r'([\U00010000-\U0010ffff\U00002600-\U000027BF'
    r'\U0001F300-\U0001F9FF\U00002702-\U000027B0]'
    r'[️︎]?)'  # consume variante gráfica para evitar cuadrado negro
)


def lf(path, size, idx=1):
    try:
        return ImageFont.truetype(path, size, index=idx)
    except Exception:
        return ImageFont.truetype(path, size)


def ef(size=40):
    # Apple Color Emoji TTC solo soporta: 40, 48, 64, 96
    VALID = [96, 64, 48, 40]
    # Si el tamaño pedido es menor que el mínimo (40), usar 40 — nunca escalar a 96
    candidates = [s for s in VALID if s <= size] or [VALID[-1]]
    for s in candidates:
        try:
            return ImageFont.truetype(EMOJI_FONT, s)
        except Exception:
            continue
    return None


def tw_mix(draw, text, tfont, efont):
    """Mide el ancho de texto mixto emoji+texto."""
    w = 0
    for part in re.split(SPLIT_PAT, text):
        if not part:
            continue
        f = efont if EMOJI_PAT.match(part) else tfont
        b = draw.textbbox((0, 0), part, font=f)
        w += b[2] - b[0] + (4 if EMOJI_PAT.match(part) else 0)
    return w


def draw_mixed(draw, x, y, text, tfont, efont, fill):
    """Dibuja texto mixto emoji+texto."""
    ref = draw.textbbox((0, 0), "H", font=tfont)
    cap_top, cap_h = ref[1], ref[3] - ref[1]
    cx = x
    for part in re.split(SPLIT_PAT, text):
        if not part:
            continue
        if EMOJI_PAT.match(part):
            eb = draw.textbbox((0, 0), part, font=efont)
            ey = y + cap_top + (cap_h - (eb[3] - eb[1])) // 2 - eb[1]
            draw.text((cx, ey), part, font=efont, embedded_color=True)
            cx += eb[2] - eb[0] + 4
        else:
            draw.text((cx, y), part, font=tfont, fill=fill)
            b = draw.textbbox((0, 0), part, font=tfont)
            cx += b[2] - b[0]


def download_image(url, filename):
    TMP_DIR.mkdir(exist_ok=True)
    path = TMP_DIR / filename
    subprocess.run(["curl", "-s", "-L", url, "-o", str(path)], check=True)
    return path


# ─────────────────────────────────────────────────────────────────────────────
# FORMATO 1: GUÍA DE DESTINO — foto a sangre, estilo revista
# ─────────────────────────────────────────────────────────────────────────────
def make_instagram_post(bg_path, icon, question_lines, subtitle, url_slug, output_name):
    """
    Foto de destino a sangre completa.
    Gradiente oscuro cálido en la mitad inferior.
    Todo el texto sobre el gradiente, alineado al fondo.
    """
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Cargar y recortar foto a cuadrado
    bg = Image.open(bg_path).convert("RGB")
    bw, bh = bg.size
    side = min(bw, bh)
    # Recortar centrando, con leve desplazamiento hacia arriba para mostrar más cielo/paisaje
    top = max(0, (bh - side) // 2 - side // 12)
    bg = bg.crop(((bw - side) // 2, top, (bw + side) // 2, top + side))
    bg = bg.resize((W, H), Image.LANCZOS)
    img = bg.copy().convert("RGBA")

    # GRADIENTE: un solo paso de arriba a abajo, sin corte visible
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)

    # α=42 en la cima (aplaca blancos/brumas sin apagar la foto) → α=255 al fondo
    # Curva t^0.52: suave arriba, agresiva en el tercio inferior donde va el texto
    for y in range(H):
        t = y / H
        alpha = min(42 + int(t ** 0.52 * 220), 255)
        od.line([(0, y), (W, y)], fill=(5, 3, 1, alpha))

    img = Image.alpha_composite(img, ov)
    draw = ImageDraw.Draw(img)

    # FRANJA TERRACOTA SUPERIOR (branding sutil)
    draw.rectangle([(0, 0), (W, 6)], fill=TERRACOTTA)

    # MARCA en la esquina superior izquierda
    fwm = lf(BOLD_FONT, 27, 1)
    wm_b1 = draw.textbbox((0, 0), "Ganga", font=fwm)
    draw.text((30, 20), "Ganga", font=fwm, fill=(255, 255, 255, 140))
    draw.text((30 + wm_b1[2] - wm_b1[0], 20), "Viaje", font=fwm, fill=(*TERRACOTTA, 190))

    # EMOJI en esquina superior derecha
    fei = ef(54)
    if fei:
        ib = draw.textbbox((0, 0), icon, font=fei)
        draw.text((W - (ib[2] - ib[0]) - 30, 12), icon, font=fei, embedded_color=True)

    # ── PREPARAR FUENTES PARA EL BLOQUE DE TEXTO INFERIOR ─────────────────
    # Auto-escalar título: margen mínimo de 160px cada lado (Instagram recorta ~110-135px en grid portrait)
    MAX_TITLE_W = W - 320
    _title_size = 78
    while _title_size > 40:
        _ft = lf(BOLD_FONT, _title_size, 1)
        _tmp = ImageDraw.Draw(Image.new("RGB", (W, H)))
        if all((_tmp.textbbox((0,0), l, font=_ft)[2] - _tmp.textbbox((0,0), l, font=_ft)[0]) <= MAX_TITLE_W
               for l in question_lines):
            break
        _title_size -= 2
    ftitle = lf(BOLD_FONT, _title_size, 1)
    fsub   = lf(BOLD_FONT, 37, 1)
    fcta   = lf(BOLD_FONT, 37, 1)
    furl   = lf(MEDIUM_FONT, 26)
    fbrand = lf(BOLD_FONT, 33, 1)
    fe36   = ef(36)
    fe33   = ef(33)

    # ── MEDIR TODOS LOS ELEMENTOS PARA POSICIONAR DE ABAJO HACIA ARRIBA ───
    MARGIN_BOT = 46

    b1_txt, b2_txt = "Ganga", "Viaje"
    b1b = draw.textbbox((0, 0), b1_txt, font=fbrand)
    b2b = draw.textbbox((0, 0), b2_txt, font=fbrand)
    brand_h = b1b[3] - b1b[1]
    brand_y = H - MARGIN_BOT - brand_h

    url_text = f"gangaviaje.es/blog/{url_slug}"
    url_bb = draw.textbbox((0, 0), url_text, font=furl)
    url_h = url_bb[3] - url_bb[1]
    url_w = url_bb[2] - url_bb[0]
    url_y = brand_y - url_h - 10

    cta_text = "GUÍA COMPLETA EN EL LINK"
    cta_bb = draw.textbbox((0, 0), cta_text, font=fcta)
    cta_h = cta_bb[3] - cta_bb[1]
    cta_w = cta_bb[2] - cta_bb[0]
    cta_y = url_y - cta_h - 14

    # Línea separadora terracota
    sep_y = cta_y - 28

    # Subtítulo
    sub_h_ref = draw.textbbox((0, 0), "Hg", font=fsub)[3] - draw.textbbox((0, 0), "Hg", font=fsub)[1]
    sub_y = sep_y - sub_h_ref - 18

    # Líneas del título (construyendo hacia arriba)
    title_data = []
    for line in question_lines:
        bb = draw.textbbox((0, 0), line, font=ftitle)
        title_data.append((line, bb[2] - bb[0], bb[3] - bb[1]))

    cur_y = sub_y - 10
    title_positions = []
    for _, _, th in reversed(title_data):
        cur_y -= (th + 6)
        title_positions.insert(0, cur_y)
        cur_y -= 2

    # ── DIBUJAR TÍTULO (con sombra para legibilidad sobre foto) ────────────
    for (line, lw, lh), ty in zip(title_data, title_positions):
        x = (W - lw) // 2
        # Sombra desplazada
        draw.text((x + 2, ty + 2), line, font=ftitle, fill=(0, 0, 0))
        draw.text((x + 1, ty + 1), line, font=ftitle, fill=(0, 0, 0))
        # Texto principal
        draw.text((x, ty), line, font=ftitle, fill=WHITE)

    # ── SUBTÍTULO ─────────────────────────────────────────────────────────
    sw = tw_mix(draw, subtitle, fsub, fe33)
    draw_mixed(draw, (W - sw) // 2, sub_y, subtitle, fsub, fe33, (230, 208, 185))

    # ── LÍNEA SEPARADORA ──────────────────────────────────────────────────
    draw.line([(60, sep_y), (W - 60, sep_y)], fill=(*TERRACOTTA, 200), width=2)

    # ── CTA ───────────────────────────────────────────────────────────────
    if fe36:
        draw.text(((W - cta_w - 52) // 2, cta_y), "👉", font=fe36, embedded_color=True)
    draw.text(((W - cta_w) // 2 + 8, cta_y), cta_text, font=fcta, fill=WHITE)

    # ── URL ───────────────────────────────────────────────────────────────
    draw.text(((W - url_w) // 2, url_y), url_text, font=furl, fill=(185, 168, 148))

    # ── MARCA ─────────────────────────────────────────────────────────────
    bx = (W - (b1b[2] - b1b[0]) - (b2b[2] - b2b[0])) // 2
    draw.text((bx, brand_y), b1_txt, font=fbrand, fill=WHITE)
    draw.text((bx + b1b[2] - b1b[0], brand_y), b2_txt, font=fbrand, fill=TERRACOTTA)

    output_path = OUTPUT_DIR / output_name
    img.convert("RGB").save(str(output_path), quality=95)
    print(f"  ✓ {output_name}")
    return str(output_path)


# ─────────────────────────────────────────────────────────────────────────────
# FORMATO 2: GANGACONSEJOS — editorial oscuro limpio
# ─────────────────────────────────────────────────────────────────────────────
def make_consejo_post(icon, title_lines, tips, url_slug, output_name):
    """
    Fondo oscuro cálido limpio. Sin texturas. Layout proporcional.
    Emoji grande, tips bien espaciados, sin espacio vacío excesivo.
    """
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Fondo: gradiente oscuro cálido puro — SIN TEXTURAS
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    TOP_C = (28, 22, 16)
    BOT_C = (7, 5, 3)
    for y in range(H):
        t = y / H
        r = int(TOP_C[0] + (BOT_C[0] - TOP_C[0]) * t)
        g = int(TOP_C[1] + (BOT_C[1] - TOP_C[1]) * t)
        b = int(TOP_C[2] + (BOT_C[2] - TOP_C[2]) * t)
        d.line([(0, y), (W, y)], fill=(r, g, b))

    # Franja terracota superior
    d.rectangle([(0, 0), (W, 8)], fill=TERRACOTTA)

    img = img.convert("RGBA")
    draw = ImageDraw.Draw(img)

    # ── FUENTES ────────────────────────────────────────────────────────────
    ftag   = lf(BOLD_FONT, 31, 1)
    # Auto-escalar título: mismo safe zone que posts de destino (160px margen mínimo)
    MAX_TITLE_W = W - 320
    _ts = 72
    while _ts > 36:
        _ft = lf(BOLD_FONT, _ts, 1)
        _td = ImageDraw.Draw(Image.new("RGB", (W, H)))
        if all((_td.textbbox((0,0),l,font=_ft)[2]-_td.textbbox((0,0),l,font=_ft)[0]) <= MAX_TITLE_W
               for l in title_lines):
            break
        _ts -= 2
    ftitle = lf(BOLD_FONT, _ts, 1)
    # Tips: margen izquierdo de 160px, texto máx hasta 160px del borde derecho
    BUL_X  = 160
    TIP_TEXT_X = BUL_X + 20 + 12   # bullet_radio*2 + gap
    MAX_TIP_W  = W - TIP_TEXT_X - 160
    _tips_s = 38
    while _tips_s > 24:
        _ft2 = lf(BOLD_FONT, _tips_s, 1)
        _td2 = ImageDraw.Draw(Image.new("RGB", (W, H)))
        if all((_td2.textbbox((0,0),t,font=_ft2)[2]-_td2.textbbox((0,0),t,font=_ft2)[0]) <= MAX_TIP_W
               for t in tips[:5]):
            break
        _tips_s -= 2
    ftip   = lf(BOLD_FONT, _tips_s, 1)
    fcta   = lf(BOLD_FONT, 34, 1)
    furl   = lf(MEDIUM_FONT, 26)
    fbrand = lf(BOLD_FONT, 32, 1)
    fe36   = ef(36)

    # ── MEDIR TODOS LOS BLOQUES ────────────────────────────────────────────
    # Badge GangaConsejos
    tag_bb = draw.textbbox((0, 0), "GangaConsejos", font=ftag)
    tag_w, tag_h = tag_bb[2] - tag_bb[0], tag_bb[3] - tag_bb[1]
    TAG_PX, TAG_PY = 26, 13
    badge_total_h = tag_h + TAG_PY * 2

    # Emoji — tamaño máximo soportado por Apple Color Emoji TTC
    ficon = ef(96)
    EMOJI_H = 96

    # Título
    title_bbs = [draw.textbbox((0, 0), l, font=ftitle) for l in title_lines]
    TITLE_GAP = 6
    title_total_h = sum(b[3] - b[1] for b in title_bbs) + TITLE_GAP * max(0, len(title_lines) - 1)

    # Tips
    tip_bbs = [draw.textbbox((0, 0), t, font=ftip) for t in tips[:5]]
    TIP_ROW = max((b[3] - b[1] for b in tip_bbs), default=50) + 22
    tips_total_h = TIP_ROW * len(tips[:5])

    # CTA block
    cta_text = "MÁS TRUCOS EN EL LINK"
    cta_bb = draw.textbbox((0, 0), cta_text, font=fcta)
    cta_h_val = cta_bb[3] - cta_bb[1]
    url_text = f"gangaviaje.es/blog/{url_slug}"
    url_bb = draw.textbbox((0, 0), url_text, font=furl)
    url_h_val = url_bb[3] - url_bb[1]
    b1b = draw.textbbox((0, 0), "Ganga", font=fbrand)
    b2b = draw.textbbox((0, 0), "Viaje", font=fbrand)
    brand_h = b1b[3] - b1b[1]
    cta_block_h = cta_h_val + 14 + url_h_val + 12 + brand_h

    # ── CALCULAR POSICIONES (distribución proporcional) ────────────────────
    # Espacio disponible = H - márgenes fijos
    MARGIN_TOP    = 36   # badge empieza aquí
    MARGIN_BOT    = 46   # espacio bajo el brand
    SEP_H         = 2
    DIV_H         = 1

    FIXED_H = (
        MARGIN_TOP + badge_total_h +    # badge
        EMOJI_H +                        # emoji
        title_total_h +                  # título
        SEP_H +                          # línea separadora
        tips_total_h +                   # tips
        DIV_H +                          # divisor
        cta_block_h +                    # bloque CTA
        MARGIN_BOT                       # margen inferior
    )
    FLEXIBLE = H - FIXED_H  # espacio sobrante a repartir entre gaps

    # 6 huecos: badge→emoji, emoji→título, título→sep, sep→tips, tips→div, div→cta
    GAP = max(12, FLEXIBLE // 6)

    badge_y   = MARGIN_TOP
    emoji_y   = badge_y + badge_total_h + GAP
    title_y   = emoji_y + EMOJI_H + GAP
    sep_y     = title_y + title_total_h + GAP
    tips_y    = sep_y + SEP_H + GAP
    div_y     = tips_y + tips_total_h + GAP
    cta_y     = div_y + DIV_H + GAP
    url_y     = cta_y + cta_h_val + 14
    brand_y   = url_y + url_h_val + 12

    # ── DIBUJAR ────────────────────────────────────────────────────────────

    # Badge "GangaConsejos"
    bx0 = (W - tag_w - TAG_PX * 2) // 2
    draw.rounded_rectangle(
        [(bx0, badge_y), (bx0 + tag_w + TAG_PX * 2, badge_y + badge_total_h)],
        radius=14, fill=TERRACOTTA
    )
    draw.text((bx0 + TAG_PX, badge_y + TAG_PY), "GangaConsejos", font=ftag, fill=WHITE)

    # Emoji grande centrado
    if ficon:
        ib = draw.textbbox((0, 0), icon, font=ficon)
        iw = ib[2] - ib[0]
        draw.text(((W - iw) // 2, emoji_y), icon, font=ficon, embedded_color=True)

    # Título
    ty = title_y
    for line, bb in zip(title_lines, title_bbs):
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2, ty), line, font=ftitle, fill=WHITE)
        ty += bb[3] - bb[1] + TITLE_GAP

    # Separador terracota
    draw.line([(80, sep_y), (W - 80, sep_y)], fill=(*TERRACOTTA, 160), width=SEP_H)

    # Tips
    ty = tips_y
    BUL_R = 10
    for tip, bb in zip(tips[:5], tip_bbs):
        th = bb[3] - bb[1]
        cy = ty + th // 2
        draw.ellipse([(BUL_X - BUL_R, cy - BUL_R), (BUL_X + BUL_R, cy + BUL_R)], fill=TERRACOTTA)
        draw.text((TIP_TEXT_X, ty), tip, font=ftip, fill=WHITE)
        ty += TIP_ROW

    # Divisor sutil
    draw.line([(60, div_y), (W - 60, div_y)], fill=(255, 255, 255, 22), width=DIV_H)

    # CTA
    cta_w = cta_bb[2] - cta_bb[0]
    if fe36:
        draw.text(((W - cta_w - 52) // 2, cta_y), "👉", font=fe36, embedded_color=True)
    draw.text(((W - cta_w) // 2 + 8, cta_y), cta_text, font=fcta, fill=WHITE)

    # URL
    url_w = url_bb[2] - url_bb[0]
    draw.text(((W - url_w) // 2, url_y), url_text, font=furl, fill=(170, 152, 132))

    # Marca bicolor
    bx = (W - (b1b[2] - b1b[0]) - (b2b[2] - b2b[0])) // 2
    draw.text((bx, brand_y), "Ganga", font=fbrand, fill=WHITE)
    draw.text((bx + b1b[2] - b1b[0], brand_y), "Viaje", font=fbrand, fill=TERRACOTTA)

    output_path = OUTPUT_DIR / output_name
    img.convert("RGB").save(str(output_path), quality=95)
    print(f"  ✓ {output_name}")
    return str(output_path)


def write_captions(guias, consejos):
    lines = ["=" * 60, "PIES DE FOTO — INSTAGRAM GANGAVIAJE", "=" * 60, ""]
    lines += ["── GUÍAS DE DESTINO ─────────────────────────────────", ""]
    for p in guias:
        lines += [f"📸  {p['output']}", "Caption:", p["caption"],
                  f"Hashtags: {p['hashtags']}", "-" * 50, ""]
    lines += ["── GANGACONSEJOS ────────────────────────────────────", ""]
    for c in consejos:
        lines += [f"📸  {c['output']}", "Caption:", c["caption"],
                  f"Hashtags: {c['hashtags']}", "-" * 50, ""]
    out = OUTPUT_DIR / "captions.txt"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"  ✓ captions.txt")


# ─────────────────────────────────────────────────────────────────────────────
# CONTENIDO
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":

    guias = [
        {
            "bg_url":  "https://images.unsplash.com/photo-1537996194471-e657df975ab4?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "bali.jpg",
            "icon": "🌴",
            "question": ["¿CUÁNTO CUESTA", "VIAJAR A BALI?"],
            "subtitle": "🌴 Presupuesto real día a día",
            "slug": "que-ver-en-bali-guia-completa",
            "output": "ig_bali.jpg",
            "caption": (
                "Bali no es tan cara como piensas 🌴\n\n"
                "Un bungalow con piscina privada por 40€, un pad thai por 1,50€ "
                "y un spa de 1 hora por 8€. No es un error.\n\n"
                "Hemos preparado el presupuesto real de Bali: qué cuesta el vuelo, "
                "dónde alojarse según tu bolsillo, cómo moverse y qué comer "
                "sin pagar precios de turista.\n\n"
                "👉 Guía completa en el link de nuestra bio\n\n"
                "¿Has estado ya en Bali? ¿Cuánto te gastaste al día? 👇"
            ),
            "hashtags": "#bali #indonesia #viajarbali #viajesasia #gangaviaje #guiaviaje #presupuestoviaje #viajarbarato #balitravel #destinosasia",
        },
        {
            "bg_url":  "https://images.unsplash.com/photo-1476610182048-b716b8518aae?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "islandia.jpg",
            "icon": "🌋",
            "question": ["ISLANDIA:", "¿VALE LA PENA?"],
            "subtitle": "🌋 Auroras, glaciares y cascadas",
            "slug": "que-ver-en-islandia-guia-completa",
            "output": "ig_islandia.jpg",
            "caption": (
                "Islandia es cara. Pero hay formas de hacerla asequible 🌋\n\n"
                "Vuelos desde 120€, cocinar en el alojamiento, furgoneta de alquiler "
                "compartida… Los viajeros que más disfrutan Islandia son los que "
                "van bien preparados, no los que más gastan.\n\n"
                "En nuestra guía: la mejor época para las auroras boreales, "
                "el itinerario por el Ring Road en 7 días y cuánto dinero necesitas realmente.\n\n"
                "👉 Link en bio\n\n"
                "¿Islandia en tu lista? 🙋"
            ),
            "hashtags": "#islandia #iceland #auroraboreales #viajarislandia #gangaviaje #guiaviaje #viajeseuropa #ringroad #cascadas #islandiatravel",
        },
        {
            "bg_url":  "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "maldivas.jpg",
            "icon": "🏝️",
            "question": ["MALDIVAS SIN", "GASTAR UNA FORTUNA"],
            "subtitle": "🐠 La guía que nadie te cuenta",
            "slug": "maldivas-guia-viaje-economico",
            "output": "ig_maldivas.jpg",
            "caption": (
                "Sí, se puede ir a Maldivas sin hipotecarse 🏝️\n\n"
                "El truco: islas locales (guesthouses) en vez de resorts privados. "
                "Mismas playas, misma agua turquesa, una fracción del precio.\n\n"
                "En nuestra guía: cómo llegar, dónde alojarse en cada isla, "
                "cuánto cuesta realmente y qué incluir en el presupuesto.\n\n"
                "👉 Guía completa → link en bio\n\n"
                "¿Maldivas es un sueño para ti? 🌊"
            ),
            "hashtags": "#maldivas #maldives #viajaramaldivas #playas #viajesdesueño #gangaviaje #guiaviaje #destinostropicales #viajarbarato #maldivesresort",
        },
        {
            "bg_url":  "https://images.unsplash.com/photo-1500916434205-0c77489c6cf7?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "nyc.jpg",
            "icon": "🗽",
            "question": ["NUEVA YORK:", "DÓNDE ALOJARSE"],
            "subtitle": "🗽 Barrios baratos + precios reales",
            "slug": "hoteles-baratos-nueva-york-donde-alojarse",
            "output": "ig_nueva_york.jpg",
            "caption": (
                "Dormir en Nueva York no tiene por qué arruinarte 🗽\n\n"
                "Brooklyn, Queens y Jersey City: mismo metro, mismas vistas, "
                "mismo acceso a Manhattan… pero 30-40% más barato.\n\n"
                "En nuestra guía: los mejores barrios por precio, qué esperar pagar "
                "en cada zona y cuándo reservar para las mejores tarifas.\n\n"
                "👉 Guía completa → link en bio\n\n"
                "¿Has estado en Nueva York? ¿En qué barrio te alojaste? 👇"
            ),
            "hashtags": "#nuevayork #newyork #nyc #viajaranyc #gangaviaje #guiaviaje #hotelesnuevayork #newyorktravel #manhattan #brooklyn",
        },
        {
            "bg_url":  "https://images.unsplash.com/photo-1565008576549-57569a49371d?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "georgia.jpg",
            "icon": "🏔️",
            "question": ["GEORGIA:", "EL DESTINO SORPRESA"],
            "subtitle": "🏔️ Tbilisi y el Cáucaso",
            "slug": "georgia-tbilisi-caucaso-guia-completa",
            "output": "ig_georgia.jpg",
            "caption": (
                "Georgia es el destino del que más vas a oír hablar este año 🏔️\n\n"
                "Una capital medieval, montañas del Cáucaso a 2 horas en coche, "
                "el mejor vino natural de Europa y precios increíblemente bajos.\n\n"
                "En nuestra guía: qué ver en Tbilisi, cuánto cuesta viajar "
                "y los rincones que no aparecen en ninguna guía turística.\n\n"
                "👉 Link en bio\n\n"
                "¿Georgia está en tu lista? 🇬🇪"
            ),
            "hashtags": "#georgia #tbilisi #caucaso #viajarageorgia #gangaviaje #guiaviaje #destinossecretos #viajeseuropa #georgiatravel #caucasus",
        },
        {
            "bg_url":  "https://images.unsplash.com/photo-1549893072-4bc678117f45?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "croacia.jpg",
            "icon": "⛵",
            "question": ["CROACIA:", "DUBROVNIK Y SPLIT"],
            "subtitle": "⛵ Mar Adriático y muros medievales",
            "slug": "croacia-dubrovnik-split-guia-completa",
            "output": "ig_croacia.jpg",
            "caption": (
                "Croacia es impresionante. Y más asequible de lo que imaginas ⛵\n\n"
                "Dubrovnik con sus murallas medievales, Split con su palacio romano, "
                "las islas de Hvar y Brač con aguas turquesas.\n\n"
                "En nuestra guía: itinerario de 7-10 días, cómo moverse entre islas, "
                "dónde comer bien y cuándo ir para evitar la masificación de agosto.\n\n"
                "👉 Guía completa → link en bio\n\n"
                "¿Croacia en tus planes? 🙋"
            ),
            "hashtags": "#croacia #croatia #dubrovnik #split #viajesmediterraneo #gangaviaje #guiaviaje #adriatico #croatiatravel #europearoadtrip",
        },
        {
            "bg_url":  "https://images.unsplash.com/photo-1528360983277-13d401cdc186?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "japon.jpg",
            "icon": "🌸",
            "question": ["JAPÓN:", "MÁS ALLÁ DE TOKIO"],
            "subtitle": "🌸 Kioto, Osaka e Hiroshima",
            "slug": "japon-mas-alla-de-tokio-kyoto-osaka-hiroshima",
            "output": "ig_japon.jpg",
            "caption": (
                "Japón te va a cambiar. Esto no es un cliché 🌸\n\n"
                "Kioto con sus jardines zen, Osaka con su gastronomía callejera, "
                "Hiroshima y la isla de Miyajima con el torii flotante...\n\n"
                "En nuestra guía: cómo planificar el viaje, el JR Pass (cuándo vale "
                "la pena), presupuesto real y los errores del viajero por primera vez.\n\n"
                "👉 Guía completa → link en bio\n\n"
                "¿Has estado en Japón? Lo mejor que viste 👇"
            ),
            "hashtags": "#japon #japan #kyoto #osaka #hiroshima #viajarajapon #gangaviaje #guiaviaje #japantravel #asiatravel",
        },
        {
            "bg_url":  "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "paris.jpg",
            "icon": "🗼",
            "question": ["PARÍS EN 4 DÍAS:", "GUÍA COMPLETA"],
            "subtitle": "🥐 Barrios, museos y comer barato",
            "slug": "paris-tres-dias-itinerario",
            "output": "ig_paris.jpg",
            "caption": (
                "París es cara. Pero hay formas de no dejarse el sueldo 🗼\n\n"
                "Los museos más importantes tienen entrada gratuita el primer domingo "
                "del mes. Los mejores croissants no están en el centro turístico. "
                "Y el metro es barato y eficiente.\n\n"
                "En nuestra guía: itinerario de 4 días, los barrios que los turistas "
                "no conocen y cómo comer bien por 12-15€.\n\n"
                "👉 Guía completa → link en bio\n\n"
                "¿Cuál es tu rincón favorito de París? 👇"
            ),
            "hashtags": "#paris #france #viajaraparis #paristrip #gangaviaje #guiaviaje #viajeseuropa #paristravel #torreiffel #europatrip",
        },
        {
            "bg_url":  "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "playas_esp.jpg",
            "icon": "☀️",
            "question": ["LAS MEJORES PLAYAS", "DE ESPAÑA"],
            "subtitle": "☀️ Mediterráneo, Atlántico y Canarias",
            "slug": "mejores-playas-espana-guia-completa",
            "output": "ig_playas_espana.jpg",
            "caption": (
                "España tiene algunas de las mejores playas del mundo ☀️\n\n"
                "Y la mayoría de los españoles no conocen ni la mitad de ellas.\n\n"
                "Calas vírgenes en Menorca, playas kilométricas en Tarifa, "
                "aguas turquesas en Formentera, dunas de Fuerteventura...\n\n"
                "En nuestra guía: las playas más espectaculares por región, "
                "cuándo ir a cada una y cómo llegar.\n\n"
                "👉 Guía completa → link en bio\n\n"
                "¿Cuál es la mejor playa que has visto en España? 🙋"
            ),
            "hashtags": "#playasespana #spain #mediterraneo #canarias #gangaviaje #guiaviaje #viajarespana #playa #spaintravel #escapadas",
        },
        {
            "bg_url":  "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "europa_barata.jpg",
            "icon": "✈️",
            "question": ["EUROPA DESDE 100€:", "ES POSIBLE"],
            "subtitle": "✈️ Vuelo + hotel + transporte",
            "slug": "viaje-europa-barato-100-euros",
            "output": "ig_europa_barata.jpg",
            "caption": (
                "¿Un fin de semana en Europa por 100€? Sí, es real ✈️\n\n"
                "Praga, Oporto, Budapest, Berlín, Cracovia... Hay destinos europeos "
                "donde el vuelo sale por 50-70€ ida y vuelta, el hotel por 50-80€ "
                "las dos noches y la comida no supera los 20€ al día.\n\n"
                "En nuestra guía: los destinos más baratos de Europa por temporada "
                "y cuánto dinero necesitas realmente.\n\n"
                "👉 Guía completa → link en bio\n\n"
                "¿A qué ciudad europea volarías este fin de semana? 👇"
            ),
            "hashtags": "#europabarata #viajeseuropa #vuelosbaratos #escapada #gangaviaje #guiaviaje #eurotrip #viajarbarato #findesemana #europe",
        },
        {
            "bg_url":  "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "roma.jpg",
            "icon": "🍕",
            "question": ["ROMA EN 3 DÍAS:", "GUÍA COMPLETA"],
            "subtitle": "🍕 Coliseo, Vaticano y mucho más",
            "slug": "que-ver-en-roma-tres-dias",
            "output": "ig_roma.jpg",
            "caption": (
                "Roma en 3 días. ¿Es posible verla bien? Sí, si planificas 🏛️\n\n"
                "El Coliseo de mañana (reserva online, sin colas). "
                "Los Museos Vaticanos con entrada previa. "
                "Trastevere al atardecer para cenar sin pagar precios de turista.\n\n"
                "El itinerario hora a hora para 3 días: qué ver, dónde comer, "
                "cómo moverse y cuánto dinero necesitas.\n\n"
                "👉 Guía completa → link en bio\n\n"
                "¿Cuántas veces has estado en Roma? 🍕"
            ),
            "hashtags": "#roma #rome #italia #italy #viajaraitalia #gangaviaje #guiaviaje #romaitaly #colosseum #viajeseuropa",
        },
        {
            "bg_url":  "https://images.unsplash.com/photo-1508009603885-50cf7c579365?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "bangkok.jpg",
            "icon": "🛺",
            "question": ["BANGKOK:", "GUÍA PARA NOVATOS"],
            "subtitle": "🛺 Templos, comida y presupuesto",
            "slug": "bangkok-primera-vez-guia-rapida",
            "output": "ig_bangkok.jpg",
            "caption": (
                "Bangkok es caótica, ruidosa y absolutamente increíble 🛺\n\n"
                "El Wat Phra Kaew con sus mosaicos dorados, los canales de Thonburi "
                "en lancha de cola larga y un pad thai por 1,50€ en cualquier esquina.\n\n"
                "En nuestra guía: los imprescindibles, cómo moverse (BTS o Grab), "
                "dónde comer, dónde alojarse y el presupuesto real para 3-4 días.\n\n"
                "👉 Guía completa → link en bio\n\n"
                "¿Has estado en Bangkok? ¿Qué no te perdiste? 👇"
            ),
            "hashtags": "#bangkok #tailandia #thailand #viajaratailandia #gangaviaje #guiaviaje #bangkoktravel #asiatravel #comidacallejera #sudesteasiatico",
        },
        {
            "bg_url":  "https://images.unsplash.com/photo-1541343672885-9be56236302a?fm=jpg&q=85&w=1080&auto=format&fit=crop",
            "bg_file": "budapest.jpg",
            "icon": "♨️",
            "question": ["BUDAPEST:", "BALNEARIOS Y DANUBIO"],
            "subtitle": "♨️ La perla del Danubio por poco",
            "slug": "budapest-que-ver-balnearios-y-rio",
            "output": "ig_budapest.jpg",
            "caption": (
                "Budapest es de las ciudades más bonitas de Europa. Y de las más baratas ♨️\n\n"
                "El Parlamento iluminado al otro lado del Danubio, el Bastión de los "
                "Pescadores al amanecer y un baño termal en el Széchenyi por 20€.\n\n"
                "En nuestra guía: los balnearios que no son una trampa turística, "
                "qué ver en Buda y en Pest y cuánto dinero necesitas para 3-4 días.\n\n"
                "👉 Guía completa → link en bio\n\n"
                "¿Budapest en tu lista? 🙋"
            ),
            "hashtags": "#budapest #hungria #hungary #viajarabudapest #gangaviaje #guiaviaje #budapesttravel #danubio #balnearios #europabarata",
        },
    ]

    consejos = [
        {
            "icon": "✈️",
            "title": ["VOLAR MÁS BARATO:", "5 TRUCOS REALES"],
            "tips": [
                "Busca martes o miércoles, no fin de semana",
                "Activa alertas en Google Flights",
                "Aeropuertos secundarios = -30% de precio",
                "Sé flexible ±2 días en las fechas",
                "6-10 semanas antes: el punto dulce",
            ],
            "slug": "viajar-low-cost-trucos-vuelos-baratos",
            "output": "ig_consejo_vuelos.jpg",
            "caption": (
                "El 90% de la gente busca vuelos mal 👀\n\n"
                "No es que los vuelos baratos no existan — es que hay un momento "
                "concreto y una forma concreta de buscarlos.\n\n"
                "Estos 5 trucos los usamos en GangaViaje para encontrar "
                "vuelos hasta un 60% más baratos. Guarda este post.\n\n"
                "Y si quieres la guía completa con herramientas y calendarios:\n"
                "👉 Link en bio\n\n"
                "¿Cuál de estos trucos ya usabas? 👇"
            ),
            "hashtags": "#vuelosbaratos #trucosviajar #lowcost #viajarsinedinero #gangaviaje #consejosviaje #vuelos #ahorrarviajar #viajes #gangaconsejos",
        },
        {
            "icon": "🌟",
            "title": ["HOTEL BARATO:", "8 TRUCOS QUE FUNCIONAN"],
            "tips": [
                "Compara en Booking, reserva directo",
                "1 km del centro = 30-40% más barato",
                "Las estrellas no son garantía de calidad",
                "Busca entre semana, no en finde",
                "Cancela gratis: siempre la mejor opción",
            ],
            "slug": "hoteles-baratos-nueva-york-donde-alojarse",
            "output": "ig_consejo_hoteles.jpg",
            "caption": (
                "Pagar de más por el hotel es el error más común 🏨\n\n"
                "El método más sencillo: compara en Booking pero reserva directo "
                "con el hotel. Ahorras entre un 10-20% solo con eso.\n\n"
                "El truco de alejarte 1 km del centro reduce el precio un 30-40% "
                "sin perder apenas tiempo en transporte.\n\n"
                "👉 Guía completa → link en bio\n\n"
                "¿Cuándo fue la última vez que pagaste de más por un hotel? 👇"
            ),
            "hashtags": "#hotelbarato #alojamiento #viajarbarato #trucosviajar #gangaviaje #gangaconsejos #consejosviaje #booking #hoteles #ahorrarviajar",
        },
        {
            "icon": "🎒",
            "title": ["10 KG PARA 7 DÍAS:", "SÍ SE PUEDE"],
            "tips": [
                "Solo ropa que combine entre sí",
                "Lava en el destino si es más de 5 días",
                "Comprime con bolsas de vacío",
                "Toiletries sólidos: sin restricciones",
                "Pesa en casa antes de salir",
            ],
            "slug": "viajar-low-cost-trucos-vuelos-baratos",
            "output": "ig_consejo_equipaje.jpg",
            "caption": (
                "Viajar una semana con solo equipaje de mano es posible. Y te cambia la vida ✈️\n\n"
                "Sin esperar maletas. Sin pagar extra a la aerolínea. "
                "Sin llegar a destino y que tu maleta no haya llegado.\n\n"
                "Con estos trucos hemos viajado 10 días por Tailandia "
                "con una mochila de 7 kg. La clave está en qué ropa eliges, no en cuánta llevas.\n\n"
                "👉 Guía de equipaje de mano → link en bio\n\n"
                "¿Viajas con maleta o con mochila? 👇"
            ),
            "hashtags": "#equipajemano #viajarsinedinero #mochilero #trucosviajar #gangaviaje #gangaconsejos #viajarligero #lowcost #consejosviaje #mochilaviajar",
        },
        {
            "icon": "⏳",
            "title": ["¿CUÁNDO RESERVAR", "EL VUELO BARATO?"],
            "tips": [
                "Europa / cortos: 6-10 semanas antes",
                "Larga distancia: 3-5 meses antes",
                "Enero y febrero: los meses más baratos",
                "Black Friday: solo si ya lo necesitas",
                "No esperes que baje la última semana",
            ],
            "slug": "viajar-low-cost-trucos-vuelos-baratos",
            "output": "ig_consejo_cuando_reservar.jpg",
            "caption": (
                "¿Reservar pronto o esperar a última hora? Ninguna de las dos 📅\n\n"
                "El mito de que los vuelos bajan a última hora lleva años sin funcionar. "
                "Las aerolíneas lo saben y suben el precio cuando queda poco tiempo.\n\n"
                "El punto dulce real: 6-10 semanas para vuelos europeos, "
                "3-5 meses para vuelos intercontinentales.\n\n"
                "👉 Link en bio\n\n"
                "¿Cuándo sueles reservar tus vuelos? 👇"
            ),
            "hashtags": "#cuandoreservar #vuelosbaratos #trucosviajar #gangaviaje #gangaconsejos #viajes #lowcost #consejosviaje #vuelos #viajarbarato",
        },
        {
            "icon": "🔒",
            "title": ["SEGURO DE VIAJE:", "QUÉ MIRAR SIEMPRE"],
            "tips": [
                "Cobertura médica mínimo 150.000€",
                "Cancelación por cualquier motivo",
                "Contrata al reservar, no el día antes",
                "Compara: IATI, Mondo, AXA, Allianz",
                "No es lo mismo que el seguro del banco",
            ],
            "slug": "viajar-low-cost-trucos-vuelos-baratos",
            "output": "ig_consejo_seguro.jpg",
            "caption": (
                "El seguro de viaje es lo único que no debes escatimar 🛡️\n\n"
                "Una urgencia médica en EE.UU. puede costarte 50.000€. "
                "Un vuelo cancelado sin cobertura: 300€ perdidos. "
                "Una mochila robada en Bangkok sin seguro: 800€ de pérdida.\n\n"
                "En nuestra guía: qué cubre cada tipo, cuánto cuesta uno bueno "
                "y las mejores opciones para cada viaje.\n\n"
                "👉 Guía de seguros → link en bio\n\n"
                "¿Contratas seguro siempre o a veces lo saltas? 👇"
            ),
            "hashtags": "#segurodeviaje #trucosviajar #gangaviaje #gangaconsejos #consejosviaje #viajes #iati #seguroviajero #viajarbarato #travelinsurance",
        },
        {
            "icon": "🔑",
            "title": ["ALQUILER DE COCHE:", "LO QUE NO TE CUENTAN"],
            "tips": [
                "Mira la franquicia del seguro",
                "Fotografía el coche antes de salir",
                "Tarjeta de crédito puede cubrirte",
                "Lleno por lleno: la única opción lógica",
                "Rechaza los seguros del mostrador",
            ],
            "slug": "alquiler-coche-espana-que-mirar",
            "output": "ig_consejo_coche.jpg",
            "caption": (
                "Alquilar un coche sin leer la letra pequeña puede salirte muy caro 🚗\n\n"
                "El seguro que no contrataste, la franquicia que no viste, "
                "el depósito de 1.500€ bloqueado en tu tarjeta...\n\n"
                "En nuestra guía: qué revisar antes de firmar, cómo cubrirte "
                "con la tarjeta de crédito y qué compañías son realmente fiables.\n\n"
                "👉 Guía de alquiler de coche → link en bio\n\n"
                "¿Alguna vez te han cobrado algo inesperado al devolver el coche? 👇"
            ),
            "hashtags": "#alquilercoche #rentacar #trucosviajar #gangaviaje #gangaconsejos #consejosviaje #viajes #cochealquiler #viajarbarato #conductorexperiente",
        },
        {
            "icon": "☀️",
            "title": ["CANARIAS:", "¿CUÁNDO IR?"],
            "tips": [
                "Enero-febrero: barato y sin aglomeraciones",
                "Sept-octubre: el mejor equilibrio",
                "Julio-agosto: calor y precios altos",
                "Semana Santa: evítala, precio x3",
                "La Palma y La Gomera: siempre son mejor",
            ],
            "slug": "mejor-epoca-viajar-canarias",
            "output": "ig_consejo_canarias.jpg",
            "caption": (
                "Canarias funciona todo el año. Pero hay un momento donde es perfecta 🌅\n\n"
                "Septiembre y octubre: agua a 22-24°C, precios un 30% más bajos "
                "que en verano, playas tranquilas y tiempo perfecto.\n\n"
                "Los meses más baratos: enero y febrero. "
                "Las islas más tranquilas: La Palma, La Gomera y El Hierro.\n\n"
                "En nuestra guía: comparativa de las 7 islas y cuándo ir a cada una.\n"
                "👉 Link en bio\n\n"
                "¿Cuál es tu isla favorita de Canarias? 🙋"
            ),
            "hashtags": "#canarias #islascanarias #tenerife #fuerteventura #lanzarote #gangaviaje #gangaconsejos #viajaracanarias #canariasislands #españavacaciones",
        },
    ]

    # ── BORRAR IMÁGENES ANTIGUAS ──────────────────────────────────────────────
    print("Eliminando imágenes antiguas...")
    OUTPUT_DIR.mkdir(exist_ok=True)
    deleted = 0
    for f in OUTPUT_DIR.glob("ig_*.jpg"):
        f.unlink()
        deleted += 1
    print(f"  🗑  {deleted} imágenes eliminadas")

    # ── GENERAR GUÍAS ─────────────────────────────────────────────────────────
    print(f"\nGenerando {len(guias)} guías de destino...")
    for p in guias:
        try:
            bg_path = download_image(p["bg_url"], p["bg_file"])
            make_instagram_post(
                bg_path=str(bg_path),
                icon=p["icon"],
                question_lines=p["question"],
                subtitle=p["subtitle"],
                url_slug=p["slug"],
                output_name=p["output"],
            )
        except Exception as e:
            print(f"  ✗ Error en {p['output']}: {e}")

    # ── GENERAR CONSEJOS ──────────────────────────────────────────────────────
    print(f"\nGenerando {len(consejos)} GangaConsejos...")
    for c in consejos:
        try:
            make_consejo_post(
                icon=c["icon"],
                title_lines=c["title"],
                tips=c["tips"],
                url_slug=c["slug"],
                output_name=c["output"],
            )
        except Exception as e:
            print(f"  ✗ Error en {c['output']}: {e}")

    print("\nGenerando captions.txt...")
    write_captions(guias, consejos)

    total = len(guias) + len(consejos)
    print(f"\n✅ Listo — {total} imágenes + captions.txt en:\n   {OUTPUT_DIR}")
