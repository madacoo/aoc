from collections import defaultdict

def puzzle_input():
    return 368078

def move(x, y, x_dir, y_dir):
    return x + x_dir, y + y_dir

def adjacent_squares(x, y):
    "Return a list of adjacent square coordinates stored as (x, y) tuples."
    sg = spiral_grid()
    coords = [next(sg) for _ in range(9)][1:]
    return [(x + x_prime, y + y_prime) 
            for x_prime, y_prime in coords]

def stress_grid():
    "Generate a sequence of spiral grid values."
    # The value of each square is the sum of the values of adjacent square."
    # The value of 0, 0 is 1
    sg = spiral_grid()
    squares = defaultdict(int)
    x, y = next(sg) # 0, 0
    squares[(x, y)] = 1
    yield squares[(x, y)]
    while True:
        x, y = next(sg)
        value = sum([squares[(adj_x, adj_y)] 
                    for adj_x, adj_y in adjacent_squares(x, y)])
        squares[(x, y)] = value
        yield value

def spiral_grid():
    "Generate sequence of spiral grid coordinates."
    square = 1 # current square being 'built'

    x, y = 0, 0
    n = 1 # current number of squares in grid
    yield x, y

    x_dir, y_dir = 1, 0
    while True:
        if n == (2*square-1)**2:
            square += 1

        if x == square-1:
            x_dir, y_dir = 0, 1
        if y == square-1:
            x_dir, y_dir = -1, 0
        if x == -square+1:
            x_dir, y_dir = 0, -1
        if y == -square+1:
            x_dir, y_dir = 1, 0

        x, y = move(x, y, x_dir, y_dir)
        n += 1
        yield x, y


def location(square):
    "Return the x,y coordinates of square on infinite spiral grid."
    sg = spiral_grid()
    for _ in range(square):
        result = next(sg)
    return result


def mandist(x, y):
    """Return the Manhattan Distance of point x,y from origin."""
    return abs(x) + abs(y)

def test():
    assert location(1) == (0,0)
    assert location(12) == (2, 1)
    assert location(23) == (0, -2)
    assert mandist(*location((1))) == 0
    assert mandist(*location((12))) == 3
    assert mandist(*location((23))) == 2
    assert mandist(*location((1024))) == 31
    return True


# part 1
if test():
    print(mandist(*location(puzzle_input())))

# part 2
sg = stress_grid()
i, goal = 0, puzzle_input()
while i < goal: i = next(sg)
print(i)

