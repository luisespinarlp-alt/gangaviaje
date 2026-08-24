"""
Genera el PDF de un numero de la Revista GangaViaje a partir del contenido
real ya publicado (posts completos, no solo extractos). Usa Chrome headless
para "imprimir" la plantilla revista_pdf.html a PDF, en un tamano de pagina
tipo movil (4in x 7in), pensado para leerse sin descargar, directamente
en el navegador.

Uso: PYTHONPATH=. python3 scripts/generate_revista_pdf.py <slug-del-numero>
"""
import sys, os, subprocess, copy, re
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import database
import app as flask_app  # reutiliza el Jinja env ya configurado

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Fotos reales adicionales para intercalar DENTRO del cuerpo de artículos largos
# (no solo al principio) -- se insertan justo antes del <h2> marcador indicado,
# para repartir las imágenes a lo largo de toda la lectura y no dejar tramos
# de varias páginas seguidas sin ningún elemento visual.
INLINE_FIGURES = {
    "cracovia-polonia-guia-completa": [
        {
            "marker": "<h2>Kazimierz: el antiguo barrio judío, hoy el más de moda</h2>",
            "image_url": "https://images.unsplash.com/photo-1629812578764-7391a652959a?fm=jpg&q=80&w=1200&auto=format&fit=crop",
            "caption": "Un edificio de 1899 en Kazimierz, el antiguo barrio judío de Cracovia.",
        },
        {
            "marker": "<h2>La mina de sal de Wieliczka: el otro Patrimonio de la Humanidad cerca de Cracovia</h2>",
            "image_url": "https://images.unsplash.com/photo-1778765089143-5312b5e0997c?fm=jpg&q=80&w=1200&auto=format&fit=crop",
            "caption": "Una de las esculturas talladas en sal por los propios mineros, dentro de Wieliczka.",
        },
    ],
    "vuelos-baratos-trucos-encontrar-mejores-ofertas": [
        {
            "marker": "<h2>Ryanair, Vueling y las aerolíneas de bajo coste: cómo optimizar</h2>",
            "image_url": "https://images.unsplash.com/photo-1490430657723-4d607c1503fc?fm=jpg&q=80&w=1200&auto=format&fit=crop",
            "caption": "Un panel de salidas real — comparar antes de reservar sigue siendo el truco que más ahorra.",
        },
    ],
    "tristan-da-cunha-isla-mas-remota-del-mundo": [
        {
            "marker": "<h2>Cómo es vivir en el sitio más aislado del mundo</h2>",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Tristan_da_Cunha_-_Lobster_longboat.jpg/1280px-Tristan_da_Cunha_-_Lobster_longboat.jpg",
            "caption": "Un barco langostero real de Tristán da Cunha — la pesca de langosta sostiene la economía de la isla desde los años 50.",
        },
    ],
}


_FUENTES_RE = re.compile(r'<p style="font-size:0\.85rem[^"]*">Fuentes:.*?</p>', re.DOTALL)


def _strip_fuentes(content: str) -> str:
    """Quita la línea final de 'Fuentes: ...' -- es una cita de referencias
    pensada para la web, no aporta a la lectura del PDF y su longitud variable
    dejaba el artículo justo al borde de una página, causando páginas casi
    en blanco al final de cada artículo largo."""
    return _FUENTES_RE.sub("", content)


def _insert_inline_figures(content: str, post_slug: str) -> str:
    figures = INLINE_FIGURES.get(post_slug, [])
    for fig in figures:
        if fig["marker"] not in content:
            print(f"  ⚠️  marcador no encontrado para {post_slug}: {fig['marker'][:50]}")
            continue
        figure_html = (
            '<figure class="fig">'
            f'<div class="fimg" style="background-image:url(\'{fig["image_url"]}\');"></div>'
            f'<figcaption>{fig["caption"]}</figcaption>'
            '</figure>'
        )
        content = content.replace(fig["marker"], figure_html + fig["marker"], 1)
    return content


def build_pdf(slug: str):
    issue = database.get_magazine_issue_by_slug(slug)
    if not issue:
        print(f"No existe el número '{slug}'")
        return

    issue = dict(issue)
    sections = copy.deepcopy(issue["sections"])
    for s in sections:
        link = s.get("link", "")
        if link.startswith("/blog/"):
            post_slug = link.split("/blog/")[1]
            post = database.get_post_by_slug(post_slug)
            if post:
                content = _strip_fuentes(post["content"])
                s["full_content"] = _insert_inline_figures(content, post_slug)
    issue["sections"] = sections

    with flask_app.app.app_context():
        html = flask_app.render_template("revista_pdf.html", issue=issue)

    tmp_html = f"/tmp/revista_{slug}.html"
    with open(tmp_html, "w") as f:
        f.write(html)

    out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "pdf")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"revista-{slug}.pdf")

    subprocess.run([
        CHROME, "--headless", "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_path}",
        "--print-to-pdf-no-header",
        "--virtual-time-budget=15000",
        f"file://{tmp_html}",
    ], check=True)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"PDF generado: {out_path} ({size_kb:.0f} KB)")
    return out_path


if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "septiembre-2026"
    build_pdf(slug)
