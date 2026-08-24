"""
Nueva guia de destino: Rio de Janeiro, Brasil.
Datos practicos verificados via WebSearch el 2026-08-24.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database

CONTENT = """<p>Río de Janeiro es de los pocos destinos del mundo que consigue estar a la altura de la fama que precede — el Cristo Redentor con los brazos abiertos sobre la ciudad, el Pan de Azúcar asomando entre rascacielos, y las playas más famosas del planeta a un paseo del centro. Es también un destino que exige viajar con la cabeza puesta: la ciudad más espectacular de Sudamérica y, a la vez, una que pide precauciones reales, no solo las típicas de cualquier gran ciudad.</p>

<h2>Cristo Redentor: la vista que ya conoces, en persona</h2>
<p>El Cristo Redentor corona el cerro del Corcovado a 710 metros sobre el nivel del mar, con la ciudad entera desplegada a sus pies — Copacabana, Ipanema, la laguna Rodrigo de Freitas y el Pan de Azúcar, todo visible en un único golpe de vista. Se sube en un tren cremallera histórico que atraviesa el bosque tropical del Parque Nacional de Tijuca, o en furgoneta oficial si prefieres ahorrar tiempo. Ve a primera hora de la mañana: además de evitar las peores colas, la claridad matinal ofrece las mejores fotos antes de que suba la calima típica del mediodía.</p>

<h2>Pan de Azúcar: el otro mirador imprescindible</h2>
<p>Dos teleféricos consecutivos suben hasta los 396 metros del Pan de Azúcar (Pão de Açúcar), el peñón de granito que se ha convertido en el otro símbolo visual de la ciudad. La vista desde aquí es distinta y complementaria a la del Corcovado: se ve el propio Cristo Redentor a lo lejos, además de toda la bahía de Guanabara. Ir al atardecer, con la puesta de sol sobre la ciudad y las luces encendiéndose después, es de las experiencias más memorables que se pueden tener en Río.</p>

<h2>Copacabana e Ipanema: las playas más famosas del mundo</h2>
<p>Copacabana es la más icónica y animada, con su paseo de mosaico ondulado en blanco y negro y kilómetros de arena siempre llenos de vida — partidos de fútbol y vóley playa improvisados, vendedores de agua de coco y caipiriña a pie de toalla. Ipanema, justo al lado, tiene fama de ser la playa con mejor ambiente, más seguridad percibida y los atardeceres más bonitos de la ciudad — mucha gente se reúne en el Arpoador, la roca que separa ambas playas, específicamente para verlo cada tarde.</p>

<h2>Más allá de las postales: Santa Teresa y las Escaleras de Selarón</h2>
<p>El barrio bohemio de Santa Teresa, con sus calles empedradas en cuesta y su tranvía histórico, tiene el ambiente más artístico y menos turístico del centro de Río — galerías, talleres de artistas y buenos restaurantes con vistas a la bahía. Justo al pie del barrio están las Escaleras de Selarón, 250 escalones cubiertos de azulejos de colores de más de 60 países, obra del artista chileno Jorge Selarón durante más de 20 años hasta su muerte en 2013 — hoy es uno de los lugares más fotografiados de la ciudad.</p>

<h2>Seguridad: lo que hay que saber de verdad</h2>
<p>Río tiene fama de insegura y conviene tomárselo en serio sin paranoia. Las zonas turísticas principales — Copacabana, Ipanema, Leblon, Barra da Tijuca y Santa Teresa — están bien vigiladas y muy transitadas; el riesgo real ahí es el hurto oportunista (tirones de móvil, carteristas), no la violencia, pero ocurre incluso a plena luz del día en plena playa. Las precauciones que marcan la diferencia: no llevar cámaras ni móviles muy a la vista, salir con lo justo (no todas las tarjetas ni todo el efectivo), organizar el regreso al hotel antes de que anochezca, y moverte en Uber o taxi oficial por la noche en vez de caminar largas distancias. Evita entrar por tu cuenta en las favelas — si quieres conocerlas, hazlo con un tour organizado con guía local, es la forma segura y también la más respetuosa con quien vive allí.</p>

<h2>Cuándo ir y presupuesto</h2>
<p>El verano brasileño (<strong>diciembre-marzo</strong>) es caluroso y húmedo (35°C+) pero es cuando ocurre el Carnaval — la fiesta callejera más famosa del mundo, en febrero o marzo según el calendario de cada año. El invierno (<strong>junio-septiembre</strong>) es mucho más agradable para hacer turismo, con temperaturas de 20-25°C y menos lluvia. Un vuelo desde España ronda los 750€ ida y vuelta. Sobre el terreno, la comida callejera cuesta 1-3€, un almuerzo completo por peso en restaurante 4-8€, y una buena cena puede rondar 15-30€ — Brasil sigue siendo un destino asequible para estándares europeos, sobre todo fuera de los restaurantes más turísticos de Copacabana e Ipanema.</p>

<h2>Visado y documentación</h2>
<p>Los ciudadanos españoles no necesitan visado para estancias turísticas de hasta <strong>90 días en un periodo de 180</strong>. El pasaporte debe tener una validez mínima de 6 meses desde la fecha de entrada, y la policía de fronteras puede pedir un billete de vuelta o de salida del país con fecha dentro de esos 90 días — llévalo siempre a mano, aunque sea en el móvil.</p>

<h2>Antes de viajar: eSIM y seguro</h2>
<p>Para Brasil, una <strong><a href="/blog/mejor-esim-para-viajar-europa-mundo">eSIM de viaje</a></strong> es muy recomendable — tener Google Maps y Uber funcionando desde el aterrizaje es parte importante de la seguridad, no solo de la comodidad. Un <strong>seguro de viaje</strong> con buena cobertura médica es imprescindible fuera de la UE. Y si tu vuelo se retrasa más de 3 horas o lo cancelan, recuerda que tienes derecho a compensación — <a href="/blog/que-hacer-si-tu-vuelo-se-retrasa-o-cancela">aquí te explicamos cómo reclamar hasta 600€</a>.</p>
"""

post = {
    "slug": "rio-de-janeiro-brasil-guia-completa",
    "title": "Río de Janeiro: Cristo Redentor, Pan de Azúcar y Copacabana — guía completa 2026",
    "excerpt": "Cómo organizar el viaje a la ciudad más espectacular de Sudamérica: qué ver, cuándo ir, cuánto cuesta y las precauciones de seguridad que de verdad importan.",
    "content": CONTENT,
    "image_url": "https://images.unsplash.com/photo-1777952835597-e0af6659357b?fm=jpg&q=80&w=1200&auto=format&fit=crop",
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
