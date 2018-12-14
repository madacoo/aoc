from time import clock


def puzzle_input():
    with open("input.txt", "r") as f:
        return [int(i) for i in f.read().strip().split()]


def solve(instructions):
    "Return the number of steps required to 'escape' the instructions."
    i = 0
    steps = 0
    length = len(instructions)
    while (i >= 0):
        try:
            offset = instructions[i]
        except IndexError:
            return steps
        instructions[i] += 1
        i += offset
        steps += 1
    return steps


def solve2(instructions):
    "Return the number of steps required to 'escape' the instructions."
    i = 0
    steps = 0
    while (i >= 0):
        try:
            offset = instructions[i]
        except IndexError:
            return steps
        increment = 1
        if offset >= 3:
            increment = -1
        instructions[i] += increment
        i += offset
        steps += 1
    return steps
    

def timer(f, *args):
    t0 = clock()
    result = f(*args)
    t1 = clock()
    return t1-t0, result


print(timer(solve, puzzle_input()))
print(timer(solve2, puzzle_input()))
