'''
Ball Trajectory
Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

The ball always moves in a straight line.
The movement direction is determined by how the ball moved from 1 to 2.
The edges of the matrix are considered walls. If the ball hits a:
top or bottom wall, it bounces by reversing its vertical direction.
left or right wall, it bounces by reversing its horizontal direction.
corner, it bounces by reversing both directions.

1. get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]) should return [2, 3].
2. get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]) should return [3, 0].
3. get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]) should return [1, 2].

'''

def get_next_location(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # 1. Find positions of 1 and 2
    prev_row = prev_col = curr_row = curr_col = None

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                prev_row, prev_col = r, c
            elif matrix[r][c] == 2:
                curr_row, curr_col = r, c

    # 2. Get movement direction
    dy = curr_row - prev_row
    dx = curr_col - prev_col

    # 3. Get next position
    next_row = curr_row + dy
    next_col = curr_col + dx

    # 4. Bouncing walls
    if next_row < 0 or next_row >= rows:
        dy *= -1
        next_row = curr_row + dy

    if next_col < 0 or next_col >= cols:
        dx *= -1
        next_col = curr_col + dx

    return [next_row, next_col]