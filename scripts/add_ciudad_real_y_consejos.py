"""
Añade la guía completa de Ciudad Real y provincia, y reescribe los mejores GangaConsejos.
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


# ─── CIUDAD REAL ────────────────────────────────────────────────────────────────

CIUDAD_REAL = """<p>Ciudad Real y su provincia son uno de los grandes secretos del turismo español. A menos de dos horas de Madrid en AVE, esta tierra manchega guarda molinos de viento icónicos, el único corral de comedias del siglo XVII en funcionamiento del mundo, lagunas de aguas turquesas, el parque nacional más desconocido de España y una gastronomía brutal. Y casi siempre sin turistas. Si buscas destinos auténticos y asequibles, Ciudad Real es tu sitio.</p>

<h2>La ciudad de Ciudad Real: qué ver en el centro</h2>

<h3>Catedral de Santa María del Prado</h3>
<p>La joya gótico-mudéjar del centro histórico. Construida entre los siglos XV y XVI, destaca por su retablo plateresco y los azulejos que decoran el exterior — un detalle inusual que la hace única entre las catedrales españolas. La entrada es gratuita en horario de culto. Frente a ella, el <strong>Museo del Quijote y Biblioteca Cervantina</strong> conserva una colección de más de 100.000 ejemplares del Quijote en todos los idiomas del mundo. Imprescindible para entender la magnitud cultural de La Mancha.</p>

<h3>Plaza Mayor y casco histórico</h3>
<p>El corazón de la ciudad. La plaza porticada con el Ayuntamiento al fondo es el punto de encuentro de toda la ciudad. Desde aquí salen las principales calles comerciales y se accede fácilmente a pie a todos los monumentos. La <strong>Puerta de Toledo</strong>, a pocos minutos caminando, es el único vestigio que queda de las antiguas murallas medievales y uno de los emblemas fotográficos de la ciudad.</p>

<h3>Parque de Gasset</h3>
<p>El pulmón verde de Ciudad Real. Un parque enorme y muy bien cuidado con lago, patos y zonas de descanso. Ideal para un paseo matutino antes de salir a visitar la provincia. Muy frecuentado por los ciudadrealeños y buen lugar para tomarte el pulso a la ciudad real, sin postureo turístico.</p>

<h2>Almagro: el pueblo más bonito de La Mancha</h2>

<p>A 25 kilómetros de Ciudad Real, Almagro es uno de esos pueblos que te dejan sin palabras. Fue capital de la Orden de Calatrava y durante siglos una de las ciudades más importantes de Castilla. Hoy conserva intacto ese esplendor.</p>

<h3>Corral de Comedias</h3>
<p>El monumento más singular de toda la provincia. Este teatro del siglo XVII es el <strong>único corral de comedias barroco en el mundo que sigue funcionando exactamente como lo hacía hace 400 años</strong> — sin reformas, sin modernizaciones, con los mismos tablones de madera, los mismos palcos y la misma estructura que vio actuar a compañías del Siglo de Oro. Es Patrimonio de la Humanidad. En verano acoge el <strong>Festival Internacional de Teatro Clásico de Almagro</strong> (julio), uno de los más prestigiosos de Europa. Precio de la visita guiada: 5 euros.</p>

<h3>Plaza Mayor de Almagro</h3>
<p>Una de las plazas más hermosas de España, con sus arquerías de madera verde y cristal que la hacen completamente diferente a cualquier otra plaza castellana. Perfecta para tomar un café o un vino manchego viendo pasar el tiempo. No hay nada en España parecido a esta plaza.</p>

<h3>Museos y patrimonio</h3>
<p>El <strong>Museo Nacional del Teatro</strong> está aquí, con una colección única de vestuario, escenografía y documentación teatral. El convento de la Asunción de Calatrava, el palacio del Infante Don Juan Manuel y las calles empedradas del centro histórico completan una visita que merece tranquilamente un día entero.</p>

<h2>Los molinos de viento: Consuegra y la Ruta del Quijote</h2>

<p>Cuando la gente piensa en Ciudad Real piensa en molinos. Y tiene razón. Aunque técnicamente Consuegra está en Toledo (a 80 km de Ciudad Real), es la parada obligada si recorres la provincia en coche. Los 10 molinos de viento del cerro Calderico, con el castillo medieval al fondo, son <strong>la imagen más icónica de La Mancha</strong> y el paisaje que Cervantes tenía en mente cuando escribió la escena de Don Quijote. Al amanecer o al atardecer, la foto es inmejorable.</p>

<p>Ya dentro de la provincia de Ciudad Real, <strong>Mota del Cuervo</strong> (también en Cuenca pero en el corazón de La Mancha) y sobre todo el paraje de <strong>Puerto Lápice</strong> — donde la tradición sitúa la primera aventura de Don Quijote — forman parte de la Ruta del Quijote declarada Itinerario Cultural Europeo.</p>

<h2>Parque Nacional de Cabañeros: el Serengeti español</h2>

<p>Este es el gran desconocido de la provincia y uno de los secretos mejor guardados del turismo español. El <strong>Parque Nacional de Cabañeros</strong> ocupa 40.000 hectáreas entre Ciudad Real y Toledo y conserva el mejor ejemplo de bosque mediterráneo de la Península Ibérica. Sus dehesas de quejigos y robles, sus ríos limpios y sus laderas de pizarra albergan una fauna salvaje impresionante:</p>
<ul>
<li><strong>Ciervo ibérico</strong> — en otoño (septiembre-noviembre) se escucha la berrea de madrugada. Es espectacular y completamente gratuito.</li>
<li><strong>Lince ibérico</strong> — Cabañeros es uno de los últimos refugios de este felino en peligro crítico de extinción.</li>
<li><strong>Águila imperial ibérica</strong> — el ave más amenazada de Europa tiene aquí una de sus mayores poblaciones.</li>
<li><strong>Buitre negro y leonado, cigüeña negra, meloncillo, nutria...</strong></li>
</ul>
<p>Las visitas al parque se hacen en jeep todo terreno con guía (son obligatorias en la zona de rañas — llanura central del parque). Precio: 25-35 euros por persona. Duración: 3-4 horas. <strong>Reserva con semanas de antelación en otoño</strong>, se agota. El acceso al parque desde Retuerta del Bullaque o Horcajo de los Montes.</p>

<h2>Lagunas de Ruidera: las lagunas turquesas de La Mancha</h2>

