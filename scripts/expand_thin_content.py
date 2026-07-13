"""
Expande los 20 artículos con contenido insuficiente (<300 palabras).
Mantiene el contenido original y añade secciones nuevas.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import psycopg2
import config

EXPANSIONS = {

"que-hacer-amsterdam-tres-dias": """
<h2>Día 1: canales y centro histórico</h2>
<p>Empieza en Dam Square y recorre los canales del Anillo (Grachtengordel), declarado Patrimonio de la Humanidad. Un paseo en barco por los canales al atardecer es una de las mejores formas de ver la ciudad. Por la noche, pasea por el Jordaan, el barrio más tranquilo y fotogénico de Ámsterdam, con sus casitas de ladrillo reflejadas en el agua.</p>

<h2>Día 2: los museos</h2>
<p>Dedica la mañana al Rijksmuseum (reserva entrada online) para ver los Rembrandt y Vermeer originales. A pocas calles está el Museo Van Gogh — otro imprescindible con reserva previa. Si te queda energía por la tarde, el Museo Anne Frank está en el mismo barrio, aunque las colas pueden ser largas: compra el acceso con antelación y elige horario de apertura o cierre.</p>

<h2>Día 3: Vondelpark, Mercado Albert Cuyp y barrio de la moda</h2>
<p>Empieza con un desayuno tranquilo en el Vondelpark si el tiempo lo permite. Después acércate al Mercado Albert Cuyp, el más grande de la ciudad: zumo de naranja recién exprimido, arenque curado y stroopwafels para llevar. Por la tarde, el barrio De Pijp y la zona de las Nueve Calles (De 9 Straatjes) son perfectos para boutiques independientes y cafés.</p>

<h2>Cómo moverse</h2>
<p>La bicicleta es el transporte rey de Ámsterdam. Alquila una desde el primer día (5-10€/día) y muévete como un local. Para distancias largas, los tranvías (GVB) cubren bien la ciudad. El I Amsterdam City Card incluye transporte público y entrada a muchos museos — rentable si piensas visitar más de dos.</p>

<h2>Dónde comer sin gastar de más</h2>
<p>Los mercados son la opción más económica y sabrosa: el Mercado Albert Cuyp para el día, el Foodhallen (mercado interior en el barrio de Oud-West) para la noche. Para una cena con ambiente local, busca los restaurantes en el Jordaan alejados de las calles principales — la calidad sube y el precio baja considerablemente.</p>

<h2>Presupuesto orientativo para 3 días</h2>
<p>Vuelo desde Madrid o Barcelona: 60-130€ ida y vuelta. Hotel en zona céntrica: 90-150€/noche. Manutención diaria (comidas + cafés): 30-50€/persona. Museos (Rijks + Van Gogh + Anne Frank): ~60€/persona. En total, un fin de semana largo en Ámsterdam puede salir por 350-550€/persona todo incluido dependiendo de cuándo reserves.</p>
""",

"estambul-entre-dos-continentes": """
<h2>Lo imprescindible del lado europeo</h2>
<p>Santa Sofía, la Mezquita Azul y el Palacio de Topkapi forman el triángulo histórico de Sultanahmet, todos a poca distancia caminando. El Gran Bazar, con más de 4.000 tiendas, merece al menos una mañana. Reserva la entrada al Palacio de Topkapi online para evitar las colas del mediodía.</p>

<h2>El lado asiático: Kadıköy y Üsküdar</h2>
<p>Cruza el Bósforo en ferri (la travesía cuesta menos de 1€ con la tarjeta Istanbulkart) y descubre el Ámsterdam turco: Kadıköy es el barrio más animado del lado asiático, con mercado de productores, cafés y restaurantes sin precios turísticos. Üsküdar tiene un ambiente más tradicional y la Mezquita de Çamlıca ofrece vistas panorámicas de toda la ciudad.</p>

<h2>El Bósforo en barco</h2>
<p>El crucero público por el Bósforo (línea Şehir Hatları, salida desde Eminönü) es uno de los paseos más espectaculares de cualquier ciudad del mundo por unos pocos euros. Pasan por palacios de verano otomanos, fortalezas medievales y mansiones de madera que salpican las orillas del estrecho.</p>

<h2>Dónde comer</h2>
<p>Evita los restaurantes de Sultanahmet con menú turístico. Ve al Bazar de las Especias y come de pie: simit (rosca de sésamo), börek (hojaldre relleno) y döner de calidad a precios locales. Para una experiencia más tranquila, el barrio de Beyoğlu y la calle Istiklal tienen cafés y meyhane (tabernas turcas) excelentes. Un té negro turco siempre es gratis con cualquier compra en el mercado.</p>

<h2>Cómo moverse y cuándo ir</h2>
<p>La Istanbulkart (tarjeta recargable) da acceso al metro, tranvía, ferri y funicular. Carga desde el primer día — los viajes en transporte público cuestan menos de 0.50€. La mejor época para visitar Estambul es primavera (abril-mayo) y otoño (septiembre-octubre): temperaturas agradables y menos aglomeraciones que en verano. El invierno también es viable y los precios bajan notablemente.</p>

<h2>Presupuesto orientativo</h2>
<p>Vuelo desde Madrid: 80-180€ ida y vuelta según temporada. Hotel en Sultanahmet o Beyoğlu: 50-90€/noche. Comer bien en Estambul sale muy barato: un almuerzo completo en el lado asiático no supera 8-12€/persona. La lira turca hace que muchos gastos sean sorprendentemente asequibles para el viajero europeo.</p>
""",

"guia-budva-montenegro": """
<h2>Qué ver en Budva</h2>
<p>El casco antiguo amurallado (Stari Grad) es la joya de la ciudad: calles de piedra, pequeñas plazas y vistas al mar desde las murallas. A pocos minutos en coche está Sveti Stefan, el famoso islote-hotel que es de las imágenes más reconocibles del Adriático. Puedes fotografiarlo desde la orilla — el acceso al interior es solo para huéspedes.</p>

<h2>Playas cercanas</h2>
<p>La Riviera de Budva tiene algunas de las mejores playas del Adriático sin las masificaciones de Croacia. Mogren Beach, a 15 minutos a pie desde el casco antiguo, es la favorita de los locales. Más al sur, Przno y Jaz (donde se hacen grandes festivales de música) son opciones excelentes. En agosto las playas se llenan — ve pronto por la mañana o elige días entre semana.</p>

<h2>Excursiones desde Budva</h2>
<p>El Lago de Skadar (el más grande de los Balcanes) está a 45 minutos en coche y merece medio día. La bahía de Kotor, declarada Patrimonio de la Humanidad, queda a una hora — sus murallas medievales y el ambiente genuinamente mediterráneo son difíciles de superar. Si tienes más tiempo, el Parque Nacional de Durmitor al norte ofrece montañas impresionantes y el Cañón del Tara.</p>

<h2>Cómo llegar y moverse</h2>
<p>El aeropuerto más cercano es Tivat (30 minutos en coche, vuelos desde varias ciudades europeas en verano). El aeropuerto de Podgorica queda a 60 kilómetros. Alquilar un coche es la mejor opción para explorar la costa — el transporte público funciona pero es lento. La carretera costera es espectacular pero estrecha: conduce con calma.</p>

