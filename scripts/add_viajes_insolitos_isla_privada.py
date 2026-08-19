"""
Añade el segundo post de "Viajes Insólitos": alquilar una isla privada entera.
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

CONTENT = f"""<p>Cuando se piensa en alquilar una isla entera, la imagen mental suele ser la de un multimillonario en las Bahamas — y hay ejemplos que confirman exactamente eso. Pero el rango real de precios es mucho más amplio de lo que parece, y en el extremo barato hay opciones que sorprenden.</p>

<h2>El extremo del lujo: Musha Cay, Bahamas</h2>
<p>Es probablemente la isla privada más famosa del mundo — propiedad del ilusionista David Copperfield. Se alquila entera desde <strong>57.000 dólares por noche</strong> (unos 53.000€), con una estancia mínima de 5 noches, para hasta 24 invitados repartidos en varias villas. Solo la estancia mínima ya son más de 265.000€. Aun así, tiene lista de espera — se reserva con meses de antelación.</p>

{vi("Otros ejemplos reales del extremo caro", [
    "<strong>Nygard Cay (Bahamas)</strong> — en torno a 26.000€ al día.",
    "<strong>Kamalame Cay (Bahamas)</strong> — unos 5.500€ al día, hasta 40 invitados.",
    "<strong>Sa Ferradura (Ibiza, España)</strong> — alrededor de 20.000€ al día con todos los lujos.",
])}

<h2>El extremo asequible: no toda isla privada arruina</h2>
<p>Aquí está el dato que sorprende de verdad: <strong>Isla Bonita (Brasil)</strong> se puede alquilar entera para un grupo de hasta 10 amigos por unos <strong>6.000€ a la semana</strong> — repartido entre 10 personas, son 600€ por cabeza en un lugar donde no hay nadie más que vosotros. <strong>Cayo Espanto (Belice)</strong> ronda los 4.000€ para 5 días. No son las Bahamas, pero son islas privadas de verdad, con nombre propio, que cualquier grupo de amigos con presupuesto ajustado puede plantearse una vez en la vida.</p>

<h2>Por qué varía tanto el precio</h2>
<p>La diferencia no está solo en el lujo de las villas — pesa mucho la ubicación (Bahamas y Caribe son las zonas más caras del mundo para esto), la capacidad de invitados, si el precio incluye personal (chef, mayordomo, transporte en barco/helicóptero) y la temporada. Una isla remota en Brasil o Belice sin infraestructura de superlujo puede costar 40 veces menos que una en Bahamas con servicio completo.</p>

<p style="font-size:0.85rem;color:#888;">Fuentes: <a href="https://www.mushacay.com/reservations" target="_blank" rel="noopener">Musha Cay (web oficial)</a>, <a href="https://robbreport.com/lifestyle/news/bahamas-musha-cay-private-island-airbnb-1234822736/" target="_blank" rel="noopener">Robb Report</a>, <a href="https://mundo.expert/es/blog/cuanto-cuesta-alquilar-una-isla-privada" target="_blank" rel="noopener">mundo.expert</a>.</p>
"""

post = {
    "slug": "alquilar-isla-privada-precio-real",
    "title": "Alquilar una isla privada entera: desde 600€ por persona hasta 265.000€ la estancia mínima",
    "excerpt": "El rango real de precios para alquilar una isla privada por una semana — desde Isla Bonita en Brasil hasta Musha Cay, la isla de David Copperfield en Bahamas.",
    "content": CONTENT,
    "image_url": "https://images.unsplash.com/photo-1780734323790-6f18edf42997?fm=jpg&q=80&w=1200&auto=format&fit=crop",
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
