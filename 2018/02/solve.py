

def parse_input():
    with open('input') as f:
        return [line.strip() for line in f]


def count(box_id):
    """ Return a tuple of booleans describing whether str box_id
        contains two or three of the same character.
    """
    twos, threes = False, False
    for c in set(box_id):
        if box_id.count(c) == 2: twos = True
        if box_id.count(c) == 3: threes = True
        if twos and threes: break
    return twos, threes


def difference(s1, s2):
    """ Return a list of indices where s1 and s2 have dissimilar characters."""
    # assume len(s1) == len(s2)
    results = []
    for i, chars in enumerate(zip(s1, s2)):
        c1, c2 = chars 
        if c1 != c2: results.append(i)
    return results

def solve1(inp):
    two_count = three_count = 0
    for box_id in inp:
        two, three = count(box_id)
        if two: two_count += 1
        if three: three_count += 1
    return two_count * three_count


def solve2(inp):
    for box_id1 in inp:
        for box_id2 in inp:
            if box_id1 == box_id2: pass
            d = difference(box_id1, box_id2)
            if len(d) == 1:
                return box_id1[0:d[0]] + box_id1[d[0]+1:]


if __name__ == "__main__":
    inp = parse_input()
    print(solve1(inp))
    print(solve2(inp))



