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
