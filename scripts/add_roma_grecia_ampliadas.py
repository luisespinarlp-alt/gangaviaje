"""
Reescribe/amplía las guías de Roma e Islas Griegas a formato completo (1200-1500 palabras).
Script de un solo uso.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import psycopg2, config

_GC_BOX = (
    '<div style="background:linear-gradient(135deg,#fde8e6,#fff9f8);'
    'border-left:4px solid #e8523a;border-radius:8px;padding:20px 24px;margin:32px 0;">'
)

def gc(titulo, items):
    li = "".join("<li>" + i + "</li>" for i in items)
    return (
        _GC_BOX
        + '<h2 style="color:#e8523a;margin-top:0;">GangaConsejos: ' + titulo + '</h2>'
        + '<ul style="margin-bottom:0;">' + li + '</ul>'
        + '</div>'
    )

_ESIM_SEGURO = (
    '<h2>Antes de viajar: eSIM y seguro</h2>'
    '<p>Para este destino, una <strong><a href="/blog/mejor-esim-para-viajar-europa-mundo">eSIM de viaje</a></strong> '
    'es prácticamente imprescindible: datos móviles desde el aterrizaje sin pagar roaming ni buscar una SIM local. '
    'Desde 5-9€ para Europa o desde 7€ para cobertura global.</p>'
    '<p>Un <strong>seguro de viaje</strong> con cobertura médica y cancelación es muy recomendable. Y si tu vuelo '
    'sufre un retraso de más de 3 horas o lo cancelan, tienes derecho a compensación — '
    '<a href="/blog/que-hacer-si-tu-vuelo-se-retrasa-o-cancela">aquí te contamos cómo reclamar hasta 600€</a>.</p>'
)


# ─── ROMA ────────────────────────────────────────────────────────────────────

ROMA = """<p>Roma es la única ciudad del mundo donde puedes desayunar junto a un templo de 2.000 años, comer al lado de una plaza barroca y cenar en un barrio que era el puerto fluvial de la Roma imperial. Concentra tanta historia en tan poco espacio que planificar bien la visita marca la diferencia entre agotarte corriendo de un monumento a otro o disfrutar de verdad la Ciudad Eterna. Esta guía cubre lo esencial para 3-4 días, con los trucos para evitar las colas que le comen el tiempo a la mayoría de los turistas.</p>

<h2>Qué ver en Roma: los imprescindibles</h2>

<h3>Coliseo, Foro Romano y Monte Palatino</h3>
<p>Se visitan con la misma entrada y ocupan fácilmente media jornada. El Coliseo, con capacidad para 50.000 espectadores en su época, sigue impresionando por su ingeniería. El Foro Romano —el centro político y social del Imperio— y el Monte Palatino —donde vivían los emperadores, con vistas espectaculares sobre el Foro y el Circo Máximo— completan la visita. Entrada: 18€, reserva online obligatoria con franja horaria; sin reserva, la cola puede superar las dos horas en temporada alta.</p>

<h3>Museos Vaticanos y Capilla Sixtina</h3>
<p>La colección de arte más importante del mundo, culminando en el techo de Miguel Ángel en la Capilla Sixtina. Hay que reservar entrada online con semanas de antelación —sin reserva, la cola sin sombra puede superar las tres horas—. Dedica la mañana entera: son más de 7 kilómetros de galerías si las recorres todas. La Basílica de San Pedro, justo al lado, es gratuita y se puede subir a la cúpula (10€, 551 escalones) para las mejores vistas de Roma.</p>

<h3>Fontana di Trevi</h3>
<p>La fuente barroca más famosa del mundo, protagonista de "La Dolce Vita". Está siempre llena de gente, así que ve al amanecer o pasada la medianoche si quieres una foto sin multitudes. La tradición dice que lanzar una moneda con la mano derecha por encima del hombro izquierdo garantiza volver a Roma.</p>

