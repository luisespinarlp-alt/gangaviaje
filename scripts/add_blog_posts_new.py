"""8 nuevos posts de blog con intención comercial alta."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database

POSTS = [
    {
        "slug": "que-ver-en-sevilla-guia-completa",
        "title": "Qué ver en Sevilla: guía completa para tu visita",
        "excerpt": "La Catedral, el Alcázar, el barrio de Triana y la mejor época para ir. Todo lo que necesitas saber antes de viajar a Sevilla.",
        "category": "espana",
        "image_url": "https://images.unsplash.com/photo-1559827260-dc66d52bef19?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "content": """<p>Sevilla es una de las ciudades más bonitas de España y una visita obligada si viajas al sur. Clima, arquitectura monumental, tapas y flamenco se combinan en una ciudad que enamora a primera vista.</p>

<h2>Qué ver en Sevilla</h2>

<h3>1. La Catedral y la Giralda</h3>
<p>La Catedral de Sevilla es la más grande del mundo en estilo gótico. No te pierdas subir a la Giralda, el antiguo minarete árabe que hoy actúa como campanario, para disfrutar de las mejores vistas de la ciudad. Reserva la entrada con antelación: las colas pueden ser largas en temporada alta.</p>

<h3>2. El Real Alcázar</h3>
<p>Declarado Patrimonio de la Humanidad, el Alcázar es uno de los palacios en uso más antiguos del mundo. Sus jardines son impresionantes. También fue escenario de rodaje de Juego de Tronos. Precio: unos 13,50€ para adultos.</p>

<h3>3. Barrio de Santa Cruz</h3>
<p>El antiguo barrio judío es perfecto para perderse entre callejuelas blancas, naranjos y patios floridos. Es la zona más fotogénica de Sevilla y queda justo al lado del Alcázar.</p>

<h3>4. Barrio de Triana</h3>
<p>Al otro lado del río Guadalquivir, Triana es el barrio más auténtico. Aquí nació el flamenco sevillano. Visita el mercado de Triana, pasea por la calle Betis con vistas al río y cena en alguna de sus tabernas.</p>

<h3>5. Plaza de España</h3>
<p>Una de las plazas más espectaculares de España. Construida para la Exposición Iberoamericana de 1929, sus azulejos y canales son de película. Aparece en Star Wars, Episodio II.</p>

<h3>6. El Metropol Parasol (Las Setas)</h3>
<p>La estructura de madera más grande del mundo, en el centro de Sevilla. Sube al mirador al atardecer para vistas panorámicas de la ciudad por menos de 5€.</p>

<h2>La mejor época para ir a Sevilla</h2>
<p>Evita julio y agosto: el calor puede superar los 40°C. La mejor época es <strong>primavera (abril-mayo)</strong> para vivir la Semana Santa y la Feria de Abril, u <strong>otoño (septiembre-octubre)</strong> cuando el calor baja y hay menos turistas.</p>

<h2>¿Cuántos días necesitas?</h2>
<p>Con 2-3 días tienes suficiente para ver lo esencial. Si quieres hacer excursiones a Córdoba o Cádiz desde Sevilla, calcula 4-5 días.</p>

<h2>Cómo llegar a Sevilla desde Madrid</h2>
<p>El AVE Madrid-Sevilla tarda solo 2,5 horas. Los vuelos también son baratos y frecuentes desde Madrid, Barcelona y otras ciudades españolas. Busca los precios más bajos en GangaViaje.</p>

<h2>Dónde comer en Sevilla</h2>
<ul>
<li><strong>Tapas clásicas:</strong> cazón en adobo, espinacas con garbanzos, pringá</li>
<li><strong>Zona de tapas:</strong> calle Mateos Gago, Alfalfa, Triana</li>
<li><strong>Presupuesto medio:</strong> 15-25€ por persona en un sitio decente</li>
</ul>

