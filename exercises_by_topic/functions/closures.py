"""
Ejercicio:
Crea una función multiplier(n) que devuelva otra función
La función resultante multiplicará cualquier número por n.

Ejemplo:
times3 = multiplier(3)
print(times3(10))   # 30

times7 = multiplier(7)
print(times7(4))    # 28

Esto practica: funciones como objetos, creación de funciones en runtime, concepto de closure
"""


def multiplier(n):
    def times(m):
        return n * m

    return times


times3 = multiplier(3)
print(times3(10))
