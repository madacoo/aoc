
def new_recipes(scores, i, j):
    """ Given a list of ints scores and indices i, j append
        the digits of i+j as ints to scores.
    """
    for d in str(scores[i] + scores[j]):
        scores.append(int(d))
    

def move_elf(i, scores):
    """ Given an index i and a list scores return the new elf index. """
    return (i + 1 + scores[i]) % len(scores)


def solve1(n):
    """ What are the scores of the ten recipes immediately after n recipes? """
    scores = [3, 7]
    elf_i, elf_j = 0, 1
    while len(scores) < n+10:
        new_recipes(scores, elf_i, elf_j)
        elf_i = move_elf(elf_i, scores)
        elf_j = move_elf(elf_j, scores)
    return ''.join([str(x) for x in scores[n:n+10]])


def solve2(seq):
    """ How many recipes appear on the scoreboard to the left
        of the score sequence in your puzzle input?
    """
    # We don't know how many scores we need to find but checking
    # if the sequence is in the scores each time we make new recipes
    # takes way too long.
    # So make n recipes, check and if not yet done, double n and try again.
    seq = str(seq)
    n = 10
    scores = [3, 7]
    elf_i, elf_j = 0, 1
    while True:
        for _ in range(n):
            new_recipes(scores, elf_i, elf_j)
            elf_i = move_elf(elf_i, scores)
            elf_j = move_elf(elf_j, scores)
        s = ''.join([str(x) for x in scores])
        if seq in s:
            return len(s[0:s.index(seq)])
        else:
            n *= 2
        

if __name__ == '__main__':
    n = 894501
    print(solve1(n))
    print(solve2(n))
