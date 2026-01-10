"""
Word Search
Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.

The given matrix will be filled with all lowercase letters (a-z).
The word to find will always be in the matrix exactly once.
The word to find will always be in a straight line in one of these directions:
left to right
right to left
top to bottom
bottom to top
For example, given the matrix:

[
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "c"]
]
And the word "cat", return:

[[0, 1], [2, 1]]
Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the indices for the "t" (end of the word).
"""


def find_word(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])

    directions = [
        (0, 1),   # left to right
        (0, -1),  # right to left
        (1, 0),   # top to bottom
        (-1, 0),  # bottom to top
    ]

    # Traverse the entire matrix
    for i in range(rows):
        for j in range(cols):
            # Start only if the first letter matches
            if matrix[i][j] == word[0]:
                # Try all possible directions
                for dx, dy in directions:
                    x, y = i, j
                    match = True

                    # Check each character of the word
                    for k in range(1, len(word)):
                        x += dx
                        y += dy

                        # Check matrix boundaries
                        if x < 0 or x >= rows or y < 0 or y >= cols:
                            match = False
                            break

                        # Check if the character matches
                        if matrix[x][y] != word[k]:
                            match = False
                            break

                    # If all characters matched, return start and end indices
                    if match:
                        return [[i, j], [x, y]]

print(find_word([
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "a"]
],"cat"))