
import psycopg2
from datetime import datetime, date, time,timedelta
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password = "8991",
    host="127.0.0.1"
)

cur = conn.cursor()
class Products:
    @staticmethod
    def add(name):
        cur.execute("INSERT INTO Products (name) VALUES (%s)", (name,))
        conn.commit()

    @staticmethod
    def read(id=None):
        if id is None:
            cur.execute("SELECT * FROM Products")
        elif isinstance(id, int):
            cur.execute("SELECT * FROM Products WHERE id=%s", (id,))
        elif isinstance(id,list):
            cur.execute("SELECT * FROM Products WHERE id IN %s", (tuple(id),))
        return cur.fetchall()

    @staticmethod
    def update(id, name):
        cur.execute("UPDATE Products SET name=%s WHERE id=%s", (name, id))
        conn.commit()

    @staticmethod
    def delete(id):
        cur.execute("DELETE FROM Products WHERE id=%s", (id,))
        conn.commit()