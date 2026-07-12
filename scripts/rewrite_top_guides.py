"""Reescribe las 5 guías con más tráfico con contenido de calidad real + GangaConsejos."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import psycopg2, config

_GC_BOX = (
    '<div style="background:linear-gradient(135deg,#fde8e6,#fff9f8);'
    'border-left:4px solid #e8523a;border-radius:8px;padding:20px 24px;margin:32px 0;">'
)


def gc(titulo, items):
    """Genera la caja GangaConsejos."""
    li = "".join("<li>" + i + "</li>" for i in items)
    return (
        _GC_BOX
        + '<h2 style="color:#e8523a;margin-top:0;">GangaConsejos: ' + titulo + '</h2>'
        + '<ul style="margin-bottom:0;">' + li + '</ul>'
        + '</div>'
    )


# ─── Contenidos ───────────────────────────────────────────────────────────────

MALDIVAS = """<p>Las Maldivas tienen fama de ser el destino más caro del mundo — y lo son si te alojas en uno de esos resorts privados con bungalow sobre el agua que salen en Instagram. Pero hay otra Maldivas que casi nadie conoce: las <strong>islas locales</strong>, donde viven los maldivos de verdad, con guesthouses desde 40 euros la noche y un archipiélago de 1.200 islas casi para ti solo. Esta guía es para los que quieren ver las Maldivas de verdad sin hipotecarse.</p>

<h2>Maldivas de resort vs. islas locales: la diferencia real</h2>
<p>Un resort privado en las Maldivas puede costarte entre 500 y 3.000 euros por noche. Todo incluido, lancha privada, el paraíso. Pero si no tienes ese presupuesto — o simplemente no quieres gastarlo — las islas locales ofrecen exactamente las mismas aguas turquesas, el mismo arrecife de coral y las mismas playas de arena blanca por una fracción del precio.</p>
<p>Hasta 2009, los turistas no podían alojarse en las islas habitadas de las Maldivas. Desde que se abrió el turismo local, han aparecido decenas de guesthouses de calidad que compiten en relación calidad-precio con cualquier destino del sudeste asiático.</p>

<h2>Las mejores islas locales para alojarse</h2>

<h3>Maafushi — la más turística y completa</h3>
<p>Es la isla local más desarrollada para el turismo. Tiene la mejor oferta de guesthouses, restaurantes, tiendas de buceo y excursiones. A 45 minutos en lancha rápida de Malé (12-15 euros). Si es tu primera vez y quieres comodidad, empieza aquí. Las playas de bikini (zonas designadas donde las mujeres pueden llevar bañador) son buenas.</p>
<p><strong>Guesthouses recomendados:</strong> Kaani Grand Seaview, Summer Island View. Precio: 50-90 euros/noche por habitación doble con desayuno.</p>

<h3>Dhigurah — para los que buscan tranquilidad</h3>
<p>Una isla larga y estrecha con una playa de 3 kilómetros casi solitaria. Menos turistas que Maafushi, ambiente más relajado. Famosa por los avistamientos de tiburón ballena (noviembre-mayo). A 2,5 horas de Malé en lancha pública (4 euros) o 1 hora en lancha rápida privada.</p>

<h3>Fulidhoo — la joya escondida</h3>
<p>Si buscas algo realmente auténtico y tranquilo, Fulidhoo es perfecta. Una isla pequeña con apenas unos pocos guesthouses. Los arrecifes de alrededor están entre los mejor conservados del archipiélago. Menos opciones de restaurante, pero la experiencia es única.</p>

<h3>Ukulhas — Patrimonio UNESCO</h3>
<p>Isla famosa por su gestión medioambiental ejemplar — tiene uno de los sistemas de reciclaje más avanzados de las Maldivas. El arrecife es espectacular para snorkel y buceo. Muy recomendable para viajeros con conciencia ecológica.</p>

<h2>Cómo llegar a las Maldivas desde España</h2>
<p>El aeropuerto internacional está en Malé (MLE). No hay vuelos directos desde España — siempre con escala. Las mejores opciones:</p>
<ul>
<li><strong>Emirates vía Dubái:</strong> la ruta más cómoda, buena frecuencia, 12-16 horas en total</li>
<li><strong>Qatar Airways vía Doha:</strong> muy buenas conexiones, suele tener buenos precios</li>
<li><strong>Turkish Airlines vía Estambul:</strong> opción económica frecuente desde varias ciudades españolas</li>
<li><strong>Sri Lankan Airlines vía Colombo:</strong> la más barata habitualmente si tienes flexibilidad</li>
</ul>
<p><strong>Precio orientativo del vuelo:</strong> 600-1.100 euros ida y vuelta desde Madrid o Barcelona. Las mejores ofertas aparecen reservando con 3-4 meses de antelación para los meses de temporada baja (mayo-noviembre).</p>

<h2>Cómo moverse entre las islas</h2>
<ul>
<li><strong>Ferry público:</strong> la opción más barata (1-5 euros). Tarda más y solo hay uno o dos al día. Perfecto si tienes tiempo y quieres vivir la experiencia local.</li>
<li><strong>Lancha rápida (speedboat):</strong> 12-25 euros según la distancia. Más rápida y cómoda. La mayoría de guesthouses organizan el transfer desde el aeropuerto.</li>
<li><strong>Hidroavión:</strong> espectacular para islas lejanas. Vistas increíbles. 150-300 euros. Solo merece la pena si vas a atolones del norte o del sur.</li>
</ul>
<p><strong>Consejo:</strong> coordina siempre el transfer con tu guesthouse antes de llegar. Te recogerán en el muelle de Malé y te llevarán directamente.</p>

<h2>Qué hacer en las Maldivas</h2>

<h3>Snorkel y buceo</h3>
<p>El arrecife de coral de las Maldivas es uno de los mejores del mundo. Puedes hacer snorkel directamente desde la playa en muchas islas. Las excursiones de snorkel en barco para ver mantarrayas, tortugas y tiburones nodriza cuestan entre 20-40 euros por persona.</p>
<p>Para bucear, los precios en islas locales son mucho más baratos que en resorts: 60-90 euros una inmersión con equipo vs. 150-200 euros en un resort privado.</p>

<h3>Avistamiento de tiburón ballena</h3>
<p>De noviembre a mayo, los tiburones ballena se concentran alrededor de algunas islas del sur. Dhigurah es el mejor punto de partida. Las excursiones cuestan 50-80 euros e incluyen snorkel con estos gigantes inofensivos de hasta 12 metros. Una de las experiencias más impresionantes del planeta.</p>

<h3>Sandbank privada</h3>
<p>Muchos guesthouses organizan excursiones a bancos de arena en medio del océano — islas diminutas que emergen durante la marea baja. Llevas el picnic, estás solos en medio del Índico. Precio: 30-60 euros por persona.</p>

