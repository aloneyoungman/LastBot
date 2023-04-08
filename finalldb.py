from Available import Available
from Partners import Partners
from Products import Products
from Wares import Wares
from Orders import Orders
from Order_product import Order_products
from MyQueries import MyQueries
import psycopg2
from datetime import datetime, date, time,timedelta
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password = "8991",
    host="127.0.0.1"
)

cur = conn.cursor()


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
    rows = table.read()
    if rows is not None:
        return list(map(lambda row: row[0], rows))


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
    Order_products.update(order_products_ids[0],orders_ids[1],product_Ids[1])

    print('partners',Partners.read())
    print('orders',Orders.read())
    print('orders_products',Order_products.read(), orders_ids[0],product_Ids[0])

    print('order_product_by_id', MyQueries.GetOrderProducts(orders_ids[0]))
    print('orders_by_parnter_id', MyQueries.GetPartnerQrders(partners_ids[0]))



test_func()
