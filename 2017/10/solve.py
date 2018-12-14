from functools import reduce


def puzzle_input():
    "Return puzzle input as list of integers."
    with open("input.txt", "r") as f:
        return [int(i) for i in f.read().strip().split(",")]


def puzzle_input2():
    "Return puzzle input as list of ASCII codes."
    with open("input.txt", "r") as f:
        return [ord(c) for c in list(f.read().strip())]


def cycle_list(L, offset):
    result = []
    length = len(L)
    for i in range(length):
        index = (i + offset) % length
        result.append(L[index])
    return result


def reverse_sublist(L, i, j):
    return list(reversed(L[i:j])) + L[j:]


def knot_hash(L, lengths):
    for length in lengths:
        L = cycle_list(L, knot_hash.pos)
        L = reverse_sublist(L, 0, length)
        L = cycle_list(L, -knot_hash.pos)
        knot_hash.pos += (length + knot_hash.skip_size)
        knot_hash.skip_size += 1
    return L


def dense_hash(L):
    blocks = [L[i:i+16] for i in range(0, 256, 16)]
    return [reduce(lambda a, b: a ^ b, block) for block in blocks] # how could this be done without reduce?


def solve(lengths, size=256):
    L = list(range(size))
    knot_hash.skip_size = 0
    knot_hash.pos = 0
    L = knot_hash(L, lengths)
    return L[0] * L[1]


def solve2(lengths, size=256):
    lengths += [17, 31, 73, 47, 23]
    L = list(range(size))

    knot_hash.skip_size = 0
    knot_hash.pos = 0

    for _ in range(64):
        L = knot_hash(L, lengths)

    return "".join([hex(i)[2:].zfill(2) for i in dense_hash(L)])
    

print(solve(puzzle_input()))
print(solve2(puzzle_input2()))
