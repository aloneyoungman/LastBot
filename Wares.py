import psycopg2
from datetime import datetime, date, time,timedelta
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password = "8991",
    host="127.0.0.1"
)

cur = conn.cursor()
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