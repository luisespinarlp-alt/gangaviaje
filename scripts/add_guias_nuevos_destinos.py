"""
Añade guías completas de nuevos destinos: Toledo, Salamanca, Asturias, Croacia, Sicilia, Georgia.
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


# ─── TOLEDO ──────────────────────────────────────────────────────────────────

TOLEDO = """<p>Toledo es posiblemente la ciudad más impresionante de España. Declarada Patrimonio de la Humanidad por la UNESCO, esta ciudad amurallada sobre un cerro rodeado por el río Tajo conserva intactos tres milenios de historia: romana, visigótica, árabe, judía y cristiana, todo mezclado en apenas dos kilómetros cuadrados. A 70 kilómetros de Madrid, es el destino perfecto para una escapada de un día o un fin de semana completo.</p>

<h2>Qué ver en Toledo: los imprescindibles</h2>

<h3>Catedral de Toledo</h3>
<p>Una de las catedrales góticas más grandes e impresionantes de España. La construcción duró 267 años (1226-1493) y el resultado es abrumador: 88 metros de largo, vidrieras medievales del siglo XV, una sacristía con obras de El Greco, Goya, Velázquez y Tiziano que rivaliza con cualquier museo europeo. La <strong>Transparente</strong>, el retablo barroco del altar mayor, es una de las obras arquitectónicas más impactantes que verás en tu vida. Entrada: 10 euros adultos. Consejo: llega en cuanto abren (10h en temporada alta) para evitar colas.</p>

<h3>Alcázar de Toledo</h3>
<p>La imponente fortaleza cuadrada que domina el perfil de Toledo desde cualquier punto. Fue palacio romano, castillo árabe, residencia de Carlos I y escenario de uno de los episodios más dramáticos de la Guerra Civil española. Hoy alberga el Museo del Ejército, con colecciones históricas extensísimas. Entrada: 5 euros. Los domingos es gratuito.</p>

<h3>El Greco en Toledo</h3>
<p>Toledo es la ciudad del Greco. El pintor cretense vivió aquí casi 40 años y dejó obras repartidas por toda la ciudad. El museo Casa del Greco (5 euros) reconstruye su vida y obra. Pero la joya absoluta está en la Iglesia de Santo Tomé: <em>El Entierro del Señor de Orgaz</em>, considerado el mejor cuadro del Greco y uno de los grandes de la pintura española. Entrada independiente: 3 euros. Vale cada céntimo.</p>

<h3>El barrio judío y la Sinagoga del Tránsito</h3>
<p>Toledo tuvo durante siglos la comunidad judía más importante de la Península Ibérica. El antiguo barrio judío (la Judería) conserva sus callejuelas tortuosas originales. La <strong>Sinagoga del Tránsito</strong> (siglo XIV) es espectacular: techos de madera de cedro con decoración mudéjar, inscripciones en hebreo y árabe, paredes de yeso calado. Hoy alberga el Museo Sefardí. Entrada: 3 euros.</p>

<h3>La Sinagoga de Santa María la Blanca</h3>
<p>La sinagoga más antigua de Europa que se conserva en pie (siglo XII). Su interior, con cinco naves separadas por columnas con capiteles de piñas, es único en el mundo — un edificio construido por arquitectos árabes como sinagoga judía que acabó siendo iglesia cristiana. Imagen fascinante de la convivencia (y la complejidad) de las tres culturas en Toledo.</p>

<h3>La Mezquita del Cristo de la Luz</h3>
<p>Pequeña pero preciosa mezquita árabe del año 999, una de las pocas de toda España que conserva casi intacta la estructura original. Es casi un secreto a plena vista: mucha gente pasa por delante sin entrar. Entrada: 2,80 euros.</p>

<h3>Las murallas y el mirador del Valle</h3>
<p>Para la postal más famosa de Toledo — la ciudad reflejada en el Tajo — hay que cruzar el río y subir al <strong>mirador del Valle</strong>, en la margen izquierda. Al atardecer, con la luz dorando las torres de la catedral y el Alcázar, es sencillamente espectacular. Y gratis.</p>

<h2>Cómo moverse por Toledo</h2>
<p>El casco histórico es compacto pero con muchas cuestas. La mayor parte se recorre a pie. Hay un <strong>escalator mecánico gratuito</strong> que sube desde la Puerta de Alfonso VI hasta la parte alta de la ciudad — muy útil si llegas desde el aparcamiento o la estación de Renfe. Para visitar el mirador del Valle sin dar la vuelta completa, puedes tomar un taxi o usar el tren turístico (zocotren) que recorre los principales puntos de interés.</p>

<h2>Gastronomía toledana: lo que tienes que comer y beber</h2>

<h3>Mazapán</h3>
<p>El mazapán de Toledo es Denominación de Origen y completamente distinto al que conoces. Elaborado solo con almendra y azúcar (sin colorantes ni conservantes), se vende en las confiterías del casco histórico desde el siglo XVI. La Confitería Santo Tomé y Mazapanes Montero son las más auténticas. Cómete uno caliente recién hecho si puedes.</p>

<h3>Perdiz a la toledana</h3>
<p>El plato estrella de la gastronomía local. Perdiz guisada con cebolla, laurel, pimienta y vino blanco hasta que la carne se deshace. En los restaurantes del centro vale 15-22 euros la ración. Muy contundente.</p>

<h3>Carcamusas</h3>
<p>Tapa típica toledana: carne de cerdo troceada con guisantes, tomate y especias. Se sirve en cazuela de barro y es el acompañamiento perfecto para un vino de la tierra. En los bares del mercado municipal la encontrarás por 3-5 euros.</p>

<h3>Vinos de la Denominación de Origen Méntrida y La Mancha</h3>
<p>Toledo provincia produce vinos de calidad creciente. Los tintos de Méntrida (garnacha sobre todo) son potentes y muy asequibles. En los bares del centro, una copa de vino local ronda 1,50-2 euros.</p>

<h2>Cómo llegar a Toledo</h2>
<p><strong>Tren desde Madrid:</strong> la opción más cómoda. El AVE lanzadera desde Madrid Atocha llega en <strong>33 minutos</strong> a la estación de Toledo. Desde 7 euros ida en oferta (normalmente 13-18 euros). Hay varios trenes cada hora. La estación está en la parte baja — desde ahí tomas el bus 5 o un taxi hasta el casco histórico.</p>
<p><strong>Bus desde Madrid:</strong> ALSA desde el intercambiador de Méndez Álvaro. Tarda 1h15-1h30 y es más barato (5-6 euros), pero el AVE es tan barato y rápido que merece la pena.</p>
<p><strong>En coche:</strong> la A-42 desde Madrid, 70 km, sin peaje, 55 minutos. El problema: aparcar en el casco histórico es difícil y caro. Hay aparcamientos en la Puerta de Bisagra (llegada al casco) o en la zona de la estación.</p>

<h2>Cuándo ir a Toledo</h2>
<ul>
<li><strong>Corpus Christi (mayo-junio):</strong> la procesión más espectacular de España, con las calles alfombradas de flores y el Alcázar iluminado. El ambiente es único. Muy concurrido.</li>
<li><strong>Semana de Turismo (noviembre):</strong> muchos monumentos gratis o con descuento. Sin las colas del verano.</li>
<li><strong>Otoño e invierno:</strong> Toledo sin turistas es otra ciudad. Los domingos el Alcázar es gratuito. El mazapán de Navidad es el mejor del año.</li>
<li><strong>Evitar:</strong> agosto al mediodía (calor extremo y máxima saturación turística). Si vas en verano, madruga o ve al atardecer.</li>
</ul>

