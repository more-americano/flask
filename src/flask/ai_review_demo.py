"""演示用模块：故意留下 SQL 拼接缺陷，用于验证审查/修复流水线。"""

import sqlite3

def find_user_by_name(conn: sqlite3.Connection, name: str) -> list[tuple]:
    return conn.execute("SELECT id, name FROM users WHERE name = ?", (name,)).fetchall()
