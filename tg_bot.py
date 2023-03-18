import re

qa = [1,2,3]
def see_all_products():
    with open("Available.csv",encoding="UTF-8",newline="") as file:
        reader=file.readlines()
        available=[line.rstrip().split(",") for line in reader]


        print(available)
    with open("qwert.csv","w",newline="") as qwe:
        for i in available:
            qwe.writelines(",".join(j for j in i)+"\n")


see_all_products()