<h2>¿Excursión de un día o fin de semana?</h2>
<p>En un día puedes ver los imprescindibles (Catedral, El Entierro del Señor de Orgaz, Sinagoga del Tránsito, murallas, mirador del Valle). Pero Toledo merece una noche: sin los turistas de día, la ciudad cambia completamente. Los callejones iluminados por las farolas, la catedral de noche, cenar en una tasca tranquila... es una experiencia diferente."""

TOLEDO_GC = gc(
    "Toledo sin pagar de más",
    [
        "El Alcázar (Museo del Ejército) es gratuito los domingos — planifica la visita ese día y ahorra 5 euros por persona.",
        "El AVE Madrid-Toledo cuesta desde 7 euros en oferta (app Renfe, tarifas promo). Compra siempre con antelación — el precio sube mucho sin planificación.",
        "Visita la catedral justo al abrir (10h) — evitas las colas de las 11h y tienes el interior casi para ti. Merece madrugar.",
        "El mirador del Valle es el mejor mirador de Toledo y es completamente gratuito. Está en la orilla opuesta al río Tajo — cruza el puente de San Martín.",
        "Los escalators mecánicos que suben desde el río hasta el casco histórico son gratuitos — no pagues taxi para subir la cuesta.",
        "Come en el mercado municipal de Toledo: tapas y raciones mucho más baratas que en los restaurantes turísticos del centro. Las carcamusas caseras desde 3 euros.",
        "Para el mazapán, compra en las tiendas de barrio alejadas de la catedral — los precios bajan un 20-30 por ciento respecto a las tiendas de la plaza principal.",
    ]
)

TOLEDO_CONTENT = TOLEDO + TOLEDO_GC


# ─── SALAMANCA ───────────────────────────────────────────────────────────────

SALAMANCA = """<p>Salamanca es la ciudad universitaria más antigua de España y una de las más bellas de Europa. Sus edificios de piedra arenisca dorada le dan ese color cálido y único que le valió el apodo de "La Dorada". La Plaza Mayor — elegida repetidamente la más bonita de España — la Universidad más antigua de la Península, las catedrales románica y gótica unidas y una vida nocturna alimentada por 30.000 estudiantes hacen de Salamanca un destino que enamora a casi todo el mundo que la visita.</p>

<h2>Qué ver en Salamanca</h2>

<h3>La Plaza Mayor</h3>
<p>Es simplemente la plaza más bonita de España. Diseñada por Alberto de Churriguera en 1755, el conjunto de arcadas barrocas de piedra dorada forma un rectángulo perfecto que envuelve al visitante. A cualquier hora del día tiene su encanto, pero al atardecer — cuando la piedra se enciende con la luz naranja — la Plaza Mayor de Salamanca es uno de los rincones más hermosos de Europa. Y es completamente gratuita. Los retratos en los medallones de las arcadas incluyen desde reyes medievales hasta Franco — el único dictador en una plaza mayor española, controvertido hasta hoy.</p>

<h3>Universidad de Salamanca</h3>
<p>Fundada en 1218, es la universidad en funcionamiento más antigua de España y una de las más antiguas del mundo. La fachada plateresca es un prodigio de ornamentación renacentista — la tradición dice que hay una rana escondida entre los relieves y encontrarla trae suerte en los exámenes. El aula donde dio clase Fray Luis de León está conservada como en el siglo XVI. Entrada: 10 euros (incluye museo, aula histórica y biblioteca antigua).</p>

<h3>Las dos catedrales</h3>
<p>Salamanca tiene dos catedrales unidas que se pueden visitar juntas. La <strong>Catedral Vieja</strong> (siglo XII) es románica con influencias bizantinas. La <strong>Catedral Nueva</strong> (siglo XVI-XVIII) es gótica tardía mezclada con churrigueresco barroco. Lo más sorprendente: en 1992 un restaurador esculpió en la fachada nueva un astronauta y un dragón comiendo un helado, que se han convertido en los detalles más buscados por los visitantes. Entrada conjunta: 6 euros.</p>

<h3>Casa de las Conchas</h3>
<p>El edificio más fotografiado de Salamanca: una mansión del siglo XV cubierta con 300 conchas de vieira de piedra (símbolo del Camino de Santiago y de la orden de Santiago). Hoy funciona como biblioteca pública y la entrada es gratuita. El patio interior y las ventanas góticas de arriba son preciosas.</p>

<h3>Convento de San Esteban</h3>
<p>La fachada plateresca del convento dominico es uno de los mejores ejemplos del plateresco español — el estilo arquitectónico que parece joyería de piedra. Colón presentó aquí sus planes para el viaje a América ante los dominicos. El retablo interior de Churriguera es apabullante.</p>

<h3>Museo Art Nouveau y Art Déco — Casa Lis</h3>
<p>Un museo completamente diferente a todo lo que esperarías en Salamanca: joyería, porcelana, vidrio y muñecas de los años 1890-1940, en un edificio modernista junto al río Tormes. La colección de vidrio Lalique y las muñecas alemanas y francesas son extraordinarias. Entrada: 5 euros.</p>

<h2>La vida universitaria: por qué Salamanca es especial</h2>
<p>El 15 por ciento de la población de Salamanca son estudiantes universitarios. Eso se nota: hay más de 200 bares en el centro histórico, el ambiente nocturno es increíble incluso entre semana, y la ciudad tiene una energía joven y cosmopolita que contrasta con su aspecto monumental. Si vas entre octubre y mayo (curso académico), vive la Plaza Mayor de noche con los estudiantes. En julio y agosto la ciudad se llena de turistas pero pierde algo de esa alma estudiantil.</p>

<h2>Gastronomía salmantina</h2>

<h3>Jamón ibérico de Guijuelo</h3>
<p>La denominación de origen Guijuelo está a 50 km de Salamanca y produce uno de los mejores jamones ibéricos de bellota de España. En los bares del mercado del barrio del oeste (la zona universitaria) puedes comer una tapa de jamón ibérico auténtico por 3-5 euros. La diferencia con el jamón serrano normal es incomparable.</p>

<h3>Farinato</h3>
<p>Embutido típico salmantino de harina de trigo, manteca de cerdo, cebolla y especias. Se come frito, como tapa o con huevos revueltos. Tiene un sabor único que no encontrarás en ningún otro lugar de España.</p>

<h3>Hornazo</h3>
<p>Una especie de empanada rellena de chorizo, lomo y huevo duro. El hornazo de Salamanca se come especialmente en el Lunes de Aguas (el lunes después de Pascua), cuando la tradición obliga a comerlo junto al río. Pero los hay frescos todo el año en las pastelerías del centro.</p>

