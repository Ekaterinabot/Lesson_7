# 1) Описать в терминах ООП
# Разберу примером, чтоб самой было понятнее

# Создаем класс Car
class Car:
    name = "mercedez"               # создаем атрибуты класса
    make = 2010
    model = "c200"
    
from sys import stderr 
print("заводим двигатель", file=stderr)
print("отключаем двигатель", file=stderr)

# Создаем объект класса Car под названием car_a
car_a = Car()
 
# Создаем объект класса Car под названием car_b
car_b = Car()
print(type(car_b))
print(type(car_a))

print(car_b.model)
print(dir(car_b))  # чтоб посмотреть на все атрибуты объекта car_b
                   # встроенная функция
class Car:
    car_count = 0  # создаем атрибуты класса
    
    def start(self, name, make, model):    # создаем методы класса
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1
        
car_a = Car()      # создадим объект класса Car и вызовем метод start() для car_a
car_a.start("Toyota", 2015, "Corrola")
print(car_a.name)  
print(car_a.car_count)

car_b = Car()      # для car_b
car_b.start("Shevrolet", 2013, "Spark")  
print(car_b.name)  
print(car_b.car_count)

# 2) Придумать по 2-3 действия каждому представителю.
# Добавим Быстрая езда и медленная езда.
# С помощью конструктора - метод __init__
class Car:
    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model
car_a = Car("Toyota", 2015, "Corrola")      
print("Быстрая езда")
print(car_a.name) 

class Car:
    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model
car_a = Car("Shevrolet", 2013, "Spark")      
print("Медленная езда")
print(car_a.name)



# Такая структура выбрана, потому что увидела понятный пример ООП
# и начала его расписывать.
# И еще потому что автомобиль заводиться, медленно и быстро ездит 
# прямо в программе.

заводим двигатель
отключаем двигатель
<class '__main__.Car'>
<class '__main__.Car'>
c200
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'make', 'model', 'name']
Двигатель заведен
Toyota
1
Двигатель заведен
Shevrolet
2
Быстрая езда
Toyota
Медлен�ая езда
Shevrolet


...Program finished with exit code 0
Press ENTER to exit console.