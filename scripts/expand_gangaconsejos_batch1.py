"""
Amplia a 1200+ palabras los 3 posts de GangaConsejos mas cortos (batch 1 de 14 pendientes).
Mismo patron que rewrite_top_guides.py: UPDATE directo por slug, conserva title/excerpt,
solo se amplia el content insertando secciones nuevas antes del cierre existente.
"""
import psycopg2
import config
import database

SEGURO_NUEVO = """
<h2>Franquicia: la letra pequeña que hay que mirar siempre</h2>
<p>La franquicia es la cantidad que pagas tú antes de que el seguro empiece a cubrir el resto. Muchos seguros baratos tienen franquicias de 100-300€ en asistencia médica o de 30-60€ en equipaje — es decir, si la factura del hospital es de 250€ y tu franquicia es de 300€, el seguro no paga nada. Antes de comparar precios entre dos seguros, compara siempre la franquicia: un seguro 5€ más caro sin franquicia suele salir más rentable que uno barato con franquicia alta, salvo que solo lo quieras para imprevistos grandes (hospitalización, repatriación).</p>

<h2>Seguro de cancelación: qué causas cubre de verdad</h2>
<p>La cobertura de cancelación tiene más matices de los que parece. La mayoría de pólizas solo cubren cancelación por: enfermedad o accidente grave (tuyo o de un familiar directo) acreditado con informe médico, fallecimiento de un familiar cercano, despido laboral improcedente, o convocatoria judicial/electoral inesperada. <strong>No suelen cubrir</strong>: cambio de opinión, mal tiempo previsto, o que el destino deje de apetecerte. Existen pólizas de "cancelación por cualquier motivo", pero son un 40-60% más caras y normalmente solo devuelven el 75% del importe — solo compensan en viajes muy caros donde la flexibilidad total vale la pena.</p>

<h2>Viajar con niños o personas mayores: qué cambia</h2>
<p>Con niños pequeños, revisa que el seguro no ponga condiciones especiales a la cobertura médica pediátrica ni excluya enfermedades comunes de la infancia. Con mayores de 65-70 años, muchos seguros estándar bajan mucho la cobertura o suben el precio de forma notable — conviene comparar seguros específicos para mayores, que sí cubren bien patologías previas controladas (hipertensión, diabetes estable) sin las exclusiones agresivas de las pólizas genéricas. Si viajas con alguien con una enfermedad preexistente, declárala siempre al contratar: ocultarla es motivo de nulidad de la cobertura si luego hace falta usarla.</p>

<h2>¿Merece la pena usar un comparador online?</h2>
<p>Los comparadores son útiles para hacerse una idea de precios, pero fíjate en que comparen coberturas equivalentes, no solo el precio final — es habitual que el resultado "más barato" tenga una franquicia alta o un límite de asistencia médica muy inferior al resto. Usa el comparador para acotar 2-3 opciones y luego revisa las condiciones completas (el documento de "condiciones generales", no solo el resumen) antes de decidir.</p>

<h2>Preguntas frecuentes</h2>
<ul>
  <li><strong>¿Puedo contratar el seguro el mismo día del vuelo?</strong> Sí, la mayoría de aseguradoras lo permiten, pero la cobertura de cancelación de viaje deja de tener sentido si ya no puedes cancelar nada — contrátalo lo antes posible tras reservar si quieres esa cobertura.</li>
  <li><strong>¿El seguro cubre el embarazo?</strong> Depende de las semanas de gestación y de si hay complicaciones. La mayoría cubre urgencias hasta la semana 28-32; a partir de ahí, casi ninguna aerolínea permite volar de todas formas.</li>
  <li><strong>¿Qué pasa si ya estoy de viaje y quiero contratar seguro?</strong> Algunas aseguradoras lo permiten, pero no cubren nada relacionado con algo que ya haya empezado a manifestarse antes de la contratación.</li>
</ul>
"""

VUELOS_AGOSTO_NUEVO = """
<h2>Vuelos con escala: cuánto se puede ahorrar realmente</h2>
<p>En agosto, un vuelo con una escala puede costar 30-40% menos que el directo a igual fecha — la demanda se concentra en las rutas directas y las aerolíneas con escala (turcas, centroeuropeas) suelen tener más disponibilidad. Merece la pena si la escala es de 1-3 horas y el destino no es carísimo de por sí; si la escala añade 6-8 horas, el ahorro rara vez compensa el desgaste, salvo en vuelos muy largos donde de todas formas ibas a hacer una parada.</p>

<h2>Reservar ida y vuelta por separado, con aerolíneas distintas</h2>
<p>No siempre el billete combinado de ida y vuelta con la misma aerolínea es el más barato. En agosto, comparar el precio de la ida suelta con una aerolínea y la vuelta suelta con otra puede ahorrar 20-50€, sobre todo en rutas donde una aerolínea tiene mejor oferta de salida y otra de regreso. El riesgo: si compras por separado, no hay protección si pierdes una conexión por retraso de la otra aerolínea — solo tiene sentido en vuelos directos, no en itinerarios con conexiones ajustadas.</p>

<h2>Errores que encarecen el vuelo sin que te des cuenta</h2>
<ul>
  <li><strong>Buscar siempre desde el mismo dispositivo y sin borrar cookies:</strong> el mito de que las webs suben el precio por buscar mucho no está confirmado, pero sí varía por la caché del navegador — abre una ventana de incógnito si llevas varias búsquedas de la misma ruta</li>
  <li><strong>No comparar la tarifa básica con la que incluye equipaje:</strong> en agosto, con aerolíneas low cost, la diferencia entre la tarifa mínima y la que realmente necesitas (con maleta facturada) puede ser de 40-60€ — compara el precio final real, no el titular</li>
  <li><strong>Reservar sin mirar el aeropuerto de llegada exacto:</strong> algunos destinos tienen dos aeropuertos (Londres, París, Milán, Roma) con precios y distancias al centro muy distintas — el más barato no siempre es el más práctico</li>
</ul>

<h2>Programas de fidelización: ¿ayudan en agosto?</h2>
<p>Si ya tienes millas o puntos acumulados de vuelos anteriores, agosto es un mes complicado para canjearlos porque la disponibilidad de plazas "premium" (las que se pueden pagar con puntos) es más baja que en temporada media. Si tienes flexibilidad, revisa la disponibilidad de canje con 2-3 meses de antelación; a menos de un mes vista, es raro encontrar plazas de canje en fechas de agosto.</p>
"""

