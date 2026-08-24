"""
Tercer post de "Viajes Insolitos": Tristan da Cunha, la isla habitada mas
remota del mundo. Script de un solo uso.
Datos verificados via WebSearch/WebFetch (tristandc.com, sitio oficial de la
isla, y Wikipedia/Wikivoyage) el 2026-08-24 -- ver fuentes al pie del post.
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

CONTENT = f"""<p>Hay islas remotas y luego está Tristán da Cunha: el lugar habitado más aislado de la Tierra, tan lejos de todo que ni siquiera tiene aeropuerto. Si algún día quieres ir, tienes que reservar plaza en un barco de pesca y aceptar que el viaje puede durar más que unas vacaciones enteras a otro destino.</p>

<h2>¿Dónde está exactamente?</h2>
<p>Tristán da Cunha es un archipiélago volcánico en pleno Atlántico Sur, a <strong>2.810 km de Ciudad del Cabo</strong> (Sudáfrica), su punto habitado más cercano. Para hacerse una idea: es más del doble de la distancia entre Madrid y Nueva York. La isla más próxima con gente viviendo es Santa Elena — la misma donde estuvo exiliado Napoleón — y también está a más de 2.000 km.</p>

{vi("Tristán da Cunha en cifras", [
    "<strong>Población:</strong> apenas unos 220 habitantes en total.",
    "<strong>Apellidos:</strong> toda la isla se reparte entre nueve apellidos — Glass, Green, Hagan, Lavarello, Repetto, Rogers, Swain, Collins y Squibb.",
    "<strong>Distancia a Ciudad del Cabo:</strong> 2.810 km.",
    "<strong>Punto más alto:</strong> el Pico de la Reina María, un volcán activo de 2.062 metros — la última erupción registrada fue en 1961.",
    "<strong>Aeropuerto:</strong> ninguno. Nunca lo ha habido.",
])}

<h2>Cómo se llega: nada de vuelos, todo en barco</h2>
<p>El único modo de llegar a Tristán da Cunha es en barco desde Ciudad del Cabo, y el trayecto dura <strong>entre 5 y 10 días</strong> según el barco y el estado del mar. No hay una línea regular de pasajeros: los barcos que cubren la ruta son el buque de suministro del gobierno (el SA Agulhas II) y un puñado de barcos pesqueros — entre todos hacen unas 10 idas y vueltas al año, y las embarcaciones de pesca solo tienen capacidad para 12 pasajeros cada una.</p>
<p>Ir no es tan sencillo como comprar un billete. Hace falta <strong>autorización previa del Consejo de la Isla</strong>, en ocasiones un certificado de antecedentes penales (que puede tardar hasta 40 días en tramitarse), seguro médico que cubra una evacuación de emergencia a Ciudad del Cabo, y el pasaje de vuelta ya pagado por adelantado — no se puede llegar "a ver qué pasa" y decidir quedarse más tiempo del previsto.</p>

<h2>Cómo es vivir en el sitio más aislado del mundo</h2>
<p>Todos los habitantes viven en el mismo y único asentamiento de la isla, con el nombre más largo y curioso que le podían poner: <strong>Edimburgo de los Siete Mares</strong>. La economía se sostiene sobre tres pilares: la pesca de langosta (desde los años 50, es la principal fuente de ingresos de la isla), algo de agricultura de subsistencia, y la venta de sellos de correos a coleccionistas de todo el mundo — sí, los sellos de Tristán da Cunha son un objeto de culto entre filatélicos precisamente por lo inaccesible del lugar.</p>
<p>No hay señal de móvil de un operador externo ni cable submarino: la isla se comunica con el resto del mundo por teléfono y fax vía satélite. Aun así, tiene lo básico para no sentirse completamente fuera del mundo: una pequeña tienda, una emisora de radio local, un pub, un campo de fútbol y hasta una piscina.</p>

<h2>¿Se puede visitar de verdad?</h2>
<p>Sí, pero hay que quererlo mucho. No existen paquetes turísticos al uso — hay que gestionar el permiso, encontrar plaza en uno de los pocos barcos que hacen la ruta y aceptar que el viaje de ida y vuelta puede llevarse dos o tres semanas solo en trayecto. Periodistas, científicos y cineastas que quieran filmar o investigar en la isla tienen además que pagar una tasa de solicitud de 500 libras, no reembolsable, antes incluso de saber si el Consejo de la Isla aprueba la visita.</p>

<p style="font-size:0.85rem;color:#888;">Fuentes: <a href="https://www.tristandc.com/visitsorganise.php" target="_blank" rel="noopener">Tristan da Cunha — sitio oficial, cómo organizar una visita</a>, <a href="https://www.tristandc.com/population.php" target="_blank" rel="noopener">Tristan da Cunha — población</a>, <a href="https://es.wikipedia.org/wiki/Trist%C3%A1n_de_Acu%C3%B1a" target="_blank" rel="noopener">Wikipedia</a>. Foto: Brian Gratwicke (CC BY 2.0), vista de Tristán da Cunha desde la isla Nightingale.</p>
"""

post = {
    "slug": "tristan-da-cunha-isla-mas-remota-del-mundo",
    "title": "Tristán da Cunha: cómo es vivir en la isla habitada más remota del mundo",
    "excerpt": "A 2.810 km de Sudáfrica, sin aeropuerto y con solo 220 habitantes repartidos en nueve apellidos: así es la vida en el lugar habitado más aislado de la Tierra.",
    "content": CONTENT,
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/View_of_Tristan_da_Cunha_from_Nightingale_island.jpg/1920px-View_of_Tristan_da_Cunha_from_Nightingale_island.jpg",
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
