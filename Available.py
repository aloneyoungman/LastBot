import psycopg2
from datetime import datetime, date, time,timedelta
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password = "8991",
    host="127.0.0.1"
)

cur = conn.cursor()
class Available:
    @staticmethod
    def add(ware_id, product_id):
        cur.execute("INSERT INTO Available (ware_id, product_id) VALUES (%s, %s)", (ware_id, product_id))
        conn.commit()

    @staticmethod
    def read(id=None):
        if id is None:
            cur.execute("SELECT * FROM Available")
        elif isinstance(id, int):
            cur.execute("SELECT * FROM Available WHERE id=%s", (id,))
        elif isinstance(id, list):
            cur.execute("SELECT * FROM Available WHERE id IN %s", (tuple(id),))
        return cur.fetchall()

    @staticmethod
    def update(id, ware_id, product_id):
        cur.execute("UPDATE Available SET ware_id=%s, product_id=%s WHERE id=%s", (ware_id, product_id, id))
        conn.commit()

    @staticmethod
    def delete(id):
        cur.execute("DELETE FROM Available WHERE id=%s", (id,))
        conn.commit()