<h3>Pesca nocturna</h3>
<p>Los pescadores locales organizan salidas nocturnas de pesca tradicional. Suelen incluir barbacoa con lo que pescas en la playa. 20-35 euros por persona. Experiencia auténtica y muy recomendable.</p>

<h2>Dónde comer en las islas locales</h2>
<p>La gastronomía maldiva gira en torno al atún y el coco. Los <strong>hedhikaa</strong> (snacks locales) son baratos y deliciosos. Las guesthouses suelen incluir desayuno y muchas ofrecen cena por 8-15 euros (no hay alcohol en islas locales, pero sí en algunos resorts cercanos).</p>
<p>Presupuesto comida: 15-25 euros al día por persona comiendo bien.</p>

<h2>Cuándo ir a las Maldivas</h2>
<p><strong>Temporada seca (noviembre-abril):</strong> el mejor tiempo. Cielos despejados, mar en calma, visibilidad perfecta para bucear. Es temporada alta — los precios son más altos y conviene reservar con antelación.</p>
<p><strong>Temporada de lluvias (mayo-octubre):</strong> más lluvias pero raramente todo el día. Los precios bajan un 30-40% y hay muchas menos personas. Si vas a bucear igualmente es una buena época.</p>
<p><strong>El mejor mes:</strong> enero-febrero para tiempo perfecto; junio-julio para mejor precio.</p>

<h2>Presupuesto real para un viaje de una semana</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.9rem;margin:16px 0;">
<tr style="background:#f4f6f9;"><th style="padding:8px;text-align:left;">Concepto</th><th style="padding:8px;text-align:right;">Coste orientativo</th></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Vuelo ida y vuelta (por persona)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">700-900 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Alojamiento (7 noches, doble)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">350-600 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Comidas (7 días)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">100-175 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Excursiones (snorkel, sandbank, tiburón ballena)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">150-250 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Transfers entre islas</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">30-60 €</td></tr>
<tr style="background:#fde8e6;font-weight:700;"><td style="padding:8px;">TOTAL POR PERSONA</td><td style="padding:8px;text-align:right;">1.330-1.985 €</td></tr>
</table>
<p>Comparado con un resort privado que puede superar los 5.000-10.000 euros por persona, las islas locales son la mejor manera de vivir las Maldivas de verdad sin arruinarse.</p>

<h2>Visado y requisitos de entrada</h2>
<p>Los ciudadanos españoles no necesitan visado previo para las Maldivas. Se obtiene un visado de turista gratuito de 30 días a la llegada. Solo necesitas pasaporte válido, billete de vuelta y dinero suficiente para la estancia.</p>

<h2>Consejos prácticos imprescindibles</h2>
<ul>
<li><strong>Respeta las normas locales:</strong> las islas locales son de mayoría musulmana. Viste con ropa que cubra hombros y rodillas fuera de las zonas de playa designadas. No hay alcohol fuera de los resorts.</li>
<li><strong>Lleva efectivo:</strong> muchos guesthouses y tiendas pequeñas no aceptan tarjeta. Los dólares americanos se aceptan en todas partes además de la rufiyaa maldiva.</li>
<li><strong>Protector solar mineral:</strong> usa protector solar sin oxibenzona ni octinoxato ("reef safe"). Los arrecifes de las Maldivas están amenazados.</li>
<li><strong>Reserva con antelación en temporada alta:</strong> los mejores guesthouses de Maafushi y Dhigurah se llenan meses antes en diciembre-enero.</li>
<li><strong>No toques el coral:</strong> ni de pie ni con las manos. El coral tarda 10 años en recuperarse de un solo toque.</li>
</ul>
"""

MALDIVAS_GC = gc("cómo ahorrar en Maldivas", [
    "<strong>Viaja en temporada baja (mayo-octubre):</strong> los vuelos bajan hasta un 40% y los guesthouses tienen descuentos de hasta el 30%. Las lluvias son breves y la isla sigue siendo preciosa.",
    "<strong>Islas locales en vez de resort:</strong> la diferencia puede ser de 500-2.000 euros por noche. Las aguas turquesas son exactamente las mismas — y en muchas islas locales, estás casi solo.",
    "<strong>Ferry público en vez de lancha rápida:</strong> de Malé a Maafushi cuesta 4 euros en ferry público vs 15 euros en speedboat privado. Tarda el doble pero es la experiencia local auténtica.",
    "<strong>Reserva excursiones con tu guesthouse directamente:</strong> los intermediarios online cobran hasta el doble. El propio guesthouse organiza snorkel, sandbank y avistamiento de tiburones a precio local.",
    "<strong>Come en las cafeterías del pueblo:</strong> el tuna curry con arroz en un local maldivo cuesta 3-5 euros. La misma comida en el restaurante del guesthouse orientado a turistas: 12-18 euros.",
    "<strong>Activa alertas de vuelos con meses de antelación:</strong> los vuelos Madrid-Malé bajan mucho reservando con 4-6 meses de antelación. Usa Google Vuelos o Skyscanner con alertas de precio.",
])

ISLANDIA = """<p>Islandia es uno de esos destinos que cambian la perspectiva. Una isla volcánica en el borde del Círculo Ártico donde la naturaleza funciona a una escala diferente: géiseres que estallan cada 5 minutos, cascadas de 60 metros, playas de arena negra, ballenas a 30 minutos de la capital y, si tienes suerte, el cielo verde de las auroras boreales. Esta guía te cuenta todo lo que necesitas saber para organizarlo bien.</p>

<h2>Cuándo ir a Islandia: la pregunta más importante</h2>

<h3>Para ver auroras boreales: septiembre-marzo</h3>
<p>Las auroras boreales solo son visibles cuando hay oscuridad total — algo que no existe en Islandia entre mayo y julio (sol de medianoche). La temporada de auroras va de finales de agosto a principios de abril. Los mejores meses son <strong>octubre, febrero y marzo</strong>: cielos más despejados que en noviembre-diciembre y temperaturas algo menos extremas.</p>
<p>Para ver auroras necesitas tres cosas: oscuridad, cielo despejado y actividad solar alta. Descarga la app <strong>Aurora Forecast</strong> (gratuita) — te muestra la probabilidad de auroras en tiempo real. Aléjate de las luces de Reikiavik en coche (30-40 km) para mejor visibilidad.</p>
<p><strong>Realidad que nadie cuenta:</strong> no hay garantía de ver auroras. Puedes ir dos semanas y no verlas por nubes. O verlas la primera noche. La probabilidad en una semana de estancia en buena época es de aproximadamente un 60-70 por ciento.</p>

<h3>Para paisajes y comodidad: junio-agosto</h3>
<p>El verano islandés es espectacular aunque no veas auroras. El sol de medianoche permite días de actividad interminables, las carreteras de montaña están abiertas (las F-roads solo abren de junio a septiembre) y los paisajes son de un verde increíble. Es también la temporada más cara y con más turistas.</p>

