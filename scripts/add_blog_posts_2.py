"""
Script de un solo uso: añade un nuevo lote de artículos del blog de GangaViaje.
Ejecutar con: python3 -m scripts.add_blog_posts_2
"""

import database

POSTS = [
    {
        "slug": "paris-tres-dias-itinerario",
        "title": "París en 3 días: itinerario para ver lo esencial sin agobios",
        "category": "europa",
        "image_url": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Torre Eiffel, Louvre, Montmartre y Notre-Dame en tres días, repartidos por zonas para no perder horas de un lado a otro.",
        "content": """
<p>París tiene tantos imprescindibles que es fácil acabar agotado intentando verlo todo. La clave está en agrupar las visitas por zonas y no saltar de un extremo de la ciudad a otro.</p>

<h2>Día 1: Torre Eiffel y Champs-Élysées</h2>
<p>Empieza temprano en la Torre Eiffel (reserva entrada online con antelación, las colas sin reserva pueden superar las dos horas). Desde ahí, camina hasta el Trocadéro para la mejor foto, y sigue por el Sena hasta los Champs-Élysées y el Arco del Triunfo. Termina el día en el Barrio Latino, con buena oferta de restaurantes a precios razonables.</p>

<h2>Día 2: Louvre y la Île de la Cité</h2>
<p>Dedica la mañana al Museo del Louvre (compra la entrada online para evitar la cola de la pirámide de cristal). Por la tarde, cruza a la Île de la Cité para ver Notre-Dame por fuera (sigue en restauración) y la Sainte-Chapelle, con sus impresionantes vidrieras. Cierra el día paseando por el Marais, con sus tiendas y ambiente bohemio.</p>

<h2>Día 3: Montmartre y Sacré-Cœur</h2>
<p>La mañana del último día es para Montmartre: sube hasta la Basílica del Sacré-Cœur (las vistas de París desde ahí son de las mejores de la ciudad), pierde el tiempo por sus callejuelas y la Place du Tertre, llena de pintores. Si te queda tiempo antes del vuelo, el Museo d'Orsay es una alternativa más tranquila al Louvre, especialmente si te gusta el impresionismo.</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>El metro de París es la forma más rápida de moverse; un pase de varios días sale más a cuenta que billetes sueltos si vas a hacer muchos trayectos.</li>
  <li>Reserva con antelación las entradas a Torre Eiffel y Louvre: en temporada alta se agotan días antes.</li>
  <li>Los vuelos a París desde España suelen ser de los más baratos de Europa por la cantidad de frecuencias diarias — vale la pena comparar fechas con un par de días de margen.</li>
</ul>
""",
    },
    {
        "slug": "dubai-que-ver-cuanto-cuesta",
        "title": "Dubái: qué ver y cuánto cuesta un viaje de 4 días",
        "category": "internacional",
        "image_url": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Burj Khalifa, desierto, playas y centros comerciales imposibles: lo que de verdad cuesta un viaje de cuatro días a Dubái y cómo organizarlo.",
        "content": """
<p>Dubái suena a destino caro, y en parte lo es, pero con buena planificación se puede disfrutar sin que el presupuesto se dispare. Esto es lo que de verdad cuesta y cómo aprovechar cuatro días.</p>

<h2>Qué ver imprescindible</h2>
<ul>
  <li><strong>Burj Khalifa:</strong> el rascacielos más alto del mundo. La entrada al mirador del piso 124 ronda los 40-45€ si la compras online con antelación (en taquilla es más cara).</li>
  <li><strong>Dubai Mall y la fuente:</strong> justo al lado del Burj Khalifa, con el espectáculo gratuito de la fuente danzante varias veces al día.</li>
  <li><strong>Desierto en 4x4 y cena bajo las estrellas:</strong> un safari por las dunas con cena beduina es una de las experiencias más recomendadas, normalmente entre 40-70€ por persona.</li>
  <li><strong>Dubai Marina y JBR Beach:</strong> la zona moderna de rascacielos junto al mar, perfecta para pasear al atardecer.</li>
  <li><strong>Barrio histórico de Al Fahidi y el zoco de las especias:</strong> el lado más tradicional de la ciudad, gratis de visitar y muy fotogénico.</li>
</ul>

<h2>Presupuesto orientativo (4 días, 1 persona)</h2>
<ul>
  <li><strong>Vuelo:</strong> desde 350-500€ ida y vuelta desde España, según temporada.</li>
  <li><strong>Alojamiento:</strong> hoteles de 3-4 estrellas bien situados desde 50-90€/noche.</li>
  <li><strong>Comida:</strong> se puede comer bien por 15-25€/día combinando restaurantes locales y alguna cena más especial.</li>
  <li><strong>Actividades:</strong> cuenta entre 100-150€ en total si haces Burj Khalifa, safari al desierto y algún museo.</li>
</ul>

<h2>Cuándo viajar</h2>
<p>De noviembre a marzo el clima es mucho más agradable (20-30°C). En verano las temperaturas superan fácilmente los 40°C, lo que limita bastante las actividades al aire libre.</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>El metro de Dubái es moderno, barato y cubre la mayoría de zonas turísticas.</li>
  <li>Fuera de los hoteles, el alcohol solo se vende en zonas autorizadas; ten en cuenta las normas culturales del país, especialmente en lugares públicos.</li>
  <li>Compara bien las fechas de vuelo: los precios varían mucho entre temporada alta (diciembre-febrero) y el resto del año.</li>
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
