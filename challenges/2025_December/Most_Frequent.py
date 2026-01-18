"""
Most Frequent
Given an array of elements, return the element that appears most frequently.

There will always be a single most frequent element.

1. most_frequent(["a", "b", "a", "c"]) should return "a".
2. most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]) should return 2.
3. most_frequent([True, False, "False", "True", False]) should return False.
4. most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]) should return 40.
"""


def most_frequent(arr):
    times = 0
    output = ""
    for element in arr:
        current = arr.count(element)
        if current > times:
            times = current
            output = element
    return output


print(most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]))

"""
Using dictionary:

def most_frequent(arr):
    counts = {}
    for element in arr:
        counts[element] = counts.get(element, 0) + 1
    return max(counts, key=counts.get)can I use
"""