<h3>Temporada ideal para la mayoría: mayo o septiembre</h3>
<p>Precios más bajos que el verano, posibilidad de auroras en septiembre, días largos, menos turistas. Si tienes que elegir un único mes, elige <strong>septiembre</strong>.</p>

<h2>Cómo moverse por Islandia</h2>

<h3>Alquilar un coche: la única opción real</h3>
<p>Islandia no se puede explorar bien sin coche. El transporte público es muy limitado fuera de Reikiavik. Alquila un coche desde el aeropuerto de Keflavík nada más llegar.</p>
<p><strong>¿Qué tipo de coche?</strong> Para la Ring Road (carretera principal, asfaltada) un coche normal es suficiente. Si quieres hacer las F-roads (pistas de montaña 4x4 obligatorio), necesitas un SUV o 4x4. El seguro a todo riesgo es muy recomendable — el viento y la gravilla pueden dañar el coche fácilmente.</p>
<p><strong>Precio orientativo:</strong> 50-80 euros/día un coche normal, 90-140 euros/día un SUV 4x4. Compara en Rentalcars.com o directamente con Blue Car Rental o Saga.</p>

<h2>La Ring Road: dar la vuelta a Islandia en coche</h2>
<p>La carretera 1 rodea toda la isla en 1.332 km. Se puede completar en 7-10 días parando en los puntos principales. Es una de las rutas en coche más espectaculares del mundo.</p>

<h3>El Círculo Dorado (desde Reikiavik, ida y vuelta en 1 día)</h3>
<ul>
<li><strong>Þingvellir (Thingvellir):</strong> Patrimonio UNESCO. Aquí puedes caminar entre las placas tectónicas euroasiática y norteamericana. También el primer parlamento del mundo (año 930).</li>
<li><strong>Geysir:</strong> el géiser Strokkur entra en erupción cada 5-8 minutos lanzando agua a 20-30 metros. Espectacular y puntual.</li>
<li><strong>Cascada Gullfoss:</strong> "la cascada de oro". Dos saltos que en conjunto bajan 32 metros. Impresionante en cualquier época del año.</li>
</ul>

<h3>La Costa Sur</h3>
<ul>
<li><strong>Cascada Seljalandsfoss:</strong> puedes caminar detrás del agua. Lleva ropa impermeable.</li>
<li><strong>Cascada Skógafoss:</strong> una de las más fotogénicas de Islandia. Sube los 370 escalones para vistas panorámicas.</li>
<li><strong>Playa Reynisfjara:</strong> playa de arena negra con columnas de basalto hexagonales. Las olas son peligrosas — nunca des la espalda al mar.</li>
<li><strong>Vík:</strong> el pueblo más lluvioso de Islandia y uno de los más fotogénicos.</li>
</ul>

<h3>Jökulsárlón — la laguna glaciar</h3>
<p>Icebergs de colores azulados flotando en una laguna antes de llegar al mar. Uno de los lugares más impresionantes de Europa. Al lado está la Diamond Beach — icebergs sobre arena negra. Ambos gratuitos y en la Ring Road.</p>

<h3>El Norte: Akureyri y Mývatn</h3>
<ul>
<li><strong>Akureyri:</strong> la segunda ciudad de Islandia. Base perfecta para explorar el norte.</li>
<li><strong>Lago Mývatn:</strong> zona volcánica con formaciones de lava únicas, pseudocráteres, baños termales naturales (los Mývatn Nature Baths, más baratos y menos masificados que el Blue Lagoon) y aves acuáticas.</li>
<li><strong>Cascada Goðafoss:</strong> "la cascada de los dioses". Amplia y poderosa. Justo en la carretera principal.</li>
</ul>

<h3>El Blue Lagoon (cerca del aeropuerto)</h3>
<p>Las aguas termales más famosas del mundo, color turquesa leche por la sílice. Muy turístico y caro (50-100 euros la entrada). Reserva SIEMPRE con antelación — se agotan semanas antes. Está a 20 minutos del aeropuerto de Keflavík, perfecto para el primer o último día.</p>

<h2>Alojamiento en Islandia</h2>
<ul>
<li><strong>Camping:</strong> 15-25 euros/noche por tienda. Solo en verano (junio-agosto).</li>
<li><strong>Hostales (habitación compartida):</strong> 35-55 euros/noche por cama</li>
<li><strong>Guesthouses y B&amp;B:</strong> 80-150 euros/noche habitación doble</li>
<li><strong>Hoteles:</strong> 120-250 euros/noche</li>
<li><strong>Cabañas (cottages):</strong> 100-200 euros/noche. Buena opción para grupos.</li>
</ul>

<h2>Comida en Islandia: cómo no arruinarse</h2>
<p>Islandia es cara para comer. Un menú en restaurante: 20-35 euros. Un sándwich en una gasolinera: 8-12 euros. La solución: <strong>cocina tú mismo</strong>. Los supermercados Bónus (el más barato) y Krónan tienen de todo.</p>
<p>Lo que sí merece la pena probar: el cordero islandés, el skyr (yogur islandés), el pan de centeno geotérmico y el langostino de los fiordos del este.</p>

<h2>Presupuesto real para 7 días en Islandia</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.9rem;margin:16px 0;">
<tr style="background:#f4f6f9;"><th style="padding:8px;text-align:left;">Concepto</th><th style="padding:8px;text-align:right;">Económico</th><th style="padding:8px;text-align:right;">Cómodo</th></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Vuelo ida y vuelta</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">200-350 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">350-500 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Alquiler coche (7 días)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">300-400 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">500-700 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Alojamiento (7 noches)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">200-350 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">700-1.200 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Comida (cocinando parte)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">150-200 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">300-450 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Gasolina</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">100-150 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">100-150 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Blue Lagoon + entradas</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">60-100 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">100-150 €</td></tr>
<tr style="background:#fde8e6;font-weight:700;"><td style="padding:8px;">TOTAL POR PERSONA</td><td style="padding:8px;text-align:right;">1.010-1.550 €</td><td style="padding:8px;text-align:right;">2.050-3.150 €</td></tr>
</table>

