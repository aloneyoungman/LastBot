
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

# Если я тебя правильно понял ты про строку "super().__init__(name,color,side_lenght,side_lenght)"
# Давай разбираться
# Что мы здесь хотим сделать ?
#   Создать квадрат, который наследуется от прямоугольника
#   Это значит, что квадрат обязательно обладает всеми свойствами прямоугольника, а также может иметь дополнительные
#
# Что делает метод super().__init__() ?
#   Он вызывает конструктор класса родителя (в данном случае прямоугольника)
#   Это нужно для того, чтобы выполнялось наследование и объект мог обладать всеми свойствами родителя
#   Так как родитель-прямоугольник обладает свойствами height и width - нам их нужно определить и для квадрата 
#   (даже не смотря на то, что они одинаковые у квадрата)
#   Поэтому мы и передаём дважды одно и тоже значения, чтобы и задать высоту и ширину
# 
# Зачем нам это нужно, если для квадрата достаточно свойства side_lenght ?
#   Для того, чтобы работало наследование
#   Пример использования:
#   Представь, что у нас есть большое количество фигур (и кругов и квадратов и прямоугольников)
#   И нам неизвестно какой объект какого класса
#   В этом случае - мы сможем ко всем ним обратиться через свойства родителя (которые обязательно есть у всех детей) 
#   т.е. мы будем уверены, что у каждого конкретного объекта есть метод draw(), так как он точно есть у родителя

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