<p>Sevilla es perfecta para una escapada de fin de semana o como parte de una ruta por Andalucía. Con sus monumentos, gastronomía y ambiente único, siempre supera las expectativas.</p>"""
    },
    {
        "slug": "tenerife-que-hacer-guia-completa",
        "title": "Tenerife: qué hacer y ver — guía completa 2025",
        "excerpt": "El Teide, las playas del sur, los acantilados de Los Gigantes y Masca. Todo lo que no te puedes perder en Tenerife.",
        "category": "espana",
        "image_url": "https://images.unsplash.com/photo-1559827260-dc66d52bef19?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "content": """<p>Tenerife es la isla más grande de Canarias y uno de los destinos más visitados de España. Volcanes, playas de arena negra y dorada, bosques de laurisilva y un clima perfecto todo el año. Aquí tienes todo lo que debes saber.</p>

<h2>Imprescindibles de Tenerife</h2>

<h3>1. El Teide y el Parque Nacional</h3>
<p>El volcán más alto de España (3.715 m) es el gran protagonista de la isla. El Parque Nacional del Teide es Patrimonio de la Humanidad. Puedes subir en teleférico hasta los 3.555 m (reserva con antelación, hay cupos limitados) o hacer senderismo por las rutas del parque. Al atardecer, las vistas son espectaculares.</p>

<h3>2. Playas del sur: Las Américas y Los Cristianos</h3>
<p>El sur de Tenerife concentra las mejores playas con más horas de sol y menos lluvia. Playa de Las Vistas en Los Cristianos es perfecta para familias. Playa de Troya en Playa de las Américas tiene ambiente animado.</p>

<h3>3. Los Acantilados de Los Gigantes</h3>
<p>Los impresionantes acantilados de hasta 600 metros de altura son uno de los paisajes más espectaculares de Canarias. Toma una excursión en barco para verlos desde el agua y avistar ballenas y delfines en el estrecho de La Gomera.</p>

<h3>4. Masca</h3>
<p>El pueblo más pintoresco de Tenerife, escondido en un barranco en el macizo de Teno. La carretera de acceso es emocionante. Desde aquí parte el famoso barranco de Masca, una de las rutas de senderismo más espectaculares de Canarias.</p>

<h3>5. La Orotava y Puerto de la Cruz</h3>
<p>El norte de Tenerife es más verde y húmedo. La Orotava tiene uno de los centros históricos mejor conservados de las Canarias. Puerto de la Cruz tiene el famoso Lago Martiánez y el Jardín Botánico.</p>

<h3>6. Anaga</h3>
<p>El Macizo de Anaga es un bosque de laurisilva declarado Reserva de la Biosfera. Sus senderos entre helechos gigantes y niebla permanente parecen de otra época.</p>

<h2>Mejor época para ir a Tenerife</h2>
<p>Tenerife tiene buen tiempo todo el año. El sur es siempre soleado. El norte puede ser más nublado en invierno. Los meses de mayor afluencia turística son diciembre-enero (europeos del norte escapando del frío) y verano.</p>

<h2>Cómo llegar a Tenerife</h2>
<p>Tenerife tiene dos aeropuertos: el Sur (TFS, más cercano a los resorts) y el Norte (TFN, para Puerto de la Cruz). Hay vuelos directos desde casi todas las ciudades españolas y muchas europeas. Los precios son muy competitivos.</p>

<h2>Cuántos días necesitas</h2>
<p>Una semana es lo ideal para ver el norte y el sur de la isla con calma. Con 4-5 días puedes ver lo esencial si te organizas bien.</p>"""
    },
    {
        "slug": "florencia-que-ver-en-dos-dias",
        "title": "Florencia en 2 días: qué ver, itinerario y consejos",
        "excerpt": "El Duomo, los Uffizi, el Ponte Vecchio y la vista desde Piazzale Michelangelo. Guía completa para aprovechar Florencia al máximo.",
        "category": "europa",
        "image_url": "https://images.unsplash.com/photo-1529260830199-42c24126f198?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "content": """<p>Florencia es la cuna del Renacimiento y uno de los destinos culturales más importantes del mundo. En solo 2 días puedes ver los monumentos principales si planificas bien tu tiempo.</p>

