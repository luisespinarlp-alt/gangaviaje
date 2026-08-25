import os

import psycopg2
import psycopg2.extras

import config

DATABASE_URL = config.DATABASE_URL


def get_conn():
    conn = psycopg2.connect(DATABASE_URL)
    return conn


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS deals (
            id                  SERIAL PRIMARY KEY,
            title               TEXT    NOT NULL,
            description         TEXT    DEFAULT '',
            location            TEXT    DEFAULT '',
            original_price      REAL,
            sale_price          REAL    NOT NULL,
            discount_pct        INTEGER DEFAULT 0,
            image_url           TEXT    DEFAULT '',
            affiliate_url       TEXT    NOT NULL,
            source              TEXT    NOT NULL DEFAULT 'booking',
            category            TEXT    DEFAULT 'espana',
            rating              REAL    DEFAULT 0,
            reviews_count       INTEGER DEFAULT 0,
            tipo                TEXT    DEFAULT 'hotel',
            checkin             TEXT,
            checkout            TEXT,
            created_at          TIMESTAMP DEFAULT NOW(),
            published_telegram  INTEGER DEFAULT 0,
            active              INTEGER DEFAULT 1
        )
    """)
    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_deals_active
        ON deals (active, created_at DESC)
    """)
    cur.execute("ALTER TABLE deals ADD COLUMN IF NOT EXISTS views INTEGER DEFAULT 0")
    cur.execute("ALTER TABLE deals ADD COLUMN IF NOT EXISTS published_pinterest INTEGER DEFAULT 0")
    cur.execute("ALTER TABLE deals ADD COLUMN IF NOT EXISTS telegram_published_at TIMESTAMPTZ")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS price_alerts (
            id            SERIAL PRIMARY KEY,
            email         TEXT    NOT NULL,
            origin        TEXT    NOT NULL,
            destination   TEXT    NOT NULL,
            route_label   TEXT    NOT NULL,
            base_price    REAL    NOT NULL,
            deal_id       INTEGER,
            created_at    TIMESTAMP DEFAULT NOW(),
            notified_at   TIMESTAMP,
            active        INTEGER DEFAULT 1
        )
    """)
    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_price_alerts_active
        ON price_alerts (active, origin, destination)
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id          SERIAL PRIMARY KEY,
            slug        TEXT    NOT NULL UNIQUE,
            title       TEXT    NOT NULL,
            excerpt     TEXT    DEFAULT '',
            content     TEXT    NOT NULL,
            image_url   TEXT    DEFAULT '',
            category    TEXT    DEFAULT 'espana',
            created_at  TIMESTAMP DEFAULT NOW()
        )
    """)
    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_posts_created
        ON posts (created_at DESC)
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS guide_requests (
            id                  SERIAL PRIMARY KEY,
            name                TEXT    DEFAULT '',
            email               TEXT    NOT NULL,
            destination         TEXT    DEFAULT '',
            date_start          DATE,
            date_end            DATE,
            has_reservation     INTEGER DEFAULT 0,
            reservation_text    TEXT    DEFAULT '',
            source_filename     TEXT    DEFAULT '',
            status              TEXT    DEFAULT 'pendiente',
            created_at          TIMESTAMP DEFAULT NOW(),
            fulfilled_at        TIMESTAMP
        )
    """)
    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_guide_requests_status
        ON guide_requests (status, created_at DESC)
    """)
    cur.execute("ALTER TABLE guide_requests ADD COLUMN IF NOT EXISTS rating INTEGER")
    cur.execute("ALTER TABLE guide_requests ADD COLUMN IF NOT EXISTS rating_comment TEXT DEFAULT ''")
    cur.execute("ALTER TABLE guide_requests ADD COLUMN IF NOT EXISTS rated_at TIMESTAMP")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS magazine_issues (
            id                SERIAL PRIMARY KEY,
            slug              TEXT    NOT NULL UNIQUE,
            issue_label       TEXT    NOT NULL,
            headline          TEXT    NOT NULL,
            subheadline       TEXT    DEFAULT '',
            cover_image_url   TEXT    NOT NULL,
            intro             TEXT    DEFAULT '',
            sections          JSONB   NOT NULL DEFAULT '[]',
            published_at      TIMESTAMP DEFAULT NOW()
        )
    """)
    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_magazine_issues_published
        ON magazine_issues (published_at DESC)
    """)
    conn.commit()
    cur.close()
    conn.close()