<h2>Presupuesto: cuánto cuesta Montenegro</h2>
<p>Montenegro usa el euro aunque no es miembro de la UE. Los precios son notablemente más bajos que en Croacia o Italia. Un apartamento frente al mar en Budva sale por 40-70€/noche. Comer en un restaurante local (pescado fresco, carne a la brasa, queso kačkavalj) cuesta 12-20€ por persona. Una semana en la Costa de Montenegro sale fácilmente por 600-900€ todo incluido desde España.</p>

<h2>La mejor época para ir</h2>
<p>Junio y septiembre son el punto dulce: el mar ya está caliente (agua a 22-25°C), los precios son más bajos que en julio-agosto y la costa no está saturada de turistas. En julio y agosto hace mucho calor (35-38°C) y las playas se llenan, pero el ambiente es animado y los días muy largos.</p>
""",

"que-ver-en-roma-tres-dias": """
<h2>Día 1: la Roma Antigua</h2>
<p>Roma premia a quien planifica: las colas en los puntos turísticos pueden comerte horas de viaje si no reservas entrada con antelación. Empieza por el Coliseo, el Foro Romano y el Monte Palatino — se visitan con la misma entrada. Reserva con antelación y elige primera hora de la mañana para evitar el calor y las aglomeraciones del mediodía. Por la tarde, acércate a la Fontana di Trevi (mejor al atardecer, con menos gente) y la Piazza di Spagna.</p>

<h2>Día 2: el Vaticano y Trastevere</h2>
<p>Los Museos Vaticanos y la Capilla Sixtina son imprescindibles pero hay que reservar entrada online con semanas de antelación — las colas sin reserva pueden superar las tres horas. Dedica toda la mañana. Por la tarde, cruza el río hasta Trastevere: el barrio más bohemio de Roma, con restaurantes auténticos y calles de adoquín perfectas para perderse.</p>

<h2>Día 3: el Panteón, el Ghetto y el Pincio</h2>
<p>El Panteón (reserva obligatoria, 5€) es uno de los edificios mejor conservados de la Antigüedad — ver el óculo iluminar el interior es una experiencia única. A pocos pasos está la Piazza Navona. Por la tarde, sube a la colina del Pincio para las mejores vistas de la ciudad sin necesidad de pagar entrada a ningún museo. Termina el día en Campo de' Fiori, que se convierte en mercado por las mañanas y en zona de bares al atardecer.</p>

<h2>Cómo moverse por Roma</h2>
<p>Roma se recorre mejor a pie entre los principales monumentos, que están relativamente concentrados. El metro tiene solo dos líneas y no llega a muchos puntos turísticos. Los autobuses son más útiles pero pueden ir lentos por el tráfico. Los taxis tienen precio fijo desde el aeropuerto Fiumicino (48€ al centro). Evita los rickshaws turísticos — son caros e innecesarios.</p>

<h2>Dónde comer bien sin pagar de más</h2>
<p>Huye de los restaurantes con fotos plastificadas en la carta y mesas en la primera fila junto a los monumentos. Los mejores precios están dos o tres calles alejadas de los grandes focos turísticos. Un plato de pasta en Trastevere o Testaccio cuesta 10-14€. Para el desayuno, cualquier bar local con croissant y café espresso en barra sale por menos de 2€. La granita de limón en verano es una parada obligatoria.</p>

<h2>Presupuesto orientativo</h2>
<p>Vuelo desde Madrid: 60-150€ ida y vuelta. Hotel en zona céntrica: 90-160€/noche. Manutención: 30-45€/persona/día comiendo en restaurantes locales. Entradas principales (Coliseo, Vaticano, Panteón): ~50€/persona. Un fin de semana largo en Roma puede salir por 400-700€/persona dependiendo de la temporada.</p>
""",

"guia-fin-de-semana-mallorca": """
<h2>Día 1: Palma de Mallorca</h2>
<p>Mallorca es perfecta para una escapada corta: vuelos rápidos desde casi cualquier ciudad española y suficiente variedad para no aburrirte en 48-60 horas. Empieza por el centro histórico de Palma: la Catedral de Mallorca (La Seu), el Palacio de la Almudaina y el paseo marítimo. Por la tarde, pierde un par de horas en el barrio de Santa Catalina, lleno de bares y restaurantes con terraza.</p>

<h2>Día 2: Serra de Tramuntana y calas del norte</h2>
<p>Alquila un coche desde el primer día (25-45€/día) para aprovechar el tiempo. La carretera de la Serra de Tramuntana (Patrimonio de la Humanidad) hacia Valldemossa y Deià es uno de los recorridos más espectaculares de España. Come en alguno de los restaurantes del pueblo de Deià con vistas al mar y a las montañas. Por la tarde, baja hasta la Cala Tuent o el Puerto de Sóller para un baño en aguas turquesas.</p>

<h2>Las mejores playas según el tiempo que tengas</h2>
<p>Para playas a pocos minutos de Palma: Cala Major y Ca'n Pere Antoni. Para las más bonitas de la isla: Cala d'Or, Cala Mondragó (en un parque natural, aguas increíbles) y Es Trenc (la más salvaje, sin chiringuitos ni edificios). En julio y agosto las calas se llenan — ve antes de las 10 de la mañana o a última hora de la tarde.</p>

<h2>Cuándo ir y qué esperar</h2>
<p>Mayo, junio y septiembre son la mejor combinación de clima, precios y afluencia. En julio y agosto hace mucho calor (35°C) y los precios de hoteles y vuelos se disparan. Octubre es ideal para turismo rural y senderismo — el ambiente de la isla es mucho más tranquilo y auténtico. En invierno algunos hoteles cierran, pero los que abren tienen precios muy bajos y la isla es casi exclusivamente tuya.</p>

<h2>Dónde alojarse</h2>
<p>Palma para los que quieren moverse a pie y vida nocturna. Puerto de Pollença o Alcúdia para los que buscan playas tranquilas al norte. Sóller para los que prefieren montaña y ambiente más rural. Un hotel de 3 estrellas en Palma en temporada media sale por 80-130€/noche. En temporada alta los precios se multiplican — reserva con meses de antelación.</p>

<h2>Presupuesto orientativo</h2>
<p>Vuelo desde Madrid, Barcelona o Valencia: 40-100€ ida y vuelta. Hotel 3 estrellas en Palma en temporada media: 80-130€/noche. Coche de alquiler para el fin de semana: 50-90€. Comer bien en Mallorca: 15-25€/persona en restaurantes locales. Un fin de semana completo puede salir por 300-500€/persona.</p>
""",

"cuanto-cuesta-viajar-a-bali": """
<h2>Vuelo Madrid → Bali: cuánto cuesta y cómo ahorrar</h2>
<p>Bali tiene la reputación de ser barata, y en gran parte es cierta — pero solo si evitas las trampas turísticas. No hay vuelo directo desde España. Las rutas más habituales desde Madrid: vía Dubai (Emirates, ~550-750€, 16h totales) o vía Doha (Qatar Airways, ~550-800€). Los mejores precios aparecen con 3-5 meses de antelación y fuera de julio-agosto. Evita volar en Semana Santa — los precios se duplican.</p>

