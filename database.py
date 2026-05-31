import sqlite3
import os
from datetime import datetime

_is_vercel = os.getenv("VERCEL") == "1"
DB_PATH = "/tmp/gangaviaje.db" if _is_vercel else os.path.join(os.path.dirname(os.path.abspath(__file__)), "gangaviaje.db")


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS deals (
            id                INTEGER PRIMARY KEY AUTOINCREMENT,
            title             TEXT    NOT NULL,
            description       TEXT    DEFAULT '',
            location          TEXT    DEFAULT '',
            original_price    REAL,
            sale_price        REAL    NOT NULL,
            discount_pct      INTEGER DEFAULT 0,
            image_url         TEXT    DEFAULT '',
            affiliate_url     TEXT    NOT NULL,
            source            TEXT    NOT NULL DEFAULT 'booking',
            category          TEXT    DEFAULT 'espana',
            rating            REAL    DEFAULT 0,
            reviews_count     INTEGER DEFAULT 0,
            tipo              TEXT    DEFAULT 'hotel',
            checkin           TEXT,
            checkout          TEXT,
            created_at        TEXT    DEFAULT (datetime('now')),
            published_telegram INTEGER DEFAULT 0,
            active            INTEGER DEFAULT 1
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_deals_active
        ON deals (active, created_at DESC)
    """)
    conn.commit()
    conn.close()


def add_deal(deal: dict) -> int:
    conn = get_conn()
    cur = conn.execute("""
        INSERT INTO deals
            (title, description, location, original_price, sale_price, discount_pct,
             image_url, affiliate_url, source, category, tipo, rating, reviews_count, checkin, checkout)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        deal["title"], deal.get("description", ""), deal.get("location", ""),
        deal.get("original_price"), deal["sale_price"], deal.get("discount_pct", 0),
        deal.get("image_url", ""), deal["affiliate_url"], deal.get("source", "booking"),
        deal.get("category", "espana"), deal.get("tipo", "hotel"),
        deal.get("rating", 0), deal.get("reviews_count", 0),
        deal.get("checkin"), deal.get("checkout"),
    ))
    deal_id = cur.lastrowid
    conn.commit()
    conn.close()
    return deal_id


def deal_exists(affiliate_url: str) -> bool:
    conn = get_conn()
    row = conn.execute(
        "SELECT id FROM deals WHERE affiliate_url = ? AND active = 1", (affiliate_url,)
    ).fetchone()
    conn.close()
    return row is not None


def get_deals(category: str = None, limit: int = 60) -> list:
    conn = get_conn()
    conditions = ["active = 1"]
    params: list = []
    if category:
        conditions.append("category = ?")
        params.append(category)
    query = ("SELECT * FROM deals WHERE " + " AND ".join(conditions)
             + " ORDER BY discount_pct DESC, created_at DESC LIMIT ?")
    params.append(limit)
    rows = [dict(r) for r in conn.execute(query, params).fetchall()]
    conn.close()
    return rows


def get_deal(deal_id: int) -> dict | None:
    conn = get_conn()
    row = conn.execute("SELECT * FROM deals WHERE id = ?", (deal_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def get_top_deals(limit: int = 3) -> list:
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM deals WHERE active = 1 AND discount_pct >= 30 "
        "ORDER BY discount_pct DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_unpublished_deals() -> list:
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM deals WHERE published_telegram = 0 AND active = 1 "
        "ORDER BY discount_pct DESC"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def mark_published_telegram(deal_id: int):
    conn = get_conn()
    conn.execute("UPDATE deals SET published_telegram = 1 WHERE id = ?", (deal_id,))
    conn.commit()
    conn.close()


def deactivate_old_deals(hours: int = 48):
    conn = get_conn()
    conn.execute(
        "UPDATE deals SET active = 0 WHERE created_at < datetime('now', ?) AND active = 1",
        (f"-{hours} hours",),
    )
    conn.commit()
    conn.close()


def get_stats() -> dict:
    conn = get_conn()
    total = conn.execute("SELECT COUNT(*) FROM deals WHERE active = 1").fetchone()[0]
    today = conn.execute(
        "SELECT COUNT(*) FROM deals WHERE active = 1 AND date(created_at) = date('now')"
    ).fetchone()[0]
    conn.close()
    return {"total": total, "today": today}
