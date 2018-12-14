from time import clock

def puzzle_input():
    with open("input.txt", "r") as f:
        return list(map(int, f.read().strip().split()))

def three_or_more(offset):
    "Decrement if offset is three or more; otherwise increment."
    if offset >= 3:
        return offset - 1
    return offset + 1

def jump(value, index, mutation_rule):
    "Return the new value and index after a jump."
    return mutation_rule(value), index + value

def solve_functional(instructions, mutation_rule=lambda x: x + 1):
    i = steps = 0
    length = len(instructions)
    while (0 <= i < length):
        instructions[i], i = jump(instructions[i], i, mutation_rule)
        steps += 1
    return steps

t0 = clock()
print(solve_functional(puzzle_input()))
print(solve_functional(puzzle_input(), mutation_rule=three_or_more))
print(clock() - t0)
