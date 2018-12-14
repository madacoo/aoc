
def puzzle_input():
    with open('input.txt', 'r') as f:
        return f.read().split('\n')


def advance_direction(i, j, direction):
    if direction == 'D': return i+1, j
    if direction == 'U': return i-1, j
    if direction == 'R': return i,   j+1
    if direction == 'L': return i,   j-1


def choose_direction(i, j, direction):
    if direction in 'DU':
        if GRID[i][j-1] != ' ': return 'L'
        return 'R'
    else:
        if GRID[i-1][j] != ' ': return 'U'
        return 'D'
    raise Exception


def solve():
    result = []
    steps = 0
    i, j = 0, GRID[0].index('|') # row, col
    direction = 'D'
    char = '|'

    while char != ' ':
        steps += 1
        i, j = advance_direction(i, j, direction)
        char = GRID[i][j]
        if char == '+':
            direction = choose_direction(i, j, direction)
        elif char not in '|-': result.append(char)

    return "".join(result), steps


GRID = puzzle_input()
letters, steps = solve()
print(letters)
print(steps)
