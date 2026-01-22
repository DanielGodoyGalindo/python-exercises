"""
Checkerboard
Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with "X" and "O" characters of the given size.

The characters should alternate like a checkerboard.
The top-left cell must always be "X".
For example, given [3, 3], return:

[
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["X", "O", "X"]
]

1. create_board([3, 3]) should return
[["X", "O", "X"],
 ["O", "X", "O"],
 ["X", "O", "X"]].

2. create_board([6, 1]) should return
[["X"], ["O"], ["X"], ["O"], ["X"], ["O"]].

3. create_board([2, 10]) should return [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]].
4. create_board([5, 4]) should return [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]].
"""


def create_board(dimensions):
    rows, cols = dimensions
    board = []
    for r in range(rows):
        row = []
        for c in range(cols):
            # If the sum of the row index (r) and column index (c) is even,
            # place an "X"; otherwise, place an "O" to create the checkerboard pattern
            if (r + c) % 2 == 0:
                row.append("X")
            else:
                row.append("O")
        board.append(row)
    return board


print(create_board([5, 4]))
