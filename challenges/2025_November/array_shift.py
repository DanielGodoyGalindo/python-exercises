"""
Array Shift
Given an array and an integer representing how many positions to shift the array, return the shifted array.

A positive integer shifts the array to the left.
A negative integer shifts the array to the right.
The shift wraps around the array.
For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].

1. shift_array([1, 2, 3], 1) should return [2, 3, 1].
2. shift_array([1, 2, 3], -1) should return [3, 1, 2].
3. shift_array(["alpha", "bravo", "charlie"], 5) should return ["charlie", "alpha", "bravo"].
4. shift_array(["alpha", "bravo", "charlie"], -11) should return ["bravo", "charlie", "alpha"].
5. shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15) should return [5, 6, 7, 8, 9, 0, 1, 2, 3, 4].
"""


def shift_array(arr, n):
    if n >= 0:
        for _ in range(0, n):
            element = arr[0]
            arr.remove(arr[0])
            arr.append(element)
    else:
        n *= -1
        for _ in range(0, n):
            element = arr[-1]
            arr.remove(arr[-1])
            arr.insert(0, element)
    return arr


"""
Pythonic:
def shift_array(arr, n):
    # If the array is empty, return it as is
    if not arr:
        return arr

    # Reduce the shift to the array length to avoid unnecessary rotations
    n = n % len(arr)

    # Slice the array:
    # - arr[n:] takes the elements from index n to the end
    # - arr[:n] takes the first n elements
    # Concatenating them produces a left rotation
    return arr[n:] + arr[:n]
"""


print(shift_array(["alpha", "bravo", "charlie"], -11))