<p>A 90 kilómetros de Ciudad Real, las <strong>Lagunas de Ruidera</strong> son el gran sorpresa de la provincia. Nadie espera encontrar esto en Castilla-La Mancha: 15 lagunas encadenadas unidas por cascadas, con aguas de un color turquesa casi caribeño según la época del año. El parque natural se extiende por 40 kilómetros entre las provincias de Ciudad Real y Albacete.</p>
<p>En verano puedes alquilar kayaks y barcas para recorrer las lagunas. En primavera, cuando bajan las cascadas a pleno caudal, el paisaje es increíble y hay mucho menos turismo. La laguna de Batanas y la Colgada son las más bonitas para bañarse. Hay varios campings y casas rurales en el entorno.</p>

<h2>Valdepeñas: la capital del vino manchego</h2>

<p>La Denominación de Origen Valdepeñas produce algunos de los tintos con mejor relación calidad-precio de toda España. La ciudad homónima (a 70 km de Ciudad Real) tiene bodegas centenarias que puedes visitar con cata incluida por 8-15 euros. El <strong>Museo del Vino</strong> (instalado en una bodega histórica con tinajas gigantes del siglo XIX) es gratuito y explica perfectamente la historia vitivinícola de la región. Si eres aficionado al vino, merece la parada.</p>

<h2>Castillo de Calatrava la Nueva</h2>

<p>Sobre una colina que domina toda la llanura manchega, este castillo-convento del siglo XIII fue la sede principal de la Orden de Calatrava, una de las órdenes militares más poderosas de la Edad Media. Sus ruinas son impresionantes y la vista panorámica desde lo alto abarca kilómetros de llanura manchega. Entrada gratuita. Cerca de Aldea del Rey, a 35 km de Ciudad Real.</p>

<h2>Gastronomía de Ciudad Real: lo que tienes que comer</h2>

<h3>Pisto manchego</h3>
<p>El plato estrella de la región. Tomate, pimiento, calabacín y cebolla pochados a fuego lento hasta hacer una especie de ratatouille manchego. Se sirve como guarnición o con huevo frito encima. Sencillo, barato y absolutamente delicioso. Cada abuela tiene su receta y todas se lo discuten.</p>

<h3>Morteruelo</h3>
<p>Un paté rústico manchego de caza — hígado de cerdo, liebre o perdiz — con especias. Sabor intenso y muy característico. Se toma untado en pan. Muy difícil de encontrar fuera de la región.</p>

<h3>Gachas manchegas</h3>
<p>Harina de almorta (guija) con aceite de oliva, ajos y pimentón. Plato de invierno puro, contundente. Lo que comían los pastores en el campo. Hoy se mantiene en los restaurantes tradicionales y en las fiestas locales.</p>

<h3>Duelos y quebrantos</h3>
<p>El mismísimo plato que menciona Cervantes en el Quijote. Huevos revueltos con chorizo y tocino. El "desayuno" de Don Quijote los sábados. En muchos bares de la ciudad lo sirven como tapa.</p>

<h3>Queso manchego DOP y vino de Valdepeñas</h3>
<p>El queso manchego (con certificado DOP) curado de aquí no tiene nada que ver con lo que venden en el supermercado. Busca las queserías artesanales de la provincia. Y acompáñalo siempre con un tinto de Valdepeñas — la combinación perfecta y a precios de escándalo.</p>

<h2>Cómo llegar a Ciudad Real</h2>

<h3>En AVE desde Madrid</h3>
<p>La opción más cómoda. El AVE Madrid-Puertollano para en Ciudad Real. Desde Madrid Atocha: <strong>50 minutos, desde 12 euros</strong> con billet de AVE low cost (Avlo o tarifas promo de Renfe). Hay varios trenes al día. Ciudad Real tiene una de las estaciones de AVE más cercanas a Madrid — ventaja enorme para una escapada de fin de semana.</p>

<h3>En coche</h3>
<p>La A-4 (autovía del Sur) te lleva de Madrid a Ciudad Real en 2 horas sin peajes. En coche tienes más libertad para visitar la provincia — Cabañeros, Almagro, Ruidera y Consuegra están muy dispersos y el transporte público interurbano es escaso.</p>

<h3>Desde otras ciudades</h3>
<p>Desde Toledo: 1 hora en coche (no hay AVE directo). Desde Córdoba: 2,5 horas en coche o tren. Desde Sevilla: 3,5 horas.</p>

<h2>Cuándo ir a Ciudad Real</h2>
<ul>
<li><strong>Primavera (marzo-mayo):</strong> la mejor época. El campo manchego florece, las lagunas de Ruidera tienen las cascadas al máximo caudal y la temperatura es perfecta para recorrer la provincia en coche.</li>
<li><strong>Otoño (septiembre-noviembre):</strong> imprescindible si quieres escuchar la berrea de los ciervos en Cabañeros. También es vendimia en Valdepeñas. Menos turistas que en primavera.</li>
<li><strong>Verano (junio-agosto):</strong> hace un calor extremo en La Mancha (40 grados con frecuencia). Posible, pero planifica las visitas muy temprano por la mañana o al atardecer. Las lagunas de Ruidera están en su apogeo turístico.</li>
<li><strong>Invierno (dic-feb):</strong> frío intenso, pero muy barato y sin turistas. El Festival de Teatro en Almagro es en julio, no en invierno.</li>
</ul>

