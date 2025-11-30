"""
Función que recibe otra función (callback)

Implementa:

def apply_to_list(func, values):


Que aplica la función func a cada elemento de la lista.

Ejemplo:

def square(x):
    return x * x

print(apply_to_list(square, [1,2,3,4]))

Salida:

[1, 4, 9, 16]
"""


def apply_to_list(func, values):
    new_values = []
    for v in values:
        new_values.append(func(v))
    return new_values
    #  return [func(v) for v in values] --> pythonic implementation


def square(x):
    return x * x


def increment(x):
    return x + 1


print(apply_to_list(square, [1, 2, 3, 4]))
print(apply_to_list(increment, [10, 20, 30, 40]))
