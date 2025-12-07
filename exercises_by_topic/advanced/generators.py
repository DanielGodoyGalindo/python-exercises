"""
1. Generador de números primos (infinito)

Crea una función generadora:

def prime_numbers():
    ...

Que produzca primos sin límite.
"""

import os


def prime_numbers():
    num = 2
    while True:
        is_prime = True
        for n in range(2, num):
            if num % n == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1


p = prime_numbers()
print(next(p))
print(next(p))
print(next(p))
print(next(p))


"""
2. Generador que pagine una lista en bloques

Función: def paginate(items, size):

Ejemplo:
list(paginate([1,2,3,4,5,6], 2))
# → [[1,2], [3,4], [5,6]]
"""


def paginate(items, size):
    block = []
    for item in items:
        block.append(item)
        if len(block) == size:
            yield block
            block = []
    if block:  # if there is an incomplete block
        yield block


p = paginate([1, 2, 3, 4, 5, 6], 2)
print(next(p))
print(next(p))
print(next(p))

"""
3. Generador inverso

Crea una versión generadora de reversed() para cualquier iterable.

def my_reversed(iterable):
    ...
"""


def my_reversed(iterable):
    for i in reversed(iterable):
        yield i


gen = my_reversed([1, 2, 3, 4, 5, 6])
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


"""
4. Generador que lea archivo línea a línea (lazy)

Función: def read_lines(path):

No uses read().
Debe devolver una línea cada vez.
"""


def read_lines(path):
    file1 = open(path, "r")
    lines = file1.readlines()
    for line in lines:
        yield line


dirname = os.path.dirname(__file__)
path = os.path.join(dirname, "../tree.txt")
gen = read_lines(path)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


"""
5. Generador con send()

Crea un generador contador:
counter = dynamic_counter()

empieza en 0
cada send(n) cambia el incremento interno

Ejemplo:
c = dynamic_counter()
next(c)        # 0
c.send(5)      # cambia el incremento a 5
next(c)        # 5
next(c)        # 10

Nivel avanzado real.
"""


def dynamic_counter():
    internal_counter = 0
    increment = 0
    received = yield internal_counter
    while True:
        if received is not None:
            increment = received
        internal_counter += increment
        received = yield internal_counter



c = dynamic_counter()
print(next(c))
print(next(c))
c.send(2)
print(next(c))
print(next(c))
c.send(5)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
