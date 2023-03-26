
def see_all_products():
    with open("Available.csv",encoding="UTF-8",newline="") as file:
        reader = file.readlines()
        available = [line.rstrip().split(",") for line in reader]
        available_uniq = sorted(list(set(map(lambda row: row[1], available))))

    with open("Products.csv", encoding="UTF-8", newline="") as file:
        reader1=file.readlines()
        products=[line.rstrip().split(",") for line in reader1]

    products_see={}
    for available_id in available_uniq:
        products_see[available_id]=[j[1] for j in available,t[2] for t in available]
    print(products_see)
    with open("qwert.csv","w",newline="") as qwe:
        for i in available:
            qwe.writelines(",".join(j for j in i)+"\n")


see_all_products()