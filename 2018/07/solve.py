from collections import defaultdict


def read_input():
    edges = defaultdict(list)
    with open('input') as f:
        for line in f:
            words = line.split()
            edges[words[1]].append(words[7])
    return edges


def has_dependency(node, edges, done):
    for parent, children in edges.items():
        if parent in done: continue
        if node in children: return True
    return False


def next_step(candidates, edges, order):
    return sorted([n for n in candidates
                   if not has_dependency(n, edges, order)])[0]
    

def solve1(edges):
    order = ''

    candidates = set()
    for parent, children in edges.items():
        candidates.add(parent)
        for child in children: candidates.add(child)

    while candidates:
        order += next_step(candidates, edges, order)
        candidates.remove(order[-1])

    return order



if __name__ == '__main__':
    edges = read_input()
    print(solve1(edges))