<h2>Dónde alojarse</h2>
<p>Ciudad Real ciudad tiene buena oferta hotelera a precios razonables (40-80 euros noche en hotel 3-4 estrellas). Para los que quieren una experiencia más auténtica, las <strong>casas rurales de la provincia</strong> son excelentes y económicas: en los alrededores de Cabañeros, Ruidera y Almagro hay turismo rural de gran calidad por 60-100 euros la casa completa. Las casas rurales manchegas suelen incluir desayuno con productos locales y los propietarios te dan todos los consejos que necesitas para visitar la zona."""

CIUDAD_REAL_GC = gc(
    "ahorrar en Ciudad Real y La Mancha",
    [
        "El AVE tiene tarifas Avlo y promo desde 12 euros Madrid-Ciudad Real. Compra con antelación en la app de Renfe — los precios suben mucho los fines de semana.",
        "El Corral de Comedias de Almagro cuesta 5 euros pero el exterior y la Plaza Mayor son gratis y valen el viaje. Si puedes, visita durante el Festival de Teatro de julio — las representaciones más baratas arrancan desde 10 euros.",
        "El Parque Nacional de Cabañeros es gratis para entrar a las zonas de libre acceso; solo los jeeps guiados por la raña cuestan 25-35 euros. En septiembre-octubre, la berrea de ciervos al amanecer es gratuita y no necesitas guía.",
        "Las Lagunas de Ruidera: la entrada al parque natural es gratuita, solo pagas el alquiler de kayak o barca (8-15 euros/hora). Ven entre semana en temporada baja — en agosto está lleno y los precios se duplican.",
        "Para comer barato en Ciudad Real busca los menús del día: 10-13 euros con primero, segundo, postre y bebida. En Almagro el menú de muchos bares incluye pisto manchego casero de calidad.",
        "El vino de Valdepeñas en bodega cuesta 3-6 euros la botella de tinto crianza. Compra directamente en las bodegas de Valdepeñas y llévatelo — la diferencia con el precio del supermercado es enorme.",
        "Para alojamiento, las casas rurales de la provincia son mucho más baratas que los hoteles de ciudad y te permiten cocinar: busca en Escapada Rural o Rusticae para los de más calidad. Reserva con meses de antelación si vas en puentes o Semana Santa.",
    ]
)

CIUDAD_REAL_CONTENT = CIUDAD_REAL + CIUDAD_REAL_GC


# ─── GANGACONSEJOS: REESCRITURAS ─────────────────────────────────────────────

VUELOS_BARATOS_TRUCOS = """<p>Encontrar vuelos baratos no es cuestión de suerte ni de webs mágicas. Es saber exactamente cuándo buscar, cuándo reservar y qué hacer cuando las aerolíneas ponen los precios por el suelo. Esta guía recoge los trucos reales que funcionan — sin mitos ni leyendas urbanas.</p>

<h2>El error más común: buscar en el momento equivocado</h2>
<p>La mayoría de la gente busca vuelos cuando ya tienen las fechas cerradas y el viaje decidido. Eso es exactamente lo contrario de cómo funciona el mercado aéreo. Los vuelos baratos los encuentras <strong>buscando de forma habitual</strong> aunque no tengas fechas fijas, y reservando en cuanto ves un precio excepcional.</p>

<h2>Las mejores webs y apps para buscar vuelos baratos</h2>

<h3>Google Flights — el rey para comparar</h3>
<p>La herramienta más potente para buscar vuelos baratos. La clave está en usarla bien:</p>
<ul>
<li><strong>Vista de precio por fechas:</strong> selecciona origen y destino y activa el calendario de precios — ves de un vistazo qué días de la semana son más baratos.</li>
<li><strong>Explorar destinos:</strong> si no tienes destino fijo, introduce tu aeropuerto de origen y deja el destino en blanco. Google te muestra un mapa con los precios a todos los destinos. Así encuentras los chollos.</li>
<li><strong>Alertas de precio:</strong> activa una alerta para tu ruta. Google te avisa por email cuando el precio baja. Gratis y muy útil.</li>
</ul>

<h3>Skyscanner — para fechas flexibles</h3>
<p>Skyscanner tiene la opción "mes completo" que te muestra los precios de todos los días del mes en una tabla. También puedes buscar "en cualquier lugar" si tienes fechas pero no destino. Muy bueno para comparar aerolíneas.</p>

<h3>Kiwi.com — combinaciones que nadie más encuentra</h3>
<p>Kiwi crea itinerarios combinando vuelos de distintas aerolíneas que no se venden juntos oficialmente. Puede encontrar combinaciones 40-60 por ciento más baratas que el vuelo directo. El inconveniente: si pierdes una conexión, estás solo (no hay protección como en un vuelo con escala oficial).</p>

<h3>Las apps directas de las aerolíneas low-cost</h3>
<p>Ryanair, Vueling y EasyJet publican sus ofertas flash directamente en su app antes que en los comparadores. Activa las notificaciones push. Las ofertas de Ryanair los martes suelen ser las mejores de la semana.</p>

<h2>Cuándo reservar: la guía definitiva</h2>

<h3>Vuelos europeos (hasta 4 horas)</h3>
<p>La ventana óptima es <strong>6 a 10 semanas antes</strong> para vuelos de temporada normal. Para Semana Santa, puentes y verano, reserva con 3-4 meses de antelación. En temporada baja (noviembre a febrero excepto Navidad) puedes encontrar ofertas a 2-3 semanas vista.</p>

<h3>Vuelos de larga distancia</h3>
<p>El precio suele ser mejor reservando con <strong>2 a 4 meses de antelación</strong>. Para destinos muy populares en temporada alta (Nueva York en verano, Tailandia en diciembre-enero), amplía a 5-6 meses. Reservar demasiado pronto (más de 6 meses) tampoco garantiza el mejor precio — las aerolíneas no suelen abrir con sus precios más bajos.</p>

<h3>Last minute: cuándo SÍ funciona</h3>
<p>El last minute real (menos de 2 semanas) solo funciona para destinos de bajo coste y temporada baja. Para un vuelo Madrid-Berlín un martes de noviembre, sí. Para un vuelo Madrid-Nueva York en agosto, olvídalo — el precio subirá hasta el último momento.</p>

<h2>El día de la semana importa (pero no como crees)</h2>
<p>Los martes y miércoles son habitualmente los días más baratos para <strong>volar</strong> (los aviones van menos llenos). Para <strong>comprar el billete</strong>, los mejores precios aparecen con frecuencia los martes y miércoles también, cuando las aerolíneas ajustan precios tras el fin de semana. Pero no es una regla fija — si ves un precio bueno, compra sin esperar.</p>

<h2>Aeropuertos alternativos: el truco que más ahorra</h2>
<p>¿Vives cerca de varios aeropuertos? Siempre compara desde todos ellos. La diferencia entre volar desde Madrid-Barajas o desde Toledo (Aeropuerto de Madrid-Sur, servido por algunas low-cost) puede ser de 50-100 euros. Desde Barcelona, compara también con Girona y Reus. Desde Sevilla, con Jerez.</p>
<p>También considera llegar a destinos alternativos: en vez de volar a Roma directamente, vuela a Milán (más barato) y toma el tren. En vez de París, vuela a Bruselas o a Beauvais.</p>

<h2>Modo incógnito: mito parcialmente verdadero</h2>
<p>Las webs de vuelos sí usan cookies para mostrarte precios más altos si repites búsquedas. La solución: usa una pestaña de incógnito o borra las cookies antes de buscar. No siempre marca diferencia, pero es gratis hacerlo y a veces funciona.</p>

<h2>Escala en vez de directo: cuánto puedes ahorrar</h2>
<p>Un vuelo directo Madrid-Bangkok cuesta 700-1.000 euros. Con una escala en Doha, Dubái o Estambul: 350-600 euros. El tiempo extra (4-8 horas) a veces merece la pena. Especialmente si la escala larga te permite hacer una mini-visita a la ciudad de conexión sin coste extra.</p>