def add_deal(deal: dict) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO deals
            (title, description, location, original_price, sale_price, discount_pct,
             image_url, affiliate_url, source, category, tipo, rating, reviews_count, checkin, checkout)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (
        deal["title"], deal.get("description", ""), deal.get("location", ""),
        deal.get("original_price"), deal["sale_price"], deal.get("discount_pct", 0),
        deal.get("image_url", ""), deal["affiliate_url"], deal.get("source", "booking"),
        deal.get("category", "espana"), deal.get("tipo", "hotel"),
        deal.get("rating", 0), deal.get("reviews_count", 0),
        deal.get("checkin"), deal.get("checkout"),
    ))
    deal_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return deal_id


def deal_exists(affiliate_url: str) -> bool:
    """True si ya existe un deal con esta URL (activo o no) — evita duplicados."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM deals WHERE affiliate_url = %s LIMIT 1", (affiliate_url,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row is not None


def refresh_deal(affiliate_url: str, deal: dict):
    """Actualiza precio e imagen de un deal existente y lo reactiva."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE deals SET
            sale_price     = %s,
            original_price = %s,
            discount_pct   = %s,
            image_url      = %s,
            rating         = %s,
            reviews_count  = %s,
            active         = 1,
            created_at     = NOW()
        WHERE affiliate_url = %s
    """, (
        deal["sale_price"], deal.get("original_price"),
        deal.get("discount_pct", 0), deal.get("image_url", ""),
        deal.get("rating", 0), deal.get("reviews_count", 0),
        affiliate_url,
    ))
    conn.commit()
    cur.close()
    conn.close()


def search(query: str, limit_deals: int = 18, limit_posts: int = 6) -> dict:
    """Busca en deals y posts por título, location y excerpt."""
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    q = f"%{query}%"

    cur.execute("""
        SELECT * FROM deals
        WHERE active = 1 AND (
            title ILIKE %s OR location ILIKE %s OR description ILIKE %s
        )
        ORDER BY discount_pct DESC, created_at DESC
        LIMIT %s
    """, (q, q, q, limit_deals))
    deals = [dict(r) for r in cur.fetchall()]

    cur.execute("""
        SELECT slug, title, category, excerpt, image_url FROM posts
        WHERE title ILIKE %s OR excerpt ILIKE %s OR content ILIKE %s
        ORDER BY created_at DESC
        LIMIT %s
    """, (q, q, q, limit_posts))
    posts = [dict(r) for r in cur.fetchall()]

    cur.close()
    conn.close()
    return {"deals": deals, "posts": posts}


def get_deals(category: str = None, location: str = None, tipo: str = None, limit: int = 60) -> list:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    conditions = ["active = 1"]
    params: list = []
    if category:
        conditions.append("category = %s")
        params.append(category)
    if location:
        conditions.append("location ILIKE %s")
        params.append(f"%{location}%")
    if tipo:
        conditions.append("tipo = %s")
        params.append(tipo)
    query = ("SELECT * FROM deals WHERE " + " AND ".join(conditions)
             + " ORDER BY discount_pct DESC, created_at DESC LIMIT %s")
    params.append(limit)
    cur.execute(query, params)
    rows = [dict(r) for r in cur.fetchall()]
    cur.close()
    conn.close()
    return rows


def get_deals_grouped(category: str = None, per_tipo_limit: int = 40) -> list:
    """Devuelve [(tipo, [deals...]), ...] en una sola query con ROW_NUMBER."""
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cat_filter = "AND category = %s" if category else ""
    params = [per_tipo_limit]
    if category:
        params = [category, per_tipo_limit]

    cur.execute(f"""
        SELECT * FROM (
            SELECT *, ROW_NUMBER() OVER (
                PARTITION BY tipo ORDER BY discount_pct DESC, created_at DESC
            ) AS rn
            FROM deals
            WHERE active = 1 {cat_filter}
        ) sub
        WHERE rn <= %s
        ORDER BY tipo, discount_pct DESC
    """, params)

    rows_by_tipo: dict = {}
    for row in cur.fetchall():
        t = row["tipo"]
        if t not in rows_by_tipo:
            rows_by_tipo[t] = []
        rows_by_tipo[t].append(dict(row))

    cur.close()
    conn.close()

    # Mantener el orden de config.TIPO_ORDER
    grouped = []
    for tipo in config.TIPO_ORDER:
        if tipo in rows_by_tipo:
            grouped.append((tipo, rows_by_tipo[tipo]))
    return grouped


def increment_views(deal_id: int) -> None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE deals SET views = views + 1 WHERE id = %s", (deal_id,))
    conn.commit()
    cur.close()
    conn.close()


def add_price_alert(email: str, origin: str, destination: str, route_label: str, base_price: float, deal_id: int | None) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO price_alerts (email, origin, destination, route_label, base_price, deal_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (email, origin, destination, route_label, base_price, deal_id))
    alert_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return alert_id


def get_active_price_alerts() -> list:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM price_alerts WHERE active = 1")
    rows = [dict(r) for r in cur.fetchall()]
    cur.close()
    conn.close()
    return rows


def mark_alert_notified(alert_id: int) -> None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE price_alerts SET notified_at = NOW(), active = 0 WHERE id = %s", (alert_id,))
    conn.commit()
    cur.close()
    conn.close()


def get_deal(deal_id: int) -> dict | None:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM deals WHERE id = %s", (deal_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return dict(row) if row else None


def get_deals_grouped_by_location(location: str, per_tipo_limit: int = 20) -> list:
    """Devuelve [(tipo, [deals...]), ...] filtrado por location (búsqueda parcial)."""
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    grouped = []
    for tipo in config.TIPO_ORDER:
        cur.execute(
            "SELECT * FROM deals WHERE active = 1 AND tipo = %s AND location ILIKE %s "
            "ORDER BY discount_pct DESC, created_at DESC LIMIT %s",
            (tipo, f"%{location}%", per_tipo_limit)
        )
        rows = [dict(r) for r in cur.fetchall()]
        if rows:
            grouped.append((tipo, rows))
    cur.close()
    conn.close()
    return grouped


def get_top_deals(limit: int = 3) -> list:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(
        "SELECT * FROM deals WHERE active = 1 AND discount_pct >= 30 "
        "ORDER BY discount_pct DESC LIMIT %s", (limit,)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(r) for r in rows]


def get_unpublished_deals() -> list:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(
        "SELECT * FROM deals WHERE published_telegram = 0 AND active = 1 "
        "ORDER BY discount_pct DESC"
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(r) for r in rows]


def mark_published_telegram(deal_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE deals SET published_telegram = 1, telegram_published_at = NOW() WHERE id = %s", (deal_id,))
    conn.commit()
    cur.close()
    conn.close()


def requeue_stale_telegram_deals(min_days: int = 7, batch: int = 5) -> int:
    """
    Reintroduce en la cola de Telegram un lote rotatorio de ofertas de catálogo
    fijo (todo menos TravelPayouts, que ya genera contenido nuevo por sí solo).
    Sin esto, una oferta de hotel/actividad/coche se publica una única vez en
    toda su vida y el canal acaba siendo solo vuelos. Prioriza las que llevan
    más tiempo sin volver a publicarse.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE deals SET published_telegram = 0
        WHERE id IN (
            SELECT id FROM deals
            WHERE active = 1 AND source != 'travelpayouts' AND published_telegram = 1
              AND (telegram_published_at IS NULL OR telegram_published_at < NOW() - (%s || ' days')::interval)
            ORDER BY telegram_published_at ASC NULLS FIRST
            LIMIT %s
        )
    """, (min_days, batch))
    n = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return n


def get_unpublished_deals_pinterest() -> list:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(
        "SELECT * FROM deals WHERE published_pinterest = 0 AND active = 1 "
        "ORDER BY discount_pct DESC"
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(r) for r in rows]


def get_guide_slug(location: str) -> str | None:
    """Busca una guía de blog para una ciudad/ubicación de deal. La mayoría de
    títulos empiezan por el nombre de la ciudad ("Roma: qué ver...", "París en
    3 días...") así que basta con el prefijo, sin exigir ":" justo después."""
    if not location:
        return None
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT slug FROM posts WHERE title ILIKE %s ORDER BY LENGTH(title) ASC LIMIT 1",
        (f"{location}%",)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row[0] if row else None


def mark_published_pinterest(deal_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE deals SET published_pinterest = 1 WHERE id = %s", (deal_id,))
    conn.commit()
    cur.close()
    conn.close()


def deactivate_old_deals(hours: int = 48):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE deals SET active = 0 WHERE created_at < NOW() - (%s || ' hours')::interval AND active = 1",
        (hours,),
    )
    conn.commit()
    cur.close()
    conn.close()


def get_stats() -> dict:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM deals WHERE active = 1")
    total = cur.fetchone()[0]
    cur.execute(
        "SELECT COUNT(*) FROM deals WHERE active = 1 AND created_at::date = CURRENT_DATE"
    )
    today = cur.fetchone()[0]
    cur.execute(
        "SELECT COALESCE(ROUND(AVG(discount_pct)), 30) FROM deals WHERE active = 1 AND discount_pct > 0"
    )
    avg_discount = int(cur.fetchone()[0] or 30)
    cur.execute("SELECT COUNT(*) FROM posts")
    post_count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return {"total": total, "today": today, "avg_discount": avg_discount, "post_count": post_count}


def add_post(post: dict) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO posts (slug, title, excerpt, content, image_url, category)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (slug) DO NOTHING
        RETURNING id
    """, (
        post["slug"], post["title"], post.get("excerpt", ""),
        post["content"], post.get("image_url", ""), post.get("category", "espana"),
    ))
    row = cur.fetchone()
    post_id = row[0] if row else None
    conn.commit()
    cur.close()
    conn.close()
    return post_id


def get_posts(limit: int = 30, category: str = None, exclude_category: str | list = None) -> list:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    conditions, params = [], []
    if category:
        conditions.append("category = %s")
        params.append(category)
    if exclude_category:
        if isinstance(exclude_category, (list, tuple)):
            conditions.append("category NOT IN %s")
            params.append(tuple(exclude_category))
        else:
            conditions.append("category != %s")
            params.append(exclude_category)
    where = ("WHERE " + " AND ".join(conditions)) if conditions else ""
    params.append(limit)
    cur.execute(f"SELECT * FROM posts {where} ORDER BY created_at DESC LIMIT %s", params)
    rows = [dict(r) for r in cur.fetchall()]
    cur.close()
    conn.close()
    return rows


def get_post_by_slug(slug: str) -> dict | None:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM posts WHERE slug = %s", (slug,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return dict(row) if row else None


def add_magazine_issue(issue: dict) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO magazine_issues (slug, issue_label, headline, subheadline, cover_image_url, intro, sections)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (slug) DO UPDATE SET
            issue_label = EXCLUDED.issue_label,
            headline = EXCLUDED.headline,
            subheadline = EXCLUDED.subheadline,
            cover_image_url = EXCLUDED.cover_image_url,
            intro = EXCLUDED.intro,
            sections = EXCLUDED.sections
        RETURNING id
    """, (
        issue["slug"], issue["issue_label"], issue["headline"],
        issue.get("subheadline", ""), issue["cover_image_url"], issue.get("intro", ""),
        psycopg2.extras.Json(issue["sections"]),
    ))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return row[0] if row else None


