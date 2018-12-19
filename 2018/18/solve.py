

def read_input():
    area = dict()
    with open('input') as f:
        for y, line in enumerate(f):
            for x, acre in enumerate(line.strip()):
                area[(x, y)] = acre
    return area



def count_adjacent_acres(x, y, area):
    trees = lumber = 0
    steps = (-1, 0, 1)
    for xd in steps:
        for yd in steps:
            if not xd and not yd: continue
            try:
                acre = area[(x+xd, y+yd)]
            except KeyError:
                continue
            if acre == '|':
                trees += 1
            elif acre == '#':
                lumber += 1
    return trees, lumber
            


def tick(area):
    new_area = dict()
    for y in range(50):
        for x in range(50):
            acre = area[(x, y)]
            trees, lumber = count_adjacent_acres(x, y, area)
            if acre == '.' and trees >= 3:
                acre = '|'
            elif acre == '|' and lumber >= 3:
                acre = '#'
            elif acre == '#' and (not trees or not lumber):
                acre = '.'
            new_area[(x, y)] = acre
    return new_area


def count(area):
    trees = lumber = 0
    for k, acre in area.items():
        if acre == '|': trees += 1
        elif acre == '#': lumber += 1
    return trees*lumber


def print_area(area):
    print()
    for y in range(50):
        for x in range(50):
            acre = area[(x, y)]
            print(acre, end='')
        print()


def solve1(n):
    area = read_input()
    for minute in range(n):
        area = tick(area)
    return count(area)


def solve2():
    tortoise  = read_input()
    hare = tick(read_input())
    tmin, hmin = 0, 1
    while True:
        tortoise = tick(tortoise)
        hare = tick(tick(hare))
        tmin += 1
        hmin += 2
        if count(tortoise) == count(hare):
            break
    return tmin + (1000000000-tmin) % (hmin-tmin)


if __name__ == '__main__':
    print(solve1(10))
    print(solve1(solve2()))