<h2>Alertas de precio: la herramienta más infravalorada</h2>
<p>Configura alertas en Google Flights, Skyscanner y Hopper para las rutas que te interesan. Define tu precio máximo objetivo. Cuando el precio baje, recibes un email. No tienes que estar vigilando constantemente — el sistema trabaja por ti. Esta estrategia sola puede ahorrarte 100-200 euros por vuelo si tienes paciencia.</p>""" + gc(
    "vuelos baratos: resumen de lo que funciona",
    [
        "Usa Google Flights con el calendario de precios y activa alertas — es gratis y te avisa cuando el precio baja a tu objetivo.",
        "Para vuelos europeos, reserva entre 6 y 10 semanas antes. Para larga distancia, entre 2 y 4 meses antes.",
        "Kiwi.com encuentra combinaciones de aerolíneas que otros buscadores no ven — ideal para rutas sin vuelo directo barato.",
        "Compara siempre desde todos los aeropuertos cercanos a tu ciudad: la diferencia puede ser 50-100 euros.",
        "Los martes y miércoles suelen tener precios más bajos tanto para volar como para comprar el billete.",
        "Busca siempre en modo incógnito o con cookies borradas para evitar que los precios suban en búsquedas repetidas.",
        "Las apps de Ryanair y Vueling publican ofertas flash antes que los comparadores — activa las notificaciones push.",
    ]
)

HOTELES_BARATOS = """<p>Conseguir un hotel bueno y barato no es difícil si sabes dónde y cómo mirar. El precio de una misma habitación puede variar un 40 por ciento según dónde la reserves y cuándo. Esta guía explica exactamente qué hacer para pagar siempre el precio más bajo.</p>

<h2>El error más común: buscar solo en un sitio</h2>
<p>La mayoría de la gente entra en Booking.com, ve un precio y reserva. Error. El mismo hotel puede estar 20-40 euros más barato en su web propia, en Hotels.com o en Expedia en la misma fecha. Siempre compara en al menos dos plataformas antes de reservar.</p>

<h2>Las mejores plataformas para encontrar hoteles baratos</h2>

<h3>Google Hotels — el comparador más completo</h3>
<p>Antes de ir a ninguna otra web, busca el hotel en Google. El panel de Google Hotels muestra los precios de todas las plataformas (Booking, Expedia, la web del hotel, agencias) para las mismas fechas. De un vistazo ves quién tiene el precio más bajo. Y <strong>siempre muestra el precio final con impuestos incluidos</strong>, que es lo que importa.</p>

<h3>Booking.com — el más completo para comparar</h3>
<p>El mayor inventario de hoteles del mundo. Activa el "precio secreto" iniciando sesión con tu cuenta — hay descuentos adicionales de 10-15 por ciento solo por estar registrado. El programa Genius da descuentos adicionales en muchos hoteles tras hacer 2 reservas. Filtra siempre por "cancelación gratuita" para poder cancelar si encuentras algo mejor.</p>

<h3>Hotels.com — los 10 por 1</h3>
<p>El programa de fidelización de Hotels.com es de los mejores: cada 10 noches reservadas, te dan 1 noche gratis (del valor medio de las anteriores). Si viajas varias veces al año, esta recompensa acaba siendo muy significativa.</p>

<h3>La web directa del hotel: cuándo reservar ahí</h3>
<p>Los hoteles independientes y los hoteles boutique suelen dar un descuento del 5-10 por ciento si reservas directamente con ellos (llama o escribe por email mencionando que has visto el precio en Booking). Las grandes cadenas también tienen el "mejor precio garantizado" en su web — y si encuentras algo más barato en otro sitio, te lo igualan.</p>

<h2>Cancelación gratuita: la estrategia del doble booking</h2>
<p>Una táctica que pocos usan: reserva el hotel que te gusta con cancelación gratuita y luego sigue buscando. Si en los días siguientes aparece algo mejor o más barato, cancelas la primera y reservas la nueva. No hay ningún riesgo y te aseguras no quedarte sin habitación. Esta estrategia funciona especialmente bien para destinos muy demandados donde los hoteles se llenan.</p>

<h2>Cuándo reservar: temporada alta vs. temporada baja</h2>

<h3>Temporada alta y festivos: reserva con mucha antelación</h3>
<p>Para Semana Santa, puentes de mayo, verano (julio-agosto) y Navidad, los precios solo suben con el tiempo. Reservar con 3-4 meses de antelación en temporada alta siempre es más barato que hacerlo tarde. Y la disponibilidad desaparece rápido en destinos populares.</p>

<h3>Temporada baja: el last minute puede funcionar</h3>
<p>Para viajes entre noviembre y febrero (excepto Navidad-Año Nuevo y puentes), los hoteles necesitan llenar habitaciones y dan precios de last minute muy buenos a 1-2 semanas vista. Ciudades europeas como Berlín, Praga o Lisboa en invierno: precios 30-50 por ciento más baratos que en verano.</p>

<h2>Alternativas al hotel: cuándo ahorran de verdad</h2>

<h3>Apartamentos en Airbnb o Booking</h3>
<p>Para estancias de 4 o más noches o para grupos de 3 o más personas, un apartamento suele salir más barato que un hotel y te permite cocinar (ahorro enorme en desayunos y cenas). Booking.com ahora tiene una sección de apartamentos que compite directamente con Airbnb y suele tener mejor política de cancelación.</p>

<h3>Hostales y pensiones</h3>
<p>Mucho más que literas y estudiantes. Los hostales boutique en España ofrecen habitaciones dobles privadas con baño desde 30-50 euros en muchas ciudades, la mitad que un hotel de la misma zona. Busca en Hostelworld filtrando solo habitaciones privadas.</p>

<h3>Casas rurales</h3>
<p>Para escapadas de fin de semana a zonas rurales, las casas rurales enteras suelen ser más económicas que un hotel cuando van 4 o más personas. Y la experiencia es incomparablemente mejor.</p>

<h2>El precio de la ubicación: el factor más subestimado</h2>
<p>Un hotel a 10 minutos a pie del centro puede ser 30-50 euros más barato por noche que uno en pleno centro. Si el transporte público es bueno y no tienes movilidad reducida, considera hoteles un poco alejados del epicentro turístico. En Roma, por ejemplo, los hoteles en el Trastevere o en Prati son mucho más baratos que los del centro histórico y estás igual de bien ubicado.</p>