def get_magazine_issues(limit: int = 24) -> list:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM magazine_issues ORDER BY published_at DESC LIMIT %s", (limit,))
    rows = [dict(r) for r in cur.fetchall()]
    cur.close()
    conn.close()
    return rows


def get_magazine_issue_by_slug(slug: str) -> dict | None:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM magazine_issues WHERE slug = %s", (slug,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return dict(row) if row else None


def add_guide_request(name: str, email: str, destination: str, date_start: str, date_end: str,
                       reservation_text: str = "", source_filename: str = "") -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO guide_requests
            (name, email, destination, date_start, date_end, has_reservation, reservation_text, source_filename)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (name, email, destination, date_start or None, date_end or None,
          1 if reservation_text else 0, reservation_text, source_filename))
    request_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return request_id


def get_guide_requests(status: str = None, limit: int = 100) -> list:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    if status:
        cur.execute("SELECT * FROM guide_requests WHERE status = %s ORDER BY created_at DESC LIMIT %s", (status, limit))
    else:
        cur.execute("SELECT * FROM guide_requests ORDER BY created_at DESC LIMIT %s", (limit,))
    rows = [dict(r) for r in cur.fetchall()]
    cur.close()
    conn.close()
    return rows


def cleanup_old_reservation_texts(days: int = 30) -> int:
    """Borra el texto de la reserva (datos potencialmente sensibles) pasados N días,
    conservando el resto de la solicitud (destino, fechas, estado) para estadísticas."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE guide_requests
        SET reservation_text = '', source_filename = ''
        WHERE reservation_text != ''
          AND created_at < NOW() - (%s || ' days')::INTERVAL
    """, (days,))
    deleted = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return deleted