<h2>Cómo llegar a Salamanca</h2>
<p><strong>Tren desde Madrid:</strong> Alvia desde Madrid Chamartín en 1h30-2h. Precio: 15-30 euros según tarifa. Hay varios trenes al día.</p>
<p><strong>Bus desde Madrid:</strong> ALSA desde Moncloa, 2h30, 14-20 euros. Precio económico pero más lento.</p>
<p><strong>En coche desde Madrid:</strong> A-50 por Ávila o A-6 por Segovia, 200 km, aproximadamente 2 horas. Sin peaje la mayor parte del recorrido.</p>

<h2>Cuándo ir y cuánto tiempo necesitas</h2>
<p>Salamanca merece un fin de semana completo, aunque los imprescindibles se pueden ver en un día intenso. <strong>La mejor época</strong> es de octubre a junio, con la universidad en pleno funcionamiento. En verano el turismo es alto pero hay buenos precios en alojamiento al haber menos estudiantes. La Semana Santa en Salamanca es espectacular — procesiones nocturnas con la catedral iluminada."""

SALAMANCA_GC = gc(
    "Salamanca: la ciudad dorada sin vaciar la cartera",
    [
        "La Plaza Mayor es gratis a cualquier hora. Para la mejor foto sin turistas, ve antes de las 9h o después de las 21h.",
        "Los menús del día en los bares de la zona universitaria (Gran Vía, calle Bordadores) cuestan 9-12 euros con bebida — mucho más barato que los del centro histórico turístico.",
        "El Alcázar y la Catedral Nueva son gratuitos los domingos por la mañana hasta las 11h. El resto de la semana, la entrada conjunta es 6 euros.",
        "El tren Alvia Madrid-Salamanca tiene tarifas promo desde 15 euros. Reserva con antelación en la app de Renfe.",
        "Alójate en los alrededores de la Plaza del Liceo o en el barrio del oeste (zona universitaria) — hoteles 20-30 euros más baratos que los del casco histórico, a 5 minutos caminando.",
        "El Museo Casa Lis (Art Nouveau) cuesta 5 euros y es uno de los más singulares de España — vale cada céntimo y no tiene colas.",
        "Para el jamón ibérico auténtico de Guijuelo, ve al mercado del Barrio del Oeste o a las charcuterías de la calle Toro, no a los restaurantes del centro turístico.",
    ]
)

SALAMANCA_CONTENT = SALAMANCA + SALAMANCA_GC


# ─── ASTURIAS ────────────────────────────────────────────────────────────────

ASTURIAS = """<p>Asturias es la España que no se parece a España. Mientras el resto del país se quema bajo el sol en agosto, Asturias mantiene un verde intenso, montañas que llegan hasta el mar, playas salvajes con olas de surf, aldeas de piedra que parecen sacadas de otro siglo y una gastronomía brutal basada en la sidra y el marisco más fresco de la cornisa cantábrica. Es uno de los destinos más infrautilizados del turismo español y eso es precisamente su mayor virtud.</p>

<h2>Qué ver en Asturias: la guía completa</h2>

<h2>Oviedo: la capital</h2>
<p>Una ciudad media perfecta para caminar: compacta, con un centro histórico muy bien conservado, infinidad de sidrería y restaurantes, y una de las mejores colecciones de arte prerrománico del mundo. La <strong>Catedral de San Salvador</strong> (gótica, con la famosa Cámara Santa donde se guardan las reliquias más veneradas del norte de España, incluyendo el Sudario de Oviedo) y los <strong>monumentos prerrománicos asturianos</strong> (Santa María del Naranco, San Miguel de Lillo) — Patrimonio UNESCO — son imprescindibles. La escultura de La Regenta paseando por la calle Uría te hará parar a hacerte la foto inevitable.</p>

<h2>Gijón: la ciudad más cosmopolita</h2>
<p>Puerto de mar, playa de arena larga, terrazas, sidrería y una vida cultural intensa. El casco antiguo de Cimadevilla, sobre el promontorio que se adentra en el mar, tiene un encanto especial. La <strong>playa de San Lorenzo</strong> (tres kilómetros de arena en pleno centro urbano) y el <strong>cerro de Santa Catalina</strong> (con el famoso Elogio del Horizonte de Chillida) son los dos iconos fotográficos de la ciudad. Gijón tiene la mejor oferta de sidrerías de toda Asturias.</p>

<h2>Los Picos de Europa</h2>
<p>El primer parque nacional de España (1918) y uno de los más espectaculares de Europa. Tres macizos kársticos de caliza que se elevan hasta 2.650 metros a apenas 20 kilómetros del mar. Los imprescindibles:</p>
<ul>
<li><strong>Covadonga y los Lagos:</strong> el santuario donde comenzó la Reconquista española y, a 12 km por una carretera de montaña vertiginosa, los Lagos de Enol y La Ercina. En julio-agosto el acceso en coche está prohibido (hay bus lanzadera obligatorio desde Covadonga, 10 euros). La vista de los lagos con los picos nevados al fondo es una de las imágenes más impresionantes de toda España.</li>
<li><strong>Ruta del Cares:</strong> el trekking más famoso de Asturias. Un sendero de 12 km (solo ida, o 24 ida y vuelta) excavado en la roca sobre el desfiladero del río Cares. Sin dificultad técnica, pero hay que madrugar para hacerlo sin las masas de agosto. Punto de partida: Poncebos (por el lado asturiano) o Caín (por el lado leonés).</li>
<li><strong>Funicular de Bulnes:</strong> el único funicular de montaña de España que conecta Poncebos con el pueblo de Bulnes (inaccesible por carretera). Sube 400 metros de desnivel en 7 minutos. El pueblo, con una docena de casas de piedra, parece detenido en el siglo XIX. Billete: 18 euros ida y vuelta.</li>
<li><strong>Naranjo de Bulnes (Picu Urriellu):</strong> la montaña más icónica de los Picos. Su pared vertical de 600 metros es el sueño de los alpinistas. Desde Sotres o desde el mirador de Óscar se ve perfectamente sin necesidad de escalarla.</li>
</ul>

<h2>La costa asturiana: playas salvajes</h2>
<p>Asturias tiene más de 200 playas, casi ninguna masificada. Las más espectaculares:</p>
<ul>
<li><strong>Playa del Silencio (Cudillero):</strong> rodeada de acantilados, sin acceso por carretera hasta la orilla, una media luna de arena perfecta. Una de las playas más bonitas de España. Llega temprano.</li>
<li><strong>Playa de Torimbia (Llanes):</strong> nudista, entre acantilados, sin chiringuitos. Acceso solo a pie (15 minutos desde el aparcamiento). Preciosa.</li>
<li><strong>Playa de Gulpiyuri (Llanes):</strong> la playa más curiosa de España — interior, separada del mar por los acantilados, se llena y vacía con la marea a través de un túnel submarino. Solo 50 metros de arena en medio de los prados.</li>
<li><strong>Playa de Rodiles (Villaviciosa):</strong> la mejor playa de surf de Asturias. Olas perfectas en otoño e invierno, arena fina, 800 metros de largo.</li>
</ul>

