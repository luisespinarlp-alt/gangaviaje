"""Amplia a 1200+ palabras el batch 2 de GangaConsejos (3 de los 11 restantes)."""
import psycopg2
import config
import database

APPS_NUEVO = """
<h2>Apps de fotografía y recuerdos</h2>
<p><strong>Google Photos</strong> con copia de seguridad automática — la más importante de todas: si pierdes el móvil o te lo roban, las fotos ya están en la nube. Actívala antes de salir de casa, no cuando ya estés en el aeropuerto. <strong>Polarr o Snapseed</strong> para retocar fotos directamente en el móvil sin depender del ordenador. Si viajas mucho en grupo, un álbum compartido de Google Photos donde todos suben sus fotos evita el clásico "pásame las fotos" por WhatsApp con calidad reducida.</p>

<h2>Apps para reservar experiencias y actividades</h2>
<p><strong>GetYourGuide y Civitatis</strong> — para reservar tours, entradas sin colas y excursiones con cancelación gratuita hasta 24h antes. Compara siempre precio en ambas antes de reservar, varía según la actividad. <strong>Tiqets</strong> — especializada en entradas a museos y atracciones con entrega instantánea al móvil, útil para evitar colas en sitios muy turísticos (Sagrada Familia, Coliseo, Alhambra). Reservar con antelación en temporada alta no es opcional en estos sitios — muchos se agotan con semanas de margen.</p>

<h2>Apps que solo necesitas en destinos concretos</h2>
<p>En Asia, <strong>Grab</strong> sustituye a Uber en gran parte del sudeste asiático (Tailandia, Vietnam, Filipinas, Malasia, Singapur) — descárgala antes de llegar. En China, casi ninguna app occidental funciona sin VPN: <strong>WeChat</strong> es imprescindible para pagos y comunicación. En Japón, <strong>Japan Official Travel App</strong> tiene mapas offline y traductor especializado en carteles japoneses. En Latinoamérica, <strong>Rappi</strong> cubre desde comida a domicilio hasta recados en varias ciudades grandes.</p>

<h2>Cuántas apps descargar realmente</h2>
<p>El error más común es llegar al aeropuerto con 15 apps a medio configurar. Descarga y configura solo 5-6 antes de salir: buscador de vuelos, Booking o Airbnb, Google Maps con mapa offline descargado, tu eSIM, y traductor con idioma descargado. El resto (apps locales de transporte, restaurantes) las puedes instalar ya en destino con wifi del hotel o del aeropuerto, en cuanto sepas exactamente cuáles necesitas.</p>
"""

COCHE_NUEVO = """
<h2>Edad mínima y recargo por conductor joven</h2>
<p>La mayoría de empresas exigen tener al menos 21 años y carné con 1-2 años de antigüedad; para categorías premium (SUV, descapotables) suelen pedir 23-25. Si tienes entre 21 y 25 años, es habitual un recargo de "conductor joven" de 5-15€/día que no siempre aparece en el precio inicial del comparador — se añade al llegar al mostrador. Revisa este dato en las condiciones antes de reservar si estás en ese rango de edad, para no llevarte una sorpresa.</p>

<h2>Carné de conducir internacional: ¿hace falta?</h2>
<p>Dentro de la Unión Europea, el carné español es suficiente, no hace falta nada más. Fuera de la UE (EE.UU., la mayoría de Asia, algunos países de Latinoamérica), muchas empresas piden el <strong>Permiso Internacional de Conducir</strong> además del carné nacional — se tramita en la Jefatura de Tráfico en un solo trámite, cuesta unos 10€ y tarda pocos días. No todos los países lo exigen legalmente, pero muchas empresas de alquiler sí lo piden como requisito propio, así que conviene llevarlo si el destino no es Europa.</p>

<h2>Combustible: gasolina, diésel o híbrido</h2>
<p>Si no conoces el tipo de combustible del coche que has reservado, pregúntalo al recoger las llaves — echar el combustible equivocado por error es uno de los incidentes más caros y comunes (puede dejar el motor inutilizable). En categorías económicas, España sigue teniendo mucha oferta de diésel, más barato por kilómetro en trayectos largos; para ciudad, un híbrido reduce bastante el gasto de combustible aunque el alquiler base sea algo más caro.</p>

<h2>Devolver el coche en otra ciudad</h2>
<p>Recoger en un aeropuerto y devolver en otro (por ejemplo, entrada por Madrid y salida por Málaga) es posible en la mayoría de las empresas grandes, pero suele llevar un <strong>recargo de "one-way"</strong> que puede ser de 50 a más de 200€ según la distancia y la empresa. Compara este recargo contra el coste de un vuelo o tren interno de vuelta al punto de origen — a veces sale más barato devolver el coche donde lo recogiste y moverte de otra forma para el último tramo.</p>
"""