<h3>Panteón de Agripa</h3>
<p>Uno de los edificios mejor conservados de toda la Antigüedad, con casi 2.000 años y una cúpula de hormigón sin armar que sigue siendo la más grande del mundo en su categoría. Ver el óculo central iluminando el interior según cambia la luz del día es una de las experiencias más especiales de Roma. Entrada: 5€, reserva recomendada aunque las colas suelen ser cortas.</p>

<h3>Piazza Navona y el centro histórico</h3>
<p>Una de las plazas más bonitas de Europa, construida sobre un antiguo estadio romano, con la Fontana dei Quattro Fiumi de Bernini como pieza central. Alrededor, el centro histórico —Campo de' Fiori (mercado por la mañana, bares por la noche), el barrio judío y sus restaurantes tradicionales— es la mejor zona para perderse sin rumbo.</p>

<h3>Trastevere</h3>
<p>El barrio con más ambiente de Roma: calles adoquinadas, fachadas de colores, hiedra colgando de los balcones y la mejor concentración de restaurantes auténticos de la ciudad. De día es tranquilo y fotogénico; de noche se llena de vida con sus bares y trattorias. La Basílica de Santa Maria in Trastevere, con sus mosaicos dorados del siglo XII, merece una parada.</p>

<h3>La colina del Pincio y Villa Borghese</h3>
<p>Las mejores vistas panorámicas de Roma, completamente gratuitas, sin necesidad de reservar entrada a ningún museo. Villa Borghese es el gran pulmón verde de la ciudad —perfecto para un paseo tranquilo o alquilar una bicicleta— y alberga la Galleria Borghese, con obras de Bernini y Caravaggio (reserva obligatoria, aforo limitado).</p>

<h2>Itinerario orientativo de 3 días</h2>
<p><strong>Día 1 — Roma antigua:</strong> Coliseo, Foro Romano y Palatino por la mañana; Fontana di Trevi y Piazza di Spagna al atardecer.<br>
<strong>Día 2 — Vaticano y Trastevere:</strong> Museos Vaticanos y Capilla Sixtina toda la mañana; cruzar el Tíber y comer/cenar en Trastevere.<br>
<strong>Día 3 — Centro histórico:</strong> Panteón, Piazza Navona, Campo de' Fiori y el barrio judío; atardecer desde el Pincio.</p>
<p>Con un cuarto día, añade Villa Borghese, el Trastevere de noche con más calma, o una excursión a Ostia Antica, las ruinas del puerto romano, mucho menos masificadas que el centro.</p>

<h2>Cómo moverse por Roma</h2>
<p>El centro histórico se recorre mejor a pie: la mayoría de los monumentos principales están a 20-30 minutos andando entre sí. El metro tiene solo dos líneas (A y B) y no llega a muchos puntos turísticos del centro por las excavaciones arqueológicas que complican nuevas líneas. Los autobuses cubren mejor el centro pero van lentos por el tráfico. Desde el aeropuerto de Fiumicino, el taxi tiene tarifa fija de 48€ al centro; el tren Leonardo Express llega a Termini en 32 minutos por 14€.</p>

<h2>Gastronomía romana: lo que tienes que comer</h2>

<h3>Los cuatro platos de pasta romanos</h3>
<p>Carbonara (huevo, guanciale, pecorino, pimienta —nunca nata—), cacio e pepe (pecorino y pimienta negra), amatriciana (guanciale, tomate, pecorino) y gricia (la "carbonara sin huevo"). Un buen plato en una trattoria de barrio cuesta 10-14€; huye de los sitios con menú turístico plastificado junto a los monumentos.</p>

<h3>Supplì y pizza al taglio</h3>
<p>El supplì —croqueta de arroz rellena de mozzarella y salsa de tomate— es la comida callejera romana por excelencia (1,50-2,50€). La pizza al taglio, vendida por peso en cualquier panadería, es la mejor opción para comer rápido y barato entre visitas.</p>

<h3>Gelato artesanal</h3>
<p>Busca heladerías que digan "gelato artesanale" o "produzione propria" —si el pistacho es de un verde eléctrico, no es real—. Los colores apagados y naturales son la señal de calidad.</p>

