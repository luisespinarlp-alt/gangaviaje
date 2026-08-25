"""
Cuarto post de "Viajes Insolitos": Oymyakon, el lugar habitado mas frio de
la Tierra. Script de un solo uso.
Datos verificados via WebSearch (Guinness World Records, WMO, Wikivoyage,
Scientific American) el 2026-08-25 -- ver fuentes al pie del post.
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

CONTENT = f"""<p>Hay destinos fríos, y luego está Oymyakon: un pueblo de Siberia donde los coches se dejan el motor encendido las 24 horas del día porque si lo apagas, no vuelve a arrancar. Es, con toda probabilidad, el lugar habitado más frío del planeta — y sí, se puede visitar.</p>

<h2>¿Dónde está exactamente?</h2>
<p>Oymyakon está en la <strong>República de Sajá (Yakutia)</strong>, en el extremo noreste de Rusia, en un valle rodeado de montañas unos cientos de kilómetros al sur del Círculo Polar Ártico. El nombre viene del evenki y significa algo así como "el lugar que no se congela" — irónico, porque cerca del pueblo hay un manantial de aguas termales que nunca llega a helarse del todo, aunque todo lo demás sí.</p>

{vi("Oymyakon en cifras", [
    "<strong>Población:</strong> unos 500 habitantes.",
    "<strong>Temperatura media en enero:</strong> alrededor de -50°C.",
    "<strong>Récord de frío oficial (Guinness):</strong> -67,7°C, registrado en 1933 — algunas fuentes históricas hablan de -71,2°C en 1924, sin confirmación oficial equivalente.",
    "<strong>Distancia a Yakutsk</strong> (la capital regional, con aeropuerto): unos dos días de viaje por carretera.",
    "<strong>Alojamiento:</strong> no hay hotel — quien visita se aloja en casa de una familia local.",
])}

<h2>La rivalidad por el "Polo del Frío"</h2>
<p>Oymyakon no está solo en esta carrera: a unos cientos de kilómetros está Verjoyansk, un pueblo algo más grande (unos 1.200 habitantes) que se disputa con él el título no oficial de "Polo del Frío" del hemisferio norte. Ambos han registrado temperaturas históricas casi idénticas, y la rivalidad es motivo de orgullo local en los dos sitios. Lo curioso es que Verjoyansk tiene también el récord contrario: en junio de 2020 alcanzó <strong>38°C</strong>, la temperatura más alta jamás registrada al norte del Círculo Polar Ártico, confirmada oficialmente por la Organización Meteorológica Mundial en 2021. El mismo punto del planeta capaz de bajar de -67°C en invierno ha llegado a superar los 38°C en verano — pocos lugares en la Tierra tienen una oscilación térmica tan extrema.</p>

<h2>Cómo es vivir con -50°C de media</h2>
<p>Los detalles cotidianos son los que de verdad dan la medida de lo extremo del sitio. Los coches se dejan con el motor encendido de forma permanente, día y noche, porque el aceite y el líquido refrigerante se congelan en cuestión de minutos si el motor se apaga con este frío — parar el coche puede significar no poder volver a arrancarlo. Los móviles se apagan solos en pocos minutos a la intemperie, y la tinta de los bolígrafos se congela dentro del propio bolígrafo. El colegio del pueblo solo cierra por frío cuando el termómetro baja de -55°C — hasta ese punto, las clases siguen su curso normal.</p>
<p>La comida llega en camión por carreteras heladas, y la dieta tradicional se apoya mucho en carne y pescado (incluida carne de caballo, típica de la cocina yakuta) porque durante el invierno prácticamente no crece nada. Salir a la calle exige varias capas de piel de verdad — la ropa técnica moderna no siempre basta a estas temperaturas.</p>

<h2>¿Se puede visitar de verdad?</h2>
<p>Sí, y cada vez recibe más visitantes curiosos por el propio extremo. Se llega volando hasta Yakutsk, que tiene un aeropuerto con conexiones regulares, y desde ahí son unos dos días de carretera hasta Oymyakon — buena parte del trayecto por la conocida como "Carretera de los Huesos" (Kolymá), construida en la época soviética por prisioneros de los campos de trabajo, un tramo de la historia rusa tan duro como el propio clima de la zona. Como no hay hotel, quien visita se aloja con una familia local, lo que convierte el viaje en una experiencia bastante más cercana de lo habitual. La mejor época para ir depende de qué se busque: pleno invierno (diciembre-febrero) para vivir el frío extremo de verdad, o el breve verano de junio-julio, cuando el paisaje se vuelve verde y las temperaturas pueden rondar los 30°C — el mismo lugar, dos experiencias radicalmente distintas.</p>

<p style="font-size:0.85rem;color:#888;">Fuentes: <a href="https://www.guinnessworldrecords.com/world-records/lowest-temperature-inhabited" target="_blank" rel="noopener">Guinness World Records — temperatura más baja en lugar habitado</a>, <a href="https://wmo.int/media/news/wmo-recognizes-new-arctic-temperature-record-of-380c" target="_blank" rel="noopener">Organización Meteorológica Mundial — récord de calor ártico en Verjoyansk</a>, <a href="https://en.wikivoyage.org/wiki/Oymyakon" target="_blank" rel="noopener">Wikivoyage</a>. Foto: Ilya Varlamov (CC BY-SA 4.0), calle principal de Oymyakon en invierno.</p>
"""

post = {
    "slug": "oymyakon-lugar-habitado-mas-frio-del-mundo",
    "title": "Oymyakon: cómo es vivir en el lugar habitado más frío del planeta",
    "excerpt": "Coches que nunca se apagan, móviles que mueren en minutos y una media de -50°C en enero: así es la vida en el pueblo siberiano que se disputa el título de lugar más frío de la Tierra.",
    "content": CONTENT,
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Oymyakon_-_190228_DSC_5642.jpg",
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
