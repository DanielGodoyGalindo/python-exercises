from abc import abstractmethod
import math

"""
1. Herencia con Animales

Clase base Animal:
método hablar() que levante NotImplementedError

Clases hijas:
Perro → devuelve "Guau"
Gato → devuelve "Miau"

Prueba polimorfismo creando una lista de animales y llamando hablar().
"""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk():
        return NotImplementedError("This method has to be implemented by the subclass")


class Dog(Animal):
    def talk(self):
        return "Guau!"


class Cat(Animal):
    def talk(self):
        return "Miau!"


d1 = Dog("dog1", 1)
c1 = Cat("cat1", 3)
d2 = Dog("dog2", 5)

animal_list = (d1, c1, d2)

for a in animal_list:
    print(a.talk())


"""
2. Vehículos

Clase base Vehiculo:
atributos marca, modelo

método mover()

Clases derivadas:
Coche → imprime "Conduciendo"
Bicicleta → imprime "Pedaleando"
"""


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move():
        return NotImplementedError("This method has to be implemented by the subclass")


class Car(Vehicle):
    def move(self):
        print("Driving!")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling!")


c = Car("Ford", "Mustang")
b = Bicycle("Scott", "Spark")

c.move()
b.move()


"""
3. Figuras geométricas (Herencia + Polimorfismo)

Clase padre Figura:
método abstracto area()

Hijas: Circulo, Triangulo, Rectangulo

Crea una lista de figuras y calcula todas las áreas.
"""


class Figure:
    @abstractmethod
    def area():
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.sqrt(self.radius)


class Triangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height / 2


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


c = Circle(6)
t = Triangle(4, 5)
r = Rectangle(7, 4)

figure_list = (c, t, r)

for f in figure_list:
    print(f.area())


"""
4. Herencia múltiple simple

Crea:
clase Volador con método volar()
clase Nadador con método nadar()
clase Pato que herede de ambas

Prueba el orden de resolución de métodos (MRO) con Pato.__mro__.

The method resolution order (MRO) is the order that Python follows to look up attributes and methods in a class hierarchy. 
It determines which method or attribute to use when names collide in multiple inheritance scenarios.

https://realpython.com/ref/glossary/mro/
"""


class Flying:
    def fly(self):
        return "I can fly!"


class Swimmer:
    def swim(self):
        return "I can swim!"


class Duck(Flying, Swimmer):
    def __init__(self):
        pass


ducky = Duck()
print(ducky.fly())
print(
    Duck.__mro__
)  # (<class '__main__.Duck'>, <class '__main__.Flying'>, <class '__main__.Swimmer'>, <class 'object'>)

"""
5. Sistema de empleados

Clase base Empleado:
    nombre
    salario_base
    método calcular_salario()

Clases hijas:
EmpleadoTiempoCompleto → salario base + bonus
EmpleadoPorHoras → cantidad horas * pago por hora

Crea una lista de empleados y calcula salarios.
"""


class Employee:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary():
        raise NotImplementedError("This method has to be implemented by subclasses.")


class Full_time_employee(Employee):
    def __init__(self, name, base_salary, salary_bonus):
        super().__init__(name) # calling init from parent class
        self._base_salary = base_salary
        self._salary_bonus = salary_bonus

    def calculate_salary(self):
        print(f"{self.name} (Full_time_employee salary): ")
        return self._base_salary + self._salary_bonus


class Hourly_employee(Employee):
    def __init__(self, name, worked_hours):
        super().__init__(name)  
        self.worked_hours = worked_hours
        self.hour_pay = 8

    def calculate_salary(self):
        print(f"{self.name} (Hourly_employee salary): ")
        return self.worked_hours * self.hour_pay


fte1 = Full_time_employee("Dani", 1200, 200)
he1 = Hourly_employee("Pepito", 40)
fte2 = Full_time_employee("Fulanito", 2000, 300)
he2 = Hourly_employee("Menganito", 160)

employees_list = (fte1, fte2, he1, he2)

for e in employees_list:
    print(e.calculate_salary())
