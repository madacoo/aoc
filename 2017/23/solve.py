from collections import defaultdict
from math import sqrt


def puzzle_input():
    with open('input.txt', 'r') as f:
        return f.read().strip().split('\n')


def execute(pc):
    def evaluate(y):
        try:
            return int(y)
        except ValueError:
            return registers[y]

    instr, x, y = instructions[pc].split(' ')
    if instr == 'set':
        registers[x] = evaluate(y)
    elif instr == 'sub':
        registers[x] -= evaluate(y)
    elif instr == 'mul':
        registers[x] *= evaluate(y)
        execute.mul_count += 1
    elif instr == 'jnz':
        if evaluate(x) != 0: pc += (evaluate(y)-1)

    return pc + 1


def prime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0: return False
    return True



# part a
registers = defaultdict(int)
instructions = puzzle_input()
program_counter = 0
execute.mul_count = 0
while program_counter >= 0 and program_counter < len(instructions):
    program_counter = execute(program_counter)
print(execute.mul_count)

# part b
print(len([b for b in range(106700, 123701, 17) if not prime(b)]))

