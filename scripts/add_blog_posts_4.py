"""
Script de un solo uso: añade un cuarto lote de artículos del blog de GangaViaje,
alineados con los nuevos destinos de vuelos (Budapest, Tokio).
Ejecutar con: python3 -m scripts.add_blog_posts_4
"""

import database

POSTS = [
    {
        "slug": "budapest-que-ver-balnearios-y-rio",
        "title": "Budapest: qué ver y por qué tiene los mejores balnearios de Europa",
        "category": "europa",
        "image_url": "https://images.unsplash.com/photo-1551867633-194f125bddfa?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Castillo de Buda, Parlamento iluminado y baños termales centenarios: por qué Budapest es de los destinos europeos con mejor relación calidad-precio.",
        "content": """
<p>Budapest es en realidad dos ciudades unidas por el Danubio: Buda, la parte histórica y elevada, y Pest, la zona llana y moderna. Esa combinación, junto a sus baños termales, la hace distinta a cualquier otra capital europea.</p>

<h2>Qué ver en Buda</h2>
<p>Sube al Castillo de Buda y al Bastión de los Pescadores para tener la mejor panorámica de la ciudad y del Parlamento al otro lado del río. La Iglesia de Matías, con su tejado de tejas de colores, está justo al lado y es de visita obligada.</p>

<h2>Qué ver en Pest</h2>
<p>El Parlamento húngaro, uno de los edificios más fotografiados de Europa, se ve mejor desde la orilla de Buda o en un crucero nocturno por el Danubio, cuando se ilumina por completo. La Basílica de San Esteban y la Plaza de los Héroes completan el recorrido por esta parte de la ciudad.</p>

<h2>Los baños termales, la experiencia imprescindible</h2>
<p>Budapest está construida sobre aguas termales naturales, y eso se traduce en balnearios centenarios como el Széchenyi (el más grande y fotogénico, con piscinas exteriores incluso en invierno) o el Gellért, de estilo art nouveau. Una tarde de baños termales cuesta menos que en casi cualquier otro spa europeo de nivel similar.</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>Lleva bañador y chanclas si vas a los balnearios; algunos alquilan toalla pero conviene confirmarlo al comprar la entrada.</li>
  <li>El transporte público es barato y eficiente; un billete de varios días sale a cuenta si vas a moverte mucho entre Buda y Pest.</li>
  <li>Budapest suele ser de los destinos europeos más económicos para comer y alojarse, comparado con capitales como Viena o París.</li>
</ul>
""",
    },
    {
        "slug": "tokio-primera-vez-que-saber",
        "title": "Tokio por primera vez: lo que hay que saber antes de ir",
        "category": "internacional",
        "image_url": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Templos centenarios junto a rascacielos de neón, metro impecable y comida de calidad a cualquier precio: una primera guía práctica para Tokio.",
        "content": """
<p>Tokio impresiona por el contraste: barrios tradicionales con templos centenarios convivven con zonas como Shibuya o Akihabara, llenas de luces de neón y tecnología. Para una primera visita conviene organizar el viaje por distritos.</p>

<h2>Distritos imprescindibles</h2>
<ul>
  <li><strong>Shibuya y Shinjuku:</strong> el cruce de Shibuya (el más concurrido del mundo) y los rascacielos iluminados de Shinjuku son la imagen más conocida de Tokio.</li>
  <li><strong>Asakusa:</strong> el templo Senso-ji, el más antiguo de la ciudad, rodeado de calles tradicionales con tiendas de artesanía.</li>
  <li><strong>Akihabara:</strong> el barrio del manga, los videojuegos y la electrónica, una experiencia muy distinta al resto de la ciudad.</li>
  <li><strong>Harajuku y Shibuya:</strong> moda alternativa y el tranquilo Santuario Meiji, justo al lado del bullicio de Takeshita Street.</li>
</ul>

<h2>Presupuesto orientativo (por día, 1 persona)</h2>
<ul>
  <li><strong>Alojamiento:</strong> hoteles cápsula desde 25€/noche; hoteles estándar desde 60-80€/noche.</li>
  <li><strong>Comida:</strong> un ramen o un menú en una cadena de sushi cuesta entre 6-10€; restaurantes de gama media, 20-30€.</li>
  <li><strong>Transporte:</strong> la JR Pass merece la pena solo si vas a salir de Tokio; dentro de la ciudad, un pase de metro de varios días sale más a cuenta.</li>
</ul>

<h2>Cuándo viajar</h2>
<p>Primavera (marzo-mayo, temporada de cerezos en flor) y otoño (octubre-noviembre) son las épocas más agradables y también las más concurridas. El verano es muy húmedo y caluroso.</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>El metro de Tokio es puntual y muy seguro, pero la red es compleja: una app de rutas como Google Maps funciona perfectamente y evita confusiones.</li>
  <li>Lleva siempre algo de efectivo: muchos restaurantes pequeños y locales tradicionales no aceptan tarjeta.</li>
  <li>El vuelo desde España suele tener al menos una escala; comparar fechas con margen de unos días puede ahorrar bastante en el billete.</li>
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