<h2>Itinerario Florencia en 2 días</h2>

<h3>Día 1: El centro histórico</h3>

<p><strong>Mañana:</strong> Empieza en el <strong>Duomo</strong>. La Catedral de Santa María del Fiore con su cúpula de Brunelleschi es impresionante. Reserva online para subir a la cúpula (€20, merece la pena), las colas sin reserva son inmensas. Al lado está el Baptisterio con sus Puertas del Paraíso.</p>

<p><strong>Mediodía:</strong> Pasea por el <strong>Mercado Central</strong> (Mercato Centrale) para comer. El piso de arriba tiene puestos de comida excelentes y precios razonables. Prueba el lampredotto (tripas florentinas) si te animas, o la pasta fresca.</p>

<p><strong>Tarde:</strong> Los <strong>Uffizi</strong>. El museo más importante de arte del Renacimiento del mundo. Reserva siempre con antelación. Aquí están La Primavera y El Nacimiento de Venus de Botticelli. Calcula al menos 2-3 horas.</p>

<p><strong>Al atardecer:</strong> Pasea por el <strong>Ponte Vecchio</strong>, el puente medieval con joyerías incrustadas. Luego por el Oltrarno (barrio al otro lado del Arno).</p>

<h3>Día 2: Museos y vistas</h3>

<p><strong>Mañana:</strong> El <strong>Palazzo Pitti</strong> y los Jardines de Bóboli. El antiguo palacio de los Médici tiene varios museos. Los jardines son perfectos para pasear.</p>

<p><strong>Tarde:</strong> <strong>Piazzale Michelangelo</strong>. La mejor panorámica de Florencia, especialmente al atardecer. Sube caminando (20 minutos) o en autobús. Al lado está la Iglesia de San Miniato al Monte.</p>

<p><strong>Última noche:</strong> Cena en el Oltrarno, el barrio más auténtico y menos turístico. Busca una trattoria local.</p>

<h2>Consejos prácticos para Florencia</h2>
<ul>
<li><strong>Reserva todo online:</strong> Uffizi, Cúpula del Duomo y Academia (El David) se agotan semanas antes en temporada alta</li>
<li><strong>El David de Miguel Ángel</strong> está en la Galleria dell'Accademia, no en la Piazza della Signoria (el de la plaza es una copia)</li>
<li><strong>Evita agosto:</strong> calor insoportable y masificación extrema</li>
<li><strong>La mejor época:</strong> abril-mayo o septiembre-octubre</li>
<li><strong>Tarjeta Firenze Card (€85):</strong> acceso a 72 museos en 72 horas, salta colas en Uffizi y Academia</li>
</ul>

<h2>Cómo llegar a Florencia</h2>
<p>En tren desde Roma (1h30 en Frecciarossa), Venecia (2h15) o Milán (1h45). En avión al aeropuerto Amerigo Vespucci, pequeño pero bien conectado con ciudades españolas.</p>"""
    },
    {
        "slug": "phuket-guia-playas-templos-viaje",
        "title": "Phuket: guía completa de playas, templos y qué hacer",
        "excerpt": "Patong, Kata, las Islas Phi Phi y el Gran Buda. Todo lo que necesitas saber para organizar tu viaje a Phuket.",
        "category": "internacional",
        "image_url": "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "content": """<p>Phuket es la isla más grande de Tailandia y uno de los destinos turísticos más populares del sudeste asiático. Playas de arena blanca, aguas turquesas, templos budistas y una gastronomía increíble a precios muy accesibles.</p>

<h2>Las mejores playas de Phuket</h2>

<h3>Patong Beach</h3>
<p>La playa más famosa y animada. Perfecta si buscas ambiente, bares y vida nocturna. En temporada alta puede ser masificada. El paseo marítimo de Bangla Road es el epicentro del ocio nocturno.</p>

