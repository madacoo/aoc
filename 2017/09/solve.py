import re

def puzzle_input():
    with open("input.txt", "r") as f:
        return f.read().strip()


def solve(s):
    total = value = 0

    s = re.sub('!.', '', s) # remove escaped characters

    garbage_count = sum([len(garbage)-2 
                         for garbage in re.findall('<.*?>', s)])

    s = re.sub('<.*?>', '', s) # remove garbage

    for c in s:
        # parentheses parsing
        if c == '{':
            value += 1
        elif c == '}':
            total += value
            value -= 1
        
    return total, garbage_count


print(solve(puzzle_input()))