<h2>Trucos específicos para ahorrar más</h2>
<ul>
<li><strong>Desayuno en el hotel vs. cafetería de la calle:</strong> el desayuno de hotel cuesta 10-18 euros por persona. Una cafetería local suele ser 4-6 euros y es mejor comida. Reserva sin desayuno incluido y desayuna fuera.</li>
<li><strong>Los domingos por la noche son los más baratos en ciudades de negocio</strong> (Madrid, Barcelona, Bilbao) porque los viajeros de empresa no van los domingos. En ciudades de turismo de ocio, el viernes suele ser el más caro.</li>
<li><strong>Negocia siempre para estancias largas:</strong> si vas a estar 7 o más noches, llama al hotel directamente y pide un descuento. Muchos lo hacen sin problema, especialmente en temporada baja.</li>
</ul>""" + gc(
    "hoteles baratos: cómo pagar siempre el precio justo",
    [
        "Compara siempre en Google Hotels antes de reservar — muestra precios de todas las plataformas (con impuestos) en una sola pantalla.",
        "Activa el precio secreto de Booking.com iniciando sesión — hasta 15 por ciento de descuento adicional en muchos hoteles.",
        "Reserva siempre con cancelación gratuita y sigue buscando — si encuentras algo mejor, cancelas sin coste. El doble booking temporal es perfectamente legal.",
        "El desayuno del hotel es el mayor sobre-coste del turismo: 10-18 euros por cabeza. Desayuna en la cafetería de al lado y ahorra 20-35 euros al día por pareja.",
        "Para grupos de 3+ o estancias de 4+ noches, un apartamento en Booking o Airbnb sale siempre más barato y tienes cocina.",
        "Hoteles a 10 minutos del centro: 30-50 euros menos por noche que los del casco histórico. Con metro o bus no notarás la diferencia.",
        "Para temporada baja (noviembre-febrero), el last minute a 1-2 semanas vista en ciudades europeas puede ahorrarte 30-50 por ciento.",
    ]
)

EQUIPAJE_MANO = """<p>Pagar por el equipaje de mano ya es la norma en casi todas las aerolíneas low-cost de Europa. Ryanair, Vueling y EasyJet cobran entre 6 y 50 euros por meter una maleta en el avión dependiendo de cuándo lo añadas. Esta guía explica exactamente cómo viajar sin pagar un euro de más en equipaje.</p>

<h2>Las reglas reales del equipaje de mano (actualizado 2024)</h2>

<h3>Ryanair</h3>
<p>La aerolínea más estricta. El equipaje de mano gratuito es solo una mochila pequeña de <strong>40×20×25 cm</strong> que cabe debajo del asiento. Para llevar una trolley en el compartimento superior necesitas la tarifa "Plus" o pagar el suplemento (6-30 euros según cuándo lo añadas). Si intentas subir una trolley grande sin haberla pagado, en la puerta de embarque te cobrarán 50 euros.</p>

<h3>Vueling</h3>
<p>Permite un bolso de mano de <strong>40×20×30 cm</strong> gratis. Para trolley de cabina (hasta 55×40×20 cm) necesitas la tarifa "Optima" o pagar el suplemento. En Vueling, el suplemento se añade más barato reservando online que en el aeropuerto.</p>

<h3>EasyJet</h3>
<p>Una bolsa pequeña de <strong>45×36×20 cm</strong> gratis. Para trolley de cabina, necesitas tarifa "FLEXI" o el añadido de equipaje (7-30 euros). EasyJet es algo más flexible que Ryanair con las medidas en la práctica.</p>

<h3>Iberia Express y Vueling (grupo IAG)</h3>
<p>Permiten una maleta de cabina de 55×40×20 cm en la mayoría de tarifas base. Más generosas que las otras low-cost.</p>

<h2>Cómo viajar una semana entera con solo equipaje de cabina</h2>

<h3>La clave: la técnica del rollo (roll packing)</h3>
<p>Enrollar la ropa en vez de doblarla permite meter un 30-40 por ciento más de ropa en el mismo espacio y reduce las arrugas. Empieza por la ropa más gruesa (vaqueros, jerseys) y termina con la más fina. Mete los calcetines dentro de los zapatos para no desperdiciar ese espacio.</p>

<h3>Qué meter para 7 días con maleta de cabina</h3>
<ul>
<li>3-4 camisetas o tops (que combinen entre sí)</li>
<li>1 pantalón versátil (vaquero o chino)</li>
<li>1 pantalón o falda ligero/a</li>
<li>1 jersey o sudadera</li>
<li>1 chaqueta (la llevas puesta en el avión si hace falta)</li>
<li>5-7 pares de ropa interior</li>
<li>2-3 pares de calcetines</li>
<li>1 par de zapatos de caminar + sandalias o zapatillas (las más grandes las llevas puestas)</li>
<li>Neceser con líquidos en bolsa de 1 litro (botes de menos de 100 ml)</li>
</ul>
<p>Esto cabe perfectamente en una trolley de cabina de 55x40x20 cm.</p>

<h3>Ropa que se seca rápido: la ventaja del viajero experimentado</h3>
<p>Las camisetas de microfibra (tipo deportivo o de traveler) se secan en 2-3 horas colgadas. Con 3 de estas puedes viajar indefinidamente: usas una, lavas otra a mano en el hotel y la tercera de reserva. Las marcas Uniqlo, Decathlon y Columbia tienen buenas opciones baratas.</p>

<h2>La bolsa de aseo: lo que realmente pasan y lo que confiscan</h2>

<h3>Regla de los 100 ml</h3>
<p>Todos los líquidos, geles, cremas y pastas (incluyendo dentífrico) deben ir en recipientes de máximo 100 ml y en una bolsa de plástico transparente de 1 litro por persona. Esto incluye el gel de ducha, champú, crema solar, colonia, pasta de dientes. Lo que más sorprende: la mantequilla de cacahuete, el queso blando y la Nutella también son "líquidos" según seguridad.</p>

<h3>Soluciones inteligentes</h3>
<ul>
<li><strong>Pastillas de jabón y champú sólido:</strong> no cuentan como líquido. Lush y Ethique hacen champús y acondicionadores sólidos que duran meses.</li>
<li><strong>Compra en destino:</strong> para vuelos de más de 3-4 días, compra el champú y gel grande en el supermercado de destino (1-2 euros). Al volver, deja el resto o metes lo que queda en un bote de 100 ml.</li>
<li><strong>Colonias en miniatura:</strong> las muestras de perfume de los grandes almacenes son perfectas para el avión. O decanta tu colonia en un atomizador de viaje de 10 ml.</li>
</ul>