<h2>Los pueblos más bonitos de Asturias</h2>
<ul>
<li><strong>Cudillero:</strong> el pueblo pesquero más bonito del Cantábrico. Las casas de colores se amontonan en anfiteatro sobre el puerto. Ir al atardecer para ver los barcos pesqueros volver y cenar pescado fresco.</li>
<li><strong>Llanes:</strong> la capital de la costa oriental asturiana. Murallas medievales conservadas, cubos de la memoria (cubos de hormigón pintados por artistas contemporáneos sobre el paseo marítimo), sidrerías y acceso a las mejores playas del oriente.</li>
<li><strong>Lastres:</strong> otro puerto pesquero precioso, conocido por las escenas de la serie Doctor Mateo. Las casas blancas con balcones floridos sobre el mar y el faro son la imagen más pintoresca del oriente asturiano.</li>
<li><strong>Taramundi:</strong> en el occidente profundo, famoso por su artesanía en cuchillería (los navajas artesanales de Taramundi son únicos en el mundo), por el turismo rural y por su gastronomía autóctona con ingredientes de huerta.</li>
</ul>

<h2>La sidra asturiana: la experiencia imprescindible</h2>
<p>La sidra asturiana no es como ninguna otra sidra del mundo. Se sirve "escanciada" — desde una botella alzada a más de un metro de altura hasta el vaso a la altura de la cintura — para oxigenarla y crear la espuma característica. El ritual del escancio es tan importante como la bebida misma. La tradición dice que hay que beberla de un trago (el "culín") dejando una pequeña cantidad en el fondo para lavar el vaso. Una botella de sidra natural: 2-4 euros.</p>

<h2>Gastronomía asturiana</h2>
<ul>
<li><strong>Fabada asturiana:</strong> el plato nacional. Fabes (alubias blancas grandes) con chorizo, morcilla y lacón (cerdo). Contundente, aromática, perfecta para un día de lluvia y montaña. Los botes de fabada de calidad para llevar a casa cuestan 4-8 euros.</li>
<li><strong>Marisco:</strong> la centolla, el erizo de mar, los percebes y las nécoras del Cantábrico son de una calidad excepcional. En los puertos pesqueros de Luarca, Cudillero o Llanes, el marisco del día cuesta la mitad que en Madrid.</li>
<li><strong>Queso Cabrales:</strong> el queso azul más intenso de España, elaborado en cuevas naturales de los Picos de Europa. El original tiene DOP y un sabor potentísimo. Cómpralo directamente en Arenas de Cabrales.</li>
<li><strong>Cachopo:</strong> no es un plato tradicional antiguo, pero se ha convertido en el símbolo de la gastronomía asturiana actual. Filetes de ternera empanados rellenos de jamón y queso, de tamaño descomunal. Un cachopo es suficiente para dos personas.</li>
</ul>

<h2>Cómo llegar a Asturias</h2>
<p><strong>Avión:</strong> el Aeropuerto de Asturias (OVD) está entre Oviedo y Gijón. Iberia, Ryanair y Vueling tienen vuelos desde Madrid y Barcelona. Precios desde 25-50 euros si reservas con antelación.</p>
<p><strong>Tren:</strong> el Alvia Madrid-Oviedo tarda unas 4,5 horas. Precio desde 35-50 euros en oferta. Sale de Madrid Chamartín.</p>
<p><strong>En coche desde Madrid:</strong> 480 km por la A-6 y luego A-66 (Ruta de la Plata). Unas 5 horas. Es la opción más flexible para visitar la costa y los Picos.</p>

<h2>Cuándo ir a Asturias</h2>
<ul>
<li><strong>Julio-agosto:</strong> la mejor época para playa. Tiempo más estable (aunque puede llover igualmente — es Asturias). Precios altos y Picos masificados.</li>
<li><strong>Mayo-junio y septiembre-octubre:</strong> la mejor relación calidad-precio. El verde está en su punto, hay menos turistas, los precios son más bajos y el tiempo suele ser bueno.</li>
<li><strong>Otoño (octubre-noviembre):</strong> colores increíbles en los bosques, sidra nueva recién salida del lagar, sin turistas. Llover sí va a llover.</li>
</ul>"""

ASTURIAS_GC = gc(
    "Asturias: verde y asequible si sabes cómo",
    [
        "Para la Ruta del Cares (el mejor trekking del norte), empieza desde Poncebos a las 8h de la mañana en agosto — a las 10h ya está lleno de gente y el calor aprieta.",
        "En julio-agosto, el acceso a los Lagos de Covadonga en coche está restringido. El bus lanzadera sale desde Covadonga y cuesta 10 euros — toma el bus de las 8h para ver los lagos sin masificación.",
        "Una botella de sidra natural en sidrería cuesta 3-5 euros. No te limites a 'pedir sidra' como turista — pide que te enseñen a escanciarla tú mismo.",
        "Para marisco fresco y barato, ve directamente a los puertos pesqueros: en Luarca o Cudillero el precio de las nécoras y centollas es la mitad que en los restaurantes del centro de Oviedo.",
        "Las casas rurales de la zona de los Picos (Arenas de Cabrales, Cangas de Onís) cuestan 60-100 euros la noche para toda la familia y tienen una calidad impresionante. Mucho mejor que los hoteles de Oviedo a ese precio.",
        "El Funicular de Bulnes (18 euros ida y vuelta) te lleva al pueblo más aislado de España en 7 minutos — si solo haces una cosa de pago en los Picos, que sea esta.",
        "Vuela a Asturias en temporada baja (noviembre, febrero, marzo) — Ryanair y Vueling tienen vuelos Madrid-Asturias desde 18-25 euros. El tiempo es lluvioso pero los Picos y los pueblos son igual de bonitos.",
    ]
)

ASTURIAS_CONTENT = ASTURIAS + ASTURIAS_GC


# ─── CROACIA / DUBROVNIK ──────────────────────────────────────────────────────

CROACIA = """<p>Croacia tiene el defecto de ser demasiado bonita. Dubrovnik, la "Perla del Adriático", es una de las ciudades medievales mejor conservadas del mundo. Split tiene el palacio romano más habitado del planeta. Las islas de Hvar, Brač y Vis tienen aguas de un azul turquesa que no parece mediterráneo. El país entero es un desfile de destinos espectaculares. El problema: todo el mundo lo sabe y en verano se nota. Esta guía te da lo mejor de Croacia sin caer en las trampas turísticas.</p>

<h2>Dubrovnik: la ciudad amurallada más bonita de Europa</h2>

<h3>Las murallas</h3>
<p>El paseo por las murallas de Dubrovnik es la experiencia más impresionante de la ciudad. Dos kilómetros de murallas medievales que rodean el casco histórico con vistas al mar Adriático por un lado y a los tejados naranjas de la ciudad por el otro. <strong>Precio: 35 euros</strong> (sí, es caro, pero merece la pena). Consejo crucial: ve muy temprano por la mañana (las 8h cuando abren) o al atardecer. En julio y agosto a las 11h la muralla es un horno humano insoportable.</p>

<h3>Stradun y el casco histórico</h3>
<p>La calle principal de Dubrovnik es una de las calles más elegantes de Europa: 300 metros de piedra pulida que brilla al sol, flanqueada por palacios y monumentos barrocos. El casco histórico en su conjunto fue declarado Patrimonio de la Humanidad. Recorrerlo es gratis — el problema son los cruceristas que llenan la Stradun de 10h a 17h. Madruga o quédate hasta tarde.</p>

