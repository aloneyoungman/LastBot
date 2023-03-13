import csv

available=[]
wares=[]
products=[]

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


def see_all():
    available_uniq=[]
    #для того чтобы отсортировать по складам ищу уникальные значения id складов
    for i in range(len(available)):
        available_uniq.append(available[i][1])
    available_uniq=sorted(list(set(available_uniq)))

    for i in available_uniq:
        print(f"Товары склада {i}: ")
        for j in range(len(available)):
            if available[j][2]==products[j][0] and available[j][1]==i:
                print(products[j])



def add_product(name,weight,price,ware):
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