<h2>Alojamiento: desde 15€ hasta 500€ por noche</h2>
<p>Bali tiene opciones para todos los presupuestos. Un bungalow con piscina privada en Ubud o Canggu puede costar tan solo 40-60€/noche. Las villas más lujosas con personal incluido llegan a 300-500€/noche — pero divididas entre un grupo de amigos salen muy asequibles. Para mochileros, los hostels en Kuta o Seminyak tienen camas desde 8-15€. Reserva con anticipación para diciembre-enero (temporada alta) y julio-agosto.</p>

<h2>Comida: el presupuesto más sorprendente</h2>
<p>Comer en Bali es extraordinariamente barato si vas a los warung (restaurantes locales): un plato de nasi goreng (arroz frito) o mie goreng (fideos) cuesta 1-2€. El satay de pollo, las brochetas de carne o los platos de tofu son igual de baratos. Los mercados nocturnos en Seminyak o Ubud tienen decenas de opciones. Solo los restaurantes orientados a turistas occidentales llegan a precios europeos.</p>

<h2>Transporte dentro de Bali</h2>
<p>Alquilar una moto es lo más barato (5-8€/día) pero requiere carné internacional y experiencia en tráfico asiático. Los taxis Gojek y Grab (aplicaciones de transporte) son muy económicos y fiables — un trayecto de 20 km cuesta 3-5€. Alquilar un coche con conductor todo el día sale por 40-60€ y es ideal para visitar templos y arrozales fuera de los circuitos turísticos masivos.</p>

<h2>Presupuesto total por semana</h2>
<p>Un viaje de 10 días a Bali puede salir muy diferente según el estilo: mochilero básico (150-220€/semana todo excepto vuelo), viajero estándar con buen hotel y excursiones (350-500€/semana), o experiencia de lujo (1.000€+/semana). El vuelo es el mayor gasto. Una vez allí, los euros rinden mucho más que en cualquier destino europeo.</p>

<h2>¿Qué no incluir en el presupuesto de Bali?</h2>
<p>Los tratamientos de spa y masajes son increíblemente baratos (8-15€/hora en spas locales, 60-100€ en los de hoteles boutique). Las clases de surf en Kuta cuestan 20-35€ con instructor. Las excursiones organizadas al volcán Gunung Batur al amanecer salen por 40-60€ con transporte y guía. Todos estos extras son mucho más baratos que equivalentes en Europa.</p>
""",

"lisboa-fin-de-semana-barrios": """
<h2>Alfama: el barrio más antiguo</h2>
<p>Lisboa es una ciudad de colinas, miradores y tranvías históricos que se disfruta caminando despacio. El barrio de Alfama es el más antiguo: calles estrechas y empinadas que sobrevivieron al terremoto de 1755. Sube hasta el Castillo de San Jorge para una de las mejores vistas de la ciudad, y no te pierdas una sesión de fado en directo en alguna de las casas de fado del barrio — precio entre 20-35€ con consumición incluida.</p>

<h2>Bairro Alto y Chiado: el corazón cultural</h2>
<p>El Bairro Alto es el barrio de la vida nocturna y las pequeñas tascas con vino barato. De día, el Chiado adyacente tiene librerías históricas (la Livraria Bertrand, la más antigua del mundo en funcionamiento), galerías y cafés. El Miradouro de São Pedro de Alcântara ofrece una de las mejores vistas de la ciudad desde aquí.</p>

<h2>Belém: los Jerónimos y la Torre</h2>
<p>El barrio de Belém queda a 20 minutos en tranvía desde el centro y concentra tres visitas imprescindibles: el Monasterio de los Jerónimos (Patrimonio de la Humanidad), la Torre de Belém junto al Tajo y el Padrão dos Descobrimentos. Y, por supuesto, los pasteles de Belém originales en la Fábrica de Pastéis de Belém — pruébalos calientes con azúcar y canela, hay cola pero merece la pena.</p>

<h2>LX Factory y Mouraria</h2>
<p>El LX Factory es un antiguo complejo industrial reconvertido en mercado de diseñadores, restaurantes y estudios creativos. El domingo por la mañana tiene el mercado más interesante. El barrio de Mouraria, junto a Alfama, es el más multicultural de Lisboa: mezcla de cultura árabe, africana y portuguesa, con restaurantes auténticos y muy económicos.</p>

<h2>Cómo moverse</h2>
<p>El tranvía 28 (el histórico amarillo) recorre Alfama, Chiado y Bairro Alto — es turístico pero práctico. El metro llega a Belém y a los barrios modernos. Para las colinas, los elevadores (ascensores históricos) ahorran caminata. Un pase de 24h de transporte público cuesta 6.40€ e incluye tranvías, metro y autobuses. Lisboa también es perfecta para explorar en bicicleta eléctrica — varias empresas de alquiler por la ciudad.</p>

<h2>Presupuesto orientativo</h2>
<p>Vuelo desde Madrid: 50-120€ ida y vuelta. Alojamiento en zona céntrica: 70-130€/noche. Manutención: 20-35€/persona/día comiendo en pastelerías, tascas y restaurantes locales. Lisboa es bastante más barata que Madrid, Barcelona o París para estancias cortas.</p>
""",

"alquiler-coche-espana-que-mirar": """
<h2>La letra pequeña que nadie lee</h2>
<p>Alquilar un coche para una escapada parece sencillo hasta que llegas al mostrador y te ofrecen seguros adicionales, depósitos elevados o cargos que no esperabas. Los comparadores de coches (Rentalcars, Kayak, AutoEurope) muestran el precio base, pero el precio final puede subir notablemente si no sabes qué rechazar y qué aceptar.</p>

<h2>La franquicia del seguro: el punto clave</h2>
<p>El precio "barato" casi siempre incluye un seguro básico con franquicia alta (lo que pagarías tú en caso de daño). Comprueba el importe exacto: puede ser 800€, 1.500€ o incluso más. Tienes tres opciones para cubrirte: pagar el seguro sin franquicia de la propia compañía (normalmente 15-25€/día extra), usar una tarjeta de crédito con cobertura de alquiler incluida (Visa Premium, American Express Gold) o contratar una póliza independiente online antes del viaje (7-12€/día en empresas como WorldNomads o Carefree Travel).</p>

<h2>El depósito en tarjeta de crédito</h2>
<p>La mayoría de las compañías retienen entre 300€ y 1.500€ como depósito en la tarjeta de crédito del conductor principal. Esta cantidad queda bloqueada (no cobrada) hasta la devolución del coche. Importante: necesitas una tarjeta de crédito real, no de débito ni prepago — algunas compañías no aceptan Revolut o tarjetas virtuales para el depósito.</p>

<h2>Revisar el coche antes de salir</h2>
<p>Dedica 10 minutos a fotografiar el vehículo desde todos los ángulos antes de salir del parking, incluyendo los bajos, el techo y el interior. Envíate las fotos por email o WhatsApp para que queden con marca de tiempo. Comprueba que los rayones o golpes existentes están reflejados en el contrato — si no están anotados y te los imputan al volver, tendrás prueba gráfica para reclamar.</p>

