# Задание 1 - 2
import time

class Auto:
    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1

class Car(Auto):
    def __init__(self, brand, age, color, mark, weight, max_speed):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max_speed is {self.max_speed}")

class Truck(Auto):
    def __init__(self, brand, age, color, mark, weight, max_load):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

# Создание объектов класса Car
car1 = Car("Audi", 2, "синий", "A6", 1500, 250)
car2 = Car("BMW", 4, "черный", "X5", 1800, 300)


# Проверка методов и атрибутов класса Car
car1.move()
car1.stop()
car1.birthday()
print(car1.age)
print(car1.max_speed)


car2.move()
car2.stop()
car2.birthday()
print(car2.age)
print(car2.max_speed)

# Создание объектов класса Truck
truck1 = Truck("Volvo", 3, "серый", "FH16", 5000, 2000)
truck2 = Truck("Mercedes-Benz", 5, "желтый", "Actros", 4000, 3000)

# Проверка методов и атрибутов класса Truck
truck1.move()
truck1.load()
print(truck1.max_load)

truck2.move()
truck2.load()
print(truck2.max_load)


# Задание 3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def subtract(self, other_circle):
        if self.radius == other_circle.radius:
            return Point(self.center.x, self.center.y)
        else:
            return abs(self.radius - other_circle.radius)

# Создание объектов класса Circle
point = Point(0, 0)
circle1 = Circle(point, 3)
circle2 = Circle(point, 5)

# Проверка метода subtract класса Circle
result = circle1.subtract(circle2)
print(result)
