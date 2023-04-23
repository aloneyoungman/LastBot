
class Shape:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def draw(self):
        print(f'''Информация о фигуре''')
        print(f'Цвет: {self.color}')
        print( f'Имя: {self.name}')
class Rectangle(Shape):
    def __init__(self,name,color,width,height):
        super().__init__(name,color)
        self.width=width
        self.height=height

    def draw(self):
        super().draw()
        print(f'Ширина: {self.width}')
        print(f'Высота: {self.height}')


class Circle(Shape):
    def __init__(self,name,color,radius):
        super().__init__(name,color)
        self.radius=radius

    def draw(self):
        super().draw()
        print(f'Радиус:{self.radius}')

class Square(Rectangle):
    def __init__(self,name,color,side_lenght):
        super().__init__(name,color,side_lenght,side_lenght)
        self.side_lenght=side_lenght
#Не понимаю почему нужно в 34 строке указывать side_lenght да еще и 2 раза, пришел к этому методом проб и ошибок. Если объяснишь, буду благодарен
    def draw(self):
        print(f'Информация о квадрате')
        print(f'Имя: {self.name} \nЦвет: {self.color}\nДлина стороны квадрата: {self.side_lenght}')


Oval=Shape("Oval","Red")
rectangle=Rectangle("Rectangle","blue","3","4")
circle=Circle("Circle","black",3)
square=Square("Square","green","5")
Oval.draw()
rectangle.draw()
circle.draw()
square.draw()