<h2>Lo que nadie te cuenta de Islandia</h2>
<ul>
<li><strong>El tiempo cambia en minutos:</strong> sol, lluvia, viento y nieve pueden ocurrir el mismo día. Lleva capas y ropa impermeable siempre.</li>
<li><strong>Las F-roads son para 4x4:</strong> si tu seguro no cubre F-roads y te metes, puedes pagar el remolque (600-1.000 euros) de tu bolsillo. Comprueba siempre el contrato de alquiler.</li>
<li><strong>La gasolina es cara:</strong> llena el depósito siempre que puedas. En zonas remotas puede no haber gasolinera en 200 km.</li>
<li><strong>No recojas musgo ni rocas volcánicas:</strong> es ilegal y puede suponer una multa importante. El musgo islandés tarda 100 años en crecer.</li>
<li><strong>Respeta las señales de seguridad:</strong> cada año mueren turistas en Islandia por acercarse demasiado a los acantilados o dar la espalda al mar.</li>
<li><strong>Descarga los mapas offline:</strong> Maps.me o Google Maps sin conexión. En zonas rurales no siempre hay cobertura.</li>
</ul>
"""

ISLANDIA_GC = gc("cómo ahorrar en Islandia", [
    "<strong>Vuela en mayo o septiembre:</strong> los precios de vuelo bajan un 30-40% respecto a julio-agosto. Además hay menos turistas y el paisaje sigue siendo espléndido.",
    "<strong>Acampa en verano:</strong> la diferencia entre camping (18 euros/noche) y guesthouse (120 euros/noche) es enorme. Con 7 noches de camping ahorras más de 700 euros por pareja.",
    "<strong>Compra en el supermercado Bónus:</strong> el más barato de Islandia. Prepara desayunos y almuerzos tú mismo — una barra de pan, queso, embutido y fruta cuesta 8-10 euros y da para dos personas todo el día.",
    "<strong>Compara precios de alquiler de coche:</strong> la diferencia entre empresas puede ser de 200-300 euros en una semana. Rentalcars.com, Blue Car Rental y Saga son los más competitivos.",
    "<strong>Mývatn Nature Baths en vez de Blue Lagoon:</strong> misma experiencia termal volcánica por la mitad de precio (25-30 euros vs 50-100 euros) y con la mitad de turistas.",
    "<strong>Vigila el precio de la gasolina:</strong> la gasolinera más barata suele ser N1 o Costco (si hay uno en tu ruta). Llena siempre el depósito antes de entrar en zonas remotas.",
    "<strong>Alójate en Akureyri para explorar el norte:</strong> usar Akureyri como base es más barato que dormir en guesthouses rurales aislados a lo largo de la Ring Road.",
])

PARIS = """<p>París tiene la capacidad de superar siempre las expectativas — incluso cuando ya conoces la Torre Eiffel de mil fotos. El problema es que hay tanto que ver que es fácil acabar agotado corriendo de monumento en monumento sin disfrutar de lo que hace única a esta ciudad: sus barrios, sus cafés, sus mercados y ese ritmo de vida que los parisinos han elevado a categoría de arte. Este itinerario está diseñado para verlo todo sin sacrificar el placer de callejear.</p>

<h2>Antes de llegar: lo que tienes que reservar sí o sí</h2>
<p>París en temporada alta (junio-agosto, Semana Santa, Navidades) se colapsa. Estos monumentos se agotan con semanas de antelación:</p>
<ul>
<li><strong>Torre Eiffel (subida):</strong> reserva online con al menos 2-3 semanas de antelación. Sin reserva, la cola para billete en taquilla puede ser de 3-4 horas.</li>
<li><strong>Musée d'Orsay:</strong> reserva la franja horaria online. Evita los martes (está cerrado).</li>
<li><strong>Versalles:</strong> si piensas ir, reserva con una semana de antelación mínimo.</li>
</ul>

<h2>Transporte en París</h2>
<p>El metro de París es rápido, barato y llega a todas partes. El billete sencillo cuesta 2,15 euros, pero lo más práctico es comprar un <strong>carnet de 10 viajes (17,35 euros)</strong> o la tarjeta <strong>Paris Visite</strong> si vas a hacer muchos trayectos (desde 13 euros/día). El RER B desde CDG hasta el centro cuesta 11,80 euros y tarda 35 minutos. Evita los taxis desde el aeropuerto — son carísimos.</p>

<h2>Itinerario París en 3 días</h2>

<h3>Día 1: Los museos y el Sena</h3>
<p><strong>Mañana (8:00-13:00):</strong> Empieza temprano en el <strong>Musée d'Orsay</strong> (abre a las 9:30h). Es el museo de arte impresionista más importante del mundo: Monet, Van Gogh, Renoir, Degas. Calcula 2 horas. Después pasea por el <strong>Jardin des Tuileries</strong> hasta el Louvre.</p>
<p><strong>Tarde (13:00-19:00):</strong> El <strong>Louvre</strong>. Es enorme — no intentes verlo todo. Elige la Venus de Milo, la Victoria de Samotracia y la Mona Lisa. Desde el Louvre, pasea por la orilla del Sena hasta la <strong>Île de la Cité</strong> para ver Notre-Dame (reabierta en diciembre 2024 tras el incendio de 2019).</p>
<p><strong>Noche:</strong> Cena en el barrio de <strong>Le Marais</strong>. El mejor barrio para comer bien a precio razonable: restaurantes judíos en la Rue des Rosiers, bistros franceses en las calles adyacentes. Después, paseo nocturno por la <strong>Place des Vosges</strong>.</p>

<h3>Día 2: La Torre Eiffel, Montmartre y la vida parisina</h3>
<p><strong>Mañana temprana (8:00-10:00):</strong> Ve a la <strong>Torre Eiffel</strong> a primera hora. A las 9h la plaza del Trocadéro tiene mucho menos gente que a las 11h. Si tienes reserva para subir, hazlo ahora.</p>
<p><strong>Media mañana (10:30-13:00):</strong> Pasea a lo largo del <strong>Campo de Marte</strong>. Compra en una boulangerie del barrio (baguette, queso, jamón, vino) y haz picnic en el césped con la torre detrás. Coste: 8-12 euros por persona. Esto es París de verdad.</p>
<p><strong>Tarde (14:00-19:00):</strong> Sube a <strong>Montmartre</strong> en metro. El barrio de los artistas, la basílica del <strong>Sacré-Cœur</strong> y las mejores vistas de París. Llega por la parte trasera (calle Lepic) para evitar la zona turística más agresiva.</p>
<p><strong>Noche:</strong> Apéritif en cualquier terraza de <strong>Pigalle</strong>. Después, vuelve al Trocadéro para el espectáculo de luces de la Torre Eiffel — cada hora en punto hace un espectáculo de 5 minutos. Impresionante.</p>

<h3>Día 3: El Marais, los mercados y la vida local</h3>
<p><strong>Mañana (9:00-13:00):</strong> Empieza en el <strong>Marché d'Aligre</strong> (abre a las 7:30h, cierra al mediodía). Después, pasea por el <strong>Marais</strong> de día — las galerías de arte, las tiendas vintage de la Rue de Bretagne y el <strong>Centre Pompidou</strong> (la fachada con sus tuberías de colores es un hito arquitectónico que hay que ver).</p>
<p><strong>Tarde (13:00-18:00):</strong> Elige según tus intereses: el <strong>Père Lachaise</strong> (Oscar Wilde, Jim Morrison, Édith Piaf), el barrio de <strong>Saint-Germain-des-Prés</strong> o simplemente sentarte en un café a ver pasar París.</p>
<p><strong>Última noche:</strong> Cena en <strong>Oberkampf</strong> o <strong>Belleville</strong>, los barrios donde come la gente joven local. Precios más bajos que el centro, ambiente auténtico, mejor comida.</p>

