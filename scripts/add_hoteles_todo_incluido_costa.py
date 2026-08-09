"""
Añade el post "Hoteles todo incluido más baratos en la costa española para agosto".
Script de un solo uso.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database
from scrapers.booking_es import _deep_url

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

# Enlaces reales de afiliado ya confirmados (Iberostar vía CJ) para Mallorca y Canarias.
def _affiliate_url(deal_id):
    conn = database.get_conn()
    cur = conn.cursor()
    cur.execute("SELECT affiliate_url FROM deals WHERE id = %s", (deal_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else "#"

URL_CANARIAS = _affiliate_url(459)
URL_MALLORCA_1 = _affiliate_url(464)  # Jardín del Sol Suites
URL_MALLORCA_2 = _affiliate_url(461)  # Ciudad Blanca
URL_MALLORCA_3 = _affiliate_url(462)  # Bahía de Palma
URL_MALLORCA_4 = _affiliate_url(463)  # Cristina

URL_BENIDORM = _deep_url("Benidorm")
URL_GRAN_CANARIA = _deep_url("Maspalomas")
URL_COSTA_SOL = _deep_url("Costa del Sol")
URL_SALOU = _deep_url("Salou")
URL_CADIZ = _deep_url("Costa de la Luz Cádiz")
URL_HUELVA = _deep_url("Costa de la Luz Huelva")
URL_LANZAROTE = _deep_url("Lanzarote")
URL_FUERTEVENTURA = _deep_url("Fuerteventura")
URL_ALMERIA = _deep_url("Aguadulce Almería")

CONTENT = f"""<p>Agosto es el mes más caro para viajar por la costa española, pero también donde el todo incluido tiene más sentido: sabes exactamente lo que vas a gastar antes de salir de casa, sin sorpresas de restaurante ni de barra. El problema es que "todo incluido" no significa lo mismo en todos los hoteles — varía la franja horaria del buffet, si las bebidas son de marca o genéricas, y si el régimen real es todo incluido o media pensión disfrazada. Esta guía va de más barato a más caro, con hoteles reales y precios de referencia — no está ordenada por ningún interés nuestro, solo por precio.</p>

{gc("cómo comprobar que el todo incluido es de verdad", [
    "Lee el detalle del régimen en la ficha, no solo el nombre del paquete — algunos hoteles llaman \"todo incluido\" a lo que en realidad es media pensión con barra libre limitada a ciertas horas.",
    "Comprueba el horario del buffet y de la barra libre: en temporada alta muchos hoteles recortan horas.",
    "Bebidas: mira si son \"nacionales\" (marca blanca/genéricas) o de marca — cambia bastante la experiencia, aunque no el precio.",
    "Compara el mismo hotel en Booking, Hotels.com y la web del hotel — el régimen y el precio pueden variar entre plataformas para las mismas fechas.",
])}

<h2>De más barato a más caro (precio por persona y noche, agosto)</h2>
<p>Según agencias especializadas en todo incluido (BuscoUnChollo, Hotelestodoincluido), estos son los rangos reales que te vas a encontrar este agosto en la costa española. Los precios exactos varían por antelación y disponibilidad, así que trátalos como orden de magnitud, no como precio garantizado:</p>
<ul>
<li><strong>Desde ~42€/persona/noche — Hotel Portomagno, Aguadulce (Almería).</strong> Recomendado por experiencia propia: estuvimos la semana pasada y es de las mejores relaciones calidad-precio que hemos visto. Hotel 4 estrellas en primera línea de playa, con opción de pensión completa o todo incluido (con bebidas dentro y fuera de las comidas). Como referencia, hay ofertas de 3 noches en pensión completa por 126€/persona.</li>
<li><strong>Desde ~60€/persona/noche — Benidorm.</strong> Es probablemente la zona con más densidad de hoteles todo incluido de toda España, lo que mantiene los precios ajustados por pura competencia. Opciones conocidas en la zona: <strong>Hotel Flamingo Oasis</strong> y <strong>Hotel Villa del Mar</strong>, en primera línea de Playa de Poniente.</li>
<li><strong>Desde ~75€/persona/noche — Gran Canaria (Maspalomas / Playa del Inglés).</strong> Canarias tiene la ventaja de no tener temporada alta de calor como el resto de España, así que en agosto no pagas la sobretasa térmica que sí pagas en el Mediterráneo.</li>
<li><strong>Desde ~125€/noche (por habitación) — Costa del Sol.</strong> El <strong>Hotel Palia La Roca</strong> en Benalmádena y el <strong>Parasol Garden</strong> frente a la playa (en torno a 150€ para dos adultos y un niño en agosto) son de los más baratos de la zona.</li>
<li><strong>Desde ~125-160€/noche — Iberostar en Mallorca.</strong> Baleares suele ser la costa española más cara en agosto, así que no son los más baratos de España, pero dentro de Mallorca son de las opciones todo incluido más ajustadas de la isla — precios reales confirmados, no estimados: <a href="{URL_MALLORCA_3}">Iberostar Waves Cristina</a> (125€), <a href="{URL_MALLORCA_2}">Iberostar Waves Bahía de Palma</a> (130€), <a href="{URL_MALLORCA_1}">Iberostar Waves Ciudad Blanca</a> (145€), <a href="{URL_MALLORCA_4}">Iberostar Selection Jardín del Sol Suites</a> (160€).</li>
</ul>
<p>Dónde reservar en cada zona: <a href="{URL_ALMERIA}">Aguadulce (Almería)</a> · <a href="{URL_BENIDORM}">Benidorm</a> · <a href="{URL_GRAN_CANARIA}">Gran Canaria (Maspalomas)</a> · <a href="{URL_COSTA_SOL}">Costa del Sol</a>.</p>

