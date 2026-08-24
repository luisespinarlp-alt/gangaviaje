"""Amplia a 1200+ palabras el batch 3 de GangaConsejos (3 de los 8 restantes)."""
import psycopg2
import config
import database

SOLO_NUEVO = """
<h2>El presupuesto: viajar solo cuesta más por noche, pero puedes compensarlo</h2>
<p>La habitación individual en un hotel casi nunca cuesta la mitad de una doble — el llamado "suplemento de individual" puede ser del 60-80% del precio de la doble. Los hostels resuelven este problema: una cama en dormitorio compartido cuesta lo mismo estés solo o en grupo, y sigue siendo la opción más barata para viajar solo con presupuesto ajustado. Para compensar el gasto en alojamiento, en comida el ahorro es mayor viajando solo: comes lo que quieres, cuando quieres, sin ceder a preferencias ajenas ni a restaurantes caros por consenso de grupo.</p>

<h2>Comer solo en un restaurante: menos raro de lo que parece</h2>
<p>Es el miedo social más citado por quien viaja solo por primera vez, y el que menos dura. En la mayoría de países, comer solo en un restaurante es completamente normal y nadie te presta atención — llevar un libro o el móvil hace que la situación se sienta aún más natural. En destinos asiáticos, comer solo en puestos de comida callejera o barras es la norma, no la excepción. Si te da vergüenza al principio, empieza por cafeterías o sitios con barra antes de mesas para dos.</p>

<h2>Qué llevar cuando viajas solo (y qué no)</h2>
<p>Sin nadie que cargue la mitad del equipaje compartido (cargador extra, botiquín, adaptadores), viajar ligero es más importante que nunca. Una mochila de cabina en vez de maleta facturada te da libertad total de movimiento — puedes cambiar de plan, coger un tren de última hora o cambiar de alojamiento sin depender de recoger una maleta grande. Lleva siempre un candado pequeño para taquillas de hostel, y un power bank — te vas a apoyar mucho más en el móvil (mapas, traducción, cámara) sin nadie más con quien repartir esa carga de batería.</p>

<h2>Viajar solo siendo mujer: consideraciones reales</h2>
<p>Millones de mujeres viajan solas cada año sin incidentes, y la mayoría de destinos turísticos son perfectamente seguros. Las precauciones que marcan la diferencia: elegir alojamiento con buenas reseñas específicas de viajeras solas (Hostelworld y Booking permiten filtrar por este tipo de comentario), evitar llegar de madrugada a una ciudad nueva sin transporte ya organizado, y unirte a grupos de Facebook o apps específicas para viajeras solas (Girls LOVE Travel, Tourlina) para consejos actualizados destino por destino. Destinos con buena reputación específica para mujeres viajando solas: Japón, Islandia, Portugal, Nueva Zelanda y la mayoría de Europa occidental.</p>
"""

