"""
Nueva guia de destino: China (Pekin, la Gran Muralla, Xi'an y Shanghai).
Datos practicos (visado, trenes, precios) verificados via WebSearch el
2026-08-24 -- fuentes citadas en el propio texto donde aplica un dato concreto.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database

CONTENT = """<p>China es probablemente el gran destino pendiente de la mayoría de viajeros españoles: un país inmenso, con miles de años de historia, contrastes brutales entre tradición y modernidad, y una barrera de idioma e infraestructura digital que asusta más de lo que debería. La buena noticia es que desde finales de 2024 es más fácil de visitar que nunca — sin visado y con una red de trenes de alta velocidad que conecta sus grandes ciudades en horas, no en días.</p>

<h2>Pekín: la capital imperial</h2>
<p>La Ciudad Prohibida es la visita obligada: el complejo palaciego más grande y mejor conservado del mundo, con 980 edificios y casi 9.000 habitaciones, residencia de los emperadores chinos durante casi 500 años. Necesitarás medio día completo para recorrerla sin prisa. Justo al lado está la plaza de Tiananmen, la plaza pública más grande del mundo, y el Templo del Cielo, donde los emperadores hacían sus rituales anuales por la buena cosecha — sus jardines son de los rincones más tranquilos de toda la ciudad.</p>
<p>El Palacio de Verano, algo más alejado del centro, es otra visita imprescindible: un enorme parque imperial con lago artificial, pabellones y el curioso "barco de mármol" — merece una tarde completa y es donde mejor se entiende la escala del poder imperial chino.</p>

<h2>La Gran Muralla: Mutianyu, no Badaling</h2>
<p>Hay varios tramos de la Gran Muralla visitables como excursión de un día desde Pekín, y la elección del tramo cambia por completo la experiencia. <strong>Badaling</strong> es el más cercano y accesible en transporte público, pero también el más masificado — recibe más de 10 millones de visitantes al año. <strong>Mutianyu</strong>, a un poco más de distancia (hay que ir en autobús organizado o taxi privado), tiene entre un 60-70% menos de visitantes, está igual de bien restaurada, y el paisaje de bosque que la rodea es más espectacular. Para la primera visita de la mayoría de viajeros, Mutianyu es la mejor opción sin discusión.</p>

<h2>Xi'an: los guerreros de terracota</h2>
<p>A poco más de una hora en tren bala desde Pekín, Xi'an merece una parada de 1-2 días solo por el Ejército de Terracota: más de 8.000 guerreros de tamaño real, cada uno con rasgos faciales distintos, enterrados junto al primer emperador de China hace más de 2.200 años y descubiertos por accidente en 1974 por unos agricultores cavando un pozo. La entrada (un único billete de 120 yuanes, unos 15€, que cubre los tres fosos excavados) requiere pasaporte para comprarla, y conviene reservar con antelación en temporada alta. Calcula 5-6 horas para la visita completa más el trayecto desde el centro de Xi'an.</p>
<p>Xi'an en sí misma es una de las ciudades con más historia de China — fue el punto de partida de la Ruta de la Seda — y conserva la muralla de la ciudad antigua mejor preservada del país, que se puede recorrer entera en bicicleta.</p>

<h2>Shanghái: el contraste absoluto</h2>
<p>Si Pekín es la China imperial, Shanghái es la China del futuro. El Bund, el paseo marítimo junto al río Huangpu, ofrece una de las postales más impresionantes de Asia: edificios coloniales europeos de principios del siglo XX de un lado, y el skyline futurista de rascacielos de Pudong (con la Torre de Shanghái, el tercer edificio más alto del mundo) al otro lado del río. De noche, con todo iluminado, es aún más espectacular.</p>
<p>El Jardín Yuyuan, un jardín clásico chino del siglo XVI en pleno centro histórico, y el barrio de la Concesión Francesa, con sus calles arboladas y arquitectura europea reconvertida en cafés y tiendas de diseño, completan las visitas imprescindibles. Shanghái tiene además la mejor escena gastronómica moderna del país si quieres un descanso de la comida más tradicional.</p>