<h2>Combustible: política "lleno por lleno"</h2>
<p>La opción más sencilla es recoger el coche con el depósito lleno y devolverlo lleno — el estándar habitual. Rechaza la oferta de "recoger lleno y devolver vacío" que muchas compañías hacen: pagas el combustible a precio de compañía (siempre más caro) y rara vez consumes todo el depósito. Si te ofrecen recoger el coche con el depósito a mitad, exige entregarlo así o paga solo la diferencia real.</p>

<h2>Qué compañías usar y cuáles evitar</h2>
<p>Las marcas más fiables para España son Europcar, Hertz, Avis y Enterprise para garantías, aunque con precios más altos. Entre las de bajo coste con buena reputación están Goldcar, Sixt y Record Go. Las comparadoras de precio más completas son Rentalcars.com (incluye precio de seguro en muchos casos) y AutoEurope. Evita compañías con nombre desconocido que aparecen en comparadoras con precios muy por debajo del mercado.</p>
""",

"presupuesto-real-fin-de-semana-madrid": """
<h2>Alojamiento: dónde buscar y qué esperar pagar</h2>
<p>Madrid es de los destinos urbanos con mejor relación calidad-precio de España si sabes dónde mirar. Un hotel de 3 estrellas bien situado (Sol, Atocha, Chamberí) ronda los 70-110€/noche en temporada media. Los apartamentos en Lavapiés o Malasaña salen algo más baratos y dan más independencia. Para un fin de semana de 2 noches, el alojamiento para dos personas suma 140-220€.</p>

<h2>Transporte: llegar y moverse por Madrid</h2>
<p>El AVE desde Barcelona: 50-90€ ida y vuelta si reservas con días de antelación. Desde Sevilla: 45-80€. Desde Valencia: 40-70€. En avión, los vuelos con Vueling, Iberia o Ryanair salen más baratos si vuelas a Barajas — el aeropuerto T4 tiene conexión directa en metro (Metro Línea 8, 2.50€ con suplemento de aeropuerto). Dentro de Madrid, el metro es rápido y económico: un billete cuesta 1.50-2€ según zonas.</p>

<h2>Comer y beber: el coste real</h2>
<p>El menú del día en Madrid (primer plato + segundo + postre + bebida) sale por 11-14€ en casi cualquier barrio fuera del centro turístico. El mercado de San Miguel y el Mercado de Antón Martín son opciones de calidad a precios razonables para tapear. Una caña de cerveza o una copa de vino en la mayoría de bares de Malasaña, Chueca o La Latina cuesta 2-3€. Comer mal en Madrid es difícil; comer muy caro también, si sabes dónde ir.</p>

<h2>Qué hacer: las mejores opciones gratuitas y de pago</h2>
<p>El Museo del Prado y el Reina Sofía tienen acceso gratuito las últimas dos horas del día (18h-20h de lunes a sábado, 19h-21h domingos en el Prado). El Retiro, la Casa de Campo y el Madrid Río son totalmente gratuitos. Para una tarde de museos, el Pase del Arte (Prado + Reina Sofía + Thyssen) cuesta 30€ y da acceso durante un año.</p>

<h2>Presupuesto total para dos personas, dos noches</h2>
<p>Alojamiento (2 noches, habitación doble): 140-220€. Transporte (ida y vuelta, metro incluido): 80-160€ según origen. Comidas (4 comidas + cenas + desayunos): 120-180€ para dos. Entradas y ocio: 0-60€ según lo que hagas. <strong>Total estimado: 340-620€ para dos personas</strong>, un fin de semana muy completo en una de las mejores capitales de Europa.</p>
""",

"berlin-dos-dias-que-ver": """
<h2>Día 1: el centro histórico y político</h2>
<p>Berlín es una ciudad enorme y con mucha historia, pero en dos días bien organizados se puede ver lo esencial. Empieza en la Puerta de Brandeburgo, símbolo de la ciudad, y camina hasta el Reichstag (la cúpula de cristal tiene vistas espectaculares — reserva entrada gratuita con antelación en el sitio web oficial). Sigue hacia el Memorial del Holocausto y la Isla de los Museos al atardecer.</p>

<h2>El Muro de Berlín</h2>
<p>El East Side Gallery es el tramo de muro más largo conservado (1,3 km) y el más fotografiado, con murales políticos de artistas de todo el mundo. El Checkpoint Charlie, aunque ahora muy turístico, merece una parada breve — el museo adyacente es interesante pero caro (15€). Si quieres algo más auténtico, el Memoriale del Muro en Bernauer Strasse da mucho más contexto histórico y la entrada es gratuita.</p>

<h2>Día 2: Kreuzberg, Neukölln y la escena alternativa</h2>
<p>Berlín tiene una de las escenas culturales más vibrantes de Europa. El barrio de Kreuzberg mezcla cultura turca, galerías independientes y una oferta gastronómica increíble. El Mercado Turco del Canal (martes y viernes) es una experiencia imprescindible. Neukölln, el barrio más de moda, tiene cafés con encanto, tiendas vintage y restaurantes de todas las culturas del mundo a precios muy asequibles.</p>

<h2>Cómo moverse</h2>
<p>La tarjeta de 48h de transporte público (AB) cuesta 20€ y cubre metro (U-Bahn), tren urbano (S-Bahn) y autobús dentro de las zonas A y B, que incluyen todos los puntos de interés. Berlín también tiene 1.000 km de carril bici — alquilar una bicicleta (10-15€/día) es la mejor forma de ver los barrios de forma relajada.</p>

<h2>Dónde comer sin gastar de más</h2>
<p>El döner berlinés es legendario: nació aquí y sale por 4-6€ en cualquier kiosko del mercado o callejero. El Mercado de Mauer (Mauerpark, domingos) tiene puestos de comida de todo el mundo. Para comer sentado, los restaurantes vietnamitas y turcos en Kreuzberg dan muy bien por muy poco. Las Currywurst (salchicha con curry) son el fast food local por excelencia: 2-3€ en los Imbiß de toda la ciudad.</p>

<h2>Presupuesto orientativo</h2>
<p>Vuelo desde Madrid: 60-140€ ida y vuelta. Hotel o Airbnb en Mitte, Prenzlauer Berg o Kreuzberg: 70-120€/noche. Manutención muy completa: 25-40€/persona/día. Berlín es más barata que París o Londres para alojamiento y comida — uno de los mejores destinos de fin de semana de Europa por precio-calidad.</p>
""",

"barcelona-en-un-dia": """
<h2>Mañana: Sagrada Família y Eixample</h2>
<p>Si tienes una sola jornada en Barcelona, lo mejor es no intentar verlo todo y centrarte en tres zonas que se pueden encadenar bien. Empieza temprano en la Sagrada Família — reserva la entrada online con antelación, las colas sin reserva previa pueden superar la hora en temporada alta. Dedica al menos 90 minutos a recorrerla con calma. Pasea después por el Eixample para ver la arquitectura modernista: la Casa Batlló y la Casa Milà (La Pedrera) están en el mismo paseo de Gràcia.</p>

