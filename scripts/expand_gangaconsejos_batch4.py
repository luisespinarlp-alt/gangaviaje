"""Amplia a 1200+ palabras el batch 4 de GangaConsejos (3 de los 5 restantes).
Los dos posts de eSIM son muy similares entre si -- se diferencian a proposito:
el primero mantiene el angulo educativo (que es / como funciona), el segundo
el angulo comparativo/de compra (cual elegir segun destino)."""
import psycopg2
import config
import database

VUELOS_TRUCOS_NUEVO = """
<h2>Temporada baja: los meses más baratos del año para volar</h2>
<p>Más allá de trucos puntuales, la variable que más pesa en el precio es la temporada. En vuelos desde España, los meses de <strong>enero (después del 10), febrero, y la segunda quincena de septiembre-octubre-noviembre</strong> son sistemáticamente los más baratos del año en la mayoría de rutas europeas e internacionales. Si tienes flexibilidad total de fechas, mover el viaje a estos meses puede ahorrar más que cualquier truco de búsqueda — la demanda baja hace más que cualquier alerta de precio.</p>

<h2>Comunidades y newsletters de chollos de vuelos</h2>
<p>Además de las alertas automáticas, seguir comunidades especializadas encuentra errores de tarifa y ofertas flash que los buscadores no destacan. Canales de Telegram y grupos de Facebook dedicados a "vuelos baratos España" comparten capturas de pantalla de tarifas anómalas (a veces errores de la propia aerolínea) que duran horas antes de corregirse. No todas son reales — verifica siempre en la web oficial de la aerolínea antes de pagar en una web de terceros que no conozcas.</p>

<h2>Buscar en otra moneda: ¿funciona de verdad?</h2>
<p>Existe la teoría de que cambiar la moneda de búsqueda (a dólares, libras o moneda del país de destino) muestra precios distintos por cómo cada aerolínea fija sus tarifas locales. Es cierto en algunos casos puntuales — sobre todo en aerolíneas asiáticas o sudamericanas que fijan precio en moneda local y el cambio de divisa introduce pequeñas diferencias — pero no es una garantía ni un truco fiable para aerolíneas europeas. Merece la pena probarlo en búsquedas de larga distancia, no como estrategia principal.</p>

<h2>Cuándo una oferta flash es real y cuándo es trampa</h2>
<p>Las ofertas flash genuinas de aerolíneas suelen tener: fechas de viaje muy amplias (varios meses de margen), disponibilidad limitada real (pocas plazas, se agotan rápido) y proceden de la web oficial de la aerolínea o agencias reconocidas. Sospecha de ofertas que solo existen en webs desconocidas, que piden pago por transferencia en vez de tarjeta, o que prometen precios muy por debajo de cualquier búsqueda en Google Flights para las mismas fechas — ahí es más probable que sea una estafa que un chollo real.</p>
"""

ESIM_QUE_ES_NUEVO = """
<h2>Problemas comunes y cómo solucionarlos</h2>
<p>Los fallos más habituales al usar una eSIM tienen solución rápida en la mayoría de casos: si no detecta datos al llegar, comprueba que el <strong>roaming de datos esté activado específicamente para el perfil de la eSIM</strong> (es un ajuste independiente del roaming de tu línea principal, fácil de pasar por alto). Si el QR da error al escanear, casi siempre es porque ya se escaneó una vez — los códigos QR de eSIM son de un solo uso, así que si tuviste que reiniciar el móvil antes de completar la instalación, tendrás que pedir uno nuevo al proveedor. Si la velocidad es muy lenta, prueba a activar y desactivar el modo avión — a veces el móvil tarda en conectar a la mejor antena local disponible.</p>

<h2>¿La eSIM consume más batería que una SIM física?</h2>
<p>No hay diferencia relevante de consumo entre eSIM y SIM física — el gasto de batería depende del uso de datos (mapas, vídeo, redes sociales), no del tipo de tarjeta. Sí conviene desactivar la búsqueda automática de red de tu línea principal si la vas a tener sin datos activos durante el viaje, porque el móvil gasta batería intentando conectarse a una red con la que no tiene plan de datos activo.</p>

<h2>¿Puedo usar la misma eSIM en una tablet o en otro móvil?</h2>
<p>Cada eSIM se vincula a un dispositivo concreto en el momento de la activación — no se puede mover libremente de un móvil a una tablet como sí se hace con una SIM física. Si necesitas datos en dos dispositivos a la vez (móvil y tablet, por ejemplo), tendrás que comprar una eSIM para cada uno, o usar la función de "compartir datos" (punto de acceso wifi) desde el móvil que sí tiene la eSIM activa hacia el segundo dispositivo.</p>

<h2>Privacidad: lo que debes saber</h2>
<p>Comprar una eSIM de viaje normalmente no requiere registrar tu identidad como sí exige la ley en algunos países para SIMs físicas locales (pasaporte, huella, formulario) — esto la hace más rápida de contratar y, para muchos viajeros, más discreta. Aun así, el proveedor de la eSIM (Airalo, Holafly) sí conoce tu email y método de pago, igual que cualquier otro servicio online que contrates. No supone ningún riesgo adicional frente a comprar cualquier otro producto digital.</p>
"""