<h2>Dónde comer en París sin arruinarse</h2>
<ul>
<li><strong>El menú del mediodía:</strong> la mayoría de bistros ofrecen menú de 2-3 platos por 14-18 euros al mediodía. Los mismos platos cuestan el doble por la noche. El mejor secreto de París.</li>
<li><strong>Boulangeries:</strong> desayuna aquí. Café más croissant: 3-4 euros. En cualquier café turístico: 7-10 euros.</li>
<li><strong>Picnic en el parque:</strong> lo hacen los propios parisinos. Compra en el supermercado Monoprix. 10-15 euros para dos personas.</li>
<li><strong>Falafel en Le Marais:</strong> la Rue des Rosiers tiene los mejores falafel de París. L'As du Fallafel es el más famoso. 7-9 euros.</li>
<li><strong>Evita comer cerca de los monumentos:</strong> los restaurantes a 100 metros de la Torre Eiffel o el Louvre tienen precios inflados y calidad mediocre.</li>
</ul>

<h2>Los errores más comunes en París</h2>
<ul>
<li><strong>No reservar la Torre Eiffel:</strong> la cola sin reserva puede arruinarte la mañana</li>
<li><strong>Intentar verlo todo:</strong> París se disfruta caminando y parando, no corriendo de monumento en monumento</li>
<li><strong>Coger taxi desde el aeropuerto:</strong> el RER es 5 veces más barato</li>
<li><strong>Comer cerca de los monumentos:</strong> da media vuelta y camina 5 calles</li>
<li><strong>Ignorar los barrios menos turísticos:</strong> Belleville, Oberkampf y Canal Saint-Martin son la París real</li>
<li><strong>No llevar paraguas:</strong> París llueve con frecuencia todo el año</li>
</ul>

<h2>Presupuesto orientativo para 3 días en París</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.9rem;margin:16px 0;">
<tr style="background:#f4f6f9;"><th style="padding:8px;text-align:left;">Concepto</th><th style="padding:8px;text-align:right;">Por persona</th></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Vuelo ida y vuelta desde España</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">50-150 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Alojamiento (3 noches)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">150-300 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Transporte (metro, RER aeropuerto)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">25-40 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Comida (3 días, siendo inteligente)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">60-120 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Entradas (Torre Eiffel, Louvre, Orsay)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">45-65 €</td></tr>
<tr style="background:#fde8e6;font-weight:700;"><td style="padding:8px;">TOTAL</td><td style="padding:8px;text-align:right;">330-675 €</td></tr>
</table>
"""

PARIS_GC = gc("cómo ahorrar en París", [
    "<strong>Vuela entre semana y fuera de temporada alta:</strong> los vuelos Madrid/Barcelona-París pueden encontrarse desde 30-60 euros ida y vuelta con Vueling, Iberia Express o Transavia si reservas con 4-8 semanas de antelación.",
    "<strong>Museos gratis el primer domingo del mes:</strong> el Louvre, el Musée d'Orsay y el Centre Pompidou son gratuitos el primer domingo de cada mes. Planifica tu visita alrededor de este día y ahorra 25-30 euros por persona.",
    "<strong>Carnet de 10 viajes de metro (17,35 euros):</strong> si coges el metro más de 8 veces en 3 días es más barato que pagar suelto (2,15 euros/viaje).",
    "<strong>Desayuna en boulangerie, no en cafés turísticos:</strong> café más croissant en una panadería local: 3-4 euros. El mismo desayuno en un café cerca de la Torre Eiffel: 9-12 euros.",
    "<strong>Almuerzos con el menú del mediodía:</strong> los bistros parisinos ofrecen menú de 2 platos por 14-18 euros al mediodía. Por la noche, los mismos platos cuestan 30-40 euros. Come fuerte a mediodía y cena ligero.",
    "<strong>Alójate en barrios fuera del centro:</strong> Belleville, Oberkampf o Montrouge están a 10-15 minutos del centro en metro. El alojamiento cuesta un 30-50% menos que en Saint-Germain o Le Marais.",
    "<strong>La Torre Eiffel por fuera es gratis:</strong> ver la Torre Eiffel de noche desde el Trocadéro (gratis) es tan impactante como subir (26 euros). Si el presupuesto es ajustado, no lo dudes.",
])

NUEVA_YORK = """<p>Nueva York supera todas las expectativas. La energía de sus calles, la escala de sus rascacielos, la densidad de planes y la diversidad de sus barrios hacen que incluso los más escépticos acaben enamorándose. Esta guía no es una lista de monumentos — es una guía práctica para entender cómo funciona la ciudad y cómo sacarle el máximo partido, tanto si vas una semana como si vas diez días.</p>

<h2>Entender Nueva York: los cinco boroughs</h2>
<ul>
<li><strong>Manhattan:</strong> donde está todo lo que conoces de las películas. Midtown (Times Square, Empire State), Downtown (Wall Street, 9/11 Memorial), Uptown (Central Park, Harlem)</li>
<li><strong>Brooklyn:</strong> el barrio más de moda. DUMBO, Williamsburg (hipster, restaurantes, noche), Park Slope (familias, tranquilo)</li>
<li><strong>Queens:</strong> el más multicultural. Jackson Heights para comida latina e india, Flushing para la mejor comida china fuera de China</li>
</ul>

<h2>Cómo moverse en Nueva York</h2>

<h3>El metro: la clave para no arruinarse</h3>
<p>El metro de Nueva York funciona las 24 horas. Precio: 2,90 dólares por trayecto. Para estancias de más de 4 días, la tarjeta de 7 días (34 dólares) es mucho más económica. Descarga la app <strong>Citymapper</strong> o usa Google Maps en modo tránsito.</p>

<h3>A pie</h3>
<p>Manhattan está diseñado en cuadrícula y es muy fácil orientarse. Las avenidas van de norte a sur, las calles de este a oeste. La mayor parte del turismo en Midtown y Downtown se puede hacer caminando.</p>

<h2>Qué ver en Nueva York — los imprescindibles</h2>

<h3>The High Line</h3>
<p>Un parque elevado construido sobre una antigua vía de tren abandonada. 2,3 km de paseo con arte, jardines y vistas de Manhattan. Gratis. Imprescindible. Empieza en el extremo sur (calle 10) y termina en el Hudson Yards.</p>

