"""
Script de un solo uso: añade un quinto lote de artículos del blog de GangaViaje,
alineado con el nuevo destino de vuelos (Venecia) y la ampliación de Klook (Milán, Bruselas).
Ejecutar con: python3 -m scripts.add_blog_posts_5
"""

import database

POSTS = [
    {
        "slug": "venecia-que-ver-canales-y-gondolas",
        "title": "Venecia: qué ver más allá de los canales y las góndolas",
        "category": "europa",
        "image_url": "https://images.unsplash.com/photo-1534113414509-0eec2bfb493f?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Plaza de San Marcos, Puente de los Suspiros y los barrios menos turísticos: cómo aprovechar uno o dos días en Venecia sin caer en las trampas para turistas.",
        "content": """
<p>Venecia es de esas ciudades que hay que ver al menos una vez, aunque solo sea por lo distinta que es a cualquier otra capital europea: sin coches, construida sobre el agua y con un laberinto de canales que invita a perderse.</p>

<h2>Plaza de San Marcos y alrededores</h2>
<p>Es el punto de partida obligado: la Basílica de San Marcos, el Palacio Ducal y el Campanile, con vistas a toda la ciudad desde arriba. Justo al lado, el Puente de los Suspiros conecta el palacio con las antiguas prisiones — uno de los rincones más fotografiados de la ciudad.</p>

<h2>Una góndola, sí, pero con cabeza</h2>
<p>El paseo en góndola es caro (suele rondar los 80€ por 30 minutos, precio fijo regulado) pero sigue siendo una experiencia única. Para abaratarlo, compártelo entre varias personas o prueba el "traghetto", una góndola compartida que cruza el Gran Canal por unos pocos céntimos — la versión local, sin el paseo turístico pero igual de auténtica.</p>

<h2>Los barrios menos turísticos</h2>
<p>Aléjate de San Marcos y explora Cannaregio o Dorsoduro: canales mucho más tranquilos, sin las multitudes del centro, y con alguna de las mejores opciones para comer "cicchetti" (la versión veneciana del tapeo) a precios razonables.</p>

<h2>Excursión a las islas</h2>
<p>Si tienes un día más, Murano (famosa por el vidrio soplado) y Burano (con sus casas de colores) son una escapada fácil en vaporetto desde el centro de Venecia.</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>El vaporetto (barco-bus) es el transporte público de la ciudad; un pase de uno o varios días sale más a cuenta que billetes sueltos.</li>
  <li>Venecia aplica una tasa de acceso a visitantes de día en fechas de alta afluencia — conviene comprobarlo antes de planificar la visita.</li>
  <li>Reserva la Basílica de San Marcos con antelación: la cola sin reserva puede superar la hora en temporada alta.</li>
</ul>
""",
    },
]


def main():
    inserted = 0
    for post in POSTS:
        post_id = database.add_post(post)
        if post_id:
            print(f"Insertado: {post['slug']} (id={post_id})")
            inserted += 1
        else:
            print(f"Ya existía: {post['slug']}")
    print(f"\nTotal insertados: {inserted}/{len(POSTS)}")


if __name__ == "__main__":
    main()