<h2>Presupuesto orientativo</h2>
<p>Vuelo desde España: 40-150€ ida y vuelta según temporada y antelación. Alojamiento en zona céntrica: 90-160€/noche. Manutención comiendo en trattorias de barrio: 30-45€/persona/día. Entradas principales (Coliseo, Vaticano, Panteón): unos 40-50€/persona en total. Un fin de semana largo de 3-4 días puede salir por 400-700€ por persona según la época del año.</p>

<h2>Cuándo ir a Roma</h2>
<ul>
<li><strong>Primavera (abril-mayo) y otoño (septiembre-octubre):</strong> temperaturas ideales (18-25°C) y menos aglomeración que en verano. La mejor época para visitar.</li>
<li><strong>Verano (julio-agosto):</strong> calor intenso (35°C+ no es raro) y máxima afluencia turística. Si vas en estas fechas, empieza a visitar monumentos a primera hora.</li>
<li><strong>Invierno:</strong> Roma sin turistas de masas, precios de vuelos y hoteles más bajos, aunque algunos días de lluvia. La Navidad con las luces del Vaticano tiene su encanto especial.</li>
</ul>
"""

ROMA_GC = gc(
    "Roma sin pagar de más",
    [
        "Reserva Coliseo y Museos Vaticanos online con semanas de antelación — no solo ahorras horas de cola, también evitas que se agoten las franjas horarias en temporada alta.",
        "El Panteón y la Basílica de San Pedro son gratuitos (subir a la cúpula del Panteón no es posible, pero la de San Pedro cuesta solo 10€ y merece la pena).",
        "Las mejores vistas de Roma —desde el Pincio— no cuestan nada. No hace falta pagar entrada a ningún mirador de pago.",
        "Come dos o tres calles alejado de los grandes monumentos: los precios bajan a la mitad y la comida suele ser mejor.",
        "El tren Leonardo Express (14€) desde Fiumicino es más barato que el taxi (48€) y tarda prácticamente lo mismo en hora punta.",
        "Los domingos, el primer domingo de cada mes, muchos museos estatales (incluidos parte de los Foros) tienen entrada gratuita — pero espera muchísima más gente.",
    ]
)

ROMA_CONTENT = ROMA + ROMA_GC + _ESIM_SEGURO


# ─── ISLAS GRIEGAS ───────────────────────────────────────────────────────────

GRECIA = """<p>Grecia es de esos destinos que superan todas las expectativas: el azul imposible del mar Egeo, pueblos blancos colgados sobre acantilados volcánicos, templos que llevan en pie más de 2.500 años y una gastronomía mediterránea que convierte cada comida en un pequeño ritual. Esta guía cubre Atenas y las islas más visitadas, con consejos reales de presupuesto y logística de ferris para no perder días de viaje en desplazamientos.</p>

<h2>Atenas: la cuna de la civilización occidental</h2>
<p>La capital griega suele tratarse como una simple escala hacia las islas, pero merece al menos dos días completos. La <strong>Acrópolis</strong> y el Partenón siguen siendo el imprescindible absoluto —resérvalo a primera hora de la mañana (abre a las 8h), antes de que lleguen los grupos y el calor apriete—. El <strong>Museo de la Acrópolis</strong>, a los pies de la colina, presenta las piezas originales con una museografía moderna y merece 2 horas. El barrio de <strong>Monastiraki</strong>, con su mercadillo de antigüedades y sus tabernas, y <strong>Plaka</strong>, el casco antiguo de calles empedradas a los pies de la Acrópolis, son la mejor zona para perderse caminando. El <strong>Museo Nacional Arqueológico</strong> tiene la colección de arte griego antiguo más importante del mundo —la máscara de oro de Agamenón, las esculturas cicládicas— y necesita fácilmente 3 horas.</p>