def set_guide_request_status(request_id: int, status: str):
    conn = get_conn()
    cur = conn.cursor()
    if status == "enviada":
        cur.execute("UPDATE guide_requests SET status = %s, fulfilled_at = NOW() WHERE id = %s", (status, request_id))
    else:
        cur.execute("UPDATE guide_requests SET status = %s, fulfilled_at = NULL WHERE id = %s", (status, request_id))
    conn.commit()
    cur.close()
    conn.close()


def get_guide_request(request_id: int) -> dict | None:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM guide_requests WHERE id = %s", (request_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return dict(row) if row else None


def set_guide_request_rating(request_id: int, rating: int, comment: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE guide_requests SET rating = %s, rating_comment = %s, rated_at = NOW() WHERE id = %s",
        (rating, comment, request_id),
    )
    conn.commit()
    cur.close()
    conn.close()


def get_guide_testimonials(min_rating: int = 4, limit: int = 12) -> list:
    """Valoraciones reales con comentario, para mostrar como testimonios en la landing."""
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(
        """
        SELECT name, destination, rating, rating_comment, rated_at
        FROM guide_requests
        WHERE rating >= %s AND rating_comment != ''
        ORDER BY rated_at DESC
        LIMIT %s
        """,
        (min_rating, limit),
    )
    rows = [dict(r) for r in cur.fetchall()]
    cur.close()
    conn.close()
    return rows