<h2>Mediodía: El Born y el Barrio Gótico</h2>
<p>Coge el metro hasta Jaume I y dedica el mediodía al Barrio Gótico y El Born. La Catedral de Barcelona, la Plaça Reial y la Basílica de Santa Maria del Mar (gratuita y preciosa) están todas a 10 minutos a pie entre ellas. Para comer, los mercados del Born o la Boqueria en Las Ramblas son opciones clásicas — aunque la Boqueria tiene fama de ser cara y turística, los puestos del fondo siguen siendo auténticos y económicos.</p>

<h2>Tarde: el Poble Sec, Montjuïc o la Barceloneta</h2>
<p>En función del tiempo y tus preferencias: sube a Montjuïc en telefèric (10€ ida y vuelta) para las mejores vistas de la ciudad y el Puerto. O baja a la Barceloneta para un paseo por la playa y una cerveza con vistas al mar. El barrio de Poble Sec y la calle Parlament tiene los mejores bares de tapas sin precios turísticos. Por la noche, el barrio de Gràcia tiene ambiente local y restaurantes tranquilos alejados de los circuitos masivos.</p>

<h2>Trucos para un solo día</h2>
<p>La T-Casual de metro (10 viajes, 11.35€) cubre toda la zona metropolitana y se puede compartir entre varias personas. Evita Las Ramblas para comprar o comer — los precios son turísticos y la calidad normalmente inferior a lo que encontrarás dos calles más allá. El bus turístico no merece la pena en un solo día — el metro y los pies son más eficientes. Lleva agua: Barcelona en verano supera los 32°C y caminarás mucho.</p>

<h2>Cuándo visitar Barcelona</h2>
<p>Mayo y octubre son los meses ideales: clima agradable, precios más bajos y menos saturación que en pleno verano. Julio y agosto son los meses más caros y calurosos, con playas y monumentos al límite. Semana Santa y los puentes nacionales también elevan mucho los precios del alojamiento.</p>
""",

"escapadas-rurales-espana-desconectar": """
<h2>Cuándo elegir una escapada rural</h2>
<p>No todo viaje tiene que implicar un avión y una lista interminable de monumentos. A veces lo que más descansa es un pueblo pequeño, naturaleza alrededor y poco más que hacer que pasear y comer bien. España tiene una densidad de paisajes y pueblos medievales que pocos países pueden igualar en Europa.</p>

<h2>Ainsa (Huesca)</h2>
<p>Un casco histórico medieval prácticamente intacto, rodeado por los Pirineos. Punto de partida perfecto para rutas de senderismo por el Parque Nacional de Ordesa y Monte Perdido, a media hora en coche. El pueblo tiene tiendas de productos locales (quesos, embutidos del Pirineo, miel) y restaurantes con cocina aragonesa sólida. En invierno la nieve transforma el paisaje; en primavera el deshielo llena los barrancos y los Pirineos lucen en su esplendor.</p>

<h2>Albarracín (Teruel)</h2>
<p>Considerado uno de los pueblos más bonitos de España, y con razón: sus casas de fachadas rojo óxido encajadas en la roca sobre el río Guadalaviar son únicas. El centro histórico amurallado se recorre en un par de horas pero el ambiente invita a quedarse más. A 30 km están los yacimientos rupestres de arte prehistórico de Albarracín, Patrimonio de la Humanidad.</p>

<h2>Rupit (Barcelona)</h2>
<p>Un pueblo medieval en el Prepirineo catalán que parece un set de película de época. Casas de piedra del siglo XVII, un puente colgante sobre un río y sin apenas turismo masivo. Está a 90 minutos de Barcelona, lo que lo hace perfecto para una escapada express de fin de semana. El entorno natural del Collsacabra tiene rutas de senderismo para todos los niveles.</p>

<h2>Frigiliana (Málaga)</h2>
<p>El pueblo blanco más bonito de la Axarquía, a 7 km de Nerja y a menos de una hora de Málaga capital. Sus calles en cuesta llenas de macetas con flores y azulejos árabes forman uno de los escenarios más fotogénicos del sur de España. Perfecta combinación de pueblo de montaña y playa cercana para los que no quieren elegir.</p>

<h2>Cómo organizarlo: lo que necesitas saber</h2>
<p>La mayoría de estas escapadas requieren coche propio — el transporte público en zonas rurales de España es limitado. Las casas rurales (turismo rural) suelen alquilarse por noches completas y los precios son sorprendentemente razonables: 60-120€/noche para 2-4 personas. Reserva con tiempo en puentes y festivos, ya que estas escapadas son cada vez más populares entre los españoles.</p>
""",

"budapest-que-ver-balnearios-y-rio": """
<h2>Buda: el lado histórico y elevado</h2>
<p>Budapest es en realidad dos ciudades unidas por el Danubio: Buda, la parte histórica y elevada, y Pest, la zona llana y moderna. Sube al Castillo de Buda y al Bastión de los Pescadores para tener la mejor panorámica de la ciudad y del Parlamento al otro lado del río. La Iglesia de Matías, junto al Bastión, tiene uno de los interiores más ornamentados de Europa Central. La subida a pie desde el río cuesta 30 minutos — también hay funicular (turístico pero cómodo).</p>

<h2>Pest: el Parlamento, la Gran Avenida y el Mercado Central</h2>
<p>El Parlamento de Budapest, a orillas del Danubio, es uno de los edificios neogóticos más espectaculares del mundo — las visitas guiadas al interior salen por 8-18€ según temporada. La Gran Avenida (Andrássy Út, Patrimonio de la Humanidad) lleva desde el centro hasta el Bosque Ciudad y el Parque de los Héroes. El Mercado Central (Nagyvásárcsarnok) es el mejor lugar para probar la gastronomía húngara: langos, paprikás, salami húngaro y foie gras a precios muy razonables.</p>

<h2>Los balnearios: la experiencia imprescindible de Budapest</h2>
<p>Budapest tiene más de 100 fuentes termales y varios baños históricos impresionantes. Los más famosos: Széchenyi (en el Bosque Ciudad, el más grande y fotogénico, con piscinas exteriores e interiores), Gellért (en un edificio art nouveau espectacular, más caro pero más elegante) y Rudas (más auténtico y menos turístico, con azulejos otomanos originales del siglo XVI). La entrada suele rondar los 18-28€ según el baño y los servicios.</p>

<h2>El crucero por el Danubio</h2>
<p>Ver Budapest desde el agua al atardecer o de noche (cuando se iluminan el Parlamento, el Castillo y los puentes) es una de las experiencias más memorables de la ciudad. Los cruceros nocturnos de 1-2 horas cuestan 15-35€ según la empresa y si incluye cena o bebidas. Reserva online para conseguir los mejores asientos en la cubierta.</p>

