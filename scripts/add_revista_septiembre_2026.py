"""
Primer numero de la Revista GangaViaje: Septiembre 2026.
Curaduria de contenido ya publicado (destino, insolito, consejo, oferta real,
mas la novedad de Guia a Medida) -- sin republicar articulos completos, solo
extractos editoriales + enlace a la pieza real en la web.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database

issue = {
    "slug": "septiembre-2026",
    "issue_label": "Septiembre 2026",
    "headline": "Cracovia: la escapada barata que parece cara",
    "subheadline": "Casco antiguo intacto, castillo real y dos visitas Patrimonio de la Humanidad a las puertas de la ciudad. La portada de este número.",
    "cover_image_url": "https://images.unsplash.com/photo-1686252289176-6c4d15b7bc88?fm=jpg&q=80&w=1600&auto=format&fit=crop",
    "intro": "Bienvenidos al primer número de la Revista GangaViaje. Cada mes vamos a reunir aquí, en un solo sitio, lo mejor de lo que publicamos durante esas semanas: el destino que más nos ha convencido, la curiosidad de viaje que no nos hemos podido quitar de la cabeza, el consejo que más dinero ahorra y, si lo encontramos, alguna oferta real que merezca la pena. Nada de contenido de relleno — si un mes no hay nada bueno que contar, ese mes la revista será más corta. Empezamos con septiembre, probablemente el mes más infravalorado del calendario de viajes.",
    "sections": [
        {
            "label": "Destino del mes",
            "icon": "🗺️",
            "title": "Cracovia: la escapada barata que parece cara",
            "excerpt": "Casco antiguo intacto, un castillo real a la altura de cualquier capital y dos visitas Patrimonio de la Humanidad a las puertas de la ciudad — la mina de sal de Wieliczka y, a poco más de una hora, Auschwitz-Birkenau. Septiembre es, además, uno de los mejores meses para ir: buen tiempo y bastante menos gente que en verano.",
            "pull_quote": "Es, con diferencia, la visita más dura y también una de las más importantes que se pueden hacer en Europa.",
            "image_url": "https://images.unsplash.com/photo-1686252289176-6c4d15b7bc88?fm=jpg&q=80&w=1200&auto=format&fit=crop",
            "second_image_url": "https://images.unsplash.com/photo-1707836995984-d7eb71186d09?fm=jpg&q=80&w=1200&auto=format&fit=crop",
            "second_image_caption": "La Plaza Mayor de Cracovia (Rynek Główny), con el Sukiennice y las torres de la Basílica de Santa María al fondo.",
            "link": "/blog/cracovia-polonia-guia-completa",
            "cta": "Leer la guía completa",
        },
        {
            "label": "Viajes Insólitos",
            "icon": "🌍",
            "title": "La isla donde vivir significa esperar un barco",
            "excerpt": "Tristán da Cunha tiene poco más de 220 habitantes, repartidos entre solo nueve apellidos, y ni un aeropuerto. La única forma de llegar es un barco desde Ciudad del Cabo que tarda entre 5 y 10 días. Esta es la historia del lugar habitado más remoto del planeta — y de por qué, aun así, sigue recibiendo visitantes cada año.",
            "pull_quote": "Toda la isla se reparte entre nueve apellidos: Glass, Green, Hagan, Lavarello, Repetto, Rogers, Swain, Collins y Squibb.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/View_of_Tristan_da_Cunha_from_Nightingale_island.jpg/1920px-View_of_Tristan_da_Cunha_from_Nightingale_island.jpg",
            "second_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Edinburgh_of_the_Seven_Seas_01.jpg/1280px-Edinburgh_of_the_Seven_Seas_01.jpg",
            "second_image_caption": "Edimburgo de los Siete Mares, el único asentamiento de Tristán da Cunha.",
            "link": "/blog/tristan-da-cunha-isla-mas-remota-del-mundo",
            "cta": "Descubrir la isla",
        },
        {
            "label": "El consejo del mes",
            "icon": "💡",
            "title": "Los trucos de vuelos baratos que de verdad funcionan en 2026",
            "excerpt": "Septiembre es el mes en el que se empieza a planificar el resto del año de viajes. Antes de abrir el buscador, repasa qué funciona de verdad en 2026 y qué son mitos que ya no sirven de nada — desde la ventana de compra óptima hasta el truco (infrautilizado) de los aeropuertos alternativos.",
            "pull_quote": "Cambiar las fechas de salida o vuelta en 1-2 días puede generar ahorros del 20-50%.",
            "image_url": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=1200&auto=format&fit=crop",
            "link": "/blog/vuelos-baratos-trucos-encontrar-mejores-ofertas",
            "cta": "Ver todos los trucos",
        },
        {
            "label": "Chollo del mes",
            "icon": "🎟️",
            "title": "Vuelos baratos a todo el mundo, más de 500 aerolíneas",
            "excerpt": "Un buscador que compara más de 500 aerolíneas y 10.000 destinos de un vistazo — el punto de partida para cualquiera de los planes de este número, empezando por Cracovia.",
            "image_url": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?fm=jpg&q=80&w=1200&auto=format&fit=crop",
            "link": "https://www.dpbolvw.net/click-101767089-17053226",
            "cta": "Buscar vuelos",
        },
        {
            "label": "Novedad",
            "icon": "✨",
            "title": "Guía a Medida: le dices destino y fechas, te la preparamos nosotros",
            "excerpt": "Este mes hemos lanzado algo nuevo: dinos a dónde vas y cuándo, y en 48 horas tienes una guía de viaje personalizada — itinerario día a día, recomendaciones reales y las mejores ofertas para esas fechas. Gratis, sin letra pequeña.",
            "image_url": "https://images.unsplash.com/photo-1655722723663-75b47de17a31?fm=jpg&q=80&w=1200&auto=format&fit=crop",
            "link": "/guia-a-medida",
            "cta": "Pide la tuya gratis",
        },
    ],
}

if __name__ == "__main__":
    issue_id = database.add_magazine_issue(issue)
    print("número publicado, id:", issue_id)
