from collections import defaultdict

def puzzle_input():
    with open("input.txt", "r") as f:
        return f.readlines()

def parse(instruction):
    terms = instruction.split()
    r1, val1 = terms[0], terms[2]
    arith_op = '+' if 'inc' in terms else '-'
    r2, val2 = terms[4], terms[6]
    compar_op = terms[5]

    command = "registers['{}'] {}= {}".format(r1, arith_op, val1)
    condition = "registers['{}'] {} {}".format(r2, compar_op, val2)

    return command, condition

def solve(instructions):
    registers = defaultdict(int)
    max_seen = 0
    for instr in instructions:
        command, condition = parse(instr)
        if eval(condition): 
            exec(command)
            r = command.split()[0]
            val = eval(r)
            if val > max_seen: max_seen = val
    return max_seen, registers[max(registers, key=lambda k: registers[k])]

print(solve(puzzle_input()))

