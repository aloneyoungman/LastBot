import psycopg2
from datetime import datetime, date, time,timedelta
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password = "8991",
    host="127.0.0.1"
)

cur = conn.cursor()
class MyQueries:
    @staticmethod
    def GetWareProducts(ware_id):
        cur.execute("""
        SELECT products.id, products.name
        FROM available
        INNER JOIN products ON available.product_id=products.id
        WHERE available.ware_id = %s
        """, (ware_id,))
        return cur.fetchall()

    @staticmethod
    def GetOrderProducts(order_id):
        cur.execute("""
        SELECT Orders.id, Orders.order_date, Partners.name, wares.adress, Products.name
        FROM Order_products
        INNER JOIN orders ON Order_products.order_id=orders.id
        INNER JOIN partners ON orders.partner_id=Partners.id
        INNER JOIN wares ON orders.from_ware=Wares.id
        INNER JOIN products ON Order_products.product_id=products.id
        WHERE orders.id = %s
        """, (order_id,))
        return cur.fetchall()

    @staticmethod
    def GetPartnerQrders(partner_id):
        cur.execute("""
        SELECT orders.id, orders.order_date, wares.adress 
        FROM orders
        INNER JOIN Order_products ON orders.id=Order_products.order_id
        INNER JOIN wares ON orders.from_ware=wares.id
        INNER JOIN products ON Order_products.product_id=products.id
        WHERE orders.partner_id = %s
        GROUP BY orders.id, orders.order_date, wares.adress
        """, (partner_id,))
        return cur.fetchall()