<h2>Cuándo ir y presupuesto</h2>
<p>La primavera (abril-mayo) y el otoño (septiembre-octubre) son la mejor época: temperaturas agradables y precios más bajos que en verano. Diciembre tiene un mercado de Navidad precioso en la Plaza Vörösmarty. Budapest es uno de los destinos europeos más asequibles: vuelo desde Madrid 80-160€, hotel céntrico 60-100€/noche, comida en restaurantes locales 8-15€/persona. Un fin de semana completo puede salir por 300-450€/persona.</p>
""",

"vuelos-baratos-madrid-venecia": """
<h2>¿Qué aeropuerto de Venecia usar?</h2>
<p>¿Buscas vuelos baratos de Madrid a Venecia? Madrid-Venecia es una de las rutas europeas con más opciones de bajo coste. Venecia tiene dos aeropuertos: el Marco Polo (VCE), a 13 km del centro y conectado por barco lanzadera (30 min, ~15€) o autobús, y el Treviso (TSF), a 40 km, usado principalmente por Ryanair. Treviso tiene vuelos más baratos pero el traslado suma tiempo y dinero — calcula bien el coste real total.</p>

<h2>Cuándo buscar y cómo conseguir los mejores precios</h2>
<p>La ruta Madrid-Venecia tiene opciones de low cost todo el año. Las mejores tarifas aparecen entre 6 y 10 semanas antes del viaje para escapadas de fin de semana, y entre 3 y 5 meses antes para viajes de temporada alta (carnaval de febrero, verano, Navidad). Los martes y miércoles suelen ser los días más baratos para volar. Usa Google Flights con el calendario de precios para ver qué semanas son más económicas.</p>

<h2>Aerolíneas que vuelan Madrid-Venecia</h2>
<p>Vueling tiene vuelos directos a Marco Polo desde el aeropuerto T4 de Barajas con buena frecuencia. Ryanair vuela a Treviso con precios desde 19-40€ en temporada baja. Iberia y Air Europa también cubren la ruta pero generalmente a precios más altos. Para temporada alta (junio-agosto), reserva con 3-4 meses de antelación — los precios se disparan en julio y en Semana Santa.</p>

<h2>Alternativas: combinar avión y tren</h2>
<p>Una opción que funciona bien es volar a Milán (Bergamo con Ryanair o Malpensa con Vueling) y coger el tren a Venecia (90 min, 15-30€ en Frecciarossa). Los vuelos Madrid-Milán suelen ser más frecuentes y a veces más baratos que los directos a Venecia. Esta opción también permite hacer una parada en Milán.</p>

<h2>Lo que no te dices cuando compras el billete barato</h2>
<p>Los vuelos de 30€ rara vez se quedan en 30€. Suma: equipaje de cabina (8-15€ con Ryanair o Vueling), asiento asignado (5-15€), tasas aeroportuarias (ya incluidas en casi todos los buscadores). El precio realista para un vuelo de bajo coste Madrid-Venecia con equipaje de mano y asiento es 50-90€. Sigue siendo barato para una de las ciudades más espectaculares del mundo.</p>

<h2>Cuándo ir a Venecia</h2>
<p>Septiembre y octubre son perfectos: el calor del verano baja, el acqua alta (inundaciones) no ha empezado todavía y los precios de hoteles caen. Noviembre y diciembre tienen el acqua alta frecuente pero la ciudad cubierta de niebla tiene un encanto diferente. Evita julio-agosto si puedes: temperaturas muy altas, humedad extrema y turismo masivo. El Carnaval (enero-febrero) es una experiencia única pero los precios de alojamiento se multiplican por 3.</p>
""",

"tokio-primera-vez-que-saber": """
<h2>Los distritos imprescindibles</h2>
<p>Tokio impresiona por el contraste: barrios tradicionales con templos centenarios conviven con zonas como Shibuya o Akihabara, llenas de luces de neón. Shibuya y Shinjuku son el corazón moderno — el cruce de Shibuya es el más concurrido del mundo y los rascacielos iluminados de Shinjuku son la imagen más reconocible de Tokio nocturno. No te pierdas el mercado Tsukiji (exterior, el interior cerró) para desayunar sushi fresco a precios locales.</p>

<h2>Asakusa y el Tokio tradicional</h2>
<p>Asakusa es el barrio más antiguo y tradicional de la ciudad. El Templo Senso-ji, el más visitado de Japón, vale la pena verlo a primera hora de la mañana cuando los turistas aún no han llegado. La calle Nakamise, que lleva hasta el templo, tiene tiendas de souvenirs artesanales y snacks japoneses tradicionales. Desde Asakusa, puedes ver el contraste visual con el Tokyo Skytree (la torre más alta de Japón) de fondo.</p>

<h2>Transporte: el sistema más eficiente del mundo</h2>
<p>El metro de Tokio puede intimidar al principio pero es extremadamente fiable. Consigue una IC Card (Suica o Pasmo) recargable desde el aeropuerto — funciona en todo el transporte público de la ciudad. Los viajes en metro cuestan entre 1.50-3€ según la distancia. El JR Pass (tren de alta velocidad por todo Japón) solo es rentable si viajas también fuera de Tokio. Para la primera visita, el metro y los trenes JR locales son suficientes.</p>

<h2>Comida: qué comer y cuánto gastar</h2>
<p>Comer en Tokio es una experiencia en sí misma. Los ramen desde 8-12€ en cualquier ramenería son extraordinarios. El sushi en conveyor belt (kaiten-zushi) sale por 15-25€ por persona. Las bento box de los supermercados 7-Eleven o Lawson son sorprendentemente buenas y cuestan 3-6€. Para comer "caro" como un local, un omakase (menú del chef) en un restaurante de sushi sin estrellas Michelin empieza en 50-80€ por persona.</p>

<h2>Presupuesto y cuándo ir</h2>
<p>Vuelo desde Madrid (con escala, 12-14h): 600-900€ ida y vuelta. Hotel en zona céntrica (Shinjuku, Ginza, Asakusa): 80-150€/noche. Manutención diaria: 30-50€/persona comiendo bien. La primavera (sakura, finales de marzo a mediados de abril) y el otoño (koyo, mediados de noviembre) son las temporadas más bonitas pero también las más caras. Junio tiene mucha lluvia. Enero-febrero es la temporada más barata.</p>
""",

"mejor-epoca-viajar-canarias": """
<h2>Octubre a abril: la temporada para escapar del frío peninsular</h2>
<p>Canarias es de los pocos destinos europeos donde se puede viajar en cualquier mes del año sin miedo al mal tiempo. Si vives en la península y quieres escapar del invierno, esta es la temporada estrella. Las temperaturas se mantienen entre 18°C y 24°C, el agua del mar entre 20-22°C, y los precios de hotel y vuelos son más bajos que en verano (excepto Navidad, Reyes y Semana Santa). Enero y febrero son los meses más baratos de todo el año.</p>

<h2>Julio y agosto: verano en Canarias</h2>
<p>Las temperaturas suben hasta 28-32°C en los valles y zonas bajas. El calor es seco y soportable comparado con la España peninsular, y la brisa atlántica hace que se sienta menos agobiante. Es la temporada alta turística, con precios de vuelo y hotel disparados. El principal inconveniente: playas muy concurridas, especialmente en Gran Canaria (Maspalomas) y Tenerife (Los Cristianos, Playa de las Américas).</p>