<h3>Kata y Kata Noi Beach</h3>
<p>Más tranquilas que Patong. Kata Noi es especialmente bonita, con aguas más limpias y menos turistas. Buena opción para familias.</p>

<h3>Kamala y Surin Beach</h3>
<p>Preferidas por visitantes que buscan algo más exclusivo y tranquilo. Restaurantes de nivel en primera línea de playa.</p>

<h3>Freedom Beach</h3>
<p>Playa más salvaje, solo accesible en barco desde Patong. Vale la pena el esfuerzo para escapar de las multitudes.</p>

<h2>Excursiones imprescindibles desde Phuket</h2>

<h3>Islas Phi Phi</h3>
<p>Las islas más fotografiadas de Tailandia. La Bahía Maya (escenario de la película The Beach) y las aguas de Ko Phi Phi Lee son espectaculares. Reserva una excursión en barco desde Phuket. Llega pronto por la mañana para evitar las multitudes.</p>

<h3>Bahía de Phang Nga</h3>
<p>Conocida por la Roca James Bond (Ko Tapu), icono de la película El hombre de la pistola de oro. Las formaciones de karst que emergen del agua son únicas.</p>

<h3>El Gran Buda</h3>
<p>La estatua de mármol de 45 metros en lo alto del Colina Nakkerd ofrece vistas panorámicas de la isla. Entrada gratuita, pero cubre los hombros y las rodillas.</p>

<h2>Cuándo ir a Phuket</h2>
<p>La mejor época es de <strong>noviembre a abril</strong> (temporada seca). De mayo a octubre hay monzones — las playas del oeste de Phuket pueden cerrarse por oleaje. Sin embargo, los precios bajan considerablemente en temporada baja.</p>

<h2>Cuánto cuesta viajar a Phuket</h2>
<ul>
<li><strong>Vuelo desde España:</strong> 500-900€ ida y vuelta con escalas</li>
<li><strong>Alojamiento:</strong> desde 20€/noche en hostal hasta 200€/noche en resort 5 estrellas</li>
<li><strong>Comida:</strong> 3-8€ por persona en restaurantes locales</li>
<li><strong>Excursión Phi Phi:</strong> 30-60€ por persona</li>
<li><strong>Presupuesto diario:</strong> 50-80€ por persona en un viaje cómodo</li>
</ul>

<h2>Consejos para viajar a Phuket</h2>
<ul>
<li>Alquila una moto o scooter para moverte por la isla (unos 8-12€/día). Conduce con precaución</li>
<li>Regatear es habitual en mercados y tiendas locales</li>
<li>El tuk-tuk es caro para turistas — negocia siempre el precio antes de subir</li>
<li>Lleva ropa que cubra los hombros y rodillas para visitar templos</li>
</ul>"""
    },
    {
        "slug": "ciudad-de-mexico-que-ver-guia",
        "title": "Ciudad de México: qué ver y hacer — guía de viaje completa",
        "excerpt": "Teotihuacán, el Zócalo, Xochimilco, Coyoacán y la gastronomía más rica de Latinoamérica. Guía completa para Ciudad de México.",
        "category": "internacional",
        "image_url": "https://images.unsplash.com/photo-1512813195386-6cf811ad3542?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "content": """<p>Ciudad de México (CDMX) es una de las ciudades más grandes y fascinantes del mundo. Historia prehispánica y colonial, gastronomía de fama mundial, arte y cultura vibrante. Es además uno de los destinos de larga distancia más baratos para los españoles.</p>

<h2>Qué ver en Ciudad de México</h2>

<h3>1. El Zócalo y el Centro Histórico</h3>
<p>La Plaza de la Constitución (Zócalo) es una de las plazas más grandes del mundo. Aquí están la Catedral Metropolitana (la más grande de América), el Palacio Nacional (con los murales de Diego Rivera) y el Templo Mayor (las ruinas aztecas). Todo en un radio de 200 metros.</p>

