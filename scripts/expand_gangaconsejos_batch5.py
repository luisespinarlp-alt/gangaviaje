"""Amplia a 1200+ palabras el batch 5 (ultimo) de GangaConsejos: los 2 posts que quedaban."""
import psycopg2
import config
import database

HOTELES_NUEVO = """
<h2>Qué no suele incluir el "todo incluido"</h2>
<p>Antes de comparar precios entre hoteles, revisa la letra pequeña de qué queda fuera — es donde más se diferencian unos paquetes de otros aunque el precio final sea parecido. Lo que casi nunca está incluido, incluso en paquetes "todo incluido" completos: <strong>parking</strong> (puede sumar 5-15€/día en hoteles de costa), <strong>spa y tratamientos de bienestar</strong> (suele ofrecerse con descuento, no gratis), <strong>excursiones y actividades organizadas</strong> fuera del propio hotel, y <strong>bebidas premium o de importación</strong> (fuera de la carta de bebidas "nacionales" incluidas). Algunos hoteles también limitan el todo incluido a un restaurante buffet concreto, cobrando suplemento por cenar en los restaurantes a la carta del propio complejo — pregunta esto específicamente si el hotel tiene varios restaurantes.</p>

<h2>Trucos para pagar menos incluso en agosto</h2>
<p>Dentro del propio mes de agosto, los precios varían bastante según la semana exacta: la <strong>última semana de agosto</strong> (25-31) suele bajar de precio de forma notable porque muchas familias ya han vuelto a la rutina escolar en algunas comunidades autónomas. Reservar con <strong>cancelación gratuita</strong> y seguir comparando después de reservar es otro truco simple pero efectivo — si el precio baja, cancelas y vuelves a reservar sin coste, siempre que quede margen antes de la fecha límite de cancelación gratuita.</p>

<h2>Todo incluido vs. media pensión con restaurantes fuera</h2>
<p>En destinos con oferta gastronómica interesante fuera del hotel (Cádiz, Almería, buena parte de Canarias), puede compensar económicamente elegir media pensión más barata y comer fuera del hotel algunos días — sobre todo si el todo incluido del hotel elegido tiene fama de comida mediocre según las reseñas. Haz la cuenta real: si la diferencia de precio entre todo incluido y media pensión es de 15-20€/persona/día, y comer bien fuera cuesta 20-25€/persona, el todo incluido casi siempre sale más rentable — pero no siempre, especialmente en zonas con buena oferta de menú del día económico.</p>
"""

RETRASOS_NUEVO = """
<h2>Denegación de embarque por overbooking</h2>
<p>Es una situación distinta al retraso o la cancelación, y también está cubierta por el Reglamento 261/2004: si la aerolínea ha vendido más billetes de los asientos disponibles y te deniega el embarque en contra de tu voluntad (aunque hayas llegado a tiempo con tu billete válido), tienes derecho a la <strong>misma compensación económica</strong> que en una cancelación (250-600€ según distancia), más el derecho a elegir entre reembolso completo o transporte alternativo. Si te ofrecen voluntariamente ceder tu plaza a cambio de una compensación (bonos, vuelo alternativo con ventajas), puedes aceptar libremente — en ese caso las condiciones las negocias tú directamente con la aerolínea, no aplica la compensación fija.</p>

<h2>Equipaje perdido o dañado: otro derecho distinto</h2>
<p>Para el equipaje rige el <strong>Convenio de Montreal</strong>, no el Reglamento 261/2004 — son derechos separados y compatibles entre sí. Si tu maleta llega dañada, debes reportarlo en el propio aeropuerto antes de salir de la zona de recogida de equipajes, rellenando un PIR (Property Irregularity Report). Para maletas perdidas, tienes hasta 21 días para reclamar por retraso en la entrega y hasta 7 días para daños visibles. La compensación máxima por equipaje bajo este convenio ronda los 1.300 DEG (unos 1.500-1.600€, la cifra exacta varía con el tipo de cambio), aunque en la práctica la aerolínea suele pedir factura o valoración de lo que llevabas dentro.</p>

<h2>¿Y si el vuelo era parte de un paquete con hotel?</h2>
<p>Si compraste el vuelo como parte de un paquete vacacional (vuelo + hotel a través de una agencia o turoperador), tus derechos del Reglamento 261/2004 sobre el vuelo siguen aplicando igual — son independientes del contrato del paquete. Además, si el retraso te hace perder noches de hotel ya pagadas, puedes reclamar esa parte proporcional al turoperador por separado, no a la aerolínea. Guarda ambas reclamaciones documentadas por separado: son procesos distintos con interlocutores distintos.</p>
"""

POSTS = [
    ("hoteles-todo-incluido-baratos-costa-espana-agosto", "<h2>Antes de reservar</h2>", HOTELES_NUEVO),
    ("que-hacer-si-tu-vuelo-se-retrasa-o-cancela", "<h2>Vuelos con escala: cómo funciona</h2>", RETRASOS_NUEVO),
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
