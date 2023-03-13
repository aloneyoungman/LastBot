import csv

# Какие то важные моменты буду отмечать (!)
# Свои комменты буду оставлять без оступов, чтобы ты не путал со своими
available=[]
wares=[]
products=[]

# Не знаю насколько осмысленно ты это использовал - но есть два способа работы с БД\файлами 
# Можно один раз их открыть "прочитать", и хранить всё время в оперативке
# А сохранять в файл только при завершении работы с программой. 
# 
# Второй вариант - не хранить данные в оперативке (т.е. не создавать единый список с данными)
# А каждый раз обращаться напрямую к файлам и добавлять/редактировать/удалять напрямую из файлов
# 
# У тебя же смешаны 2 этих подхода
# Дальше по коду - ты одновременно работаешь и с общим массивом и с файлами (например при добавлении)
# Нужно оставить только один вариант
# Сейчас я бы тебе рекомендовал остановиться на прямой работе с файлами (т.е. каждый раз когда работаешь с данными - ты работаешь с файлами)




# Лучше - если чтение будет реализовано в виде отдельных методов
#
# Если работаешь с БД (или csv в данном случае) - будет круто, если в комментах будешь оставлять то, какие данные получаешь.
# Например (id, ware_id, product_id) для Available

with open("Available.csv","r") as av:
    reader=csv.reader(av)
    for row in reader:
        available.append(row)

with open("Products.csv","r") as pr:
    reader=csv.reader(pr)
    for row in reader:
        products.append(row)

with open("Wares.csv","r") as wa:
    reader=csv.reader(wa)
    for row in reader:
        wares.append(row)

# Лучше, если ты будешь писать методы, которые возвращают список, а не сразу выводят
# А вывод уже проиходит в основном теле программы 
# Это позволит тебе эти функции легче переиспользовать в дальнейшем для бота.

def see_all():
    available_uniq=[]
    #для того чтобы отсортировать по складам ищу уникальные значения id складов
# (!) Для работы со списками/словарями - есть функция map() - обязательно почитай про неё подробнее
# Она позволяет без циклов "получить свойсто всех объектов в списке"
# Например твой цикл можно было бы заменить на
#   available_uniq = list(map(lambda row:row[0], available))
#
# Т.е. мы в функцию передаём, как нужно работать с каждым объектом в нашем списке (через лямбду - получить 0 элемент вложенного списка)
# А второй параметр - то, по какому объекту итерируемся
# Преобразовывать в лист сразу - не обязательно (скорее даже вредно) - если интересно - можешь почитать про генераторы (!)
# (https://book.pythontips.com/en/latest/map_filter.html)
# В кратце - генераторы позволяют не загружать в память ПК весь лист сразу, а знать "как получить следующий элемент на основании текущего"
# Используются для циклов или других генераторов 
# 
# Также здесь можно было бы использовать словарь в формате {уникальный id склада - список с id всех продуктов в нём
# С таким было бы во много раз удобнее работать  
    for i in range(len(available)):
        available_uniq.append(available[i][1])
    available_uniq=sorted(list(set(available_uniq)))
# Даже переменные простых циклов - стоит именовать понятно. Например ware_id.
    for i in available_uniq:
        print(f"Товары склада {i}: ")
# Здесь также можно использовать map() и filter() и/или использовать словарь, чтобы упростить код   
        for j in range(len(available)):
            if available[j][2] == products[j][0] and available[j][1] == i:
                print(products[j])



def add_product(name,weight,price,ware):
# У python есть общепринятый стандарт того, как писать код (!) 
# https://peps.python.org/pep-0008/
# Переменные должны быть написаны в camel_case, т.е. твою переменную стоило бы назвать add_available 
# Крайне настоятельно рекомендую предерживаться стандартов написания кода - потом будет тяжело переучиваться, а это важно
    addavailable=[str(len(available)+1),str(ware),str(len(products)+1)]
    available.append(addavailable)
    addproduct=[str(len(products)+1),str(name),str(weight),str(price)]
    products.append(addproduct)
    with open("Available.csv","w",newline="") as av:
        write=csv.writer(av)
        write.writerows(available)

    with open("Products.csv","w",newline="") as pr:
        write=csv.writer(pr)
        write.writerows(products)

    print(available)
    print(products)

def change_product(id,name,weight,price,ware):
    for i in range(len(available)):
        if available[i][2]==str(id):
            available[i]=[str(available[i][0]),str(ware),str(id)]
            products[i]=[str(id),str(name),str(weight),str(price)]
            print(available[i][0])

    with open("Available.csv","w",newline="") as av:
        write=csv.writer(av)
        write.writerows(available)

    with open("Products.csv","w",newline="") as pr:
        write=csv.writer(pr)
        write.writerows(products)


def delete_product(id):
    availablenew=[]
    productsnew=[]
    for i in range(len(available)):
        if available[i][2]!=str(id):
            availablenew.append(available[i])
        if products[i][0]!=str(id):
            productsnew.append(products[i])
    for i in range(len(availablenew)):
        availablenew[i][0]=str(i+1)
        availablenew[i][2]=str(i+1)
        productsnew[i][0]=str(i+1)
    print(availablenew)
    print(productsnew)
    with open("Available.csv","w",newline="") as av:
        write=csv.writer(av)
        write.writerows(availablenew)

    with open("Products.csv","w",newline="") as pr:
        write=csv.writer(pr)
        write.writerows(productsnew)

def see_wares():
    waresall=[]

    for i in range(len(wares)):
        weight=[0]
        for j in range(len(available)):
            if available[j][1]==wares[i][0]:
                weight[0]+=int(products[j][2])

        waresall.append([wares[i][0],weight[0],wares[i][1]])

    for t in waresall:
        print(t)
# Основное тело - лучше писать после инициализации всех функций.
see_all()

def add_ware(max_weight):
    waresnew=[]
    for war in wares:
        waresnew.append(war)

    waresnew.append([str(len(waresnew)+1),str(max_weight)])
    with open("Wares.csv","w",newline="") as wa:
        write=csv.writer(wa)
        write.writerows(waresnew)
    print(waresnew)


see_wares()
see_all()