<h3>Game of Thrones: la guía Dubrovnik real</h3>
<p>Si eres fan de Juego de Tronos, Dubrovnik es la peregrinación obligada. Casi todo el Desembarco del Rey se rodó aquí: Escalera de la Vergüenza (Escaleras Jesuitas, entrada libre), la Fortaleza Lovrijenac (Fort Alardyce), la Sala Roja (interior del Fuerte de San Juan, museo marítimo). Hay tours oficiales de GoT (20-30 euros) pero con un mapa descargable gratis puedes encontrar los localizaciones tú solo.</p>

<h2>Split: el palacio romano donde vive la gente</h2>
<p>El Palacio de Diocleciano (siglo IV) es el monumento romano mejor conservado fuera de Italia — y lo que lo hace único es que dentro viven 3.000 personas, hay bares, restaurantes, hoteles y tiendas. El centro histórico de Split no es un museo: es un barrio que respira. Pasea por el Peristilo (el patio central del palacio), visita la Catedral de San Duje (construida dentro del mausoleo del propio Diocleciano) y súbete a las murallas para ver el mar. Entrada al palacio: gratis. Museos interiores: 3-10 euros.</p>

<h2>Las islas croatas</h2>

<h3>Hvar — la más glamurosa</h3>
<p>Hvar es la isla más de moda de Croacia. Lavanda, viñedos, calas de agua cristalina, villas históricas y una escena de fiestas nocturnas de las más activas del Mediterráneo. El casco histórico de la ciudad de Hvar (con su plaza renacentista, el fuerte Španjola y el arsenal medieval) es precioso. El problema: en julio-agosto, los yates y los turistas hacen que los precios se disparen a niveles absurdos. Septiembre es el mejor mes para ir a Hvar.</p>

<h3>Brač — la playa de Zlatni Rat</h3>
<p>La playa más famosa de Croacia: Zlatni Rat (Cabo Dorado), una lengua de guijarros blancos que se adentra en el mar y cambia de forma con las corrientes. Realmente impresionante. La isla de Brač es más tranquila y barata que Hvar y tiene las mejores canteras de piedra caliza blanca (con la que se construyó el Palacio de la Casa Blanca en Washington).</p>

<h3>Vis — la joya sin masificar</h3>
<p>La isla más alejada de la costa y la que más tardó en abrirse al turismo (fue base militar hasta 1995). Hoy es la preferida de los viajeros que quieren la Croacia auténtica: pocas turistas, precios razonables, pueblo de pescadores de verdad, vino tinto Vis que es uno de los mejores del Adriático y la Cueva Azul (similar a la de Capri) que solo se puede visitar en barca.</p>

<h2>Parque Nacional de los Lagos de Plitvice</h2>
<p>El parque más visitado de Croacia y uno de los más bonitos del mundo: 16 lagos encadenados, cascadas turquesas, pasarelas de madera sobre el agua. Está en el interior del país, a 2 horas de Zagreb y 2,5 horas de Split. <strong>Reserva la entrada online con semanas de antelación</strong> — en verano se agotan. Precio: 15-40 euros según temporada. Hay que llegar a primera hora: los primeros en entrar lo ven sin aglomeraciones. Para la tarde hay demasiada gente.</p>

<h2>Gastronomía croata</h2>
<ul>
<li><strong>Peka:</strong> carne o marisco cocinados bajo una campana de hierro cubierta de brasas. Método de cocción tradicional dálmata. Hay que encargarla con horas de antelación en la mayoría de restaurantes. Merece absolutamente la espera.</li>
<li><strong>Pasticada:</strong> carne de buey marinada con vino y especias, guisada durante horas. El plato festivo de Dalmacia.</li>
<li><strong>Bruschetta dálmata con aceite de oliva local</strong> y el queso de la isla de Pag (uno de los mejores quesos de Europa) son las tapas más típicas.</li>
<li><strong>Vino:</strong> Croacia produce vinos blancos y tintos de gran calidad (Grk, Plavac Mali, Malvazija) a precios muy razonables para lo que son.</li>
</ul>

<h2>Cómo llegar a Croacia desde España</h2>
<p><strong>Avión a Dubrovnik (DBV):</strong> Vueling, Ryanair e Iberia tienen vuelos directos desde Madrid, Barcelona y otras ciudades españolas. Precio: 50-150 euros según temporada.</p>
<p><strong>Avión a Split (SPU):</strong> más barato y con más vuelos low-cost. Desde Split se accede fácilmente a las islas y a los lagos de Plitvice.</p>
<p><strong>Avión a Zagreb (ZAG):</strong> mejor precio para quien quiere combinar capital + Plitvice + costa en coche.</p>

<h2>Cuándo ir: el consejo más importante</h2>
<p><strong>Junio y septiembre son los meses perfectos.</strong> El mar ya está templado, hay sol, los precios son 20-40 por ciento más bajos que en julio-agosto y los monumentos se pueden visitar sin empujones. Julio y agosto funcionan pero son carísimos y masificados, especialmente en Dubrovnik. En octubre cierra casi todo en las islas pero el clima en Split y Dubrovnik sigue siendo muy agradable."""

CROACIA_GC = gc(
    "Croacia sin arruinarte en el intento",
    [
        "El paseo por las murallas de Dubrovnik (35 euros) ve haciéndolo a las 8h cuando abren: sin turistas y sin el calor insoportable de las 11h.",
        "Junio y septiembre son un 20-40 por ciento más baratos que julio-agosto en alojamiento y actividades, con el mar templado y sin las masas.",
        "Para las islas, los ferries de Jadrolinija son la opción más barata (2-10 euros según trayecto). Los catamaranes rápidos cuestan el doble pero tardan la mitad.",
        "Los restaurantes con cartas en 5 idiomas en el casco histórico de Dubrovnik son caros y mediocres. Camina 10 minutos hasta el barrio de Lapad para encontrar los locales donde come la gente de Dubrovnik.",
        "Reserva la entrada a Plitvice online semanas antes en verano — se agotan. El precio en taquilla es más caro que online.",
        "En Split, el Palacio de Diocleciano se recorre gratis. Los museos interiores cuestan 3-10 euros pero el ambiente del palacio vivido ya vale el viaje.",
        "Compra el vino Plavac Mali o Malvazija en las bodegas locales de las islas o en los supermercados Konzum — la misma botella que en un restaurante de Dubrovnik cuesta 5 veces más.",
    ]
)

CROACIA_CONTENT = CROACIA + CROACIA_GC


# ─── SICILIA ─────────────────────────────────────────────────────────────────

SICILIA = """<p>Sicilia es el Mediterráneo en su versión más intensa y menos filtrada. La isla más grande del mar Mediterráneo acumula 3.000 años de historia sobre ella — griegos, romanos, árabes, normandos y españoles la han conquistado y dejado su huella en una mezcla arquitectónica única en el mundo. Los templos griegos de Agrigento son más grandes e impresionantes que muchos de los de Grecia. La gastronomía siciliana es la mejor de toda Italia. Y el Etna, el volcán más alto y activo de Europa, bufa desde el centro de la isla mientras los sicilianos hacen su vida a sus pies.</p>

<h2>Palermo: el caos perfecto</h2>

