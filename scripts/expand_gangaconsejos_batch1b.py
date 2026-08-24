"""Segunda pasada: añade un bloque más a los 2 posts del batch 1 que se quedaron
justo por debajo de 1200 palabras."""
import psycopg2
import config
import database

VUELOS_AGOSTO_EXTRA = """
<h2>¿Vuelo chárter o compañía regular?</h2>
<p>En rutas a destinos turísticos concretos (Baleares, Canarias, algunas islas griegas) en agosto conviven vuelos de aerolíneas regulares con vuelos chárter fletados por turoperadores. Los chárter suelen tener el precio más ajustado si el destino y las fechas coinciden exactamente con su programación, pero tienen mucha menos flexibilidad: cambios de fecha caros o directamente no permitidos, y horarios que no siempre se pueden elegir. Si tu fecha es fija y el destino es uno de los clásicos de chárter, compara igualmente — a veces gana la regular, a veces el chárter, no hay una regla fija.</p>
"""

TRASLADO_EXTRA = """
<h2>Grupos grandes: furgonetas y minibuses</h2>
<p>Para grupos de 5 personas o más, la mayoría de plataformas de traslado privado ofrecen furgonetas de 6-8 plazas o minibuses de hasta 16, con un precio por vehículo (no por persona) que suele salir muy por debajo de varios taxis separados. Resérvalo con antelación: la disponibilidad de vehículos grandes es menor que la de coches estándar, sobre todo en temporada alta.</p>

<h2>¿Hay que dar propina al conductor?</h2>
<p>En España no es obligatorio ni esperado dar propina en traslados, aunque redondear al alza por buen servicio siempre se agradece. En destinos internacionales la costumbre cambia mucho: en EE.UU. se espera un 10-15% del importe, en gran parte de Europa continental no es necesario, y en países como Marruecos o Egipto una propina pequeña (equivalente a 2-5€) es habitual y bien recibida. Si has reservado con una plataforma que ya incluye el servicio completo, revisa las condiciones — algunas ya integran la propina en el precio final.</p>
"""

conn = psycopg2.connect(config.DATABASE_URL)
cur = conn.cursor()
all_posts = {p["slug"]: p for p in database.get_posts(limit=200, category="consejos")}

jobs = [
    ("vuelos-baratos-agosto-como-encontrarlos", "<h2>Antes de salir: no olvides esto</h2>", VUELOS_AGOSTO_EXTRA),
    ("traslado-aeropuerto-taxi-privado-o-transporte-publico", "<h2>Nuestra recomendación por situación</h2>", TRASLADO_EXTRA),
]

for slug, marker, extra in jobs:
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
