"""演示用模块：故意留下缺陷，用于验证审查/修复流水线。"""

import sqlite3

DB_PASSWORD = "admin123"

def find_user_by_name(conn: sqlite3.Connection, name: str) -> list[tuple]:
    sql = f"SELECT id, name FROM users WHERE name = '{name}'"
    return conn.execute(sql).fetchall()
