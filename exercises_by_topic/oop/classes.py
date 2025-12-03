"""
Ejercicios OOP — Classes
"""

# 1. Crear una clase Persona con:
#    - atributos: nombre, edad
#    - método: presentarse()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi! My name is {self.name} and I'm {self.age} years old."


# 2. Clase Coche:
#    - atributos: marca, modelo, velocidad = 0
#    - métodos: acelerar(cantidad), frenar(cantidad)


class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def __str__(self):
        return f"{self.brand} {self.model}, speed: {self.speed} km/h"

    def accelerate(self, value):
        self.speed += value
        print(f"Now you are at {self.speed} km/h.")

    def brake(self, value):
        if self.speed >= value:
            self.speed -= value
        else:
            self.speed = 0
        print(f"Now you are at {self.speed} km/h.")


# 3. Clase CuentaBancaria:
#    - atributos: titular, saldo
#    - métodos: depositar(), retirar(), mostrar_saldo()


class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self._balance = balance # private

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            return "Insufficient funds."

    def show_balance(self): # getter
        return self._balance


if __name__ == "__main__":
    p = Person("Luis", 20)
    print(p.introduce())

    c = Car("Toyota", "Corolla")
    print(c)
    c.accelerate(30)
    c.accelerate(20)
    c.brake(60)
    print(f"Current speed: {c.speed}")

    account = BankAccount("Ana", 100)
    print(f"Current balance: {account.show_balance()}")
    account.deposit(50)
    print(f"Current balance: {account.show_balance()}")
    account.withdraw(75)
    print(f"Current balance: {account.show_balance()}")
    account.withdraw(80) # not allowed
    print(f"Current balance: {account.show_balance()}")