<h2>Cuándo sí vale la pena pagar el equipaje facturado</h2>
<p>No siempre tienes que luchar contra el equipaje de cabina. Hay casos en que pagar por facturar vale la pena:</p>
<ul>
<li>Viajes de más de 2 semanas (inevitable llevar más ropa)</li>
<li>Destinos donde no puedes lavar ropa fácilmente</li>
<li>Si llevas equipo deportivo (bicicleta, surf, esquí)</li>
<li>Si viajas con niños (la logística del equipaje de cabina con niños no merece el ahorro)</li>
</ul>
<p><strong>Truco:</strong> si sabes que vas a facturar, añade el equipaje en el momento de la reserva del vuelo — es siempre más barato que añadirlo después o pagar en el aeropuerto. La diferencia puede ser de 10-20 euros.</p>""" + gc(
    "equipaje de mano: viajar sin pagar de más",
    [
        "Añade el equipaje facturado siempre en el momento de la compra del vuelo — puede ser 10-20 euros más barato que añadirlo después o pagar en el aeropuerto.",
        "Técnica del rollo para hacer la maleta: la ropa enrollada ocupa un 30-40 por ciento menos de espacio que doblada.",
        "Lleva la chaqueta y el jersey puestos al embarcar si el volumen es justo — no cuentan como equipaje de mano.",
        "Champú y jabón sólidos (Lush, Decathlon) no cuentan como líquidos: ahorra espacio en el neceser y pasan sin problema el control.",
        "Para vuelos de Ryanair, la trolley de cabina se paga menos cara reservando en el momento del vuelo que añadiéndola después — nunca esperes al check-in.",
        "Con 3 camisetas de microfibra que se secan en 2-3 horas puedes viajar 2 semanas solo con equipaje de mano.",
        "Si llevas líquidos al límite, pon la bolsa de plástico accesible antes del control de seguridad — si tienes que buscarla en el fondo de la mochila, atrasa la cola y te pones nervioso.",
    ]
)

CUANDO_RESERVAR_VUELO = """<p>¿Cuándo es el mejor momento para reservar un vuelo? Es la pregunta que todo el mundo hace y casi nadie responde bien porque la respuesta depende del destino, la temporada y el tipo de vuelo. Esta guía te da reglas concretas basadas en cómo funciona realmente la industria aérea.</p>

<h2>Cómo fijan los precios las aerolíneas: lo que necesitas entender</h2>
<p>Los precios de los vuelos no son fijos. Las aerolíneas usan <strong>yield management</strong>: algoritmos que ajustan los precios en tiempo real miles de veces al día según la demanda, la ocupación del vuelo, el tiempo hasta la salida y lo que hace la competencia. No existe "el mejor día de la semana para comprar" universalmente — esa es una leyenda urbana.</p>
<p>Lo que sí existe: <strong>ventanas de precios óptimas</strong> según el tipo de destino y temporada.</p>

<h2>Reglas por tipo de vuelo</h2>

<h3>Vuelos europeos cortos (menos de 4 horas)</h3>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
<tr style="background:#fde8e6;">
  <th style="padding:8px 12px;text-align:left;border-bottom:2px solid #e8523a;">Temporada</th>
  <th style="padding:8px 12px;text-align:left;border-bottom:2px solid #e8523a;">Ventana óptima</th>
  <th style="padding:8px 12px;text-align:left;border-bottom:2px solid #e8523a;">¿Last minute funciona?</th>
</tr>
<tr style="border-bottom:1px solid #eee;">
  <td style="padding:8px 12px;">Verano (jul-ago)</td>
  <td style="padding:8px 12px;">3-4 meses antes</td>
  <td style="padding:8px 12px;">No</td>
</tr>
<tr style="background:#f9f9f9;border-bottom:1px solid #eee;">
  <td style="padding:8px 12px;">Temporada media (abr-jun, sep-oct)</td>
  <td style="padding:8px 12px;">6-10 semanas antes</td>
  <td style="padding:8px 12px;">A veces</td>
</tr>
<tr style="border-bottom:1px solid #eee;">
  <td style="padding:8px 12px;">Temporada baja (nov-feb)</td>
  <td style="padding:8px 12px;">2-6 semanas antes</td>
  <td style="padding:8px 12px;">Sí, con frecuencia</td>
</tr>
<tr style="background:#f9f9f9;">
  <td style="padding:8px 12px;">Puentes y festivos</td>
  <td style="padding:8px 12px;">3-5 meses antes</td>
  <td style="padding:8px 12px;">Nunca</td>
</tr>
</table>

<h3>Vuelos de larga distancia (América, Asia, África)</h3>
<p>La ventana óptima es <strong>2 a 4 meses antes</strong> para vuelos de larga distancia en temporada normal. Para temporada alta (verano para América, diciembre-enero para el sudeste asiático), amplía a 4-6 meses. Más de 6 meses de antelación rara vez garantiza el mejor precio — las aerolíneas no abren con sus precios más bajos.</p>

<h2>El mejor día de la semana para volar (esto sí importa)</h2>
<p>Aunque el mejor día para <em>comprar</em> un billete es discutible, el mejor día para <em>volar</em> está más claro:</p>
<ul>
<li><strong>Más barato:</strong> martes, miércoles y sábado por la mañana</li>
<li><strong>Más caro:</strong> viernes tarde, domingo tarde (fin de semana de escapada), lunes muy temprano (viajeros de negocios)</li>
</ul>
<p>Si puedes ser flexible con los días de vuelo, un vuelo de ida el martes y vuelta el miércoles puede ser 30-80 euros más barato que el mismo trayecto viernes-domingo.</p>

<h2>Las alertas de precio: el método más inteligente</h2>
<p>En vez de intentar adivinar el "mejor momento", deja que la tecnología trabaje por ti:</p>
<ol>
<li>Entra en Google Flights y busca tu ruta</li>
<li>Activa el "seguimiento de precios" (icono de campana)</li>
<li>Google te envía un email cuando el precio baja significativamente</li>
</ol>
<p>También puedes hacerlo en Skyscanner (alertas de precio) y en Hopper (app que predice si el precio va a bajar o subir y te recomienda cuándo comprar). Es gratis y completamente automático.</p>

