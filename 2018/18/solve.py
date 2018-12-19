

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
    trees = 0
    lumber = 0
    for k, acre in area.items():
        if acre == '|':
            trees += 1
        elif acre == '#':
            lumber += 1
    return trees, lumber


def print_area(area):
    print()
    for y in range(50):
        for x in range(50):
            acre = area[(x, y)]
            print(acre, end='')
        print()


area = read_input()
for minute in range(10):
    area = tick(area)
trees, lumber = count(area)
print(trees*lumber)