<h3>Los mercados de Ballarò y Vucciria</h3>
<p>Los mercados callejeros de Palermo son el corazón vivo de la ciudad. Ballarò (el más grande) y la Vucciria son mercados árabes del siglo XII que siguen funcionando como entonces: puestos de pescado fresco, verduras, especias, fruta exótica, ropa y todo lo imaginable en calles estrechas llenas de gritos y olores. La Vucciria de noche se convierte en un bar al aire libre improvisado. Imprescindible y completamente gratis.</p>

<h3>La Capilla Palatina</h3>
<p>El interior más impresionante de toda Sicilia. Una capilla normanda del siglo XII con mosaicos dorados bizantinos que cubren cada centímetro de las paredes y el techo — el resultado de mezclar artesanos árabes, griegos y normandos trabajando juntos. El efecto es irreal: entras en una caja de oro. Está dentro del Palacio de los Normandos. Entrada: 12 euros. Vale absolutamente cada céntimo.</p>

<h3>La Catedral de Palermo y la Cúpula Árabe</h3>
<p>Otro ejemplo del estilo siciliano único: una catedral normanda con arcos árabes, añadidos barrocos y una cúpula neoclásica, todo mezclado sin ningún pudor. La entrada a la nave principal es gratuita; subir a las terrazas para ver el panorama cuesta 5 euros.</p>

<h2>Taormina: la postal de Sicilia</h2>
<p>El pueblo más turístico de Sicilia tiene razones de sobra para serlo: el Teatro Greco-Romano de Taormina, con el Etna nevado como telón de fondo y el mar a sus pies, es una de las imágenes más impactantes de toda Italia. Los griegos eligieron bien el sitio. El pueblo medieval encaramado sobre el acantilado, la Piazza IX Aprile con su panorámica y las calles llenas de buganvillas son una postal permanente. Entrada al teatro: 10 euros. Taormina ciudad: gratis.</p>

<h2>El Valle de los Templos de Agrigento</h2>
<p>El sitio arqueológico más impresionante de Italia (y hay mucha competencia). Los templos griegos del siglo V a.C. de Agrigento están mejor conservados que los de Atenas — el Templo de la Concordia, con todas sus columnas en pie, parece que lo terminaron ayer. La visita al complejo (con todos los templos) lleva 3-4 horas mínimo. Entrada: 10 euros. Ir al amanecer o al atardecer para la luz perfecta sobre las columnas doradas.</p>

<h2>Siracusa: la ciudad más bella de Sicilia</h2>
<p>La antigua ciudad griega que Cicerón llamó "la más grande y bella de todas las ciudades griegas" todavía mantiene esa belleza. Ortigia, el centro histórico en una islita unida al continente por un puente, es uno de los espacios urbanos más perfectos del Mediterráneo: el Teatro Griego del siglo V a.C. (en funcionamiento), la Catedral construida dentro de un templo griego del 480 a.C., la Fuente de Aretusa y las calles barrocas doradas. La entrada al Parque Arqueológico es 13 euros. Ortigia es de libre acceso.</p>

<h2>El Etna: subir al volcán activo más alto de Europa</h2>
<p>El Etna (3.350 metros) es el volcán activo más alto de Europa y está en erupción casi permanente. Subir al cráter es una experiencia sin igual: el paisaje lunar de lava negra, el humo saliendo de las fisuras y las vistas sobre toda Sicilia y el estrecho de Messina con Calabria al fondo. Se puede subir:</p>
<ul>
<li><strong>En telecabina + jeep 4x4 + guía:</strong> la opción más cómoda. Desde el parking de Rifugio Sapienza, telecabina hasta los 2.500 m y luego jeep hasta los 2.900 m. Precio total: 70-80 euros. Deja tiempo suficiente: hay colas en temporada alta.</li>
<li><strong>A pie desde abajo:</strong> para senderistas con experiencia. La ruta desde Rifugio Sapienza (1.923 m) hasta los cráteres principales es de unas 4-5 horas ida y vuelta. Sin coste adicional (solo el aparcamiento o el bus desde Catania).</li>
</ul>
<p><strong>Importante:</strong> los cráteres activos solo se visitan con guía oficial por seguridad. Comprueba el nivel de actividad volcánica antes — en días de actividad alta los accesos se cierran.</p>

<h2>Gastronomía siciliana: la mejor de Italia</h2>

<h3>Arancini</h3>
<p>Bolas de arroz fritas rellenas de ragú de carne, mozzarella y guisantes. El street food más icónico de Sicilia. En Palermo hay arancinis de tamaño descomunal. Precio: 2-4 euros la pieza. La variante palermitana tiene forma cónica; la catanesa, esférica. La rivalidad entre ambas ciudades sobre la forma "correcta" del arancino es completamente real y muy siciliana.</p>

<h3>Cannoli</h3>
<p>El postre siciliano por excelencia: tubo de masa frita relleno de ricotta de oveja endulzada con fruta escarchada y pistachos. El cannolo auténtico se rellena en el momento de servir — desconfía de los que ya vienen rellenos (la masa se ablanda). En las pastelerías de Palermo o Catania: 1,50-2,50 euros la pieza.</p>

<h3>Caponata</h3>
<p>La versión siciliana de la ratatouille: berenjena, tomate, apio, aceitunas, alcaparras y vinagre. Agridulce, intensa, perfecta como entrante o guarnición. Cada familia tiene su receta y ninguna se parece exactamente a otra.</p>

<h3>Granita y brioche</h3>
<p>El desayuno siciliano: granita (hielo granulado de limón, almendra, café o pistacho) con un brioche esponjoso. En verano, a las 8h de la mañana, es el desayuno de toda Sicilia. Precio: 2-3 euros. El de almendra en Catania y el de limón de Messina son los mejores.</p>

<h2>Cómo llegar a Sicilia desde España</h2>
<p><strong>Avión a Palermo (PMO):</strong> Ryanair, Vueling y EasyJet tienen vuelos directos desde Madrid y Barcelona. Precio: 40-100 euros según temporada.</p>
<p><strong>Avión a Catania (CTA):</strong> más vuelos low-cost y a veces más barato. Mejor punto de partida si quieres hacer Etna + Taormina + Siracusa.</p>