TRASLADO_NUEVO = """
<h2>Alquiler de coche en el aeropuerto: la cuarta opción</h2>
<p>Si el viaje incluye moverte fuera de la ciudad (costa, varias localidades, zona rural), alquilar coche directamente en el aeropuerto puede salir más rentable que sumar traslado + transporte local durante varios días. Revisa siempre el precio con todo incluido (seguro a todo riesgo sin franquicia, segundo conductor, kilometraje ilimitado) antes de comparar con el traslado — el precio de "gancho" del alquiler casi nunca es el precio real final. <a href="/blog/alquilar-coche-barato-espana-trucos">Aquí tienes los trucos para no pagar de más al alquilar coche</a>.</p>

<h2>Cómo evitar las trampas más comunes en aeropuertos internacionales</h2>
<p>En destinos como Marrakech, Bangkok o El Cairo, es habitual que alguien fuera de la zona oficial de taxis se ofrezca a "ayudarte con las maletas" o te diga que la parada oficial "está cerrada" para llevarte a un coche sin licencia. Regla simple: ignora a cualquiera que se te acerque antes de llegar tú mismo a la parada oficial señalizada. Si has reservado traslado privado, el conductor siempre espera con un cartel con tu nombre dentro de la terminal de llegadas, nunca fuera intentando abordarte antes.</p>

<h2>Reservar con antelación vs. contratar en el momento</h2>
<p>Reservar el traslado antes de viajar suele costar 15-30% menos que contratarlo al llegar, además de garantizarte precio fijo sin sorpresas de última hora. La excepción es el transporte público, donde el precio es el mismo se compre cuando se compre. Para traslados privados, resérvalos con al menos 24-48h de antelación — muchas plataformas permiten cancelación gratuita hasta pocas horas antes, así que reservar pronto no tiene desventaja real.</p>

<h2>Qué hacer si tu vuelo llega con retraso</h2>
<p>Con un traslado privado reservado con seguimiento de vuelo, el conductor ajusta la hora de recogida automáticamente y no se cobra extra por el retraso — es una de las ventajas menos conocidas frente al taxi, que no sabe que llegas tarde. Con transporte público, comprueba antes de aterrizar el horario del último servicio nocturno; en ciudades donde el metro cierra pronto (Madrid cierra sobre la 1:30, por ejemplo), un vuelo con retraso puede dejarte sin esa opción y forzarte a un taxi de todas formas.</p>
"""

POSTS = [
    {
        "slug": "mejor-seguro-de-viaje-2026-cual-contratar",
        "insert_before": "<h2>Nuestra recomendación</h2>",
        "new_content": SEGURO_NUEVO,
    },
    {
        "slug": "vuelos-baratos-agosto-como-encontrarlos",
        "insert_before": "<h2>Antes de salir: no olvides esto</h2>",
        "new_content": VUELOS_AGOSTO_NUEVO,
    },
    {
        "slug": "traslado-aeropuerto-taxi-privado-o-transporte-publico",
        "insert_before": "<h2>Nuestra recomendación por situación</h2>",
        "new_content": TRASLADO_NUEVO,
    },
]

conn = psycopg2.connect(config.DATABASE_URL)
cur = conn.cursor()

all_posts = {p["slug"]: p for p in database.get_posts(limit=200, category="consejos")}

for p in POSTS:
    slug = p["slug"]
    current = all_posts[slug]["content"]
    marker = p["insert_before"]
    if marker not in current:
        print(f"✗  {slug}: marcador '{marker}' no encontrado, saltando")
        continue
    new_content = current.replace(marker, p["new_content"].strip() + "\n\n" + marker)
    cur.execute("UPDATE posts SET content=%s WHERE slug=%s", (new_content, slug))
    words = len(new_content.split())
    print(f"✓  {slug}  —  ~{words} palabras  ({cur.rowcount} fila actualizada)")

conn.commit()
cur.close()
conn.close()
print("\n✅  Batch 1 (3 posts) ampliado")
