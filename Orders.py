import psycopg2
from datetime import datetime, date, time,timedelta
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password = "8991",
    host="127.0.0.1"
)

cur = conn.cursor()
class Orders:
    @staticmethod
    def add(partner_id, ware_id,order_date):
        cur.execute("INSERT INTO Orders (partner_id, from_ware,order_date) VALUES (%s, %s,%s)", (partner_id, ware_id,order_date))
        conn.commit()

    @staticmethod
    def read(id=None):
        if id is None:
            cur.execute("SELECT * FROM Orders")
        elif isinstance(id, int):
            cur.execute("SELECT * FROM Orders WHERE id=%s", (id,))
        elif isinstance(id, list):
            cur.execute("SELECT * FROM Orders WHERE id IN %s", (tuple(id),))
        return cur.fetchall()
    @staticmethod
    def update(id, partner_id, from_ware, order_date):
        cur.execute("UPDATE Orders SET partner_id = %s, from_ware = %s, order_date = %s WHERE id = %s", (partner_id, from_ware,order_date, id))
        conn.commit()

    @staticmethod
    def delete(id):
        cur.execute("DELETE FROM Orders WHERE id=%s", (id,))
        conn.commit()