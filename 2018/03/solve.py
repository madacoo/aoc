from collections import namedtuple, defaultdict


Rect = namedtuple("Rect", "box_id, x, y, w, h")


def read_input():
    """ Return a list of Rects. """
    rects = []
    with open('input') as f:
        for line in f:
            box_id, rect = line.strip().split(' @ ')
            box_id = box_id.replace('#', '')
            coords, dimensions = rect.split(': ')
            x, y = [int(s) for s in coords.split(',')]
            w, h = [int(s) for s in dimensions.split('x')]
            rects.append(Rect(box_id, x, y, w, h))
    return rects


def count_overlaps(rects):
    """ Return a dictionary with tuples as keys describing x, y coordinates
        the value of which is a count of how many Rects cover that coordinate.
    """
    coords = defaultdict(int)
    for r in rects:
        for x in range(r.x, r.x + r.w):
            for y in range(r.y, r.y + r.h):
                coords[(x, y)] += 1
    return coords


def overlaps(r, coords):
    """ Return True if Rect r overlaps with another Rect
        else return False.
    """
    for x in range(r.x, r.x + r.w):
        for y in range(r.y, r.y + r.h):
            if coords[(x, y)] > 1:
                return True
    return False


def solve1(rects):
    """ How many square inches of fabric are within two or more claims? """
    return len([v for k, v in count_overlaps(rects).items() if v > 1])
        

def solve2(rects):
    """ What is the ID of the only claim that doesn't overlap? """
    coords = count_overlaps(rects)
    return [r.box_id for r in rects if not overlaps(r, coords)][0]


if __name__ == "__main__":
    rects = read_input()
    print(solve1(rects))
    print(solve2(rects))

