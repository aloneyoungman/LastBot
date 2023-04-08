import psycopg2
from datetime import datetime, date, time,timedelta
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password = "8991",
    host="127.0.0.1"
)

cur = conn.cursor()
class Order_products:
    @staticmethod
    def add(order_id, product_id):
        cur.execute("INSERT INTO Order_products (order_id, product_id) VALUES (%s, %s)", (order_id, product_id))
        conn.commit()

    @staticmethod
    def read(id=None):
        if id is None:
            cur.execute("SELECT * FROM Order_products")
        elif isinstance(id, int):
            cur.execute("SELECT * FROM Order_products WHERE id=%s", (id,))
        elif isinstance(id, list):
            cur.execute("SELECT * FROM Order_products WHERE id IN %s", (tuple(id),))
        return cur.fetchall()
    @staticmethod
    def update(id, order_id, product_id):
        cur.execute("UPDATE Order_products SET order_id = %s, product_id = %s WHERE id = %s", (order_id, product_id, id))
        conn.commit()

    @staticmethod
    def delete(id):
        cur.execute("DELETE FROM Order_products WHERE id=%s", (id,))
        conn.commit()