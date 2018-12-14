
def puzzle_input():
    rule_dict = {}
    with open('input.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split(" => ")
            for k in transformations(key):
                rule_dict[k] = value
    return rule_dict


def transformations(grid):
    """Iterate over the 8 possible transformations
       of a grid, as a result of rotations and flips.
    """

    def rotate(grid):
        result = []
        for row in zip(*grid.split('/')[::-1]):
            result.append(''.join(row))
        return '/'.join(result)
        
    def flip(grid):
        return '/'.join([r[::-1] for r in grid.split('/')])

    for flipping in range(2):
        for rotation in range(4):
            yield grid
            grid = rotate(grid)
        grid = flip(grid)


def get_block(grid, x, y, size):
    return '/'.join([r[x:x+size] for r in grid[y:y+size]])


def split(grid):
    cells = []
    g = grid.split('/')
    size = len(g[0])
    cell_size = 2 if size % 2 == 0 else 3
    # I had a bug here that took me a good couple hours to find: 
    # y needs to be iterated over outside of x, not inside.
    # Otherwise the order of the resulting cells is rotated.
    for y in range(0, size, cell_size):
        for x in range(0, size, cell_size):
            cells.append(get_block(g, x, y, cell_size))
    return cells


def join(cells):
    if len(cells) == 1: return cells[0]
    results = []
    cells = [c.split('/') for c in cells]
    width = int(len(cells) ** 0.5)
    for col in range(0, len(cells), width):
        for r in range(0, len(cells[0])):
            results.append(''.join(
                [cells[col+i][r] for i in range(width)]))
    return '/'.join(results)


rule_dict = puzzle_input()

# part a
grid = ".#./..#/###"
for iteration in range(5):
    grid = join([rule_dict[cell] for cell in split(grid)])
print(grid.count('#'))

# part b
grid = ".#./..#/###"
for iteration in range(18):
    grid = join([rule_dict[cell] for cell in split(grid)])
print(grid.count('#'))

# The following is what I used to find the bug mentioned above.
# I piped the output to a file and played around with it until
# finally realising my mistake. I am so happy I finally killed that bug.
"""
# part b
grid = ".#./..#/###"
for iteration in range(6):
    cells = split(grid)
    new_cells = []
    for cell in cells:
        new_cell = rule_dict[cell]
        new_cells.append(new_cell)

    print(iteration)
    print(grid.replace('/', '\n'))
    print()
    print(cells)
    print()
    print(new_cells)
    print()
    grid = join(new_cells)
    print(grid.replace('/', '\n'))
    print(grid.count('#'))
    print()

print(369) # from running someone else's code I knew that this should be the result after 6 iterations
# it's somewhat weird that the code worked for part a since it wasn't actually producing the correct grid on each iteration
"""