<h3>2. Teotihuacán</h3>
<p>A solo 50 km de la ciudad, las pirámides del Sol y de la Luna son de las más grandes del mundo. Imprescindible. Sal temprano (antes de las 8h) para evitar el calor y las multitudes. Se puede ir en autobús desde la Terminal del Norte por muy poco dinero.</p>

<h3>3. Coyoacán</h3>
<p>El barrio bohemio por excelencia de CDMX. Aquí nació Frida Kahlo y está su Casa Azul (ahora museo). Mercadillo, cafés con ambiente y la mejor comida callejera de la ciudad.</p>

<h3>4. Xochimilco</h3>
<p>Los canales prehispánicos con trajineras de colores. Los domingos es especialmente animado, con música y vendedores en barca. Una experiencia única que no existe en ningún otro lugar.</p>

<h3>5. Palacio de Bellas Artes</h3>
<p>El edificio más impresionante de la ciudad, con una mezcla de Art Nouveau y Art Déco. Dentro hay murales de los grandes maestros mexicanos: Rivera, Orozco, Siqueiros. La cúpula interior de cristal Tiffany es espectacular.</p>

<h3>6. Bosque de Chapultepec</h3>
<p>El parque urbano más grande de América Latina. Aquí está el Castillo de Chapultepec, el Museo Nacional de Antropología (el mejor de América Latina para entender las culturas prehispánicas) y varios otros museos.</p>

<h2>Gastronomía: la razón #1 para ir</h2>
<p>La comida mexicana es Patrimonio Inmaterial de la UNESCO. No te vayas sin probar:</p>
<ul>
<li>Tacos al pastor (Los Cocuyos, en el centro, son legendarios)</li>
<li>Pozole, mole y chiles en nogada (temporada)</li>
<li>Elotes y esquites en cualquier puesto callejero</li>
<li>Mercado de San Juan para ingredientes y comida gourmet</li>
</ul>

<h2>Cuándo ir a Ciudad de México</h2>
<p>CDMX está a 2.240 metros de altitud — el clima es primaveral todo el año (18-25°C). Evita la temporada de lluvias (junio-septiembre, aunque llueve por las tardes y rápido). Lo mejor: octubre-mayo.</p>

<h2>Seguridad en Ciudad de México</h2>
<p>CDMX tiene mala fama injustificada en algunos aspectos. Las zonas turísticas (Roma, Condesa, Polanco, Coyoacán) son completamente seguras para el turista. Usa sentido común, evita mostrar objetos de valor y usa el metro en horas no punta.</p>

<h2>Cómo llegar desde España</h2>
<p>Vuelos directos desde Madrid (Aerolíneas como Iberia, Aeromexico, Air Europa). Precio habitual: 400-700€ ida y vuelta. Duración: unas 11-12 horas.</p>"""
    },
    {
        "slug": "escapadas-fin-de-semana-desde-madrid-baratas",
        "title": "Escapadas baratas de fin de semana desde Madrid",
        "excerpt": "Toledo, Segovia, Cuenca, Salamanca, Ávila... Los mejores destinos a menos de 2 horas de Madrid para escapar el fin de semana.",
        "category": "espana",
        "image_url": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "content": """<p>Vivir en Madrid tiene una ventaja enorme: en menos de 2 horas tienes acceso a algunos de los destinos más bonitos de España. Ciudades medievales, parques naturales, Sierra Nevada y pueblos de cuento. Aquí tienes las mejores escapadas de fin de semana desde Madrid con presupuesto ajustado.</p>

<h2>Las mejores escapadas desde Madrid</h2>

<h3>1. Toledo (1 hora)</h3>
<p>La ciudad imperial es la escapada clásica desde Madrid. El casco histórico está Patrimonio de la Humanidad y se puede ver a pie en un día. No te pierdas la Catedral Primada, el Alcázar y el barrio judío. El tren AVE llega en solo 30 minutos desde Atocha por unos 15-25€ ida. Sube a pie por el río para las mejores fotos.</p>

