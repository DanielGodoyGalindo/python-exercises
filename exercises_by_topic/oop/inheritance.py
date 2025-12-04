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


'''
4. Herencia múltiple simple

Crea:
clase Volador con método volar()
clase Nadador con método nadar()
clase Pato que herede de ambas

Prueba el orden de resolución de métodos (MRO) con Pato.__mro__.
'''



'''
5. Sistema de empleados

Clase base Empleado:
nombre
salario_base
método calcular_salario()

Clases hijas:
EmpleadoTiempoCompleto → salario base + bonus
EmpleadoPorHoras → cantidad horas * pago por hora

Crea una lista de empleados y calcula salarios.
'''