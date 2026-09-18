import sqlite3


DB_NAME = "database/scores.db"


def connect():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            score INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def add_user(user_id, name):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users (user_id, name, score)
        VALUES (?, ?, 0)
    """, (str(user_id), name))

    conn.commit()
    conn.close()


def add_score(user_id, name, amount):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (user_id, name, score)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id)
        DO UPDATE SET
            name = excluded.name,
            score = score + excluded.score
    """, (str(user_id), name, amount))

    conn.commit()
    conn.close()


def get_score(user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT score FROM users WHERE user_id = ?",
        (str(user_id),)
    )

    result = cursor.fetchone()

    conn.close()

    return result[0] if result else 0


def get_top_users(limit=10):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_id, name, score
        FROM users
        ORDER BY score DESC
        LIMIT ?
    """, (limit,))

    result = cursor.fetchall()

    conn.close()

    return result


def get_user_rank(user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*) + 1
        FROM users
        WHERE score > (
            SELECT score
            FROM users
            WHERE user_id = ?
        )
    """, (str(user_id),))

    result = cursor.fetchone()

    conn.close()

    return result[0] if result else None


init_db()
