"""
Añade el primer post de la nueva categoría "Viajes Insólitos":
pueblos italianos que venden casas por 1 euro.
Script de un solo uso.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database

_VI_BOX = (
    '<div style="background:linear-gradient(135deg,#e6f5f3,#f8fffe);'
    'border-left:4px solid #2E9E8F;border-radius:8px;padding:20px 24px;margin:32px 0;">'
)

def vi(titulo, items):
    li = "".join("<li>" + i + "</li>" for i in items)
    return (
        _VI_BOX
        + '<h2 style="color:#2E9E8F;margin-top:0;">' + titulo + '</h2>'
        + '<ul style="margin-bottom:0;">' + li + '</ul>'
        + '</div>'
    )

CONTENT = f"""<p>En 2026 el programa sigue vivo y más grande que nunca: el Ministerio de Cultura italiano lo ha integrado dentro de su plan de "residencialidad activa" (PNRR Cultura), y ya está presente en <strong>14 regiones de Italia</strong>. El precio de la casa es literal: un euro. La condición, también literal: reformarla en un plazo fijado, o pierdes el depósito.</p>

<h2>Dónde está activo ahora mismo</h2>
<p>Sambuca y Mussomeli (Sicilia), Ollolai (Cerdeña), Norma (Lazio), Calatafimi Segesta, Augusta, Caltagirone y Pratola Peligna, entre otros — con programas similares en marcha en Toscana, Piamonte, Calabria y Las Marcas. Cada municipio publica su propio listado y sus propias condiciones, así que conviene mirar el ayuntamiento concreto antes de ilusionarse con un pueblo en particular.</p>

{vi("Lo que de verdad piden a cambio del euro", [
    "Un depósito de garantía — entre 1.000€ y 6.000€ según el municipio — que te devuelven íntegro al terminar la reforma.",
    "Presentar un proyecto de rehabilitación viable, normalmente dentro de los primeros 6 meses tras la compra.",
    "Empezar las obras en el primer año, y terminarlas en un plazo de hasta 3 años según el pueblo.",
    "Pagar tú los gastos de notaría, registro y catastro — eso nunca es gratis, aunque la casa sí lo sea.",
])}

<h2>Lo que de verdad cuesta la reforma</h2>
<p>Esto es lo que casi nunca se cuenta: una reforma básica ronda entre <strong>10.000€ y 30.000€</strong>. Una reforma completa de calidad puede superar los <strong>200.000€</strong>, dependiendo del estado del inmueble y de cuánto quieras conservar de la estructura original. La casa es un euro; convertirla en habitable, no.</p>

<h2>¿Merece la pena?</h2>
<p>Depende de qué busques. No es una forma de vivir gratis — nadie sale de esto sin gastar dinero de verdad. Es una vía de entrada barata para comprar en pueblos italianos preciosos, con mucho carácter y muy despoblados, que de otra forma no te podrías permitir — a cambio del compromiso real de arreglarlos y, muchas veces, de mudarte allí una parte del año.</p>

<p style="font-size:0.85rem;color:#888;">Fuentes: <a href="https://www.infobae.com/espana/2026/06/18/el-pueblo-italiano-que-ofrece-casas-por-un-euro-estos-son-los-requisitos-para-acceder-a-la-compra-de-viviendas/" target="_blank" rel="noopener">Infobae</a>, <a href="https://es.gizmodo.com/esta-idilica-ciudad-en-sicilia-vende-casas-a-1-euro-con-1831920927" target="_blank" rel="noopener">Gizmodo</a>, <a href="https://www.cambio16.com/casas-a-un-euro-contra-la-despoblacion-del-sur-de-italia/" target="_blank" rel="noopener">Cambio16</a>.</p>
"""

post = {
    "slug": "pueblos-italia-casas-1-euro-2026",
    "title": "Pueblos italianos que te venden una casa por 1€ (y lo que de verdad cuesta después)",
    "excerpt": "El programa sigue activo en 2026 en 14 regiones de Italia. Qué piden a cambio del euro, y cuánto cuesta de verdad la reforma que nadie cuenta.",
    "content": CONTENT,
    "image_url": "https://images.unsplash.com/photo-1631994121341-9209081396dd?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "category": "insolitos",
}

if __name__ == "__main__":
    post_id = database.add_post(post)
    if post_id is None:
        conn = database.get_conn()
        cur = conn.cursor()
        cur.execute(
            "UPDATE posts SET title=%s, excerpt=%s, content=%s, image_url=%s, category=%s WHERE slug=%s RETURNING id",
            (post["title"], post["excerpt"], post["content"], post["image_url"], post["category"], post["slug"]),
        )
        row = cur.fetchone()
        conn.commit()
        conn.close()
        post_id = row[0] if row else None
        print("post ya existía, actualizado:", post_id)
    else:
        print("post nuevo insertado, id:", post_id)