RYANAIR_NUEVO = """
<h2>El embarque: prioritario o normal</h2>
<p>El embarque prioritario (incluido en la tarifa Priority o comprable aparte por 5-6€) permite subir en los primeros grupos y guardar sitio para el equipaje de mano en el compartimento superior. En vuelos muy llenos, quienes embarcan en los últimos grupos a veces tienen que facturar la maleta de cabina gratis en la puerta porque ya no queda espacio — no es una multa, pero sí una molestia si llevas líquidos o algo frágil dentro. Si tu maleta de cabina es grande y el vuelo va lleno, el embarque prioritario evita ese riesgo.</p>

<h2>Cambios de vuelo: cuánto cuesta y cómo evitarlo</h2>
<p>Cambiar la fecha o el horario de un vuelo de Ryanair ya comprado cuesta la diferencia de tarifa más una comisión de gestión (normalmente 35-50€ en tarifas básicas). La tarifa Flexi Plus incluye un cambio gratuito, pero solo compensa pagarla si ya sabes de antemano que hay bastante probabilidad de que cambien tus planes. Si tienes duda entre dos fechas cercanas, comprar en tarifa básica la que tengas más segura suele salir más barato que comprar Flexi Plus "por si acaso".</p>

<h2>Reembolsos: cuándo Ryanair sí devuelve dinero</h2>
<p>Ryanair no da reembolsos por cancelación voluntaria del pasajero, solo crédito de vuelo en algunos casos. Sí está obligada a reembolsar el importe completo si es la propia aerolínea quien cancela el vuelo, y a ofrecer compensación adicional de hasta 600€ si la cancelación se comunica con menos de 14 días de antelación y no es por causa de fuerza mayor (huelga de terceros, meteorología extrema). Guarda siempre el email de cancelación de Ryanair — es la prueba que necesitarás para reclamar.</p>

<h2>Ryanair en aeropuertos secundarios: el truco que no cambia</h2>
<p>Muchas rutas "a Londres" en realidad aterrizan en Stansted o Luton, a 45-60 minutos del centro en tren; "a Milán" puede ser Bérgamo, a más de una hora de la ciudad. Esto no es un engaño — está indicado en la reserva — pero conviene sumar el coste y tiempo del traslado antes de comparar el precio final con otras aerolíneas que vuelan al aeropuerto principal. En trayectos cortos el ahorro sigue mereciendo la pena; en viajes de un único día, el tiempo de traslado puede comerse buena parte del plan.</p>
"""

DESTINOS_AGOSTO_NUEVO = """
<h2>Escapadas cortas si no puedes coger vacaciones largas</h2>
<p>Si agosto solo te da un puente o un fin de semana largo, algunas opciones aprovechan bien el tiempo sin necesitar vuelo largo: <strong>los Picos de Europa</strong> (Asturias-Cantabria-León) para desconectar del calor, <strong>el Pirineo aragonés o catalán</strong> con temperaturas 10°C más bajas que la costa, o <strong>una escapada a Oporto</strong> — menos masificado que Lisboa en agosto y con vuelos directos desde varias ciudades españolas por menos de 80€.</p>

<h2>Viajar en agosto con niños: qué destinos funcionan mejor</h2>
<p>Con niños pequeños, el calor extremo de destinos como el sur de España o Marruecos interior puede hacer el viaje incómodo en las horas centrales del día. Destinos con clima más suave y buena infraestructura familiar: <strong>Galicia y Asturias</strong> (temperaturas moderadas, playas de arena fina y poco oleaje en muchas calas), <strong>los lagos del norte de Italia</strong> (Como, Garda — frescos, con actividades acuáticas suaves), y <strong>Dinamarca o los Países Bajos</strong> (agosto templado, muy adaptados para viajar con carrito y transporte accesible).</p>

<h2>El truco de la "semana intermedia"</h2>
<p>Dentro del propio agosto, la última semana (25-31) es sistemáticamente más barata que la primera quincena en casi todos los destinos — muchos turistas ya han vuelto a la rutina pero el buen tiempo se mantiene en la mayoría de Europa. Si tu trabajo permite algo de flexibilidad, mover el viaje a esos últimos días de agosto puede bajar el precio del alojamiento un 20-30% respecto a la primera quincena, con playas notablemente menos llenas.</p>

<h2>Alternativa al avión: destinos en tren desde España</h2>
<p>Si quieres evitar el caos de los aeropuertos en agosto, varios destinos son perfectamente viables en tren de alta velocidad o nocturno: <strong>el sur de Francia</strong> (Toulouse, Montpellier) en pocas horas desde Barcelona, o combinando AVE + regional se llega bien a buena parte del norte de España sin depender de vuelos ni de la saturación de las autopistas del verano.</p>
"""

POSTS = [
    ("viajar-solo-primera-vez-guia-completa", "<h2>El mayor miedo: aburrirse o sentirse solo</h2>", SOLO_NUEVO),
    ("ryanair-trucos-evitar-cargos-extras-2026", "<h2>Cuándo comprar para conseguir el precio más bajo</h2>", RYANAIR_NUEVO),
    ("destinos-agosto-2026-donde-ir-este-verano", "<h2>Consejo final: cuándo reservar para agosto</h2>", DESTINOS_AGOSTO_NUEVO),
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
