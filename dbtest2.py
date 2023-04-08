
import psycopg2

conn = psycopg2.connect(
    dbname="db_name",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()





cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS wares (
    id SERIAL PRIMARY KEY,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS available (
    id SERIAL PRIMARY KEY,
    wareid INTEGER REFERENCES wares (id),
    productid INTEGER REFERENCES products (id)
);

CREATE TABLE IF NOT EXISTS partners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    inn VARCHAR(12) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    partnerid INTEGER REFERENCES partners (id),
    fromware INTEGER REFERENCES wares (id),
    orderdate DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS orderproducts (
    id SERIAL PRIMARY KEY,
    orderid INTEGER REFERENCES orders (id),
    productid INTEGER REFERENCES products (id)
);
""")
```


class Products:
    @staticmethod
    def add(name):
        cur.execute("INSERT INTO products (name) VALUES (%s) RETURNING id", (name,))
        conn.commit()


    @staticmethod
    def read(id=None):
        if id is not None:
            cur.execute("SELECT * FROM products WHERE id = %s", (id,))
            return cur.fetchone()
        else:
            cur.execute("SELECT * FROM products")
            return cur.fetchall()

    @staticmethod
    def update(id, name):
        cur.execute("UPDATE products SET name = %s WHERE id = %s", (name, id))
        conn.commit()

    @staticmethod
    def delete(id):
        cur.execute("DELETE FROM products WHERE id = %s", (id,))
        conn.commit()

class MyQueries:
    @staticmethod
    def getwareproducts(wareid):
        cur.execute("""
        SELECT products.id, products.name
        FROM available
        INNER JOIN products ON available.productid=products.id
        WHERE available.wareid = %s
        """, (wareid,))
        return cur.fetchall()

    @staticmethod
    def getorderproducts(orderid):
        cur.execute("""
        SELECT orders.id, orders.orderdate, partners.name, wares.address, products.name
        FROM orderproducts
        INNER JOIN orders ON orderproducts.orderid=orders.id
        INNER JOIN partners ON orders.partnerid=partners.id
        INNER JOIN wares ON orders.fromware=wares.id
        INNER JOIN products ON orderproducts.productid=products.id
        WHERE orders.id = %s
        """, (orderid,))
        return cur.fetchall()

    @staticmethod
    def getpartnerorders(partnerid):
        cur.execute("""
        SELECT orders.id, orders.orderdate, wares.address, arrayagg(products.name)
        FROM orders
        INNER JOIN orderproducts ON orders.id=orderproducts.orderid
        INNER JOIN wares ON orders.from
        ware=wares.id
        INNER JOIN products ON order_products.product_id=products.id
        WHERE orders.partner_id = %s
        GROUP BY orders.id, orders.order_date, wares.address
        """, (partner_id,))
        return cur.fetchall()


Products.add("New Product")


print(Products.read())
