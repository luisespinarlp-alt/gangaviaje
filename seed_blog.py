"""
Script de un solo uso: inserta el lote inicial de artículos del blog de GangaViaje.
Ejecutar con: python3 seed_blog.py
"""

import database

POSTS = [
    {
        "slug": "mejor-epoca-viajar-canarias",
        "title": "¿Cuál es la mejor época para viajar a Canarias?",
        "category": "playa",
        "image_url": "https://images.unsplash.com/photo-1559827260-dc66d52bef19?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Las Islas Canarias tienen buen clima todo el año, pero hay meses claramente mejores según lo que busques: playa tranquila, fiestas o senderismo.",
        "content": """
<p>Canarias es de los pocos destinos europeos donde se puede viajar literalmente en cualquier mes del año sin miedo al mal tiempo. Aun así, no todos los meses son iguales según lo que busques.</p>

<h2>Octubre a abril: la mejor opción para huir del frío</h2>
<p>Si vives en la península y quieres escapar del invierno, esta es la temporada estrella. Las temperaturas se mantienen entre 18°C y 24°C, el agua del mar sigue templada por la inercia del verano, y los precios de hoteles bajan respecto a julio-agosto. Tenerife y Gran Canaria reciben en estos meses a gran parte de su turismo del norte de Europa.</p>

<h2>Mayo y junio: la mejor relación precio-clima</h2>
<p>Antes de que empiece la temporada alta de verano, mayo y junio ofrecen días largos, buen tiempo y todavía precios razonables en vuelos y alojamiento. Es la época preferida por quienes quieren hacer rutas de senderismo por el Teide o la Caldera de Taburiente sin el calor del verano.</p>

<h2>Julio y agosto: para quien busca ambiente y fiesta</h2>
<p>Es temporada alta y se nota en el precio, pero también en el ambiente: playas más animadas, más oferta de ocio nocturno y todas las terrazas abiertas. Si no te importa pagar algo más y prefieres playas concurridas, esta es tu época.</p>

<h2>Nuestra recomendación</h2>
<ul>
  <li><strong>Para desconectar y ahorrar:</strong> noviembre, febrero o marzo.</li>
  <li><strong>Para hacer rutas y trekking:</strong> mayo o junio.</li>
  <li><strong>Para playa con ambiente:</strong> julio o agosto, reservando con antelación.</li>
</ul>

<p>Sea cuando sea, reserva los vuelos con margen: los precios a Canarias desde Madrid y Barcelona suelen subir bastante a medida que se acerca la fecha de viaje, especialmente en puentes y vacaciones escolares.</p>
""",
    },
    {
        "slug": "guia-fin-de-semana-mallorca",
        "title": "Mallorca en un fin de semana: itinerario para aprovechar cada hora",
        "category": "playa",
        "image_url": "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Con dos días y medio bien planificados puedes ver Palma, la Serra de Tramuntana y alguna cala sin sentir que vas con prisa.",
        "content": """
<p>Mallorca es perfecta para una escapada corta: vuelos rápidos desde casi cualquier ciudad española y suficiente variedad para no aburrirte en 48-60 horas.</p>

<h2>Día 1: Palma de Mallorca</h2>
<p>Empieza por el centro histórico: la Catedral de Mallorca (La Seu), el Palacio de la Almudaina y el paseo marítimo. Por la tarde, pierde un par de horas en el barrio de Santa Catalina, lleno de bares y restaurantes con buena relación calidad-precio. Cena cerca del puerto para ver el atardecer sobre la bahía.</p>

<h2>Día 2: Serra de Tramuntana</h2>
<p>Alquila un coche y dedica el día a la sierra. Imprescindibles: Valldemossa (pueblo de piedra con la Cartuja), Deià (mirador y playa de Cala Deià) y Sóller, al que puedes llegar también en el tren histórico desde Palma si prefieres no conducir por las curvas.</p>

<h2>Día 3 (medio día): cala y vuelta</h2>
<p>Si tu vuelo es por la tarde, aprovecha la mañana en una cala cercana al aeropuerto: Cala Mondragó o Es Trenc, según la zona donde te alojes, tienen aguas turquesas sin necesidad de desplazarte mucho.</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>En temporada alta (junio-septiembre), reserva coche de alquiler con semanas de antelación: se agota rápido.</li>
  <li>El aeropuerto de Palma está muy bien conectado; los vuelos desde Madrid y Barcelona suelen durar poco más de una hora.</li>
  <li>Las carreteras de la Serra de Tramuntana son estrechas y con curvas: calcula más tiempo del que indica el GPS.</li>
</ul>
""",
    },
    {
        "slug": "presupuesto-real-fin-de-semana-madrid",
        "title": "Cuánto cuesta de verdad un fin de semana en Madrid",
        "category": "ciudad",
        "image_url": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Desglosamos lo que cuesta vuelo o tren, alojamiento, comida y ocio para dos días en Madrid, con opciones ajustadas y opciones algo más cómodas.",
        "content": """
<p>Madrid es de los destinos urbanos con mejor relación calidad-precio de España si sabes dónde mirar. Aquí va un presupuesto realista para dos personas, dos noches.</p>

<h2>Alojamiento</h2>
<p>Un hotel de 3 estrellas bien situado (Sol, Atocha, Chamberí) ronda los 70-110€/noche en temporada media. Si prefieres apartamento, las zonas de Lavapiés o Embajadores suelen ser algo más baratas que el centro puro.</p>

<h2>Transporte</h2>
<p>Si vienes en avión desde otra ciudad española, cuenta entre 40€ y 90€ ida y vuelta según con cuánta antelación reserves. El Metro de Madrid cuesta 1,50-2€ por trayecto, o puedes sacar un abono turístico de 1, 2 o 3 días desde 8,50€.</p>

<h2>Comida</h2>
<p>Un menú del día decente cuesta entre 12€ y 16€. Para cenar tapeando, calcula 20-25€ por persona en una zona como La Latina. Si quieres algo más especial, un restaurante de gama media-alta puede subir a 40-50€ por persona.</p>

<h2>Ocio y cultura</h2>
<p>El Museo del Prado cuesta 15€ (gratis las últimas dos horas de cada día), el Reina Sofía 12€, y el Palacio Real 13€. Muchos museos públicos tienen entrada gratuita en horarios concretos: merece la pena revisarlo antes de ir.</p>

<h2>Total estimado por persona (2 noches)</h2>
<ul>
  <li><strong>Ajustado:</strong> 150-180€ (vuelo low cost reservado con antelación, hotel sencillo, menús del día).</li>
  <li><strong>Cómodo:</strong> 250-320€ (mejor ubicación, alguna cena especial, entradas a museos).</li>
</ul>

<p>El mayor ahorro viene siempre de reservar el vuelo o tren con varias semanas de antelación: el precio puede duplicarse si compras en el último momento.</p>
""",
    },
    {
        "slug": "que-ver-en-roma-tres-dias",
        "title": "Roma en 3 días: qué ver sin agotarte en el intento",
        "category": "europa",
        "image_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Roma se puede recorrer a fondo en tres días si organizas bien las zonas y reservas con antelación las entradas a los lugares con más cola.",
        "content": """
<p>Roma premia a quien planifica: las colas en los puntos turísticos pueden comerte horas de viaje si no reservas entrada con antelación.</p>

<h2>Día 1: la Roma Antigua</h2>
<p>Coliseo, Foro Romano y Monte Palatino se visitan juntos con la misma entrada. Reserva con antelación y elige franja horaria a primera hora para evitar el calor y las aglomeraciones del mediodía. Por la tarde, acércate a la Fontana di Trevi y la Plaza de España.</p>

<h2>Día 2: el Vaticano</h2>
<p>Dedica la mañana completa a los Museos Vaticanos y la Capilla Sixtina (entrada con horario reservado, imprescindible en temporada alta) y termina en la Basílica de San Pedro. Por la tarde, cruza el Tíber y pasea por Trastevere, el barrio con mejor ambiente para cenar.</p>

<h2>Día 3: Centro histórico y Panteón</h2>
<p>El Panteón de Agripa es gratis y se visita en poco tiempo. Combínalo con un paseo por Piazza Navona y el barrio judío, donde encontrarás algunos de los restaurantes más auténticos de la ciudad.</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>Compra las entradas al Coliseo y al Vaticano online y con antelación: ahorran horas de cola.</li>
  <li>Roma se camina mucho: lleva calzado cómodo, las distancias entre puntos de interés son más largas de lo que parecen en el mapa.</li>
  <li>El verano en Roma es muy caluroso (35°C no es raro en agosto): primavera y otoño son mejores épocas para visitarla.</li>
</ul>
""",
    },
    {
        "slug": "viajar-low-cost-trucos-vuelos-baratos",
        "title": "7 trucos reales para encontrar vuelos más baratos",
        "category": "espana",
        "image_url": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Nada de magia ni horas secretas para comprar: estos son los trucos que realmente funcionan para pagar menos por tu próximo vuelo.",
        "content": """
<p>Hay mucho mito alrededor de cómo encontrar vuelos baratos. Estos son los trucos que de verdad marcan diferencia, sin necesidad de borrar cookies ni comprar a las 3 de la madrugada.</p>

<h2>1. Reserva con antelación, pero no demasiada</h2>
<p>El punto dulce suele estar entre 6 y 10 semanas antes del viaje para vuelos nacionales y europeos, y 3-5 meses para vuelos de larga distancia. Comprar con un año de antelación no siempre es más barato.</p>

<h2>2. Sé flexible con las fechas</h2>
<p>Salir un martes o miércoles, en vez de viernes o domingo, puede ahorrarte una buena cantidad. Los buscadores que muestran el calendario de precios por mes son tu mejor amigo aquí.</p>

<h2>3. Compara aeropuertos cercanos</h2>
<p>Si vives cerca de dos aeropuertos, o el destino tiene alternativas cercanas (por ejemplo, volar a Girona en vez de Barcelona), compara ambos: la diferencia puede ser de 30-50€.</p>

<h2>4. Vigila las alertas de precio</h2>
<p>Configurar una alerta para una ruta concreta te avisa cuando el precio baja, sin tener que estar comprobándolo manualmente cada día.</p>

<h2>5. Cuidado con el equipaje</h2>
<p>Las aerolíneas low cost compensan precios bajos con cargos por maleta. Calcula el precio total con el equipaje que necesites antes de comparar con otra aerolínea que lo incluya.</p>

<h2>6. Vuelos con escala, si no te importa el tiempo</h2>
<p>Un vuelo con una escala razonable (1-2 horas) puede costar bastante menos que el directo, especialmente en rutas de larga distancia.</p>

<h2>7. Revisa el precio en incógnito, pero no por las cookies</h2>
<p>El verdadero motivo por el que conviene comprobar en una ventana nueva es evitar resultados personalizados por búsquedas anteriores, no una supuesta subida automática de precio por visitas repetidas (eso, en la práctica, no está demostrado).</p>
""",
    },
    {
        "slug": "guia-budva-montenegro",
        "title": "Budva, Montenegro: el secreto del Adriático que aún no está masificado",
        "category": "internacional",
        "image_url": "https://images.unsplash.com/photo-1601244005535-a48d21d951ac?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Playas del Adriático, un casco antiguo amurallado y precios todavía muy por debajo de Croacia. Te contamos por qué merece la pena conocerlo.",
        "content": """
<p>Mientras Dubrovnik y la costa croata se han llenado de turistas y precios altos, Budva ofrece un Adriático muy similar con un coste de vida considerablemente menor.</p>

<h2>Qué ver</h2>
<p>El casco antiguo amurallado (Stari Grad) es la joya de la ciudad: calles de piedra, pequeñas plazas y vistas al mar desde las murallas. A pocos minutos en coche está Sveti Stefan, el famoso islote-hotel que es de las imágenes más fotografiadas del Adriático, visible desde varios miradores cercanos sin necesidad de pagar por alojarte allí.</p>

<h2>Playas</h2>
<p>Mogren I y II son las playas más cercanas al centro, con aguas cristalinas y rodeadas de pinos. Si prefieres algo más tranquilo, la playa de Jaz queda a un corto trayecto en coche o autobús.</p>

<h2>Presupuesto</h2>
<p>Una comida completa en un restaurante de gama media cuesta 10-15€ por persona, muy por debajo de lo que pagarías en la costa croata o italiana en temporada alta. El alojamiento también es notablemente más económico.</p>

<h2>Cómo llegar</h2>
<p>El aeropuerto de Tivat es el más cercano a Budva (unos 25 minutos en coche). También se puede volar a Podgorica, la capital, algo más alejada pero a veces con mejores precios de vuelo.</p>

<h2>Mejor época</h2>
<p>Junio y septiembre ofrecen el mejor equilibrio entre buen tiempo, agua templada y precios todavía razonables, evitando el pico de julio-agosto.</p>
""",
    },
    {
        "slug": "que-hacer-amsterdam-tres-dias",
        "title": "Ámsterdam en 3 días: canales, museos y un paseo en bici obligatorio",
        "category": "europa",
        "image_url": "https://images.unsplash.com/photo-1576924542622-772281b13aa8?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Una ciudad pequeña y muy bien conectada que se disfruta mejor a pie o en bicicleta. Te contamos cómo organizar tres días sin perderte nada esencial.",
        "content": """
<p>Ámsterdam es una de las capitales europeas más fáciles de recorrer: compacta, plana y con un transporte público excelente, además de carriles bici por todas partes.</p>

<h2>Día 1: canales y centro histórico</h2>
<p>Empieza en Dam Square y recorre los canales del Anillo (Grachtengordel), declarado Patrimonio de la Humanidad. Un paseo en barco por los canales al atardecer es una de las mejores formas de ver la ciudad desde otra perspectiva.</p>

<h2>Día 2: museos</h2>
<p>El Rijksmuseum y el Museo Van Gogh son los dos imprescindibles, pero suelen tener colas largas: reserva entrada online con antelación. Si te queda tiempo, la Casa de Ana Frank requiere reserva con semanas de adelanto, así que planifícalo antes de viajar.</p>

<h2>Día 3: en bici hacia los barrios menos turísticos</h2>
<p>Alquila una bicicleta (la forma más auténtica de moverte por la ciudad) y explora barrios como De Pijp, con su mercado Albert Cuyp, o Jordaan, lleno de cafés y tiendas vintage.</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>El transporte desde el aeropuerto de Schiphol al centro tarda unos 15-20 minutos en tren.</li>
  <li>El alojamiento en Ámsterdam es caro comparado con el sur de Europa: reservar con antelación ayuda bastante a controlar el presupuesto.</li>
  <li>Respeta los carriles bici al caminar: están muy señalizados y la prioridad es real, no solo decorativa.</li>
</ul>
""",
    },
    {
        "slug": "estambul-entre-dos-continentes",
        "title": "Estambul: la única ciudad del mundo repartida entre dos continentes",
        "category": "internacional",
        "image_url": "https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Mezquitas centenarias, bazares interminables y un Bósforo que separa Europa de Asia en pocos minutos de ferri. Una guía para tu primera visita.",
        "content": """
<p>Estambul concentra siglos de historia bizantina y otomana en un mismo paseo: pocas ciudades permiten cruzar de Europa a Asia en un trayecto de ferri de 20 minutos.</p>

<h2>Lo imprescindible del lado europeo</h2>
<p>Santa Sofía, la Mezquita Azul y el Palacio de Topkapi forman el triángulo histórico de Sultanahmet, todos a poca distancia caminando entre ellos. El Gran Bazar, con más de 4.000 tiendas, merece al menos dos o tres horas, aunque solo sea para perderse entre sus pasillos.</p>

<h2>Cruzar a Asia</h2>
<p>Tomar el ferri desde Eminönü hasta Kadıköy, en el lado asiático, es una de las experiencias más recomendables y baratas de la ciudad. El barrio de Kadıköy tiene un ambiente más local y bohemio, con mercados y cafés menos orientados al turismo.</p>

<h2>Comida</h2>
<p>Probar un simit (especie de rosquilla con sésamo) en cualquier puesto de calle, un döner kebab de verdad (poco que ver con el de Europa) y un té turco en un çay bahçesi son básicos de cualquier visita.</p>

<h2>Presupuesto</h2>
<p>Estambul sigue siendo uno de los destinos con mejor relación calidad-precio de Europa: comidas completas desde 5-8€ y alojamiento de buena calidad notablemente más barato que en capitales de Europa occidental.</p>

<h2>Mejor época</h2>
<p>Primavera (abril-mayo) y otoño (septiembre-octubre) ofrecen temperaturas agradables, evitando el calor húmedo del verano.</p>
""",
    },
    {
        "slug": "alquiler-coche-espana-que-mirar",
        "title": "Alquilar coche en España: 6 cosas que mirar antes de reservar",
        "category": "espana",
        "image_url": "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "El precio que ves primero rara vez es el precio final. Repasamos qué revisar en la letra pequeña para no llevarte sorpresas al recoger el coche.",
        "content": """
<p>Alquilar un coche para una escapada parece sencillo hasta que llegas al mostrador y te ofrecen seguros adicionales, depósitos elevados o cargos que no esperabas. Esto es lo que conviene revisar antes de pagar.</p>

<h2>1. Franquicia del seguro</h2>
<p>El precio "barato" casi siempre incluye un seguro básico con una franquicia alta (lo que tendrías que pagar tú en caso de daño). Comprueba el importe exacto: puede ir desde 300€ hasta más de 1.500€ según la compañía.</p>

<h2>2. Depósito de garantía</h2>
<p>La mayoría de empresas bloquean un importe en tu tarjeta de crédito (no débito, en muchos casos) al recoger el coche. Este bloqueo puede tardar días en liberarse tras la devolución.</p>

<h2>3. Combustible</h2>
<p>Comprueba si la política es "lleno por lleno" (lo más justo) o si te cobran el depósito completo aunque devuelvas el coche con gasolina.</p>

<h2>4. Conductor adicional</h2>
<p>Añadir un segundo conductor suele tener coste extra si no se indica en el momento de la reserva.</p>

<h2>5. Edad del conductor</h2>
<p>Conductores de menos de 25 años suelen pagar un recargo adicional, y algunas compañías ni siquiera alquilan a menores de 21.</p>

<h2>6. Dónde recoges el coche</h2>
<p>Recoger en el aeropuerto suele tener un recargo frente a hacerlo en una oficina del centro de la ciudad. Si tu itinerario lo permite, comparar ambas opciones puede ahorrarte dinero.</p>

<p>En resumen: compara siempre el precio total con todos los extras incluidos, no solo el precio base que aparece primero en el buscador.</p>
""",
    },
    {
        "slug": "lisboa-fin-de-semana-barrios",
        "title": "Lisboa en un fin de semana: barrio a barrio",
        "category": "europa",
        "image_url": "https://images.unsplash.com/photo-1585465607853-9e4b7c8c5b5f?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Lisboa se entiende mejor recorriéndola barrio a barrio que persiguiendo una lista de monumentos. Aquí va un plan para dos días intensos.",
        "content": """
<p>Lisboa es una ciudad de colinas, miradores y tranvías históricos que se disfruta caminando despacio, aunque eso signifique subir alguna cuesta de más.</p>

<h2>Alfama</h2>
<p>El barrio más antiguo de la ciudad, con calles estrechas y empinadas que sobrevivieron al terremoto de 1755. Sube hasta el Castillo de San Jorge para una de las mejores vistas de la ciudad, y no te pierdas una sesión de fado en directo en alguna de las tabernas del barrio.</p>

<h2>Baixa y Chiado</h2>
<p>El centro reconstruido tras el terremoto, con calles en cuadrícula, comercio y la emblemática Plaza del Comercio frente al río Tajo. El elevador de Santa Justa conecta este barrio con el Bairro Alto, aunque las colas pueden ser largas en temporada alta.</p>

<h2>Belém</h2>
<p>A las afueras del centro, imprescindible para ver el Monasterio de los Jerónimos y la Torre de Belém. Aprovecha para probar el pastel de Belém original en la pastelería homónima, abierta desde 1837.</p>

<h2>Bairro Alto y Príncipe Real</h2>
<p>De día, tiendas y cafés tranquilos; de noche, el barrio con más ambiente de bares de toda la ciudad. Príncipe Real, justo al lado, tiene un aire más sofisticado con tiendas de diseño y terrazas.</p>

<h2>Consejos prácticos</h2>
<ul>
  <li>El tranvía 28 es turístico y suele ir abarrotado: considera caminar la misma ruta si no te importa el esfuerzo.</li>
  <li>Lisboa tiene muchas cuestas: lleva calzado cómodo.</li>
  <li>Los vuelos desde España suelen ser de los más baratos de toda Europa por la cercanía.</li>
</ul>
""",
    },
    {
        "slug": "consejos-equipaje-mano-no-pagar-de-mas",
        "title": "Cómo viajar solo con equipaje de mano y no pagar de más",
        "category": "espana",
        "image_url": "https://images.unsplash.com/photo-1581553680321-4fffae59fc36?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "Las aerolíneas low cost han hecho que viajar ligero sea casi obligatorio si no quieres que el equipaje cueste más que el billete. Estos trucos ayudan.",
        "content": """
<p>Con la política de equipaje de las aerolíneas low cost cada vez más restrictiva, aprender a viajar con poco se ha vuelto casi una necesidad económica.</p>

<h2>Revisa las medidas exactas, no las aproximadas</h2>
<p>Cada aerolínea tiene medidas distintas para el equipaje "gratuito" (el que cabe debajo del asiento) y el de cabina con coste adicional. Una diferencia de 2-3 cm puede hacer que te cobren en la puerta de embarque, así que mide tu maleta antes de viajar.</p>

<h2>La técnica del enrollado</h2>
<p>Enrollar la ropa en vez de doblarla aprovecha mejor el espacio y reduce las arrugas. Para prendas más delicadas, usa bolsas de compresión.</p>

<h2>Calzado: el mayor enemigo del espacio</h2>
<p>Lleva como máximo dos pares además del que llevas puesto, y rellena el interior de los zapatos con calcetines o cargadores pequeños para no perder espacio.</p>

<h2>Líquidos y neceser</h2>
<p>Lleva solo lo esencial en formato viaje (menos de 100ml) y considera comprar productos de higiene en el destino si el viaje es de varios días, en vez de cargar con envases completos.</p>

<h2>Ropa multifunción</h2>
<p>Elige prendas que combinen entre sí y sirvan para más de una ocasión: una chaqueta que valga tanto de día como de noche ahorra espacio frente a llevar una prenda para cada momento.</p>

<h2>Antes de cerrar la maleta</h2>
<p>Repasa la política de equipaje de tu aerolínea concreta la noche antes del vuelo: cambian con cierta frecuencia y lo que valía en tu último viaje puede no ser válido ahora.</p>
""",
    },
    {
        "slug": "viajar-en-pareja-con-poco-presupuesto",
        "title": "Viajar en pareja con poco presupuesto: 8 ideas que funcionan",
        "category": "espana",
        "image_url": "https://images.unsplash.com/photo-1494783367193-149034c05e8f?fm=jpg&q=80&w=1200&auto=format&fit=crop",
        "excerpt": "No hace falta gastar mucho para desconectar unos días en pareja. Estas son ideas prácticas para viajar bien sin vaciar la cuenta.",
        "content": """
<p>Viajar en pareja no tiene que significar gastar de más. Con algo de planificación, una escapada de varios días puede salir muy por debajo de lo que mucha gente asume.</p>

<h2>1. Elige temporada media, no solo destino barato</h2>
<p>El mismo destino puede costar la mitad fuera de temporada alta. Mayo, junio y septiembre suelen ofrecer buen clima en gran parte de Europa con precios mucho más bajos que julio-agosto.</p>

<h2>2. Reserva con antelación, pero compara antes de pagar</h2>
<p>Reservar pronto suele ser más barato, pero no asumas que el primer precio que ves es el definitivo: compara entre 2-3 plataformas antes de confirmar.</p>

<h2>3. Cocina algún día, si el alojamiento lo permite</h2>
<p>Un apartamento con cocina, aunque sea pequeña, permite ahorrar bastante comiendo fuera solo algunos días y cocinando el resto, sin renunciar a probar la gastronomía local.</p>

<h2>4. Aprovecha entradas gratuitas o con descuento</h2>
<p>Muchos museos y monumentos tienen horarios con entrada gratuita o descuentos para parejas/grupos. Revisarlo antes de viajar puede ahorrar bastante en una semana de turismo intensivo.</p>

<h2>5. Camina en vez de usar taxi siempre</h2>
<p>Además de ahorrar dinero, caminar por una ciudad nueva suele descubrir rincones que no aparecen en ninguna guía.</p>

<h2>6. Usa el transporte público local</h2>
<p>Los abonos turísticos de transporte suelen amortizarse con solo 3-4 trayectos al día.</p>

<h2>7. Viaja con equipaje ligero</h2>
<p>Evitar cargos por maleta adicional en vuelos low cost puede suponer un ahorro de 30-60€ por persona en el trayecto de ida y vuelta.</p>

<h2>8. Aprovecha las ofertas con descuento real</h2>
<p>Comparar precios y aprovechar ofertas genuinas (no descuentos artificiales sobre precios inflados) es la diferencia entre un viaje caro y uno ajustado sin renunciar a la calidad.</p>
""",
    },
]


def main():
    database.init_db()
    inserted = 0
    for post in POSTS:
        post_id = database.add_post(post)
        if post_id:
            inserted += 1
            print(f"  + {post['slug']}")
        else:
            print(f"  = {post['slug']} (ya existía, omitido)")
    print(f"\n{inserted} artículos nuevos insertados de {len(POSTS)} totales.")


if __name__ == "__main__":
    main()
