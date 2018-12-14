

def read_input():
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

def solve1(box_ids):
    """ What is the checksum for your list of box IDs? """
    two_count = three_count = 0
    for bid in box_ids:
        two, three = count(bid)
        if two: two_count += 1
        if three: three_count += 1
    return two_count * three_count


def solve2(box_ids):
    """ What letters are common between the two correct box IDs? """
    for bid1 in box_ids:
        for bid2 in box_ids:
            if bid1 == bid2: pass
            d = difference(bid1, bid2)
            if len(d) == 1:
                return bid1[0:d[0]] + bid1[d[0]+1:]


if __name__ == "__main__":
    box_ids = read_input()
    print(solve1(box_ids))
    print(solve2(box_ids))



