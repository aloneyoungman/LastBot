import psycopg2
from datetime import datetime, date, time,timedelta
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password = "8991",
    host="127.0.0.1"
)

cur = conn.cursor()

# Лучше, если ты будешь проверять существует ли такая таблица
# и создавать таблицу только если её ещё не существует
# Например вот https://stackoverflow.com/questions/1874113/checking-if-a-postgresql-table-exists-under-python-and-probably-psycopg2

# Также предлагаю тебе использовать автокоммит, чтобы не писать после каждой операции commit
# Хотя то, как ты сделал - правильно и в реальном проекте часто используется такой подход

# Методы согласно PEP-8 называются с большой буквы - пожалуйста поправь это

cur.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255)
    )
     """)

cur.execute("""
    CREATE TABLE IF NOT EXISTS Wares (
        id SERIAL PRIMARY KEY,
        adress VARCHAR(255)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Available (
        id SERIAL PRIMARY KEY,
        ware_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY (ware_id) REFERENCES Wares(id) ON DELETE CASCADE,
        FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Partners (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        inn VARCHAR(12)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        id SERIAL PRIMARY KEY,
        partner_id INTEGER,
        from_ware INTEGER,
        order_date DATE,
        FOREIGN KEY (partner_id) REFERENCES Partners(id) ON DELETE CASCADE,
        FOREIGN KEY (from_ware) REFERENCES Wares(id) ON DELETE CASCADE
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Order_products (
        id SERIAL PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY (order_id) REFERENCES Orders(id) ON DELETE CASCADE,
        FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE
    )
""")

conn.commit()

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

class Wares:
    @staticmethod
    def add(adress):
        cur.execute("INSERT INTO Wares (adress) VALUES (%s)", (adress,))
        conn.commit()

    @staticmethod
    def read(id=None):
        if id is None:
            cur.execute("SELECT * FROM Wares")
        elif  isinstance(id,int):
            cur.execute("SELECT * FROM Wares WHERE id=%s", (id,))
        elif isinstance(id,list):
            cur.execute("SELECT * FROM Wares WHERE id IN %s", (tuple(id),))
        return cur.fetchall()

    @staticmethod
    def update(id, adress):
        cur.execute("UPDATE Wares SET adress=%s WHERE id=%s", (adress, id))
        conn.commit()

    @staticmethod
    def delete(id):
        cur.execute("DELETE FROM Wares WHERE id=%s", (id,))
        conn.commit()

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

    @staticmethod
    def update(id, name, inn):
        cur.execute("UPDATE Partners SET name=%s, inn=%s WHERE id=%s", (name, inn, id))
        conn.commit()

    @staticmethod
    def delete(id):
        cur.execute("DELETE FROM Partners WHERE id=%s", (id,))
        conn.commit()

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

    @staticmethod
    def update(id, partner_id, from_ware, order_date):
        cur.execute("UPDATE Orders SET partner_id = %s, from_ware = %s, order_date = %s WHERE id = %s", (partner_id, from_ware,order_date, id))
        conn.commit()

    @staticmethod
    def delete(id):
        cur.execute("DELETE FROM Orders WHERE id=%s", (id,))
        conn.commit()

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

    @staticmethod
    def update(id, order_id, product_id):
        cur.execute("UPDATE Order_products SET order_id = %s, product_id = %s WHERE id = %s", (order_id, product_id, id))
        conn.commit()

    @staticmethod
    def delete(id):
        cur.execute("DELETE FROM Order_products WHERE id=%s", (id,))
        conn.commit()



id_list = [13,14]

# вариант 1
cur.execute("SELECT * FROM Products WHERE id IN %s ", (tuple(id_list) ,) )
products = cur.fetchall()
print(products)

# вариант 2 
cur.execute("SELECT * FROM Products WHERE id = ANY(%s) ", ([id_list] ,) )
products = cur.fetchall()
print(products)

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
        SELECT orders.id, orders.order_date, wares.adress, 
        FROM orders
        INNER JOIN Order_products ON orders.id=Order_products.order_id
        INNER JOIN wares ON orders.from_ware=wares.id
        INNER JOIN products ON Order_products.product_id=products.id
        WHERE orders.partner_id = %s
        GROUP BY orders.id, orders.order_date, wares.adress
        """, (partner_id,))
        return cur.fetchall()


def Clear_Db():
    Products.add("Апельсин")
    tables = [Available, Order_products, Orders, Products ,Partners, Wares]
    for table in tables:
        data = table.read()
        if data is not None and len(data)>0:
            items_ids = map(lambda item:item[0],data)
            for item_id in items_ids:
                table.delete(item_id)

def Get_All_Ids(table):
    return list(map(lambda row:row[0], table.read()))

# Если данная функция отработала и вывела все необходимые данные - значит весь код работает правильно
# В ней мы удаляем все существующие в таблице данные
# Затем заново добавляем несколько тестовых объектов
# И пытаемся выполнить разные функции
def test_func():
    Clear_Db()

    Products.add('bad_Апельсин')
    Products.add('Яблоко')
    Products.add('Банан')
    Wares.add('bad_СПБ')
    Wares.add('МСК')

    product_Ids = Get_All_Ids(Products)
    Products.update(product_Ids[0], 'Апельсин')
    wares_Ids = Get_All_Ids(Wares)
    Wares.update(wares_Ids[0], 'СПБ')

    Available.add(wares_Ids[0],product_Ids[0])
    Available.add(wares_Ids[0],product_Ids[2])

    Available.add(wares_Ids[1],product_Ids[1])
    Available.add(wares_Ids[1],product_Ids[0])
    availables_ids = Get_All_Ids(Available)
    Available.update(availables_ids[0], wares_Ids[0],product_Ids[0])

    print('products', Products.read())
    print('wares',Wares.read())
    print('available', Available.read())
    print(MyQueries.GetWareProducts(wares_Ids[0]))

    Partners.add('bad_Apple',111111)
    Partners.add('Uber',222222)
    partners_ids = Get_All_Ids(Partners)
    Partners.update(partners_ids[0],'Apple', 111111 )

    Orders.add(partners_ids[0],wares_Ids[0], datetime.now() + timedelta(days=2) )
    Orders.add(partners_ids[0],wares_Ids[1], datetime.now() + timedelta(days=-5))
    orders_ids = Get_All_Ids(Orders)
    Orders.update(orders_ids[0],partners_ids[0],wares_Ids[0], datetime.now() + timedelta(days=15))

    Order_products.add(orders_ids[0],product_Ids[0])
    Order_products.add(orders_ids[0],product_Ids[1])
    Order_products.add(orders_ids[1],product_Ids[2])
    Order_products.add(orders_ids[1],product_Ids[1])
    order_products_ids = Get_All_Ids(Order_products)
    Order_products.update(order_products_ids[0],)

    print('partners',Partners.read())
    print('orders',Orders.read())
    print('orders_products',Order_products.read(), orders_ids[0],product_Ids[0])

    print('order_product_by_id', MyQueries.GetOrderProducts(orders_ids[0]))
    print('orders_by_parnter_id', MyQueries.GetPartnerQrders(partners_ids[0]))



test_func()

# Всё ещё не нашёл нигде отрисованной схемы БД
#
# Рекомендую тебе разбить данный файл на отдельные питон файлы по классам.
# Так будет гораздо удобнее работать, а не читать большой файл
#
# Если начать работать с данными методами - будет гораздо удобнее, если метод Add() - будет возвращать id созданного элемента
# Тогда не надо будет создавать отдельный метод, как создал я
#