<h2>¿Cuándo NO esperar más?</h2>
<p>Hay situaciones en las que esperar cuesta caro:</p>
<ul>
<li><strong>Destinos de moda</strong> (Japón, Islandia, Marruecos): el precio solo sube con el tiempo, nunca baja.</li>
<li><strong>Ruta con pocos vuelos directos:</strong> si hay 1-2 opciones de aerolínea, la demanda es suficiente para que el precio no baje nunca.</li>
<li><strong>Semana Santa y puentes nacionales:</strong> los españoles reservan todos a la vez. En cuanto la fecha se confirma en el calendario oficial, los precios suben en cuestión de días.</li>
</ul>

<h2>Las ofertas flash: cómo no perderlas</h2>
<p>Las aerolíneas publican ofertas flash sin avisar — precios muy por debajo de lo habitual durante 24-72 horas para llenar vuelos con poca demanda. Para no perdértelas:</p>
<ul>
<li>Sigue a @Ryanair, @Vueling y @easyJet en redes sociales</li>
<li>Suscríbete a la newsletter de Skyscanner y Google Flights</li>
<li>Activa las notificaciones push de las apps de las aerolíneas</li>
<li>Sigue cuentas de chollos de viaje en Twitter/X e Instagram</li>
</ul>""" + gc(
    "cuándo reservar: reglas de oro para no pagar de más",
    [
        "Para vuelos europeos en temporada media, la ventana óptima es 6-10 semanas antes. Más tarde sube, más pronto rara vez baja.",
        "Activa alertas de precio en Google Flights y Skyscanner para tus rutas habituales — te avisan gratis cuando el precio cae.",
        "Volar martes, miércoles o sábado por la mañana es sistemáticamente más barato que viernes tarde o domingo tarde.",
        "Para Semana Santa y puentes, reserva en cuanto se confirmen las fechas en el calendario oficial — los precios se disparan en días.",
        "Last minute solo funciona para temporada baja (noviembre-febrero): en esos meses un vuelo Madrid-Londres a 1 semana vista puede estar a 30-40 euros.",
        "Para larga distancia (América, Asia), la ventana óptima es 2-4 meses antes. Ni antes ni después suele ser más barato.",
        "La app Hopper predice si el precio de tu vuelo va a subir o bajar y te dice cuándo comprar. Muy útil para vuelos de larga distancia.",
    ]
)

SEGURO_VIAJE = """<p>El seguro de viaje es lo único que nadie quiere contratar y todos lamentan no tener cuando lo necesitan. Una hospitalización en EEUU sin seguro puede costar 50.000 euros. Un vuelo perdido con conexión puede suponer 300-500 euros de gasto. Esta guía explica qué cubre realmente cada tipo de seguro y cuál necesitas según tu viaje.</p>

<h2>Los tipos de seguro de viaje: qué cubre cada uno</h2>

<h3>1. Seguro de asistencia médica en viaje</h3>
<p>El más importante. Cubre gastos médicos en el extranjero: consultas, hospitalización, operaciones, repatriación. <strong>Imprescindible para viajar fuera de la UE.</strong> Dentro de la UE tienes la Tarjeta Sanitaria Europea (TSJE) del SAS, que cubre urgencias en hospitales públicos de la UE — pero no cubre repatriación, ni hospitales privados, ni muchos otros casos.</p>

<h3>2. Seguro de cancelación</h3>
<p>Reembolsa el coste del viaje si tienes que cancelar por causas cubiertas: enfermedad propia o familiar, fallecimiento, accidente, despido laboral. <strong>Lo que no cubre:</strong> cambio de planes, trabajo, que no te apetezca ir. Lee siempre la lista de causas cubiertas antes de contratar.</p>

<h3>3. Seguro de equipaje</h3>
<p>Indemniza por pérdida, robo o daño del equipaje. Las aerolíneas tienen una indemnización máxima por convenio (1.300 euros para vuelos internacionales) pero el proceso es burocrático y lento. Si viajas con equipo caro (portátil, cámara), vale la pena.</p>

<h3>4. Seguro de responsabilidad civil</h3>
<p>Cubre si causas daños a terceros durante el viaje. Obligatorio para alquilar coche en muchos países (aunque el alquiler ya lo suele incluir). Para actividades deportivas en el extranjero también es muy recomendable.</p>

<h2>Destinos donde el seguro médico es imprescindible</h2>

<h3>EEUU, Canadá y México</h3>
<p>La sanidad en EEUU es la más cara del mundo. Una noche en urgencias: 3.000-10.000 dólares. Una operación: decenas de miles. Sin seguro, una emergencia puede arruinarte. Seguro obligatorio de facto. Precio del seguro para 10 días en EEUU: 40-80 euros.</p>

<h3>Asia (Tailandia, Indonesia, Vietnam, India)</h3>
<p>Los hospitales privados en ciudades como Bangkok o Bali son buenos pero caros para quien no tiene seguro. La repatriación desde Asia puede costar 15.000-30.000 euros. El seguro es imprescindible.</p>

<h3>América Latina</h3>
<p>Muy variable por país. En Argentina, Brasil o Colombia los hospitales públicos pueden ser deficientes para turistas; en Chile o Uruguay, mejores. Seguro muy recomendable en todos los casos.</p>

<h3>Europa (fuera de la UE): Reino Unido, Suiza, Noruega</h3>
<p>Tu TSJE no vale fuera de la UE. En el Reino Unido (post-Brexit) y Suiza o Noruega necesitas seguro privado. La sanidad suiza es de las más caras de Europa.</p>

<h2>Las mejores aseguradoras de viaje para españoles</h2>

<h3>IATI Seguros — mejor relación calidad-precio</h3>
<p>Especializada en seguros de viaje. Muy buena cobertura médica (hasta 600.000 euros), repatriación incluida, sin franquicia en muchos planes. Sus seguros de mochilero son especialmente competitivos para viajes largos.</p>

<h3>Allianz Travel</h3>
<p>Una de las más completas. Buena cobertura de cancelación y de equipaje. Algo más cara que IATI pero con más cobertura de actividades deportivas.</p>

<h3>AXA Travel</h3>
<p>Muy buena para viajes a EEUU por la cobertura médica alta. Precio competitivo para estancias cortas.</p>

<h3>Seguro de tu banco o tarjeta de crédito</h3>
<p>Muchas tarjetas Visa/Mastercard Premium y American Express incluyen seguro de viaje si pagas el transporte principal con la tarjeta. Revisa las condiciones de tu tarjeta antes de contratar un seguro aparte — puede que ya lo tengas cubierto.</p>