<h2>Cuál elegir: isla a isla</h2>
<p>Tenerife tiene el clima más suave y variado (norte verde y fresco, sur seco y soleado). Gran Canaria es perfecta para playas y tiene la capital más animada (Las Palmas). Lanzarote y Fuerteventura son las más áridas y tienen menos lluvia durante todo el año — ideales para sol garantizado. La Palma, La Gomera y El Hierro son las islas con más naturaleza y menos turismo masivo. Viaja a estas tres en primavera o otoño para los mejores senderos.</p>

<h2>Semana Santa y Navidades: precio máximo</h2>
<p>Son las dos temporadas con los precios más altos del año. Un vuelo Madrid-Tenerife en Semana Santa puede superar los 200€ ida y vuelta por persona. Si puedes, ve justo antes o justo después: la semana previa a la Semana Santa tiene precios mucho más bajos y el tiempo exactamente igual. Lo mismo aplica para las Navidades — la primera semana de enero suele tener precios muy razonables.</p>

<h2>Resumen por mes</h2>
<p>Enero-febrero: más barato, clima agradable, pocas nubes, playas tranquilas. Marzo-mayo: primavera perfecta, precio medio, campo en flor (sobre todo La Palma). Junio: buen momento antes de que suba el turismo. Julio-agosto: calor máximo, precios máximos, mucha gente. Septiembre-octubre: el mejor equilibrio calidad-precio. Noviembre-diciembre: excepto Navidades, temporada muy tranquila y económica.</p>
""",

"hoteles-baratos-nueva-york-donde-alojarse": """
<h2>Los mejores barrios para alojarse según tu presupuesto</h2>
<p>Alojarse en Nueva York puede costar desde 80€ hasta 800€ la noche según el barrio, la época y el tipo de alojamiento. Midtown Manhattan es el más céntrico (a 5 minutos de Times Square, el MoMA y Central Park) pero también el más caro: 150-250€/noche en temporada media. Para dormir más barato sin renunciar a buena ubicación, estas son las mejores alternativas.</p>

<h2>Lower East Side y East Village</h2>
<p>El barrio más de moda de Manhattan para los que quieren ambiente local sin pagar precios de Midtown. Hotels boutique y hostels con camas dobles desde 80-120€. A poca distancia del metro y con excelente oferta gastronómica: desde dim sum económico en Chinatown hasta restaurantes de moda del LES. Los viernes y sábados puede haber ruido nocturno — lleva tapones si eres sensible.</p>

<h2>Brooklyn: Williamsburg y Park Slope</h2>
<p>Cruzar el Puente de Brooklyn (a pie, 30 minutos) es una experiencia en sí misma. Williamsburg tiene hoteles y apartamentos desde 90-150€/noche, con más espacio y diseño que los hoteles de Manhattan al mismo precio. Park Slope es más residencial y tranquilo — perfecto para viajes en familia. El metro conecta bien con Manhattan (20 minutos a Times Square).</p>

<h2>Queens: Astoria y Long Island City</h2>
<p>Astoria es el barrio multicultural con más personalidad de Queens — cocina griega, brasileña, y mucho más a precios de barrio. Long Island City (LIC) tiene vistas espectaculares de Manhattan y hoteles a 80-130€/noche. El metro E o M llega a Midtown en menos de 15 minutos. Es una de las opciones más inteligentes para Nueva York si el presupuesto de alojamiento es ajustado.</p>

<h2>Nueva Jersey (Jersey City y Hoboken)</h2>
<p>La opción más barata con acceso fácil a Manhattan. El PATH train conecta Jersey City con el World Trade Center en 8 minutos y con Midtown en 20. Los hoteles aquí cuestan un 30-40% menos que equivalentes en Manhattan. Las vistas del skyline desde la orilla del Hudson son de las mejores de la ciudad — gratis.</p>

<h2>Cuándo reservar y cuánto esperar pagar</h2>
<p>Nueva York no tiene una temporada baja real, pero noviembre (fuera de Acción de Gracias), enero y febrero tienen los precios más bajos. El Maratón de Nueva York (primer domingo de noviembre) y el Año Nuevo llenan la ciudad. Reserva con 2-3 meses de antelación para temporada alta. Un hotel de 3 estrellas en Manhattan cuesta 130-220€/noche en temporada media; en Brooklyn o Queens, el mismo presupuesto da una habitación bastante más grande y cómoda.</p>
""",

"viajar-en-pareja-con-poco-presupuesto": """
<h2>Elige temporada media, no solo destino barato</h2>
<p>Viajar en pareja no tiene que significar gastar de más. El mismo destino puede costar la mitad fuera de temporada alta. Mayo, junio y septiembre suelen ofrecer buen clima en gran parte de Europa con precios mucho más bajos que julio-agosto. Para playas del Mediterráneo, septiembre es el mes perfecto: agua caliente, mucho menos calor y precios de alojamiento un 30-40% más bajos.</p>

<h2>Cómo dividir los gastos de forma inteligente</h2>
<p>En pareja, algunos gastos se comparten directamente (alojamiento, coche, alquiler de apartamento) mientras otros no. Para el alojamiento, un apartamento siempre sale más barato que dos habitaciones de hotel separadas — y da más privacidad. Un coche de alquiler dividido entre dos tiene el mismo coste que el transporte público para dos personas en muchos destinos. Planifica qué gastos se pueden compartir antes de salir.</p>

<h2>Destinos de alto impacto a bajo coste</h2>
<p>Para una escapada romántica sin gastar de más, algunos destinos ofrecen una experiencia excepcional a precios muy razonables: Praga (vuelos baratos desde España, hoteles desde 60€, cena con vino por 25€ para dos), Oporto (a 1h en avión, una de las ciudades más bonitas de Europa a precios muy contenidos), Algarve en primavera (playa, senderismo y gastronomía sin los precios del verano), o Marrakech (experiencia completamente diferente, económica y a 3h de vuelo desde Madrid).</p>

<h2>Comer bien sin gastar de más</h2>
<p>Busca los mercados de productores locales y los restaurantes alejados dos calles de los monumentos — la calidad no baja y el precio cae significativamente. En muchos destinos europeos, el menú del mediodía es la mejor relación calidad-precio: primer plato, segundo, postre y bebida por 10-15€/persona. Cocinar una cena en el apartamento de vez en cuando (compra en supermercado local con productos de la zona) es la cena más económica y a menudo la más memorable.</p>

<h2>El mejor "lujo barato" en pareja</h2>
<p>Algunos caprichos son muy asequibles si se eligen bien: un spa o hammam local cuesta una fracción de lo que cobraría en un hotel (8-20€ por persona en destinos como Budapest, Estambul o Marrakech). Una noche en un hotel con desayuno especial para celebrar algo cuesta mucho menos entre semana que en fin de semana. Un picnic con productos del mercado local en un parque bonito puede superar en experiencia a cualquier restaurante turístico.</p>

