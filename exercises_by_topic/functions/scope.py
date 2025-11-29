"""
Ejercicio:
Escribe una función calculate_stats(numbers) que reciba una lista de números y devuelva una tupla con:

número máximo
número mínimo
promedio

Ejemplo:
print(calculate_stats([2,5,8,3]))

Salida:
(8, 2, 4.5)
"""


def calculate_stats(numbers):
    max_number = max(numbers)
    min_number = min(numbers)
    average = sum(numbers) / len(numbers)
    return (max_number, min_number, average)


print(calculate_stats([2, 5, 8, 3]))