<h2>Cómo comparar seguros de viaje: lo que tienes que mirar</h2>
<ol>
<li><strong>Cobertura médica máxima:</strong> mínimo 150.000 euros para Europa, 300.000 euros para EEUU/Asia</li>
<li><strong>Repatriación:</strong> que esté incluida siempre, sin límite de coste</li>
<li><strong>COVID y enfermedades preexistentes:</strong> asegúrate de que no hay exclusiones que te afecten</li>
<li><strong>Franquicia:</strong> algunos seguros baratos tienen franquicia de 100-200 euros — significa que los primeros 100-200 euros los pagas tú</li>
<li><strong>Deportes y actividades:</strong> si haces senderismo, buceo, esquí o ciclismo, comprueba que estén cubiertos</li>
</ol>

<h2>Lo que el seguro NO cubre nunca</h2>
<ul>
<li>Deportes extremos (paracaidismo, base jumping, escalada de alta montaña) salvo póliza específica</li>
<li>Embarazo avanzado (generalmente a partir de la semana 28-32)</li>
<li>Enfermedades preexistentes no declaradas al contratar</li>
<li>Cancelación por "no me apetece ir"</li>
<li>Pérdida de objetos de valor no asegurados (cámara, joyas) sin denuncia policial</li>
<li>Accidentes bajo efectos del alcohol o drogas</li>
</ul>""" + gc(
    "seguro de viaje: qué contratar y cómo ahorrar",
    [
        "Para viajes dentro de la UE, la Tarjeta Sanitaria Europea (TSJE, gratuita en la Seguridad Social) cubre urgencias en hospitales públicos. Pídela antes de viajar aunque tengas seguro privado.",
        "Para EEUU, Canadá y Asia, el seguro médico es imprescindible — una hospitalización sin seguro puede costar decenas de miles de euros. No es opcional.",
        "IATI Seguros tiene la mejor relación calidad-precio para viajeros españoles: cubre hasta 600.000 euros en gastos médicos con repatriación incluida desde 25-40 euros para 2 semanas.",
        "Revisa si tu tarjeta de crédito ya incluye seguro de viaje — muchas Visa/Mastercard Premium y Amex Gold/Platinum lo tienen si pagas el vuelo con esa tarjeta.",
        "Para viajes largos (más de 1 mes), el seguro de viajero continuo anual de IATI o Allianz sale más barato que varios seguros por viaje.",
        "Guarda siempre el número de teléfono de asistencia de tu seguro en el móvil antes de salir — en una emergencia no tendrás tiempo de buscar la póliza.",
        "Si tienes actividades deportivas previstas (senderismo, buceo, esquí), comprueba explícitamente que estén cubiertas — muchos seguros básicos las excluyen.",
    ]
)


# ─── POSTS ───────────────────────────────────────────────────────────────────

NEW_POSTS = [
    {
        "slug": "ciudad-real-que-ver-provincia-guia-completa",
        "title": "Ciudad Real: qué ver en la ciudad y la provincia — guía completa",
        "excerpt": "Molinos de viento, el único corral de comedias del mundo en funcionamiento, las lagunas turquesas de Ruidera, el Parque Nacional de Cabañeros y la mejor gastronomía manchega. Ciudad Real te sorprenderá.",
        "content": CIUDAD_REAL_CONTENT,
        "image_url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "category": "espana",
        "mode": "insert",
    },
]

# GangaConsejos a reescribir (slug → contenido nuevo)
CONSEJOS_REWRITES = {
    "como-encontrar-vuelos-baratos-trucos": {
        "title": "Cómo encontrar vuelos baratos: 10 trucos que realmente funcionan",
        "excerpt": "Google Flights, alertas de precio, días de la semana, aeropuertos alternativos... Guía completa con las estrategias reales para pagar siempre el precio justo en tus vuelos.",
        "content": VUELOS_BARATOS_TRUCOS,
        "image_url": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    },
    "hoteles-baratos-como-conseguir-mejor-precio": {
        "title": "Hoteles baratos: cómo conseguir siempre el mejor precio",
        "excerpt": "La misma habitación puede costar un 40 por ciento menos si sabes dónde y cuándo buscar. Google Hotels, cancelación gratuita, doble booking y todos los trucos reales para pagar el precio justo.",
        "content": HOTELES_BARATOS,
        "image_url": "https://images.unsplash.com/photo-1566073771259-6a8506099945?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    },
    "consejos-equipaje-mano-no-pagar-de-mas": {
        "title": "Equipaje de mano: cómo viajar sin pagar de más en aerolíneas",
        "excerpt": "Las medidas exactas de Ryanair, Vueling y EasyJet, la técnica del rollo para meter más ropa, champú sólido, cuándo SÍ vale la pena facturar y todos los trucos para no perder dinero en el aeropuerto.",
        "content": EQUIPAJE_MANO,
        "image_url": "https://images.unsplash.com/photo-1553481187-be93c21490a9?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    },
    "cuando-reservar-vuelo-barato-guia": {
        "title": "Cuándo reservar un vuelo barato: la guía definitiva",
        "excerpt": "No existe el mejor día universal para comprar vuelos, pero sí ventanas de tiempo óptimas según el destino y la temporada. Reglas concretas, tabla comparativa y cómo usar las alertas de precio.",
        "content": CUANDO_RESERVAR_VUELO,
        "image_url": "https://images.unsplash.com/photo-1474302770737-173ee21bab63?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    },
    "seguro-de-viaje-cual-contratar-guia": {
        "title": "Seguro de viaje: cuál contratar y cómo no pagar de más",
        "excerpt": "IATI, Allianz, AXA o el seguro de tu tarjeta de crédito. Qué cubre cada tipo, qué destinos lo hacen imprescindible y los GangaConsejos para tener la mejor cobertura al menor precio.",
        "content": SEGURO_VIAJE,
        "image_url": "https://images.unsplash.com/photo-1521791136064-7986c2920216?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    },
}


# ─── EJECUCIÓN ───────────────────────────────────────────────────────────────

def run():
    conn = psycopg2.connect(config.DATABASE_URL)
    cur = conn.cursor()

    # 1. Insertar post nuevo (Ciudad Real)
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

    # 2. Reescribir GangaConsejos
    for slug, data in CONSEJOS_REWRITES.items():
        cur.execute("SELECT id FROM posts WHERE slug = %s", (slug,))
        row = cur.fetchone()
        if row:
            cur.execute("""
                UPDATE posts SET title=%s, excerpt=%s, content=%s, image_url=%s
                WHERE slug=%s
            """, (data["title"], data["excerpt"], data["content"], data["image_url"], slug))
            print(f"  REWRITE: {slug}")
        else:
            print(f"  NOT FOUND (skipped): {slug}")

    conn.commit()
    cur.close()
    conn.close()
    print("\nListo.")

if __name__ == "__main__":
    run()
