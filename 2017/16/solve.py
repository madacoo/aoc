
def puzzle_input():
    def parse(instruction):
        func_dict = { "x": "exchange",
                      "s": "spin",
                      "p": "partner" }
        f = func_dict[instruction[0]]
        args = instruction[1:].split("/")
        args = [a if a.isdigit() else "'{}'".format(a)
                for a in args]
        return "{}(programs, {})".format(f, ",".join(args))
        
    with open("input.txt", "r") as f:
        return list(map(parse, f.read().strip().split(",")))


def spin(L, offset):
    while offset:
        L.insert(0, L.pop())
        offset -= 1


def exchange(L, i, j):
    L[i], L[j] = L[j], L[i]


def partner(L, a, b):
    i, j = L.index(a), L.index(b)
    exchange(L, i, j)


def solve(instructions):
    programs = list("abcdefghijklmnop")
    dance(programs, instructions)
    return "".join(programs)

def dance(programs, instructions):
    for move in instructions:
        exec(move)

def solve2(instructions):
    programs = list("abcdefghijklmnop")
    results = []
    i = 0
    try:
        while True:
            s = "".join(programs)
            if s in results:
                break
            results.append(s)
            dance(programs, instructions)
            i += 1
    except KeyboardInterrupt:
        pass
    return "".join(results[1000000000 % i])

instructions = puzzle_input()
print(solve(instructions))
print(solve2(instructions))