<h2>Santorini: el icono absoluto de Grecia</h2>
<p><strong>Oia</strong>, con sus cúpulas azules y casas blancas encaramadas al borde del acantilado volcánico, es la imagen más reconocible de toda Grecia. Su puesta de sol es célebre en el mundo entero —llega con al menos una hora de antelación si quieres hueco entre la multitud, o busca uno de los miradores alternativos a las afueras del pueblo, mucho menos concurridos y casi igual de espectaculares—. <strong>Fira</strong>, la capital de la isla, es más animada, comercial y con más oferta de restaurantes y vida nocturna. Las playas de arena volcánica negra y roja (<strong>Perissa, Kamari, Red Beach</strong>) son un paisaje único que no encontrarás en ningún otro destino mediterráneo. Merece la pena reservar al menos una excursión en barco alrededor de la caldera volcánica, con parada para bañarse en aguas termales naturales.</p>

<h2>Mykonos: la isla más cosmopolita</h2>
<p>Mykonos es la isla de moda de Grecia: vida nocturna internacional, playas con chiringuitos de diseño (Paradise, Super Paradise, Psarou) y el pueblo más fotogénico del archipiélago, con <strong>Little Venice</strong> —casas con balcones de madera suspendidos sobre el mar— y los icónicos <strong>molinos de viento</strong> como telón de fondo para el atardecer. Es también la isla más cara de Grecia en temporada alta; junio y septiembre ofrecen el mismo encanto con precios bastante más razonables y menos masificación.</p>

<h2>Otras islas que merece la pena conocer</h2>
<h3>Creta</h3>
<p>La isla más grande de Grecia, con entidad propia casi de país aparte. El palacio minoico de Knossos (cuna de la civilización minoica, 3.500 años de antigüedad), playas de postal como Elafonisi y Balos, y la garganta de Samaria, uno de los desfiladeros más largos de Europa para hacer trekking. Suficiente entidad para dedicarle un viaje entero.</p>
<h3>Rodas</h3>
<p>La ciudad medieval mejor conservada de Grecia, declarada Patrimonio de la Humanidad, con las murallas de los Caballeros de San Juan casi intactas. Mezcla historia bizantina, de los Cruzados y otomana en un casco antiguo que se recorre completo en un día.</p>
<h3>Corfú</h3>
<p>La isla más verde y exuberante del Jónico, con una arquitectura marcadamente veneciana en su capital —Corfú fue posesión de Venecia durante 400 años—. Playas más tranquilas que las Cícladas y un ambiente menos turístico masivo.</p>
<h3>Naxos y Paros</h3>
<p>Las Cícladas auténticas, sin la masificación de Santorini o Mykonos pero con la misma esencia: pueblos blancos, playas espectaculares y precios notablemente más bajos. Naxos tiene montañas y pueblos de interior poco visitados; Paros combina playa y vida nocturna moderada.</p>

<h2>Cómo moverse entre islas</h2>
<p>El <strong>ferry</strong> es el medio de transporte principal entre islas. Blue Star Ferries y SeaJets cubren las rutas más habituales desde el puerto de Pireo (Atenas). En julio y agosto conviene reservar con semanas de antelación —los barcos se llenan y los precios suben cuanto más te acercas a la fecha—. Los <strong>vuelos internos</strong> de Aegean Airlines u Olympic Air son mucho más rápidos (30-45 min frente a varias horas de barco) pero también más caros; merece la pena para trayectos largos como Atenas-Creta o Atenas-Rodas si el presupuesto lo permite.</p>

<h2>Gastronomía griega imprescindible</h2>
<p>El souvlaki (brochetas de carne a la parrilla en pan de pita) es la comida callejera por excelencia, desde 3-4€. La ensalada griega (horiatiki), con tomate, pepino, cebolla, aceitunas kalamata y queso feta, es un clásico en cualquier taberna. El moussaka (berenjena, carne picada y bechamel gratinada) y el souvlaki de cordero son los platos de cuchara más contundentes. Para acabar, baklava con miel y frutos secos, o loukoumades (buñuelos griegos con miel y canela). El vino local, especialmente el blanco de Santorini elaborado con la uva assyrtiko cultivada en suelo volcánico, es una de las mejores relaciones calidad-precio de Europa.</p>

