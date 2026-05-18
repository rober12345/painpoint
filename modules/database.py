import sqlite3
import os

DB_PATH = "database/pain_point.db"

# =========================================================
# CREATE DATABASE CONNECTION
# =========================================================

def get_connection():

    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    return conn

# =========================================================
# CREATE TABLE
# =========================================================

def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS submissions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT,
        name TEXT,
        plant TEXT,
        area TEXT,
        process TEXT,
        pain_point TEXT,
        suggested_improvement TEXT,
        safety_risk TEXT,
        photo_path TEXT
    )
    """)

    conn.commit()
    conn.close()