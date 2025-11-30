"""
Ejercicio 4: validate_input con *args

Define una función: def all_numbers(*args):

Debe devolver True si todos los valores pasados son números,
de lo contrario False.

Ejemplo:
print(all_numbers(1, 3.5, 7))         # True
print(all_numbers(2, "hola", 9))      # False
print(all_numbers())                  # True (ningún argumento → no hay fallo)
"""

import numbers


def all_numbers(*args):
    for number in args:
        if not isinstance(number, numbers.Number):
            return False
    return True


print(all_numbers(1, 3.5, 7))
print(all_numbers(1, "hola", 3))
print(all_numbers())

"""
Pythonic

def all_numbers(*args):
    return all(isinstance(x, numbers.Number) for x in args)
"""