<h3>Central Park</h3>
<p>341 hectáreas en el corazón de Manhattan. Alquila una bici, haz un picnic en Sheep Meadow, da de comer a las ardillas en Strawberry Fields (el memorial de John Lennon) o da un paseo en barca por el lago. Gratis.</p>

<h3>Brooklyn Bridge y DUMBO</h3>
<p>Cruzar el puente de Brooklyn a pie (30-40 minutos desde Manhattan) es una de las experiencias más bonitas de Nueva York. Desde el barrio de DUMBO tienes las mejores vistas de Manhattan enmarcado bajo el puente.</p>

<h3>El 9/11 Memorial</h3>
<p>Las dos piscinas reflejan en el lugar exacto donde estaban las Torres Gemelas. Uno de los espacios más emocionantes de la ciudad. La entrada al memorial exterior es gratuita. El museo (29 dólares) es muy completo.</p>

<h3>Times Square — una vez y no más</h3>
<p>Tienes que ir. Ve de noche para ver las luces de neón, hazte la foto y continúa. No cenes aquí — los restaurantes son mediocres y caros.</p>

<h3>Los miradores — elige uno</h3>
<ul>
<li><strong>Top of the Rock (40 dólares):</strong> las mejores vistas de Manhattan porque ves el Empire State Building desde aquí</li>
<li><strong>Empire State Building (44 dólares):</strong> icónico, desde arriba ves el Rockefeller Center</li>
<li><strong>Edge (Hudson Yards, 36 dólares):</strong> el más nuevo y espectacular, con suelo de cristal. Menos colas</li>
<li><strong>Opción gratuita:</strong> el transbordador de Staten Island pasa frente a la Estatua de la Libertad. Solo necesitas el billete de metro.</li>
</ul>

<h3>Los museos</h3>
<ul>
<li><strong>MET (Metropolitan Museum of Art):</strong> el más grande de América. 30 dólares para turistas. Necesitas al menos medio día.</li>
<li><strong>MoMA (25 dólares):</strong> arte moderno. Los viernes de 17:00 a 21:00 es gratuito.</li>
<li><strong>Brooklyn Museum (gratis el primer sábado de mes):</strong> enorme colección, sin las colas del MET</li>
</ul>

<h2>Dónde comer en Nueva York sin gastar una fortuna</h2>
<ul>
<li><strong>Diners:</strong> el desayuno americano clásico (huevos, tostadas, café ilimitado) por 8-12 dólares.</li>
<li><strong>Halal cart:</strong> pollo o cordero con arroz y salsa blanca por 7-8 dólares. Comida de calle neoyorkina auténtica.</li>
<li><strong>Chinatown:</strong> dumplings desde 1 dólar la pieza, sopas de fideos por 10 dólares</li>
<li><strong>Pizza por porciones (slice):</strong> 3-5 dólares la porción grande. Joe's Pizza en el Village es el clásico.</li>
<li><strong>Bagel:</strong> bagel con salmón ahumado y queso crema por 8-12 dólares. Ess-a-Bagel o Absolute Bagels son instituciones.</li>
</ul>

<h2>Los barrios que no debes perderte</h2>

<h3>Williamsburg (Brooklyn)</h3>
<p>El barrio más trendy de Nueva York. Tiendas vintage, street art, los mejores brunchs de la ciudad, vistas del skyline. A 5 minutos de Manhattan en metro (línea L).</p>

<h3>Harlem</h3>
<p>El corazón de la cultura afroamericana. El gospel del domingo en la Abyssinian Baptist Church es una experiencia única (llega con tiempo). Comida soul food increíble.</p>

<h3>Chinatown y Little Italy</h3>
<p>Chinatown es auténtico y enorme. Little Italy tiene el encanto turístico con restaurantes italianos en la Mulberry Street.</p>

<h2>Presupuesto real para 7 días en Nueva York</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.9rem;margin:16px 0;">
<tr style="background:#f4f6f9;"><th style="padding:8px;text-align:left;">Concepto</th><th style="padding:8px;text-align:right;">Económico</th><th style="padding:8px;text-align:right;">Cómodo</th></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Vuelo ida y vuelta desde España</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">350-550 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">550-900 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Alojamiento 7 noches</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">500-700 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">1.200-2.000 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Metro (tarjeta semanal)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">32 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">32 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Comida 7 días</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">200-300 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">400-600 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Entradas museos y miradores</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">80-120 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">120-200 €</td></tr>
<tr style="background:#fde8e6;font-weight:700;"><td style="padding:8px;">TOTAL POR PERSONA</td><td style="padding:8px;text-align:right;">1.162-1.702 €</td><td style="padding:8px;text-align:right;">2.302-3.732 €</td></tr>
</table>

<h2>Lo que nadie te cuenta de Nueva York</h2>
<ul>
<li><strong>El jet lag es real:</strong> Nueva York son 6 horas menos que España. Aguanta hasta las 22h el primer día y te adaptas más rápido.</li>
<li><strong>Las propinas son obligatorias:</strong> en restaurantes, el 20% de propina es la norma. No es opcional — los camareros cobran sueldo mínimo asumiendo que la propina llega.</li>
<li><strong>El precio no incluye impuestos:</strong> lo que ves en el menú lleva un 8,875% de impuesto encima.</li>
<li><strong>Nueva York en agosto es muy caluroso:</strong> 30-38 grados con humedad extrema. El metro sin aire acondicionado puede ser sofocante.</li>
</ul>
"""

NUEVA_YORK_GC = gc("cómo ahorrar en Nueva York", [
    "<strong>Vuela en temporada baja:</strong> noviembre (excepto Thanksgiving), enero y febrero son los meses más baratos. Los vuelos Madrid-Nueva York pueden encontrarse desde 280-400 euros ida y vuelta en estas fechas.",
    "<strong>Tarjeta semanal de metro (34 dólares):</strong> si coges el metro más de 12 veces en la semana, la tarjeta semanal compensa frente a pagar 2,90 dólares por viaje.",
    "<strong>Ferry de Staten Island — gratis y espectacular:</strong> pasa frente a la Estatua de la Libertad, las vistas del skyline son increíbles y no te cuesta nada. No gastes 25 dólares en el ferry de turistas.",
    "<strong>MoMA gratis los viernes por la tarde:</strong> de 17:00 a 21:00 la entrada es gratuita. Llega a las 16:30 para hacer cola.",
    "<strong>Come en Chinatown y los food trucks:</strong> un halal cart o unos dumplings en Chinatown te cuestan 5-8 dólares. Lo mismo en un restaurante de Midtown: 20-30 dólares.",
    "<strong>Alójate en Brooklyn o Queens:</strong> los precios de alojamiento son un 30-50% más bajos que en Manhattan. Williamsburg está a 5 minutos en metro de Midtown.",
    "<strong>New York City Pass (136 dólares):</strong> si tienes pensado visitar varios museos y miradores, el CityPASS incluye 5 atracciones mayores y puede ahorrar 60-80 dólares respecto a pagar individualmente.",
])

BALI = """<p>Bali no es solo una isla — es un destino que reúne en 5.800 km2 playas tropicales, arrozales en terrazas milenarias, templos hindúes con siglos de historia, una gastronomía increíble y una espiritualidad que se siente en cada rincón. Pero Bali también puede decepcionar si no se planifica bien: hay zonas masificadas, tráfico denso y trampas turísticas. Esta guía te ayuda a encontrar el Bali real.</p>

