"""
Ejercicio 1 — factorial recursivo

Escribe una función recursiva que calcule el factorial de un número.

factorial(5)  # 120

"""


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))


"""
Ejercicio 2 — suma recursiva

Suma todos los elementos de una lista usando recursión:

sum_recursive([1,2,3,4])  # 10
"""


def sum_recursive(nums):
    # Base case: when the list is empty, return 0
    if len(nums) == 0:
        return 0
    else:
        # Take the first element of the current list
        first = nums.pop(0)
        # IMPORTANT:
        # For recursion with lists, we must always reduce the list,
        # otherwise the function would call itself infinitely.
        #
        # We reduce the list by removing the first element (already in 'first'),
        # so the next recursion call works with a smaller list.
        return first + sum_recursive(nums)


print(sum_recursive([1, 2, 3, 4]))

"""
Ejercicio 3 — Fibonacci recursivo

fibonacci(6)  # 8
"""

# For Fibonacci, the recursive function must make two calls.


def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(6))
