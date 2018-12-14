from collections import defaultdict


def puzzle_input():
    """Return puzzle input as list of tuples: 
        (str instruction, list str args)."""
    def parse(line):
        parts = line.split(" ")
        instruction = parts[0]
        args = tuple(map(
            lambda a:"registers['{}']".format(a) 
                if a.isalpha() else int(a),     
            parts[1:]))
        return instruction, args
    with open("input.txt", "r") as f:
        return list(map(parse, f.read().strip().split("\n")))

def parse(instruction):
    "Return instruction as str representing Python expression."
    instr, args = instruction
    if instr == "snd":
        return "last_freq = {}".format(args[0])
    elif instr == "set":
        return "{} = {}".format(args[0], args[1])
    elif instr == "add":
        return "{} += {}".format(args[0], args[1])
    elif instr == "mul":
        return "{} *= {}".format(args[0], args[1])
    elif instr == "mod":
        return "{} = {} % {}".format(args[0], args[0], args[1])
    elif instr == "rcv":
        return "print('FREQ: ', last_freq)"
    elif instr == "jgz":
        return "if {} > 0: i += {}-1".format(args[0], args[1])


registers = defaultdict(int)
last_freq = None
i = 0
instructions = puzzle_input()

while True:
    instr = parse(instructions[i])
    exec(instr)
    i += 1