<h2>Las zonas de Bali: cuál elegir según tu perfil</h2>

<h3>Seminyak y Canggu — playas y ambiente</h3>
<p>La zona más desarrollada y moderna. Seminyak tiene los mejores beach clubs (Ku De Ta, Potato Head), tiendas, restaurantes de nivel internacional y bares sofisticados. Canggu es más relajada, favorita de los nómadas digitales con cafés con wifi rápido y olas para surf.</p>
<p><strong>Ideal para:</strong> fiestas, beach clubs, surf, nómadas digitales. Precio alojamiento: 30-120 euros/noche.</p>

<h3>Ubud — cultura y naturaleza</h3>
<p>El corazón espiritual y cultural de Bali. Rodeado de arrozales en terrazas, templos, galerías de arte y centros de bienestar. Aquí está el famoso Monkey Forest, los arrozales de Tegallalang, el Tirta Empul (templo del agua sagrada) y los mejores spas de toda la isla.</p>
<p><strong>Ideal para:</strong> cultura, yoga, meditación, naturaleza. Las rice field villas (con vistas a los arrozales) son increíbles por 40-80 euros.</p>

<h3>Nusa Penida y Nusa Lembongan — islas vírgenes</h3>
<p>A 45 minutos en barco desde Sanur. Kelingking Beach (la playa del dinosaurio), Crystal Bay para bucear con manta rays y Broken Beach son imprescindibles. Menos desarrolladas, más auténticas.</p>
<p><strong>Ideal para:</strong> buceo, snorkel, fotógrafos, viajeros que huyen de masas. Precio: 15-60 euros/noche.</p>

<h3>Uluwatu y Bukit Peninsula — acantilados y olas</h3>
<p>Acantilados espectaculares, el templo de Uluwatu al borde de un precipicio de 70 metros sobre el mar, las mejores olas para surf avanzado y beach clubs con vistas de película. El atardecer con el espectáculo de danza Kecak es de las experiencias más impresionantes de Asia.</p>

<h2>Itinerario recomendado para 10 días en Bali</h2>
<ul>
<li><strong>Días 1-2:</strong> Llegada a Seminyak. Descanso del jet lag, playa, beach club al atardecer</li>
<li><strong>Días 3-4:</strong> Ubud. Arrozales de Tegallalang, Monkey Forest, templo Tirta Empul, spa tradicional</li>
<li><strong>Días 5-6:</strong> Nusa Penida. Ferry desde Sanur, Kelingking Beach, Angel's Billabong, Crystal Bay</li>
<li><strong>Días 7-8:</strong> Regreso a Bali, Uluwatu. Templo al atardecer, danza Kecak, surf o yoga</li>
<li><strong>Días 9-10:</strong> Canggu. Exploración tranquila, mercado de Seminyak, compras, última noche</li>
</ul>

<h2>Imprescindibles que no puedes perderte</h2>

<h3>Los arrozales de Tegallalang (Ubud)</h3>
<p>Las terrazas de arroz más fotografiadas de Bali. Hay que pagar una pequeña entrada (aproximadamente 1 euro). Ve a primera hora de la mañana (7-9h) para evitar el calor y las multitudes.</p>

<h3>Templo de Tanah Lot</h3>
<p>El templo más icónico de Bali — emerge del mar sobre una roca volcánica. Más impresionante al atardecer. A 20 km de Seminyak.</p>

<h3>Kelingking Beach (Nusa Penida)</h3>
<p>La playa más fotografiada de Indonesia — un acantilado con forma de dinosaurio y una playa turquesa abajo. Puedes bajar (45 minutos de bajada muy empinada) o simplemente disfrutar las vistas desde arriba.</p>

<h3>Monte Batur</h3>
<p>El volcán activo de Bali. La excursión nocturna para ver el amanecer desde la cima (1.717 metros) es una de las más populares de la isla. Sal a la 1:00-2:00 AM con guía. Precio: 20-40 euros con guía.</p>

<h3>Danza Kecak en Uluwatu</h3>
<p>Espectáculo de danza tradicional balinesa al atardecer en el templo de Uluwatu. El escenario, con el mar y los acantilados de fondo, es único. Precio: 10-15 euros. Reserva con tiempo.</p>

<h2>Cómo moverse en Bali</h2>
<p><strong>El tráfico es el mayor problema de Bali.</strong> Las distancias parecen cortas en el mapa pero tardan el doble de lo esperado.</p>
<ul>
<li><strong>Scooter alquilado:</strong> 5-8 euros/día. La forma más práctica y económica. Cuidado con el tráfico, lleva siempre casco.</li>
<li><strong>Gojek y Grab:</strong> el Uber de Indonesia. 2-5 euros trayectos cortos. No funciona en algunas zonas donde los taxistas locales han presionado para prohibirlo.</li>
<li><strong>Private driver:</strong> 40-60 euros/día (coche con conductor). Muy cómodo para excursiones de día completo, especialmente en grupo.</li>
</ul>

<h2>Dónde comer en Bali</h2>
<ul>
<li><strong>Warungs (restaurantes locales):</strong> el nasi goreng (arroz frito), nasi campur (arroz con acompañamientos) y mie goreng (fideos fritos) cuestan 1-3 euros. Son la mejor comida de la isla.</li>
<li><strong>Seminyak y Canggu:</strong> restaurantes internacionales de nivel, smoothie bowls, cafés con diseño. 8-20 euros por persona.</li>
<li><strong>Mercado nocturno de Gianyar:</strong> el mejor mercado de comida local de Bali, a 15 km de Ubud. 1-3 euros por plato.</li>
</ul>

<h2>Cuándo ir a Bali</h2>
<p><strong>Temporada seca (abril-octubre):</strong> el mejor tiempo. Mayo, junio y septiembre son perfectos — menos turistas que julio-agosto, cielos despejados, mar en calma. Julio y agosto son temporada alta con precios más altos.</p>
<p><strong>Temporada de lluvias (noviembre-marzo):</strong> lluvias intensas por las tardes, pero raramente todo el día. Los paisajes son más verdes. Los precios bajan considerablemente.</p>