<h2>Salou (Costa Dorada) — los mejor valorados por los propios huéspedes</h2>
<p>Salou concentra varios de los todo incluido mejor valorados de España, aunque no siempre los más baratos. El <strong>Ohtels Villa Dorada</strong> tiene 7,7/10 en Central de Reservas con más de 1.000 valoraciones, y los huéspedes destacan especialmente el propio todo incluido y la relación calidad-precio. El <strong>Golden Port Salou & Spa</strong> y el <strong>Estival ElDorado Resort</strong> son otras opciones habituales bien valoradas en la zona. Ojo con el <strong>Ponient Dorada Palace</strong>: tiene todo incluido real como una de sus opciones, pero también ofrece media pensión y solo alojamiento — el precio más bajo que veas anunciado (desde ~130€) suele ser de la opción más básica, no del todo incluido, así que confirma el régimen exacto antes de reservar.</p>
<p><a href="{URL_SALOU}">Ver hoteles en Salou →</a></p>

<h2>Costa de la Luz (Cádiz y Huelva) — la más tranquila y menos masificada</h2>
<p>Si buscas todo incluido sin el ambiente de discoteca de Benidorm o Salou, la Costa de la Luz es la alternativa, con precios generalmente algo más bajos por estar menos masificada. En Cádiz destacan el <strong>Hipotels Barrosa Garden</strong>, el <strong>Playaballena Aquapark & Spa</strong> (con parque acuático propio) y el <strong>Best Costa Ballena</strong>. En Huelva, el <strong>Barceló Punta Umbría Beach Resort</strong> y el <strong>Gran Hotel del Coto</strong> son las opciones todo incluido más conocidas de la zona.</p>
<p><a href="{URL_CADIZ}">Ver hoteles en Cádiz →</a> · <a href="{URL_HUELVA}">Ver hoteles en Huelva →</a></p>

<h2>Fuerteventura y Lanzarote — Canarias fuera de Gran Canaria</h2>
<p>En Fuerteventura, el <strong>Barceló Fuerteventura Mar</strong> ofrece todo incluido con animación, tenis y pádel a 7 km del aeropuerto. En Lanzarote, la cadena H10 tiene varios todo incluido bien situados. Iberostar tiene además una oferta de verano con hasta un 30% de descuento en sus hoteles de Canarias en general, con precios reales desde 126€: <a href="{URL_CANARIAS}">ver oferta de Iberostar en Canarias →</a></p>
<p><a href="{URL_LANZAROTE}">Ver hoteles en Lanzarote →</a> · <a href="{URL_FUERTEVENTURA}">Ver hoteles en Fuerteventura →</a></p>

<h2>Antes de reservar</h2>
<p>Los precios de este artículo son de referencia — cambian según la fecha exacta, la antelación con la que reserves y la disponibilidad del momento, así que compruébalos siempre en el buscador antes de decidir. Si quieres profundizar en cómo encontrar siempre el precio más bajo (comparadores, programas de fidelidad, cuándo reservar), tenemos una <a href="/blog/hoteles-baratos-como-conseguir-mejor-precio">guía completa de hoteles baratos</a>.</p>
"""

post = {
    "slug": "hoteles-todo-incluido-baratos-costa-espana-agosto",
    "title": "Hoteles todo incluido más baratos en la costa española para agosto",
    "excerpt": "De más barato a más caro: Almería, Benidorm, Gran Canaria, Costa del Sol, Salou, Costa de la Luz, Canarias y Mallorca, con hoteles reales y precios de referencia.",
    "content": CONTENT,
    "image_url": "https://images.unsplash.com/photo-1583681287496-7ba7acacc1a4?fm=jpg&q=80&w=1200&auto=format&fit=crop",
    "category": "consejos",
}

if __name__ == "__main__":
    conn = database.get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE posts SET title=%s, excerpt=%s, content=%s, image_url=%s, category=%s WHERE slug=%s RETURNING id",
        (post["title"], post["excerpt"], post["content"], post["image_url"], post["category"], post["slug"]),
    )
    row = cur.fetchone()
    conn.commit()
    conn.close()
    print("post_id actualizado:", row[0] if row else "NO ENCONTRADO (¿slug distinto?)")
