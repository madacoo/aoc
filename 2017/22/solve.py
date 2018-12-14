from collections import defaultdict


def puzzle_input():
    "Return a list of infected coordinates."
    infected = []
    with open('input.txt', 'r') as f:
        rows = f.read().strip().split('\n')
        for y, row in enumerate(reversed(rows)):
            for x, char in enumerate(row):
                if char == '#':
                    infected.append((x, y))
    return infected


infected = puzzle_input()

# part 1
pos = (12, 12)
heading = (0, 1)
infection_count = 0

for burst in range(10000):
    if pos in infected:
        heading = heading[1], -heading[0] # turn right
        infected.remove(pos)
    else:
        heading = -heading[1], heading[0] # turn left
        infected.append(pos)
        infection_count += 1
    pos = pos[0] + heading[0], pos[1] + heading[1]

print(infection_count)


# part 2

# 0: clean; 1: weakened; 2: infected; 3: flagged
infected_d = defaultdict(int)
for i in puzzle_input(): infected_d[i] = 2


pos = (12, 12)
heading = (0, 1)
infection_count = 0

for burst in range(10000000):
    if infected_d[pos] == 0: # clean
        heading = -heading[1], heading[0] # turn left
    elif infected_d[pos] == 1: # weakened:
        infection_count += 1
    elif infected_d[pos] == 2: # infected
        heading = heading[1], -heading[0] # turn right
    elif infected_d[pos] == 3: # flagged
        heading = -heading[0], -heading[1] # reverse

    infected_d[pos] = (infected_d[pos] + 1) % 4
    pos = pos[0] + heading[0], pos[1] + heading[1]

print(infection_count)
