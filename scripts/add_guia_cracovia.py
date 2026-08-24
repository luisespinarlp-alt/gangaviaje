"""
Nueva guia de destino: Cracovia, Polonia.
Datos practicos verificados via WebSearch el 2026-08-24.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database

CONTENT = """<p>Cracovia es de esas ciudades que sorprenden a quien la visita por primera vez esperando "otra ciudad barata del Este" y se encuentra con una de las plazas medievales más bonitas de Europa, un castillo real a la altura de cualquier capital y una de las visitas históricas más importantes y sobrecogedoras que se pueden hacer en el continente. Fue la capital de Polonia durante siglos y se libró de la destrucción masiva que sufrieron Varsovia y otras ciudades polacas en la Segunda Guerra Mundial — por eso su casco antiguo sigue prácticamente intacto.</p>

<h2>La Plaza Mayor (Rynek Główny): el corazón de la ciudad</h2>
<p>Es la plaza medieval más grande de Europa, y se nota en cuanto se llega: el Sukiennice (Lonja de los Paños), un mercado renacentista del siglo XIV convertido hoy en puestos de artesanía y un museo de arte polaco en la planta superior, ocupa el centro. Cada hora en punto, un trompetista toca el <em>Hejnał</em> desde lo alto de la Basílica de Santa María, la melodía se corta abruptamente a mitad — según la leyenda, en honor a un vigía medieval al que una flecha tártara le atravesó la garganta justo cuando avisaba de un ataque. El interior de la basílica, con el retablo gótico de madera tallada más grande de Europa, merece la entrada aparte.</p>

<h2>El Castillo de Wawel: la Alcázar polaca</h2>
<p>En la colina de Wawel, a orillas del río Vístula, se levanta el conjunto de castillo y catedral que fue la residencia de los reyes polacos durante siglos y sigue siendo el símbolo nacional del país. La Catedral de Wawel, con sus torres de tejados verdes, guarda las tumbas de la mayoría de reyes y héroes nacionales polacos. Según la leyenda local, en la colina vivía un dragón al que hoy recuerda una estatua junto al río que, cada pocos minutos, escupe fuego de verdad — un detalle que le encanta a quien viaja con niños.</p>

<h2>Kazimierz: el antiguo barrio judío, hoy el más de moda</h2>
<p>Kazimierz fue el barrio judío de Cracovia durante 500 años, con una comunidad próspera hasta el Holocausto. Hoy es el barrio más interesante de la ciudad para pasear sin rumbo: sinagogas centenarias conviviendo con bares alternativos, mercados vintage y la mejor escena gastronómica de Cracovia. La Plaza Nowy, con su antiguo mercado circular de aves reconvertido en puestos de zapytaj (el pan plano judío-polaco relleno), es el punto de encuentro. Si viste "La lista de Schindler", varias localizaciones reales de la película están en este barrio y en la vecina fábrica de Oskar Schindler, hoy museo.</p>

<h2>Auschwitz-Birkenau: la visita que hay que hacer bien</h2>
<p>A poco más de una hora de Cracovia está Oświęcim, donde los nazis construyeron el mayor campo de concentración y exterminio de la Segunda Guerra Mundial. Es, con diferencia, la visita más dura y también una de las más importantes que se pueden hacer en Europa — se recorren tanto Auschwitz I (el campo original) como Birkenau (Auschwitz II, mucho más grande, donde ocurrió la mayoría de los asesinatos). <strong>La entrada es obligatoriamente con reserva previa</strong> en la web oficial (visit.auschwitz.org), con una tarjeta de entrada personalizada que hay que llevar junto al pasaporte o DNI. La disponibilidad en español varía según temporada, así que resérvala con antelación, sobre todo si viajas en Semana Santa, puentes o Navidad — son las fechas de mayor demanda del año.</p>

<h2>La mina de sal de Wieliczka: el otro Patrimonio de la Humanidad cerca de Cracovia</h2>
<p>A poco más de 15 km del centro, la mina de sal de Wieliczka lleva en explotación desde el siglo XIII y fue una de las primeras doce localizaciones declaradas Patrimonio de la Humanidad por la UNESCO, en 1978. Se desciende hasta 327 metros por una red de más de 300 km de galerías, con lagos subterráneos y salas enteras esculpidas en sal por los propios mineros — la más espectacular es la Capilla de Santa Kinga, con lámparas de araña hechas también de sal cristalizada. La visita estándar dura 2-3 horas e incluye el museo de las salinas. Auschwitz y Wieliczka se pueden combinar en un tour de un día completo, aunque el contraste emocional entre ambas visitas es fuerte — mucha gente prefiere hacerlas en días separados.</p>

<h2>Cuándo ir y presupuesto</h2>
<p>La mejor época es de <strong>mayo a septiembre</strong>, con el punto álgido en julio-agosto (más calor y más turistas) — abril, mayo y septiembre ofrecen buen clima con menos aglomeración. En diciembre, el mercado navideño de la Plaza Mayor es de los más bonitos de Europa del Este, si no te importa el frío. Cracovia es notablemente barata para estándares de Europa occidental: el alojamiento sale en torno a un 20% más barato que en España, aunque comer en restaurantes puede ser algo más caro de lo esperado — el conjunto sigue compensando frente a casi cualquier ciudad de Europa occidental comparable en patrimonio.</p>

<h2>Antes de viajar: eSIM y seguro</h2>
<p>Polonia es miembro de la UE, así que el roaming de tu operador español funciona sin coste — no necesitas eSIM salvo que prefieras no depender de tu línea principal. Sí es recomendable un <strong>seguro de viaje</strong> con buena cobertura, sobre todo si vas a moverte en coche o autobús entre Cracovia y las excursiones cercanas. Y recuerda que si tu vuelo se retrasa más de 3 horas o lo cancelan, tienes derecho a compensación — <a href="/blog/que-hacer-si-tu-vuelo-se-retrasa-o-cancela">aquí te explicamos cómo reclamar hasta 600€</a>.</p>
"""

post = {
    "slug": "cracovia-polonia-guia-completa",
    "title": "Cracovia: Plaza Mayor, Wawel, Auschwitz y la mina de sal — guía completa 2026",
    "excerpt": "La escapada europea barata con más patrimonio por metro cuadrado: casco antiguo intacto, castillo real, el barrio judío de Kazimierz y dos visitas Patrimonio de la Humanidad a las puertas de la ciudad.",
    "content": CONTENT,
    "image_url": "https://images.unsplash.com/photo-1686252289176-6c4d15b7bc88?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "category": "europa",
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
