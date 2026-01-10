'''
Rectangle Count
Given two positive integers representing the width and height of a rectangle, determine how many rectangles can fit in the given one.

Only count rectangles with integer width and height.
For example, given 1 and 3, return 6. Three 1x1 rectangles, two 1x2 rectangles, and one 1x3 rectangle.
'''

def count_rectangles(width, height):
    total = 0
    for w in range(1, width + 1):
        for h in range(1, height + 1):
            total += (width - w + 1) * (height - h + 1)
    return total


print(count_rectangles(3,2))