<h3>2. Segovia (1,5 horas)</h3>
<p>El Acueducto romano, el Alcázar de cuento (modelo de Cenicienta) y la Catedral. La cochinillo asado es la especialidad local. Autobús desde Moncloa (50 min, €5) o AVE desde Chamartín (30 min). Perfecto en un día pero hay alojamiento barato si quieres quedarte.</p>

<h3>3. Cuenca (2 horas)</h3>
<p>Las Casas Colgadas sobre el barranco del Huécar son de postal. El casco antiguo medieval es impresionante. Desde la Hoz del Huécar las vistas son espectaculares. Más tranquilo que Toledo o Segovia, ideal para ir en pareja. Autobús desde Avenida de América.</p>

<h3>4. Salamanca (2,5 horas)</h3>
<p>La ciudad universitaria más antigua de España. La Plaza Mayor (la más bonita del país, dicen muchos) y la Universidad son imprescindibles. Busca la rana en la fachada de la Universidad — trae buena suerte en los exámenes. Autobús y tren frecuentes desde Madrid.</p>

<h3>5. Ávila (1,5 horas)</h3>
<p>La ciudad más alta de España, completamente amurallada. Las murallas medievales son las mejor conservadas de Europa — se pueden recorrer a pie por arriba. Pequeña y recogida, perfecta para medio día. Yemas de Santa Teresa de postre, obligatorio.</p>

<h3>6. Sierra de Guadarrama</h3>
<p>Para los que prefieren naturaleza. El Valle de El Paular, Navacerrada, La Granja de San Ildefonso o Cercedilla ofrecen senderismo, nieve en invierno y aire puro. Muchos puntos son accesibles en Cercanías desde Madrid.</p>

<h3>7. Aranjuez (45 minutos)</h3>
<p>El Palacio Real y sus jardines son los más bellos de la Comunidad de Madrid. En primavera es especialmente bonito con los jardines en flor. El "Tren de la Fresa" sale los fines de semana en temporada.</p>

<h2>Consejos para escapadas baratas desde Madrid</h2>
<ul>
<li><strong>Transporte:</strong> el autobús suele ser más barato que el tren para distancias cortas</li>
<li><strong>Alojamiento:</strong> busca hostales en el casco antiguo — suelen ser más baratos y mejor ubicados que los hoteles de cadena</li>
<li><strong>Comida:</strong> el menú del día (12-15€) es la mejor opción en todos estos destinos</li>
<li><strong>Sábado vs. domingo:</strong> llega el sábado por la mañana y vuelve el domingo por la tarde para aprovechar al máximo</li>
</ul>

<h2>Presupuesto orientativo para una escapada desde Madrid</h2>
<p>Transporte ida y vuelta: 10-30€. Alojamiento (si te quedas): 40-70€ por habitación doble. Comida: 25-35€ por persona al día. <strong>Total por persona: 75-135€ para un fin de semana con alojamiento.</strong></p>"""
    },
    {
        "slug": "vuelos-baratos-desde-barcelona",
        "title": "Vuelos baratos desde Barcelona: mejores destinos y cuándo reservar",
        "excerpt": "Los destinos europeos más baratos desde el Aeropuerto de Barcelona El Prat. Consejos para encontrar los mejores precios.",
        "category": "espana",
        "image_url": "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "content": """<p>El Aeropuerto de Barcelona El Prat es uno de los más grandes de Europa y tiene conexiones directas con cientos de destinos. Si vives en Barcelona o Cataluña, tienes acceso a vuelos increíblemente baratos a casi todo el mundo. Aquí tienes los mejores destinos y cómo conseguir los mejores precios.</p>

<h2>Destinos baratos desde Barcelona</h2>

