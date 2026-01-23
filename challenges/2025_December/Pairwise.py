"""
Pairwise
Given an array of integers and a target number, find all pairs of elements in the array whose values add up to the target and return the sum of their indices.

For example, given [2, 3, 4, 6, 8] and 10, you will find two valid pairs:

2 and 8 (2 + 8 = 10), whose indices are 0 and 4
4 and 6 (4 + 6 = 10), whose indices are 2 and 3
Add all the indices together to get a return value of 9.

1. pairwise([2, 3, 4, 6, 8], 10) should return 9.
2. pairwise([4, 1, 5, 2, 6, 3], 7) should return 15.
3. pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20) should return 22.
4. pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24) should return 10.
"""


def pairwise(arr, target):
    pairs = dict()
    for x_idx, x in enumerate(arr):
        for y_idx, y in enumerate(arr):
            if (x + y) == target and (x_idx != y_idx):
                print(f"{x} and {y} sum {target}")
                pair = str(sorted([x_idx,y_idx]))
                pairs[pair] = [x_idx,y_idx]
    output = 0
    for pair in pairs.values():
        output += sum(pair)
    return output


'''
def pairwise(arr, target):
    used = set()
    index_map = {}
    total = 0

    for i, num in enumerate(arr):
        complement = target - num

        if complement in index_map and index_map[complement] not in used:
            total += i + index_map[complement]
            used.add(i)
            used.add(index_map[complement])
        else:
            index_map[num] = i

    return total
'''

print(pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24))