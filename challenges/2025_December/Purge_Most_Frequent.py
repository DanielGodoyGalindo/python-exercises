"""
Purge Most Frequent
Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

If multiple values are tied for most frequent, remove all of them.
Do not change any of the other elements or their order.

1. purge_most_frequent([1, 2, 2, 3]) should return [1, 3].
2. purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]) should return ["a", "b", "b", "c", "c", "c"].
3. purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]) should return ["red", "green", "red", "green"].
4. purge_most_frequent([5, 5, 5, 5]) should return [].
5. purgeMostFrequent([10, 12, 7, 3, 7, 7, 12, 12]) should return [10, 3].
"""


def purge_most_frequent(arr:list):
    # Create dict with ocurrences
    elements = {}
    for element in arr:
        if element not in elements:
            elements[element] = 1
        else:
            elements[element] += 1
    # Get max values
    max_count  = 0
    for key, value in elements.items():
        if value >= max_count :
            max_count  = value
    # Get keys where max values are located
    maxs = []
    for key, value in elements.items():
        if value == max_count :
            maxs.append(key)
    # Delete elements with max value
    output = arr.copy()
    for element in maxs:
        while element in output:
            output.remove(element)
    return output

'''
Pythonic:
from collections import Counter

def purge_most_frequent(arr):
    counts = Counter(arr)
    max_count = max(counts.values())
    most_frequent = {k for k, v in counts.items() if v == max_count}
    return [x for x in arr if x not in most_frequent]
'''

print(purge_most_frequent([10, 12, 7, 3, 7, 7, 12, 12]))