<h3>Europa — por menos de 50€</h3>
<ul>
<li><strong>Sevilla:</strong> el AVE es más rápido pero los vuelos pueden ser más baratos en oferta</li>
<li><strong>Málaga:</strong> perfecta para escapadas de playa</li>
<li><strong>Lisboa:</strong> capital europea cercana, vuelos desde 20-40€ con Vueling y Ryanair</li>
<li><strong>Oporto:</strong> alternativa más tranquila a Lisboa</li>
<li><strong>París:</strong> vuelos desde 30-70€ con frecuencia</li>
<li><strong>Roma:</strong> historia y gastronomía a menos de 2 horas</li>
<li><strong>Berlín:</strong> ciudad muy barata una vez estás allí</li>
<li><strong>Dublín:</strong> Ryanair tiene vuelos muy frecuentes y baratos</li>
</ul>

<h3>Destinos de playa — por menos de 100€</h3>
<ul>
<li><strong>Canarias:</strong> Tenerife, Gran Canaria, Lanzarote — sol garantizado todo el año</li>
<li><strong>Ibiza y Mallorca:</strong> aunque es más barato ir en ferry, los vuelos en temporada baja son económicos</li>
<li><strong>Grecia:</strong> Atenas, Santorini, Heraklion — veranos muy baratos desde Barcelona</li>
<li><strong>Marruecos:</strong> Marrakech en 1 hora, vuelos desde 40€</li>
</ul>

<h2>Cómo encontrar los vuelos más baratos desde Barcelona</h2>

<h3>Las aerolineas low-cost más importantes en El Prat</h3>
<ul>
<li><strong>Vueling:</strong> con base en Barcelona, tiene muchas rutas exclusivas desde El Prat</li>
<li><strong>Ryanair:</strong> opera principalmente desde T2 del aeropuerto</li>
<li><strong>EasyJet:</strong> buenas rutas a UK y norte de Europa</li>
<li><strong>Transavia:</strong> vuelos a Países Bajos y destinos mediterráneos</li>
</ul>

<h3>El mejor momento para reservar</h3>
<ul>
<li><strong>Vuelos domésticos y Europa corta distancia:</strong> 3-8 semanas antes</li>
<li><strong>Vuelos de larga distancia:</strong> 2-4 meses antes</li>
<li><strong>Temporada alta (verano y Navidad):</strong> reserva 4-6 meses antes</li>
<li><strong>Los martes y miércoles</strong> suelen tener precios más bajos</li>
</ul>

<h3>Alertas de precio</h3>
<p>Activa alertas en Google Flights para tus destinos favoritos. Cuando el precio baje, recibirás un aviso automático. GangaViaje también publica ofertas de vuelos desde Barcelona cuando detectamos precios especialmente bajos.</p>

<h2>Truco para ahorrar más</h2>
<p>Busca vuelos a aeropuertos alternativos cercanos a tu destino. Para París: también hay vuelos a Beauvais (más lejos pero más barato). Para Londres: Stansted o Luton vs. Heathrow. Para Roma: Ciampino vs. Fiumicino.</p>

<h2>¿Cuándo hay más vuelos baratos desde Barcelona?</h2>
<p>Enero y febrero (excepto Semana Santa) son los meses con menos demanda y más ofertas. Si tienes flexibilidad de fechas, es el momento ideal para viajar a destinos europeos a precios mínimos.</p>"""
    },
    {
        "slug": "hoteles-baratos-barcelona-donde-alojarse",
        "title": "Hoteles baratos en Barcelona: los mejores barrios donde alojarse",
        "excerpt": "Dónde dormir en Barcelona sin gastar una fortuna. Los mejores barrios, precios orientativos y consejos para ahorrar en alojamiento.",
        "category": "espana",
        "image_url": "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "content": """<p>Barcelona es cara para alojarse, especialmente en temporada alta. Pero con la estrategia adecuada puedes encontrar hoteles baratos bien ubicados. Aquí tienes todo lo que necesitas saber.</p>

<h2>Los mejores barrios donde alojarse en Barcelona</h2>

