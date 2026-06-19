"""
Script de un solo uso: añade un tercer lote de artículos del blog de GangaViaje.
Ejecutar con: python3 -m scripts.add_blog_posts_3
"""

import database

POSTS = [
    {
        "slug": "barcelona-en-un-dia",
        "title": "Barcelona en un día: lo imprescindible si vas de paso",
        "category": "ciudad",
        "image_url": "https://images.unsplash.com/photo-1583422409516-2895a77efded?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Sagrada Família, Gótico y Barceloneta en una sola jornada: el itinerario que más aprovecha el tiempo si solo tienes un día en la ciudad.",
        "content": """
<p>Si tienes una sola jornada en Barcelona, lo mejor es no intentar verlo todo y centrarte en tres zonas que se pueden encadenar bien por la mañana, mediodía y tarde.</p>

<h2>Mañana: Sagrada Família</h2>
<p>Empieza temprano en la Sagrada Família: reserva la entrada online con antelación, las colas sin reserva previa pueden superar la hora en temporada alta. Dedica al menos 90 minutos a recorrerla con calma, es la obra más reconocible de Gaudí y vale la pena no tener prisa.</p>

<h2>Mediodía: Gótico y Las Ramblas</h2>
<p>Desde la Sagrada Família, baja hacia el Barrio Gótico. Pierde el tiempo por sus callejuelas estrechas, visita la Catedral de Barcelona y acércate al Mercado de la Boqueria para comer algo rápido y bueno. Las Ramblas conectan esta zona con el puerto, aunque conviene evitar comer justo en la calle principal por precios inflados.</p>

<h2>Tarde: Barceloneta y la playa</h2>
<p>Termina el día en la Barceloneta: paseo junto al mar, una cerveza con vistas y, si el tiempo acompaña, un rato de playa antes de la cena. Es la forma perfecta de cerrar una visita exprés sin sensación de haber ido corriendo todo el día.</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>El metro conecta bien las tres zonas; calcula entre 10 y 20 minutos de trayecto entre cada una.</li>
  <li>Reserva con antelación la Sagrada Família: es el punto que más cola acumula sin reserva previa.</li>
  <li>Si tienes algo más de tiempo, el Park Güell merece una tarde aparte — no entra bien en un itinerario de un solo día junto con el resto.</li>
</ul>
""",
    },
    {
        "slug": "escapadas-rurales-espana-desconectar",
        "title": "5 escapadas rurales en España para desconectar de verdad",
        "category": "rural",
        "image_url": "https://images.unsplash.com/photo-1500076656116-558758c991c1?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Pueblos con encanto, naturaleza y casi sin cobertura: cinco destinos rurales en España perfectos para un fin de semana sin pantallas.",
        "content": """
<p>No todo viaje tiene que implicar un avión y una lista interminable de monumentos. A veces lo que más descansa es un pueblo pequeño, naturaleza alrededor y poco más que hacer que pasear y comer bien.</p>

<h2>Ainsa (Huesca)</h2>
<p>Un casco histórico medieval prácticamente intacto, rodeado por los Pirineos. Punto de partida perfecto para rutas de senderismo por el Parque Nacional de Ordesa y Monte Perdido, a menos de una hora en coche.</p>

<h2>Cudillero (Asturias)</h2>
<p>Pueblo pesquero construido en anfiteatro sobre un acantilado, con casas de colores que caen casi hasta el mar. Buena base para explorar la costa asturiana y comer marisco fresco sin pagar precios de ciudad grande.</p>

<h2>Trujillo (Cáceres)</h2>
<p>Una plaza mayor monumental, un castillo árabe con vistas a la dehesa extremeña y muy poco turismo masificado. Ideal para combinar con una ruta por los pueblos cercanos de la comarca.</p>

<h2>Frigiliana (Málaga)</h2>
<p>Considerado uno de los pueblos blancos más bonitos de Andalucía, con calles empedradas en cuesta y vistas al Mediterráneo. A 15 minutos de Nerja, por si quieres combinar pueblo y playa el mismo día.</p>

<h2>Albarracín (Teruel)</h2>
<p>Casas rojizas colgadas sobre un meandro del río Guadalaviar, declarado conjunto histórico-artístico. De los destinos rurales con menos masificación de toda España, incluso en verano.</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>La mayoría de estos pueblos se disfrutan mejor en coche; alquilar uno desde el aeropuerto más cercano suele salir más barato que combinar transporte público.</li>
  <li>Reserva alojamiento con antelación en fin de semana: la oferta hotelera en pueblos pequeños es limitada y se agota rápido.</li>
  <li>Llévate efectivo: en los establecimientos más pequeños de zonas rurales no siempre se acepta tarjeta.</li>
</ul>
""",
    },
    {
        "slug": "berlin-dos-dias-que-ver",
        "title": "Berlín en 2 días: qué ver si tienes poco tiempo",
        "category": "europa",
        "image_url": "https://images.unsplash.com/photo-1560969184-10fe8719e047?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Puerta de Brandeburgo, Muro de Berlín y la isla de los museos: lo esencial de la capital alemana en 48 horas bien aprovechadas.",
        "content": """
<p>Berlín es una ciudad enorme y con mucha historia, pero en dos días bien organizados se puede ver lo esencial sin sensación de haber ido corriendo.</p>

<h2>Día 1: el centro histórico y político</h2>
<p>Empieza en la Puerta de Brandeburgo, símbolo de la ciudad, y camina hasta el Reichstag (la cúpula de cristal tiene vistas espectaculares, pero hay que reservar entrada gratuita con antelación). Sigue hacia el Memorial del Holocausto, a pocos minutos andando, y termina la mañana en Potsdamer Platz. Por la tarde, visita el East Side Gallery, el tramo más largo que queda en pie del Muro de Berlín, convertido en galería de arte urbano al aire libre.</p>

<h2>Día 2: Isla de los Museos y Kreuzberg</h2>
<p>Dedica la mañana a la Museumsinsel (Isla de los Museos), declarada Patrimonio de la Humanidad, con el Museo de Pérgamo como gran imprescindible si te gusta la arqueología. Por la tarde, cambia de ambiente y visita Kreuzberg, el barrio más alternativo de Berlín, con mucho arte urbano, mercados y la mejor oferta de comida callejera de la ciudad (el döner kebab berlinés es de visita obligada).</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>El transporte público (U-Bahn y S-Bahn) es excelente; un billete de día sale a cuenta si vas a hacer varios trayectos.</li>
  <li>Muchos museos cierran los lunes — comprueba los horarios antes de planificar el itinerario por días.</li>
  <li>Berlín tiene fama de ser una de las capitales europeas más baratas para comer y salir de noche, comparada con Londres o París.</li>
</ul>
""",
    },
    {
        "slug": "bangkok-primera-vez-guia-rapida",
        "title": "Bangkok: primera vez en Tailandia, guía rápida",
        "category": "internacional",
        "image_url": "https://images.unsplash.com/photo-1508009603885-50cf7c579365?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Templos, mercados flotantes y comida de calle por menos de 2€: lo que hay que saber antes de tu primer viaje a Bangkok.",
        "content": """
<p>Bangkok suele ser la puerta de entrada a Tailandia, y aunque al principio puede abrumar por el calor, el tráfico y el ritmo, es una de las ciudades con mejor relación calidad-precio de Asia para un primer viaje.</p>

<h2>Qué ver imprescindible</h2>
<ul>
  <li><strong>Gran Palacio y Wat Phra Kaew:</strong> el templo del Buda de Esmeralda, el conjunto más visitado de la ciudad. Cuidado con el código de vestimenta: hombros y rodillas cubiertos.</li>
  <li><strong>Wat Arun (Templo del Amanecer):</strong> al otro lado del río Chao Phraya, especialmente bonito al atardecer.</li>
  <li><strong>Mercado flotante de Damnoen Saduak:</strong> a una hora de la ciudad, vendedores en barca entre canales llenos de fruta y comida.</li>
  <li><strong>Chinatown (Yaowarat):</strong> de noche se llena de puestos de comida callejera, de los mejores de toda la ciudad.</li>
  <li><strong>Mercado de Chatuchak:</strong> uno de los mercados al aire libre más grandes del mundo, abierto solo fines de semana.</li>
</ul>

<h2>Presupuesto orientativo (por día, 1 persona)</h2>
<ul>
  <li><strong>Alojamiento:</strong> hoteles de buena calidad desde 20-35€/noche.</li>
  <li><strong>Comida:</strong> un plato de comida callejera cuesta 1-2€; un restaurante para turistas, 6-10€.</li>
  <li><strong>Transporte:</strong> el BTS (metro elevado) y los tuk-tuk son baratos; un trayecto en metro ronda los 0,50-1€.</li>
</ul>

<h2>Cuándo viajar</h2>
<p>De noviembre a febrero es la temporada más agradable (menos calor, menos humedad y casi sin lluvias). De marzo a mayo el calor es extremo, y de junio a octubre es temporada de monzón con lluvias frecuentes, aunque suelen ser cortas e intensas.</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>Negocia el precio de los tuk-tuk antes de subir, no llevan taxímetro.</li>
  <li>Lleva siempre agua y protector solar; la humedad y el calor se notan más de lo esperado.</li>
  <li>El visado para estancias cortas no suele ser necesario para ciudadanos españoles, pero comprueba siempre la normativa vigente antes de viajar.</li>
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