<h2>Cómo moverte: los trenes de alta velocidad</h2>
<p>La red de alta velocidad china es, sin exagerar, la mejor del mundo — más extensa que la de cualquier otro país. La línea Pekín-Shanghái (1.318 km) se cubre en unas 4 horas y media en los trenes G, que alcanzan 350 km/h, con billetes desde unos 65€. Pekín-Xi'an son poco más de 4 horas también. Viajar en tren en China es cómodo, puntual casi de forma obsesiva y mucho más agradable que volar entre ciudades — resérvalo con antelación en temporada alta a través de apps como Trip.com, que venden en español y aceptan tarjetas extranjeras.</p>

<h2>Antes de ir: visado, pagos y conexión</h2>
<p><strong>Visado:</strong> desde el 30 de noviembre de 2024 (y al menos hasta finales de 2026), los ciudadanos españoles con pasaporte ordinario no necesitan visado para estancias turísticas de hasta 30 días — solo pasaporte válido. Es un cambio reciente y notable: hasta hace poco, China era de los destinos asiáticos con más trámites previos.</p>
<p><strong>Pagos:</strong> China funciona casi sin efectivo, todo se paga con Alipay o WeChat Pay desde el móvil — incluido un puesto callejero de fideos. Ambas apps permiten vincular una tarjeta Visa o Mastercard extranjera directamente, sin necesidad de cuenta bancaria china, verificando la identidad con el pasaporte desde la propia app. Configúralo antes de salir de casa con wifi, no al llegar al aeropuerto.</p>
<p><strong>Internet:</strong> Google, Gmail, WhatsApp, Instagram y Facebook están bloqueados por el "Gran Cortafuegos" chino. Si necesitas usarlos, instala una VPN <strong>antes de viajar</strong> — las tiendas de aplicaciones de VPN también están bloqueadas una vez dentro del país. Para todo lo demás, WeChat es la app que sustituye a WhatsApp y funciona sin restricciones.</p>

<h2>Cuándo ir y presupuesto</h2>
<p>La mejor época es <strong>primavera (abril-mayo)</strong> u <strong>otoño (septiembre-octubre)</strong> — temperaturas suaves en todo el país y menos lluvia que en verano. Evita la Semana Dorada china (primera semana de octubre) y el Año Nuevo Chino: todo el país viaja a la vez y los precios y las colas se disparan. Para un viaje de gama media (hoteles cómodos, taxis cuando haga falta, comer bien), calcula entre 65-120€/día por persona; mochileros con más margen de incomodidad pueden bajar a 35-55€/día.</p>

<h2>Antes de viajar: eSIM y seguro</h2>
<p>Para este destino, una <strong><a href="/blog/mejor-esim-para-viajar-europa-mundo">eSIM de viaje</a></strong> es prácticamente imprescindible — activa los datos desde el aterrizaje sin depender del wifi del hotel, aunque ten en cuenta que la eSIM no te libra del cortafuegos chino — las apps bloqueadas lo siguen estando, tengas la conexión que tengas.</p>
<p>Un <strong>seguro de viaje</strong> con buena cobertura médica es muy recomendable para un destino tan grande y con tanta distancia entre ciudades. Y si tu vuelo sufre un retraso de más de 3 horas o lo cancelan, tienes derecho a compensación — <a href="/blog/que-hacer-si-tu-vuelo-se-retrasa-o-cancela">aquí te contamos cómo reclamar hasta 600€</a>.</p>
"""

post = {
    "slug": "china-pekin-shanghai-gran-muralla-guia-completa",
    "title": "China: Pekín, la Gran Muralla, Xi'an y Shanghái — guía completa 2026",
    "excerpt": "Sin visado desde 2024, con la mejor red de trenes de alta velocidad del mundo: la guía completa para tu primer viaje a China — qué ver, cuándo ir y cuánto cuesta.",
    "content": CONTENT,
    "image_url": "https://images.unsplash.com/photo-1608037521277-154cd1b89191?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "category": "internacional",
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
