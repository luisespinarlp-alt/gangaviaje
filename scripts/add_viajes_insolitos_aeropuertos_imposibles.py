"""
Quinto post de "Viajes Insolitos": los aeropuertos mas dificiles de aterrizar
del mundo (Saba y Paro). Script de un solo uso.
Datos verificados via WebSearch (CNN, Simple Flying, Guinness/récords de
aviación) el 2026-08-25 -- ver fuentes al pie del post.
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

CONTENT = f"""<p>Hay vuelos que se disfrutan desde que despegas, y hay vuelos en los que la parte más memorable es, literalmente, el último minuto. Estos dos aeropuertos tienen la pista más corta y la aproximación más difícil del mundo — y aun así, aterrizan aviones comerciales todos los días.</p>

<h2>Saba: la pista comercial más corta del mundo</h2>
<p>El aeropuerto Juancho E. Yrausquin, en la diminuta isla caribeña de Saba (territorio neerlandés), tiene una pista de solo <strong>400 metros</strong> — la más corta del mundo para vuelos comerciales regulares. Para hacerse una idea: una pista normal de aeropuerto internacional mide entre 2.500 y 4.000 metros. La pista de Saba tiene <strong>acantilados en tres de sus cuatro lados</strong>, cayendo directamente al mar, y una colina cierra el cuarto lado — no hay margen de error real en ninguna dirección.</p>

{vi("Saba en cifras", [
    "<strong>Longitud de pista:</strong> 400 metros (1.312 pies).",
    "<strong>Aerolínea que opera allí:</strong> Winair, con aviones pequeños Twin Otter de 18-19 plazas — es literalmente el único tipo de avión que puede operar en la pista.",
    "<strong>Entorno:</strong> mar en tres lados, colina en el cuarto.",
    "<strong>Souvenir local real:</strong> camisetas que se venden en la isla con el texto \"I survived the Saba landing!\" (sobreviví al aterrizaje de Saba).",
])}

<h2>Paro (Bután): entre picos del Himalaya, sin radar</h2>
<p>Si Saba gana por longitud de pista, el aeropuerto de Paro, en Bután, gana por dificultad técnica de la maniobra. Es el único aeropuerto internacional del país, situado en un valle rodeado de picos del Himalaya de hasta 5.500 metros — el avión tiene que descender maniobrando entre montañas en los últimos minutos, sin ayuda de radar, guiado solo a la vista por el piloto.</p>
<p>Por eso Paro está clasificado como aeropuerto de <strong>categoría C</strong>, la más exigente: hace falta un entrenamiento especial además de la licencia de piloto comercial normal, con un mínimo de 1.500 horas de vuelo y certificado ATP (Airline Transport Pilot). Según la fuente, la cifra varía, pero las estimaciones más citadas hablan de <strong>menos de 50 pilotos en todo el mundo</strong> certificados para aterrizar ahí. Los vuelos solo operan de día y con buen tiempo — nada de aterrizajes nocturnos ni con niebla.</p>

<h2>¿Da miedo volar hasta allí?</h2>
<p>Menos de lo que parece. Ambos aeropuertos llevan décadas operando vuelos comerciales regulares con un historial de seguridad sólido — la dificultad está en la formación exigida al piloto, no en un riesgo real para el pasajero. De hecho, en ambos casos el aterrizaje se ha convertido en parte de la experiencia turística: en Saba, los pasajeros suelen aplaudir al tocar tierra, y las vistas de la aproximación a Paro (con el Himalaya prácticamente pegado a la ventanilla) son de las postales más repetidas de quienes visitan Bután.</p>

<p style="font-size:0.85rem;color:#888;">Fuentes: <a href="https://www.cnn.com/travel/article/saba-airport-shortest-commercial-runway" target="_blank" rel="noopener">CNN — aterrizando en la pista comercial más corta del mundo</a>, <a href="https://www.cnn.com/travel/paro-bhutan-airport-landing-intl-hnk" target="_blank" rel="noopener">CNN — los trucos de uno de los aterrizajes más difíciles del mundo</a>, <a href="https://simpleflying.com/bhutan-paro-airport-worlds-scariest/" target="_blank" rel="noopener">Simple Flying</a>. Foto: James G. Lea (CC BY-SA 3.0), aeropuerto de Saba visto desde el acantilado.</p>
"""

post = {
    "slug": "aeropuertos-mas-dificiles-de-aterrizar-del-mundo",
    "title": "Saba y Paro: los aeropuertos más difíciles de aterrizar del mundo",
    "excerpt": "Una pista de solo 400 metros con acantilados en tres lados, y otra entre picos del Himalaya sin radar: los dos aeropuertos comerciales que ponen a prueba a los mejores pilotos del mundo.",
    "content": CONTENT,
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Juancho_E_Yrausquin_Airport.JPG",
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
