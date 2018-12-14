from itertools import combinations

def puzzle_input():
    "Return puzzle input as a two dimensional list of ints."
    result = []
    with open("input.txt", "r") as f:
        for line in f:
            result.append([int(i) for i in line.split("\t")])
    return result


def solve(spreadsheet):
    checksum = 0
    for row in spreadsheet:
        diff = max(row) - min(row)
        checksum += diff
    return checksum


def solve2(spreadsheet):
    def find_evenly_divisible(row):
        for a,b in combinations(row, 2):
            if max(a, b) % min(a, b) == 0:
                return max(a, b), min(a, b)
    checksum = 0
    for row in spreadsheet:
        a, b = find_evenly_divisible(row)
        checksum += int(a / b)
    return checksum


spreadsheet = puzzle_input()
print(solve(spreadsheet))
print(solve2(spreadsheet))
        
        