<h3>El Eixample — el más equilibrado</h3>
<p>El Eixample (Ensanche) es el barrio más recomendado para la mayoría de turistas. Bien comunicado con metro, cerca de todo, más tranquilo que el centro histórico y con buenos precios fuera de temporada alta. Está entre la Casa Batlló y la Sagrada Família.</p>
<p><strong>Precio orientativo:</strong> 60-120€/noche en hotel 3 estrellas</p>

<h3>El Gótico / Las Ramblas — el más céntrico pero el más caro</h3>
<p>Máxima ubicación, mínima tranquilidad. Las Ramblas suena bien en el papel pero hay mucho ruido, turismo masivo y es zona de carteristas. Dentro del Barrio Gótico hay calles más tranquilas. Los precios son altos para lo que ofrecen.</p>
<p><strong>Precio orientativo:</strong> 80-150€/noche</p>

<h3>El Born / Sant Pere — el más trendy</h3>
<p>El barrio de moda de Barcelona. El Mercado de Santa Caterina, el Palau de la Música Catalana y el Parque de la Ciudadela están aquí. Buena mezcla de viajeros y locales. Excelentes bares y restaurantes.</p>
<p><strong>Precio orientativo:</strong> 70-130€/noche</p>

<h3>Gràcia — el más auténtico y barato</h3>
<p>El barrio más barcelonés. Lejos del turismo masivo pero con mucho carácter. La Plaça del Sol y la Plaça de la Vila de Gràcia son perfectas para tomar algo como un local. A 20 minutos caminando del Eixample o en metro directo.</p>
<p><strong>Precio orientativo:</strong> 50-90€/noche</p>

<h3>Poblenou — para presupuesto ajustado</h3>
<p>El antiguo barrio industrial, hoy reconvertido en zona tech y de diseño. Menos turístico, precios más bajos, buenas conexiones con el centro. Playa a 10 minutos caminando.</p>
<p><strong>Precio orientativo:</strong> 45-80€/noche</p>

<h2>Cómo encontrar los mejores precios en hoteles de Barcelona</h2>

<h3>La mejor época para encontrar precios bajos</h3>
<ul>
<li><strong>Enero-febrero:</strong> precios mínimos del año</li>
<li><strong>Noviembre:</strong> buen clima y pocos turistas</li>
<li><strong>Evita:</strong> Semana Santa, MWC (febrero/marzo), Primavera Sound (junio), verano completo</li>
</ul>

<h3>Trucos para ahorrar</h3>
<ul>
<li>Reserva con cancelación gratuita y sigue monitorizando el precio — puedes cancelar y volver a reservar más barato</li>
<li>Compara siempre en varias plataformas (Booking, Hotels.com, web del hotel directamente)</li>
<li>Los hoteles boutique familiares suelen ser más baratos que las cadenas</li>
<li>El desayuno incluido raramente vale la pena en Barcelona — hay muchos bares baratos alrededor</li>
</ul>

<h2>Alternativas a los hoteles</h2>
<ul>
<li><strong>Apartamentos:</strong> mejor para estancias de 3+ días o grupos. El precio por noche baja mucho</li>
<li><strong>Hostales:</strong> Barcelona tiene algunos de los mejores hostales de Europa, con habitaciones privadas y privacidad a precio de hostal</li>
<li><strong>Habitaciones en casa:</strong> la opción más barata y la mejor para conocer la ciudad "de verdad"</li>
</ul>

<h2>Qué incluye el precio del hotel en Barcelona</h2>
<p>Ojo con las tasas: Barcelona cobra una tasa turística de <strong>3,25-6,75€ por persona/noche</strong> según la categoría del hotel. No siempre está incluida en el precio mostrado — asegúrate de ver el precio final antes de reservar.</p>"""
    },
]

added = 0
skipped = 0
for p in POSTS:
    result = database.add_post(p)
    if result:
        added += 1
        print(f"✓ Añadido: {p['slug']}")
    else:
        skipped += 1
        print(f"— Ya existe: {p['slug']}")

print(f"\nTotal: {added} añadidos, {skipped} ya existían")
