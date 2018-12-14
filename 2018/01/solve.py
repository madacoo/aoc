
def parse_input():
    with open('input') as f:
        return [int(line.strip()) for line in f]


def solve1(freq_changes):
    # What is the resulting frequency?
    return sum(freq_changes)


def solve2(freq_changes):
    # What is the first frequency your device reaches twice?
    current = 0
    freqs = set()
    freqs.add(current)
    while True:
        for f in freq_changes:
            current += f 
            if current in freqs:
                return current
            freqs.add(current)


if __name__ == '__main__':
    freq_changes = parse_input()
    print(solve1(freq_changes))
    print(solve2(freq_changes))