<h2>Cuándo ir a Sicilia</h2>
<p><strong>Mayo, junio y septiembre-octubre</strong> son los mejores meses: calor pero no el extremo de julio-agosto, mar templado, precios razonables y sin las masas de turistas. En julio-agosto hace un calor sofocante (38-42 grados) que hace difícil visitar los sitios arqueológicos al mediodía. En invierno el clima es suave para los estándares europeos pero muchas atracciones tienen horarios reducidos."""

SICILIA_GC = gc(
    "Sicilia asequible: cómo disfrutar lo mejor sin el coste italiano",
    [
        "El Valle de los Templos de Agrigento (10 euros) y el Teatro de Siracusa (13 euros) son las visitas más impresionantes y más baratas por lo que ofrecen — no te las saltes.",
        "Come en los mercados de Palermo (Ballarò, Vucciria) para desayunar y comer: arancino + granita = 4-5 euros, la mitad que en cualquier bar turistico.",
        "Vuela siempre a Catania (CTA) si puedes: más vuelos low-cost y mejor comunicado con el Etna, Taormina y Siracusa que Palermo.",
        "Para subir al Etna, la telecabina + jeep cuesta 70-80 euros pero sube hasta 2.900m en 30 minutos. Si eres buen caminante, el acceso a pie desde el parking de Sapienza es gratis (solo el parking, 4 euros).",
        "En Taormina, los restaurantes con terraza mirando al teatro son muy caros. Baja 10 minutos por las escaleras al barrio de Mazzarò para comer pasta y pizza al doble de calidad por la mitad del precio.",
        "Alquila un coche para Sicilia: el transporte público entre los sitios arqueológicos es lento y escaso. Un compacto por 5-7 días cuesta 80-150 euros y te da libertad total.",
        "Mayo y septiembre-octubre son los meses perfectos: mar templado, sin el calor extremo de agosto, precios 20-30 por ciento menores y acceso cómodo a todos los sitios.",
    ]
)

SICILIA_CONTENT = SICILIA + SICILIA_GC


# ─── GEORGIA (TBILISI Y EL CÁUCASO) ─────────────────────────────────────────

GEORGIA = """<p>Georgia es el destino europeo que más sorprende a quien lo descubre. Un país pequeño en el corazón del Cáucaso, entre el Mar Negro y el Mar Caspio, con una de las gastronomías más singulares del mundo, arquitectura medieval única, montañas que compiten con los Alpes, vinos de tradición milenaria (8.000 años de historia vitivinícola) y una hospitalidad que ya quisiéramos tener aquí. Y encima, baratísimo para estándares europeos. Georgia va a ser el próximo gran destino turístico — ahora mismo, antes de que se masifique, es el momento perfecto.</p>

<h2>Tbilisi: la capital más inesperada de Europa</h2>

<h3>La Ciudad Vieja (Dzveli Tbilisi)</h3>
<p>El casco antiguo de Tbilisi es un laberinto de balcones de madera tallada que se inclinan sobre calles empedradas, mezclado con iglesias ortodoxas del siglo VI, una fortaleza medieval, una sinagoga, una mezquita y baños termales de azufre árabe, todo en apenas un kilómetro cuadrado. La ciudad vieja de Tbilisi es uno de los conjuntos urbanos históricos más únicos de Europa y está casi sin turistificar — los bares, hostales y restaurantes con más encanto los encontrarás aquí. Explorar es completamente gratis.</p>

<h3>Fortaleza de Narikala</h3>
<p>La fortaleza medieval del siglo IV que domina la ciudad vieja. Se puede subir por el teleférico desde el barrio de Abanotubani (5 lari = 1,7 euros) o a pie en 20 minutos. Desde arriba, la panorámica de Tbilisi — con el río Mtkvari, los tejados rojos y las montañas al fondo — es impresionante. La entrada a la fortaleza es gratuita.</p>

<h3>Los baños de azufre de Abanotubani</h3>
<p>El barrio de las cúpulas de ladrillo que alberga los baños termales de azufre de Tbilisi. Los georgianos vienen aquí desde el siglo V a relajarse, socializar y curar enfermedades. El agua sale caliente del suelo (37-42 grados) con un olor a azufre que distingues desde 100 metros. Un baño privado con ducha, piscina y masaje incluido cuesta entre 15 y 40 euros por persona según el establecimiento. Chreli Abano es el más auténtico. Recomendación: haz el baño de azufre sí o sí — es una experiencia cultural única.</p>

<h3>Museo Nacional de Georgia</h3>
<p>La colección de joyas doradas de la civilización de Colquide (siglos VII-IV a.C.) — la tierra del vellocino de oro — es una de las más extraordinarias del mundo antiguo. El tesoro de oro del museo es comparable al Museo Egipcio de El Cairo en calidad, pero sin las colas. Entrada: 15 lari (5 euros). Imprescindible.</p>

<h2>Kazbegi y las montañas del Cáucaso</h2>
<p>A 150 km de Tbilisi (3 horas por la Carretera Militar Georgiana, una de las rutas de montaña más espectaculares de Europa), el pueblo de Kazbegi está a los pies del Monte Kazbek (5.047 metros). La imagen emblemática de Georgia: la iglesia medieval de Gergeti Trinidad sobre una colina a 2.170 metros, con el Kazbek nevado de fondo. Subir a la iglesia desde el pueblo lleva 2-3 horas a pie o 30 minutos en jeep 4x4 (20 euros). El paisaje de alta montaña es absolutamente impresionante. Hay guesthouses en Kazbegi muy baratas (15-25 euros por persona con desayuno).</p>

<h2>Kakheti: la región del vino</h2>
<p>Georgia inventó el vino hace 8.000 años y la región de Kakheti (a 1,5 horas de Tbilisi) sigue siendo el corazón vitivinícola del país. El método de vinificación en ánforas de barro (qvevri) fue declarado Patrimonio Inmaterial de la UNESCO. Los vinos georgianos son completamente diferentes a cualquier otro: los blancos macerados en ánfora durante meses tienen un color ámbar-naranja y un sabor tánico y mineral único. Las bodegas más interesantes:</p>
<ul>
<li><strong>Schuchmann Wines:</strong> la bodega más moderna y mejor equipada. Tour y cata: 30-50 lari (10-17 euros).</li>
<li><strong>Vinoterra:</strong> especializada en métodos tradicionales de qvevri. Vista impresionante sobre los viñedos.</li>
<li><strong>Bodegas familiares de Sighnaghi:</strong> el pueblo más bonito de Kakheti, amurallado, con vistas a la llanura de Alazani. Los vinos caseros que venden desde la puerta de las casas son extraordinarios y muy baratos (5-8 lari = 1,7-2,7 euros la botella).</li>
</ul>

<h2>Gastronomía georgiana: la que nadie conoce y todos adoran</h2>

<h3>Khinkali</h3>
<p>Las empanadillas georgianas. Masa fina rellena de carne picada con hierbas y caldo. La técnica correcta: coge el khinkali por el "ombligo" (la parte retorcida), dale un mordisco pequeño para que salga el caldo, bébelo y luego come el resto. El ombligo se deja en el plato — es la forma de contar cuántos has comido. Un khinkali de tamaño estándar: 1-1,5 lari (0,35-0,50 euros). Una ración habitual: 8-10 piezas.</p>

<h3>Khachapuri</h3>
<p>El pan de queso georgiano, el plato más conocido del país. En su versión adjariana (del Mar Negro): un pan con forma de barca relleno de queso fundido con un huevo y mantequilla encima. Se rompe el pan por los bordes, se mezcla todo y se come untando. Precio en restaurante local: 8-12 lari (2,70-4 euros). Una ración alimenta a dos personas sin problemas.</p>

<h3>Badridzhani</h3>
<p>Berenjenas fritas enrolladas con crema de nuez, ajo y especias. Apariencia modesta, sabor revelador. Es el entrante estrella de la cocina georgiana y hay versiones de todos los precios.</p>

<h3>Churchkhela</h3>
<p>El "snicker georgiano": nueces ensartadas en un hilo y cubiertas de jugo de uva concentrado (tatara). Se venden por toda Georgia como snack callejero. Precio: 2-5 lari.</p>

