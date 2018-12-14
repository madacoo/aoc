
def puzzle_input():
    with open("input.txt", "r") as f:
        return list(map(int, f.read().strip().split("\t")))
        
def solve(banks):
    seen = []
    length = len(banks)
    while not banks in seen:
        seen.append(banks[:])
        blocks = max(banks)
        i = banks.index(blocks)
        banks[i] = 0
        while blocks:
            i += 1
            i = i % length
            banks[i] += 1
            blocks -= 1
    return len(seen), banks
        
def test():
    banks = [0, 2, 7, 0]
    assert solve(banks) == (5, [2, 4, 1, 2])
    assert solve([2, 4, 1, 2]) == (4, [2, 4, 1, 2])
    return True
    
if test():
    solution1, banks = solve(puzzle_input())
    solution2, _ = solve(banks)
    print(solution1, solution2)
    