<h2>Cuándo ir a Grecia</h2>
<p><strong>Mayo-junio y septiembre-octubre</strong> son los meses ideales: temperaturas de 25-30°C, mucha menos aglomeración que en pleno verano y precios de vuelos y alojamiento sensiblemente más bajos. <strong>Julio y agosto</strong> son temporada alta absoluta, con calor extremo en Atenas (35-40°C) y las islas más famosas completamente llenas —si solo puedes viajar en estas fechas, prioriza islas menos masificadas como Naxos o Paros—. El invierno prácticamente cierra el turismo insular: muchos hoteles y restaurantes de las islas pequeñas cierran de noviembre a abril.</p>

<h2>Presupuesto orientativo</h2>
<p>Grecia continental (Atenas) es muy asequible: comer bien en una taberna local cuesta 10-15€ y el alojamiento ronda 50-80€/noche. En las islas más famosas —Santorini y Mykonos— el presupuesto se multiplica por 2-3, tanto en alojamiento (100-250€/noche en temporada alta) como en restaurantes. Un truco real de ahorro: las islas menos conocidas (Naxos, Paros, Milos) ofrecen paisajes casi idénticos a Santorini por la mitad de precio. Un viaje de 10 días combinando Atenas + 2 islas puede salir por 700-1.200€ por persona según la temporada y el número de islas famosas que incluyas.</p>
"""

GRECIA_GC = gc(
    "Grecia sin pagar de más",
    [
        "Visita la Acrópolis a primera hora (abre a las 8h) — no solo evitas el calor y las colas, también consigues las mejores fotos sin masas de gente detrás.",
        "Cambia Santorini o Mykonos por Naxos o Paros para el mismo paisaje de Cícladas a la mitad de precio en alojamiento y restaurantes.",
        "Reserva los ferris de julio-agosto con semanas de antelación — el precio sube y las plazas se agotan cuanto más te acercas a la fecha de viaje.",
        "El vino blanco de Santorini (uva assyrtiko) es de los mejores de Europa a precio de supermercado — cómpralo directamente en una bodega de la isla, mucho más barato que en el restaurante.",
        "Viaja en mayo-junio o septiembre-octubre: mismo buen tiempo que en agosto, la mitad de turistas y precios de vuelo y hotel notablemente más bajos.",
        "En Atenas, come en Monastiraki o Psiri en vez de las tabernas justo debajo de la Acrópolis — el mismo souvlaki cuesta la mitad a dos calles de distancia.",
    ]
)

GRECIA_CONTENT = GRECIA + GRECIA_GC + _ESIM_SEGURO


# ─── EJECUCIÓN ────────────────────────────────────────────────────────────────

UPDATES = [
    {
        "slug": "que-ver-en-roma-tres-dias",
        "title": "Roma: qué ver en la Ciudad Eterna — guía completa",
        "excerpt": "Coliseo, Vaticano, Panteón, Trastevere y Fontana di Trevi. Itinerario de 3 días, gastronomía romana y todos los trucos para evitar las colas.",
        "content": ROMA_CONTENT,
        "image_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "category": "europa",
    },
    {
        "slug": "que-ver-en-grecia-atenas-santorini",
        "title": "Grecia: Atenas, Santorini, Mykonos y las islas griegas — guía completa",
        "excerpt": "Acrópolis, Oia, Little Venice, Creta y Rodas. Cómo moverse en ferry entre islas, presupuesto real y las Cícladas alternativas más baratas que Santorini.",
        "content": GRECIA_CONTENT,
        "image_url": "https://images.unsplash.com/photo-1555993539-1732b0258235?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "category": "internacional",
    },
]


def run():
    conn = psycopg2.connect(config.DATABASE_URL)
    cur = conn.cursor()

    for p in UPDATES:
        cur.execute("""
            UPDATE posts SET title=%s, excerpt=%s, content=%s, image_url=%s, category=%s
            WHERE slug=%s
        """, (p["title"], p["excerpt"], p["content"], p["image_url"], p["category"], p["slug"]))
        print(f"  UPDATE: {p['slug']} ({len(p['content'].split())} palabras aprox.)")

    conn.commit()
    cur.close()
    conn.close()
    print(f"\nListo — {len(UPDATES)} guías actualizadas.")

if __name__ == "__main__":
    run()
