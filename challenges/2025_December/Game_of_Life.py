"""
Game of Life
Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

Each cell is either 1 (alive) or 0 (dead).
A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
Cells on the edges have fewer than eight neighbors.
Rules for updating each cell:

Any live cell with fewer than two live neighbors dies (underpopulation).
Any live cell with two or three live neighbors lives on.
Any live cell with more than three live neighbors dies (overpopulation).
Any dead cell with exactly three live neighbors becomes alive (reproduction).
For example, given:

[
  [0, 1, 0],
  [0, 1, 1],
  [1, 1, 0]
]
return:

[
  [0, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]
Each cell updates according to the number of live neighbors. For instance, [0][0] stays dead (2 live neighbors), [0][1] stays alive (2 live neighbors), [0][2] dies (3 live neighbors), and so on.
"""


def game_of_life(board):
    rows = len(board)
    cols = len(board[0])

    # Direcciones de los 8 vecinos
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Nueva matriz para el siguiente estado
    next_board = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0

            # Contar vecinos vivos
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols:
                    live_neighbors += board[ni][nj]

            # Aplicar reglas
            if board[i][j] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    next_board[i][j] = 1
                else:
                    next_board[i][j] = 0
            else:
                if live_neighbors == 3:
                    next_board[i][j] = 1

    return next_board