ALOJAMIENTO_NUEVO = """
<h2>Programas de fidelización de hoteles: ¿merece la pena apuntarse?</h2>
<p>Cadenas grandes (Marriott Bonvoy, Hilton Honors, IHG One Rewards) son gratuitas de apuntarse y dan ventajas reales desde la primera noche: wifi gratis garantizado, a veces desayuno incluido, y acumulación de puntos canjeables por noches gratis. Solo compensan si vas a repetir cadena varias veces al año — si reservas un hotel distinto cada viaje, el programa no aporta nada. Para viajeros que sí repiten cadena, apuntarse no cuesta nada y solo suma.</p>

<h2>Habitaciones con vista o sin vista: dónde ahorrar sin perder calidad</h2>
<p>La diferencia de precio entre una habitación estándar y una con vista puede ser de 20-40% en el mismo hotel, con el mismo tamaño y las mismas comodidades. Si vas a pasar poco tiempo en la habitación (turismo activo, poco tiempo despierto en el hotel), la vista es de los recortes más indoloros que existen. Reserva la habitación más básica y, si el hotel tiene buena política de upgrades, pregunta en recepción al llegar — muchas veces hacen mejoras gratuitas si hay disponibilidad y llegas con buena actitud.</p>

<h2>El desayuno incluido: ¿compensa pagar más?</h2>
<p>Haz siempre la cuenta antes de asumir que el desayuno incluido es un ahorro. Si el suplemento por desayuno son 12€/persona y un desayuno decente en una cafetería cercana cuesta 5-8€, sale más barato (y a menudo más rico) desayunar fuera, salvo en destinos donde comer fuera es caro (países nórdicos, Reino Unido, Suiza) — ahí el desayuno de hotel casi siempre compensa.</p>

<h2>Alojamiento cerca de estaciones de tren vs. centro histórico</h2>
<p>En ciudades europeas con buena red ferroviaria, alojarse cerca de la estación principal (en vez del centro histórico) suele bajar el precio un 15-25% y facilita escapadas de un día a otras ciudades sin cargar el equipaje por el centro. La pega: suelen ser zonas menos bonitas para pasear de noche. Buen equilibrio para viajes con varias paradas (interrail, multi-destino); menos ideal si el objetivo es una sola ciudad y quieres estar en el ambiente del centro.</p>
"""

POSTS = [
    ("mejores-apps-para-viajar-imprescindibles-2026", "<h2>La app que no necesitas</h2>", APPS_NUEVO),
    ("alquilar-coche-barato-espana-trucos", "<h2>Mejores destinos para alquilar coche en España</h2>", COCHE_NUEVO),
    ("alojamiento-barato-europa-trucos-reservar", "<h2>Recursos</h2>", ALOJAMIENTO_NUEVO),
]

conn = psycopg2.connect(config.DATABASE_URL)
cur = conn.cursor()
all_posts = {p["slug"]: p for p in database.get_posts(limit=200, category="consejos")}

for slug, marker, extra in POSTS:
    current = all_posts[slug]["content"]
    if marker not in current:
        print(f"✗  {slug}: marcador no encontrado")
        continue
    new_content = current.replace(marker, extra.strip() + "\n\n" + marker)
    cur.execute("UPDATE posts SET content=%s WHERE slug=%s", (new_content, slug))
    print(f"✓  {slug}  —  ~{len(new_content.split())} palabras")

conn.commit()
cur.close()
conn.close()