<h2>Herramientas para encontrar los mejores precios</h2>
<p>Para vuelos: Google Flights con la opción de mapa de precios permite ver qué destinos son baratos en tus fechas. Para alojamiento: Booking.com tiene el "precio genio" para usuarios registrados; Airbnb sigue siendo imbatible para apartamentos completos; Hotels.com acumula puntos para noches gratis. Para transporte en destino: Omio y Trainline para trenes europeos; Rentalcars para coches. Actividades: Airbnb Experiences y GetYourGuide tienen descuentos frecuentes para reserva con antelación.</p>
""",

"bangkok-primera-vez-guia-rapida": """
<h2>Qué ver en Bangkok: lo imprescindible</h2>
<p>Bangkok suele ser la puerta de entrada a Tailandia, y aunque al principio puede abrumar por el calor, el tráfico y el ritmo, es una de las ciudades con mejor relación calidad-precio de Asia. El Gran Palacio y el Wat Phra Kaew (Templo del Buda de Esmeralda) son el conjunto más visitado — llevan hombros y rodillas cubiertos o compran un sarong en la entrada. A pocos minutos a pie está el Wat Pho con el Buda Reclinado de 46 metros de largo.</p>

<h2>El río Chao Phraya y los canales (klongs)</h2>
<p>Bangkok se entiende mucho mejor desde el agua. El ferry público por el río Chao Phraya (20-30 baht, menos de 1€) conecta los principales templos y el barrio de Chinatown. Para los canales (klongs), un paseo en lancha de cola larga por las zonas más tradicionales de Thonburi (la orilla opuesta del río) muestra el Bangkok que existía antes de los rascacielos. Negocia el precio del barco antes de subir — 300-500 baht/hora es un precio razonable.</p>

<h2>Chatuchak y el mercado de fin de semana</h2>
<p>El mercado de Chatuchak (sábado y domingo) es el mercado de fin de semana más grande del mundo: 35 acres, más de 15.000 puestos y todo lo imaginable. Ropas, artesanía, comida, plantas, animales, antigüedades. Ve temprano por la mañana (antes de las 10) para evitar el calor máximo y las aglomeraciones. El metro BTS llega directamente.</p>

<h2>Comida callejera: la mejor experiencia de Bangkok</h2>
<p>La comida callejera de Bangkok tiene fama mundial y los precios son increíbles. Un pad thai en un puesto callejero cuesta 40-60 baht (1-1.50€). Una sopa de fideos, unos satay o un mango con arroz pegajoso no superan los 80 baht. El mercado nocturno de Yaowarat (Chinatown) es el mejor lugar para cenar bien gastando poco. Para gastronomía más elaborada, el barrio de Silom tiene restaurantes excelentes por 150-300 baht por persona.</p>

<h2>Cómo moverse y presupuesto</h2>
<p>El BTS (metro elevado) y el MRT (metro subterráneo) cubren bien las zonas modernas y turísticas. Los tuk-tuks son fotogénicos pero siempre negocia el precio antes — pueden ser una trampa para turistas. Las aplicaciones Grab y Bolt funcionan bien como alternativa fiable a los taxis. Bangkok es extraordinariamente barata: hotel de 3 estrellas desde 30-60€/noche, manutención completa por 15-25€/día/persona. Un vuelo desde Madrid (con escala) cuesta 500-750€ ida y vuelta según la temporada.</p>
""",

"viajar-low-cost-trucos-vuelos-baratos": """
<h2>La antelación correcta: ni demasiado pronto ni demasiado tarde</h2>
<p>Hay mucho mito alrededor de cómo encontrar vuelos baratos. El punto dulce real está entre 6 y 10 semanas antes del viaje para vuelos nacionales y europeos, y 3-5 meses antes para vuelos de larga distancia. Comprar con un año de antelación raramente es la mejor opción para destinos de corto y medio radio. Las aerolíneas lanzan precios más baratos en el período intermedio, cuando el avión todavía tiene muchos asientos vacíos.</p>

<h2>Usa el calendario de precios de Google Flights</h2>
<p>Google Flights tiene una función de "vista de cuadrícula" que muestra los precios para todas las combinaciones de fechas del mes. Si tienes flexibilidad de 2-3 días en tus fechas, esta herramienta puede ahorrarte entre 30 y 100€ en un vuelo europeo. También permite activar alertas de precio para rutas específicas — te avisa por email cuando el precio baja a un umbral que tú defines.</p>

<h2>Vuelos de conexión vs directos</h2>
<p>Los vuelos con escala suelen ser considerablemente más baratos que los directos, especialmente en rutas de larga distancia. Para destinos en Asia o América, añadir una escala de 2-3 horas puede suponer ahorros de 150-300€/persona. Para vuelos europeos de menos de 3 horas, el ahorro suele ser menor y el tiempo perdido no merece la pena. Comprueba el tiempo mínimo de escala: 90 minutos es el mínimo razonable para vuelos internacionales, 60 minutos para conexiones dentro del espacio Schengen.</p>

<h2>Equipaje: el coste que nadie cuenta</h2>
<p>El billete de bajo coste de 25€ puede convertirse en 70€ si no tienes en cuenta el equipaje. Ryanair y Vueling cobran entre 8 y 25€ por maleta de cabina (según antelación de la reserva). Facturar una maleta suma 15-40€ por trayecto. Si viajas una semana o menos, aprende a viajar solo con mochila de 10kg — pasa por todos los controles sin pagar extra en ninguna aerolínea low cost.</p>

<h2>Combinar aerolíneas y aeropuertos alternativos</h2>
<p>Para destinos grandes (Londres, París, Roma, Berlín), los aeropuertos secundarios suelen tener vuelos más baratos. Stansted para Londres (45 min en tren al centro), Beauvais para París (75 min en autobús), Ciampino para Roma (40 min en autobús), Schönefeld/BER para Berlín. Suma siempre el coste y el tiempo del traslado al precio del vuelo para comparar de verdad con los aeropuertos principales.</p>

<h2>El truco de los buscadores: no solo Skyscanner</h2>
<p>Ningún buscador tiene todos los vuelos. Skyscanner y Google Flights son los más completos, pero algunas aerolíneas no aparecen en todos los comparadores. Ryanair vende algunos vuelos exclusivamente en su web. Iberia y Vueling a veces tienen tarifas en su web directa mejores que en comparadores. Después de encontrar el precio en un buscador, entra en la web directa de la aerolínea y comprueba si el precio es el mismo o mejor.</p>
""",

}

def update_post_content(slug, extra_html):
    """Añade el HTML extra al final del contenido existente."""
    conn = psycopg2.connect(config.DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT content FROM posts WHERE slug = %s", (slug,))
    row = cur.fetchone()
    if not row:
        print(f"  SKIP (not found): {slug}")
        cur.close()
        conn.close()
        return
    current = row[0] or ""
    new_content = current.rstrip() + "\n" + extra_html.strip()
    cur.execute("UPDATE posts SET content = %s WHERE slug = %s", (new_content, slug))
    conn.commit()
    cur.close()
    conn.close()
    print(f"  OK: {slug}")

if __name__ == "__main__":
    print(f"Expandiendo {len(EXPANSIONS)} artículos...")
    for slug, html in EXPANSIONS.items():
        update_post_content(slug, html)
    print("Hecho.")
