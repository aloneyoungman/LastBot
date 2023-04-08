import psycopg2
from datetime import datetime, date, time,timedelta
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password = "8991",
    host="127.0.0.1"
)

cur = conn.cursor()
class Partners:
    @staticmethod
    def add(name, inn):
        cur.execute("INSERT INTO Partners (name, inn) VALUES (%s, %s)", (name, inn))
        conn.commit()

    @staticmethod
    def read(id=None):
        if id is None:
            cur.execute("SELECT * FROM Partners")
        elif isinstance(id, int):
            cur.execute("SELECT * FROM Partners WHERE id=%s", (id,))
        elif isinstance(id, list):
            cur.execute("SELECT * FROM Partners WHERE id IN %s", (tuple(id),))
        return cur.fetchall()
    @staticmethod
    def update(id, name, inn):
        cur.execute("UPDATE Partners SET name=%s, inn=%s WHERE id=%s", (name, inn, id))
        conn.commit()

    @staticmethod
    def delete(id):
        cur.execute("DELETE FROM Partners WHERE id=%s", (id,))
        conn.commit()