<h2>Presupuesto real para 10 días en Bali</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.9rem;margin:16px 0;">
<tr style="background:#f4f6f9;"><th style="padding:8px;text-align:left;">Concepto</th><th style="padding:8px;text-align:right;">Mochilero</th><th style="padding:8px;text-align:right;">Viajero cómodo</th></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Vuelo desde España (con escala)</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">500-700 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">700-1.100 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Alojamiento 10 noches</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">150-250 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">400-800 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Transporte interno</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">80-120 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">150-250 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Comida 10 días</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">80-120 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">200-350 €</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #eee;">Actividades y entradas</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">80-120 €</td><td style="padding:8px;text-align:right;border-bottom:1px solid #eee;">150-250 €</td></tr>
<tr style="background:#fde8e6;font-weight:700;"><td style="padding:8px;">TOTAL POR PERSONA</td><td style="padding:8px;text-align:right;">890-1.310 €</td><td style="padding:8px;text-align:right;">1.600-2.750 €</td></tr>
</table>

<h2>Consejos finales para tu viaje a Bali</h2>
<ul>
<li><strong>Visado:</strong> españoles no necesitan visado para estancias de hasta 30 días. Para más tiempo, visa on arrival renovable (35 dólares).</li>
<li><strong>Moneda:</strong> rupia indonesia (IDR). 1 euro aprox. 17.000 IDR. Cambia en money changers oficiales — evita el aeropuerto y la calle.</li>
<li><strong>Ropa para templos:</strong> lleva siempre un sarong (tela para cubrir las piernas). Los prestan o alquilan en la entrada por 1 euro.</li>
<li><strong>Agua:</strong> el agua del grifo no es potable. Bebe siempre agua embotellada.</li>
<li><strong>Los monos del Monkey Forest muerden:</strong> no lleves nada de comer visible y no te agaches a su nivel.</li>
<li><strong>Regatear es habitual</strong> en mercados y tiendas locales. Empieza ofreciendo el 50% del precio pedido.</li>
</ul>
"""

BALI_GC = gc("cómo ahorrar en Bali", [
    "<strong>Vuela en temporada de lluvias (noviembre-marzo):</strong> los precios de vuelo y alojamiento bajan un 30-40%. Las lluvias suelen ser por la tarde y el resto del día es soleado. Ahorras 200-400 euros en vuelo y 150-300 euros en alojamiento.",
    "<strong>Usa Gojek y Grab en vez de taxis:</strong> un trayecto de 15 minutos en Gojek cuesta 1,5-3 euros. El mismo trayecto en taxi negociado en la calle: 8-15 euros. El ahorro es enorme si te mueves mucho.",
    "<strong>Alquila una scooter si sabes conducir moto:</strong> 5-8 euros/día vs 30-50 euros/día de un private driver. Para moverse dentro de una zona es perfecta.",
    "<strong>Come en warungs locales:</strong> un nasi goreng en un warung local cuesta 1,5-3 euros. La misma comida en un restaurante orientado a turistas en Seminyak: 8-15 euros. Y el del warung suele estar más bueno.",
    "<strong>Mercado nocturno de Gianyar para cenar:</strong> a 15 km de Ubud, este mercado tiene la mejor comida local de Bali por 1-3 euros el plato.",
    "<strong>Cambia dinero en money changers confiables, no en el aeropuerto:</strong> el tipo de cambio del aeropuerto es un 10-15% peor. Saca cash en cajeros dentro de Bali o cambia en money changers conocidos.",
    "<strong>Alójate en Ubud o Canggu, no en Seminyak:</strong> Seminyak tiene los precios más altos. Canggu es un 20-30% más barata con el mismo ambiente.",
])

# ─── Build POSTS list ─────────────────────────────────────────────────────────
POSTS = [
    {
        "slug": "maldivas-guia-viaje-economico",
        "title": "Maldivas sin gastar una fortuna: guía completa de las islas locales",
        "excerpt": "Cómo visitar las Maldivas por 60-80 euros al día en vez de 800. Las islas locales, los mejores guesthouses, cómo moverse y qué no te puede faltar.",
        "image_url": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category": "internacional",
        "content": MALDIVAS + MALDIVAS_GC,
    },
    {
        "slug": "que-ver-en-islandia-guia-completa",
        "title": "Islandia: guía completa para viajeros — auroras, Ring Road y presupuesto real",
        "excerpt": "Todo lo que necesitas saber para organizar tu viaje a Islandia: la Ruta del Círculo Dorado, la Ring Road, cuándo ver las auroras boreales y cuánto cuesta de verdad.",
        "image_url": "https://images.unsplash.com/photo-1531366936337-7c912a4589a7?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category": "europa",
        "content": ISLANDIA + ISLANDIA_GC,
    },
    {
        "slug": "paris-tres-dias-itinerario",
        "title": "París en 3 días: itinerario completo, barrios, comida y consejos reales",
        "excerpt": "El itinerario definitivo para sacarle el máximo a París en 3 días. Qué ver, cómo evitar colas, dónde comer sin pagar como turista y los errores más comunes.",
        "image_url": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category": "europa",
        "content": PARIS + PARIS_GC,
    },
    {
        "slug": "que-ver-en-nueva-york-guia-completa",
        "title": "Nueva York: guía completa para tu primer viaje — barrios, transporte y presupuesto real",
        "excerpt": "Manhattan, Brooklyn, Central Park, los mejores barrios donde comer y moverse. Todo lo que necesitas para aprovechar al máximo tu viaje a Nueva York.",
        "image_url": "https://images.unsplash.com/photo-1485738422979-f5c462d49f74?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category": "internacional",
        "content": NUEVA_YORK + NUEVA_YORK_GC,
    },
    {
        "slug": "que-ver-en-bali-guia-completa",
        "title": "Bali: guía completa — zonas, itinerario, costes y consejos para tu viaje",
        "excerpt": "Ubud, Seminyak, Nusa Penida y los templos. Cómo dividir tu tiempo en Bali, cuánto cuesta de verdad y qué errores evitar en tu primer viaje a la isla de los dioses.",
        "image_url": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?fm=jpg&q=80&w=800&auto=format&fit=crop",
        "category": "internacional",
        "content": BALI + BALI_GC,
    },
]

# ─── Write to DB ──────────────────────────────────────────────────────────────
conn = psycopg2.connect(config.DATABASE_URL)
cur = conn.cursor()

for p in POSTS:
    cur.execute(
        """UPDATE posts SET title=%s, excerpt=%s, content=%s, image_url=%s, category=%s
           WHERE slug=%s""",
        (p["title"], p["excerpt"], p["content"], p["image_url"], p["category"], p["slug"]),
    )
    words = len(p["content"].split())
    print(f"✓  {p['slug']}  —  ~{words} palabras  ({cur.rowcount} fila actualizada)")

conn.commit()
cur.close()
conn.close()
print("\n✅  Las 5 guías actualizadas con GangaConsejos incluidos")
