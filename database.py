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


def get_deals(category: str = None, limit: int = 60) -> list:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    conditions = ["active = 1"]
    params: list = []
    if category:
        conditions.append("category = %s")
        params.append(category)
    query = ("SELECT * FROM deals WHERE " + " AND ".join(conditions)
             + " ORDER BY discount_pct DESC, created_at DESC LIMIT %s")
    params.append(limit)
    cur.execute(query, params)
    rows = [dict(r) for r in cur.fetchall()]
    cur.close()
    conn.close()
    return rows


def get_deals_grouped(category: str = None, per_tipo_limit: int = 40) -> list:
    """Devuelve [(tipo, [deals...]), ...] en el orden de config.TIPO_ORDER,
    con un cupo propio por tipo para que ningún tipo (p.ej. vuelos) desplace a los demás."""
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    grouped = []
    for tipo in config.TIPO_ORDER:
        conditions = ["active = 1", "tipo = %s"]
        params: list = [tipo]
        if category:
            conditions.append("category = %s")
            params.append(category)
        query = ("SELECT * FROM deals WHERE " + " AND ".join(conditions)
                 + " ORDER BY discount_pct DESC, created_at DESC LIMIT %s")
        params.append(per_tipo_limit)
        cur.execute(query, params)
        rows = [dict(r) for r in cur.fetchall()]
        if rows:
            grouped.append((tipo, rows))
    cur.close()
    conn.close()
    return grouped


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
    cur.execute("UPDATE deals SET published_telegram = 1 WHERE id = %s", (deal_id,))
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
    cur.close()
    conn.close()
    return {"total": total, "today": today}


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


def get_posts(limit: int = 30) -> list:
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM posts ORDER BY created_at DESC LIMIT %s", (limit,))
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
