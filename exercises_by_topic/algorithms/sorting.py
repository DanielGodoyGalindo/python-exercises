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


print(f"BubbleSort: {bubble_sort([4, 2, 9, 1])}")


"""
Ejercicio 2 — Selection Sort

selection_sort([7,3,5,2])  # [2,3,5,7]
"""


def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap numbers
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


print(f"SelectionSort: {selection_sort([7, 3, 5, 2])}")

"""
Ejercicio 3 — QuickSort (recursivo)

quicksort([3,6,8,2,5])  # [2,3,5,6,8]
"""


def quicksort(nums):
    if len(nums) <= 1:
        return nums

    # get middle number
    pivot = nums[len(nums) // 2]

    # build a list for all the smaller, equal and bigger numbers, comparing with pivot (middle number)
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    # recursively sort smaller and bigger numbers.
    # Concatenate the results to return the sorted list with all numbers.
    return quicksort(left) + middle + quicksort(right)


print(f"QuickSort: {quicksort([3, 6, 8, 2, 5])}")

"""
Ejercicio 4 — ordenar tuplas por el segundo elemento

sort_tuples([(“Alex”,30),(“Bob”,20),(“Carl”,25)])
# → [("Bob",20),("Carl",25),("Alex",30)]
"""


def sort_tuples(tuples):
    n = len(tuples)
    for i in range(n):
        smallest_idx = i
        for j in range(i + 1, n):
            if tuples[j][1] < tuples[smallest_idx][1]:
                smallest_idx = j
        tuples[i], tuples[smallest_idx] = tuples[smallest_idx], tuples[i]
    return tuples


print(f"SortTuples: {sort_tuples([("Alex", 30), ("Bob", 20), ("Carl", 25)])}")
