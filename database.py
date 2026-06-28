import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('mediquery.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_query(question, answer):
    conn = sqlite3.connect('mediquery.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO queries (question, answer, timestamp)
        VALUES (?, ?, ?)
    ''', (question, answer, datetime.now().strftime("%d-%m-%Y %H:%M")))
    conn.commit()
    conn.close()

def get_all_queries():
    conn = sqlite3.connect('mediquery.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM queries ORDER BY id DESC')
    queries = cursor.fetchall()
    conn.close()
    return queries
def get_recent_queries(limit=5):
    conn = sqlite3.connect('mediquery.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM queries ORDER BY id DESC LIMIT ?', (limit,))
    queries = cursor.fetchall()
    conn.close()
    return queries