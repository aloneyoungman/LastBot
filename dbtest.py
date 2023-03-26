import psycopg2

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
    CREATE TABLE Products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255)
    )
     """)

cur.execute("""
    CREATE TABLE Wares (
        id SERIAL PRIMARY KEY,
        adress VARCHAR(255)
    )
""")

cur.execute("""
    CREATE TABLE Available (
        id SERIAL PRIMARY KEY,
        ware_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY (ware_id) REFERENCES Wares(id),
        FOREIGN KEY (product_id) REFERENCES Products(id)
    )
""")

cur.execute("""
    CREATE TABLE Partners (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        inn VARCHAR(12)
    )
""")

cur.execute("""
    CREATE TABLE Orders (
        id SERIAL PRIMARY KEY,
        partner_id INTEGER,
        from_ware INTEGER,
        order_date DATE,
        FOREIGN KEY (partner_id) REFERENCES Partners(id),
        FOREIGN KEY (from_ware) REFERENCES Wares(id)
    )
""")

cur.execute("""
    CREATE TABLE Order_products (
        id SERIAL PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY (order_id) REFERENCES Orders(id),
        FOREIGN KEY (product_id) REFERENCES Products(id)
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
        else:
            cur.execute("SELECT * FROM Products WHERE id=%s", (id,))
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
        else:
            cur.execute("SELECT * FROM Wares WHERE id=%s", (id,))
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
        else:
            cur.execute("SELECT * FROM Available WHERE id=%s", (id,))
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
        else:
            cur.execute("SELECT * FROM Partners WHERE id=%s", (id,))
        return cur.fetchall()

    @staticmethod
    def update(id, ware_id, product_id):
        cur.execute("UPDATE Partners SET ware_id=%s, product_id=%s WHERE id=%s", (ware_id, product_id, id))
        conn.commit()

    @staticmethod
    def delete(id):
        cur.execute("DELETE FROM Partners WHERE id=%s", (id,))
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