MEJOR_ESIM_NUEVO = """
<h2>Lo que ninguna eSIM cubre</h2>
<p>Una eSIM de viaje da datos, pero normalmente <strong>no incluye un número de teléfono local</strong> propio con el que te puedan llamar desde ese país (algunos planes ofrecen esta función como extra de pago). Tampoco sustituye a la línea de emergencia: en la mayoría de países puedes llamar a los números de emergencia locales sin necesidad de tener datos ni saldo, incluso con la eSIM sin activar, porque las redes móviles están obligadas a permitir llamadas de emergencia desde cualquier tarjeta.</p>

<h2>eSIM para trabajar en remoto durante el viaje</h2>
<p>Si necesitas conexión estable para videollamadas o trabajo mientras viajas, prioriza planes con datos generosos (10GB+) o ilimitados sobre los más baratos de 1-3GB — quedarte sin datos a mitad de una reunión es el escenario que quieres evitar. Lleva también un plan B: identifica de antemano un par de cafeterías o espacios de coworking con buen wifi en el destino, por si la cobertura móvil falla en un momento crítico. Para estancias largas trabajando desde un solo país, puede salir más barato una SIM física local de datos ilimitados que una eSIM de turista.</p>

<h2>Errores comunes al comprar una eSIM</h2>
<ul>
  <li><strong>Comprar la eSIM Global cuando solo vas a un país:</strong> las eSIM globales cuestan más por GB que las locales o regionales — solo compensan si visitas varios continentes en el mismo viaje</li>
  <li><strong>No revisar la fecha de caducidad del plan:</strong> la mayoría de planes empiezan a contar los días desde la <strong>primera conexión</strong>, no desde la compra — pero algunos proveedores cuentan desde la compra, así que revisa esto antes de comprar con mucha antelación</li>
  <li><strong>Comprar datos de más "por si acaso":</strong> los datos no usados no se devuelven ni se acumulan para el siguiente viaje — mejor quedarse corto y ampliar desde la misma app si hace falta, que suele tardar minutos</li>
</ul>

<h2>¿Merece la pena para viajes muy cortos (2-3 días)?</h2>
<p>Para escapadas de fin de semana dentro de la Unión Europea, probablemente no necesites eSIM — el roaming español es gratuito en la UE. Para un fin de semana fuera de la UE (Reino Unido, Marruecos, Turquía, Suiza), los planes más pequeños de 1GB/7 días suelen ser más que suficientes y cuestan lo mismo aunque solo uses 2 de los 7 días — el ahorro de comprar "justo lo necesario" no compensa el tiempo de comparar planes de menor duración, que además no siempre existen.</p>
"""

POSTS = [
    ("vuelos-baratos-trucos-encontrar-mejores-ofertas", "<h2>Apps y herramientas esenciales</h2>", VUELOS_TRUCOS_NUEVO),
    ("esim-que-es-como-funciona-y-mejor-para-viajar", "<h2>Nuestra recomendación</h2>", ESIM_QUE_ES_NUEVO),
    ("mejor-esim-para-viajar-europa-mundo", "<h2>Consejos para usar bien tu eSIM de viaje</h2>", MEJOR_ESIM_NUEVO),
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