<h2>Cómo llegar a Georgia desde España</h2>
<p>No hay vuelos directos desde España. Las mejores conexiones:</p>
<ul>
<li><strong>Turkish Airlines vía Estambul:</strong> la ruta más frecuente y normalmente la más barata. Madrid-Tbilisi desde 200-350 euros ida y vuelta.</li>
<li><strong>Wizz Air vía Budapest o Viena:</strong> low-cost que vuela a Tbilisi. Precio similar o algo menor.</li>
<li><strong>LOT Polish Airlines vía Varsovia:</strong> buenas conexiones desde varias ciudades españolas.</li>
</ul>
<p>La moneda es el lari georgiano (GEL). 1 euro = aproximadamente 3 lari (2025). Todo es muy barato para estándares europeos.</p>

<h2>Cuándo ir a Georgia</h2>
<ul>
<li><strong>Abril-junio:</strong> la mejor época. Las montañas están nevadas, los viñedos florecen, las temperaturas son perfectas (18-25 grados en Tbilisi) y hay pocas personas.</li>
<li><strong>Septiembre-octubre:</strong> la vendimia en Kakheti. Festivales del vino, uvas maduras, hojas doradas. Maravilloso.</li>
<li><strong>Julio-agosto:</strong> calor en Tbilisi (35+ grados) pero perfecto para las montañas de Kazbegi. Alta temporada, algo más de turismo.</li>
<li><strong>Invierno (dic-feb):</strong> frío intenso pero hay esquí en Gudauri (a 2 horas de Tbilisi). La estación de esquí más barata de Europa.</li>
</ul>"""

GEORGIA_GC = gc(
    "Georgia: el destino que cambia todo lo que sabes sobre viajar barato bien",
    [
        "El lari georgiano vale aproximadamente 3 por 1 euro: khinkalis a 0,40 euros la pieza, café excelente a 1,20 euros, transporte local a 0,50 euros. El presupuesto diario de un viajero independiente está en 35-60 euros incluyendo alojamiento, comida y actividades.",
        "Los baños de azufre de Abanotubani son la experiencia más única de Tbilisi y cuestan 15-40 euros con masaje incluido — págalo sin dudar.",
        "Para Kazbegi, la Carretera Militar Georgiana en marshrutka (minibús) desde la estación de Didube en Tbilisi cuesta 10 lari (3,30 euros). El taxi privado para el día, 80-100 lari (27-33 euros) para todo el grupo.",
        "El vino georgiano embotellado en supermercados Carrefour o Goodwill de Tbilisi cuesta 8-15 lari (2,70-5 euros) una botella de calidad. Los vinos de qvevri (ánfora) valen la experiencia.",
        "Turkish Airlines vía Estambul suele ser la opción más barata desde España — compara también Wizz Air vía Budapest o Viena.",
        "En Kakheti, las bodegas familiares de Sighnaghi venden vino casero a 5-8 lari la botella (menos de 3 euros) — prueba varios y compra los que te gusten para llevar a casa.",
        "Georgia en abril-junio o septiembre-octubre es la combinación perfecta: tiempo excelente, sin turismo masivo y precios bajos. Julio-agosto es la temporada alta — aún barato pero con más turistas.",
    ]
)

GEORGIA_CONTENT = GEORGIA + GEORGIA_GC


# ─── LISTA DE POSTS A INSERTAR ────────────────────────────────────────────────

NEW_POSTS = [
    {
        "slug": "toledo-que-ver-guia-completa",
        "title": "Toledo: qué ver en la ciudad imperial — guía completa",
        "excerpt": "Catedral, murallas, El Greco, sinagoga del Tránsito, mazapán y el mirador del Valle. Toledo Patrimonio de la Humanidad a 33 minutos de Madrid en AVE.",
        "content": TOLEDO_CONTENT,
        "image_url": "https://images.unsplash.com/photo-1560969184-10fe8719e047?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "category": "espana",
    },
    {
        "slug": "salamanca-que-ver-guia-completa",
        "title": "Salamanca: qué ver en La Dorada — guía completa",
        "excerpt": "La Plaza Mayor más bonita de España, la universidad más antigua de la Península, las dos catedrales, el jamón de Guijuelo y el ambiente universitario más vivo de Castilla.",
        "content": SALAMANCA_CONTENT,
        "image_url": "https://images.unsplash.com/photo-1580674684087-9ea2b3b53b63?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "category": "espana",
    },
    {
        "slug": "asturias-que-ver-guia-completa",
        "title": "Asturias: qué ver en el Paraíso Natural — guía completa",
        "excerpt": "Picos de Europa, Ruta del Cares, playas salvajes del Cantábrico, Oviedo, Gijón, sidra escanciada y fabada. La España verde que no se parece a ningún otro destino.",
        "content": ASTURIAS_CONTENT,
        "image_url": "https://images.unsplash.com/photo-1558618047-f4e70f5d0727?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "category": "espana",
    },
    {
        "slug": "croacia-dubrovnik-split-guia-completa",
        "title": "Croacia: Dubrovnik, Split e islas — guía completa",
        "excerpt": "Las murallas de Dubrovnik, el Palacio de Diocleciano en Split, las islas de Hvar y Vis, los lagos de Plitvice y todos los consejos para no dejarte la cartera en el Adriático.",
        "content": CROACIA_CONTENT,
        "image_url": "https://images.unsplash.com/photo-1559827260-dc66d52bef19?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "category": "europa",
    },
    {
        "slug": "sicilia-guia-completa-viaje",
        "title": "Sicilia: guía completa de viaje — templos griegos, Etna y gastronomía",
        "excerpt": "El Valle de los Templos de Agrigento, Taormina con el Etna de fondo, Palermo y sus mercados, los arancini, los cannoli y cómo subir al volcán activo más alto de Europa.",
        "content": SICILIA_CONTENT,
        "image_url": "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "category": "europa",
    },
    {
        "slug": "georgia-tbilisi-caucaso-guia-completa",
        "title": "Georgia: Tbilisi, Kazbegi y el Cáucaso — guía completa",
        "excerpt": "El destino europeo más infravalorado. Baños de azufre, iglesias medievales sobre montañas, khinkali, vino de ánfora milenario y presupuesto de 35-60 euros al día todo incluido.",
        "content": GEORGIA_CONTENT,
        "image_url": "https://images.unsplash.com/photo-1565008576549-57569a49371d?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "category": "internacional",
    },
]


# ─── EJECUCIÓN ────────────────────────────────────────────────────────────────

def run():
    conn = psycopg2.connect(config.DATABASE_URL)
    cur = conn.cursor()

    for p in NEW_POSTS:
        cur.execute("SELECT id FROM posts WHERE slug = %s", (p["slug"],))
        exists = cur.fetchone()
        if exists:
            cur.execute("""
                UPDATE posts SET title=%s, excerpt=%s, content=%s, image_url=%s, category=%s
                WHERE slug=%s
            """, (p["title"], p["excerpt"], p["content"], p["image_url"], p["category"], p["slug"]))
            print(f"  UPDATE: {p['slug']}")
        else:
            cur.execute("""
                INSERT INTO posts (slug, title, excerpt, content, image_url, category)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (p["slug"], p["title"], p["excerpt"], p["content"], p["image_url"], p["category"]))
            print(f"  INSERT: {p['slug']}")

    conn.commit()
    cur.close()
    conn.close()
    print(f"\nListo — {len(NEW_POSTS)} guías procesadas.")

if __name__ == "__main__":
    run()
