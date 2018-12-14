def puzzle_input():
    return 356

def solve(step):
    spinlock = [0]
    pos = 0
    for x in range(1,2018):
        i = (pos + step) % len(spinlock)
        spinlock.insert(i, x)
        pos = i+1
    return spinlock[pos]

def solve2(step):
    result = None
    spinlock_length = 1
    pos = 0
    for x in range(1,50000001):
        i = (pos + step) % spinlock_length
        if i == 0:
            result = x
        spinlock_length += 1
        pos = i+1
    return result

step = puzzle_input()
print(solve(step))
print(solve2(step))


