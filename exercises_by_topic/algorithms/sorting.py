"""
Ejercicio 1 — Bubble Sort

Implementa bubble sort a mano:

bubble_sort([4,2,9,1])  # [1,2,4,9]
"""


def bubble_sort(nums):
    n = len(nums)
    finished = False
    while not finished:
        finished = True
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                finished = False
    return nums


print(bubble_sort([4, 2, 9, 1]))
"""
Ejercicio 2 — Selection Sort

selection_sort([7,3,5,2])  # [2,3,5,7]
"""


"""
Ejercicio 3 — QuickSort (recursivo)

quicksort([3,6,8,2,5])  # [2,3,5,6,8]
"""


"""
Ejercicio 4 — ordenar tuplas por el segundo elemento

sort_tuples([(“Alex”,30),(“Bob”,20),(“Carl”,25)])
# → [("Bob",20),("Carl",25),("Alex",30)]
"""
