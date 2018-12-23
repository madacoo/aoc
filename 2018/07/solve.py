from collections import defaultdict

class Worker:
    def __init__(self):
        self.step = None
        self.seconds = -1

    def start_work(self, step):
        if not step: return
        self.step = step
        self.seconds = seconds(step)

    def update(self):
        self.seconds -= 1
        if self.seconds == 0:
            step = self.step
            self.step = None
            return step
        return ''


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
    try:
        return sorted([n for n in candidates
                       if not has_dependency(n, edges, order)])[0]
    except IndexError:
        return False


def seconds(steps): return ord(steps)-4
    

def steps(edges):
    candidates = set()
    for parent, children in edges.items():
        candidates.add(parent)
        for child in children: candidates.add(child)
    return candidates



def solve1(edges):
    order = ''

    candidates = steps(edges)
    while candidates:
        order += next_step(candidates, edges, order)
        candidates.remove(order[-1])

    return order


def solve2(edges):
    second = -1
    done = ''
    workers = [Worker() for _ in range(5)]

    candidates = steps(edges)
    while candidates or [w for w in workers if w.step]:
        for w in workers:
            done += w.update()
            if not w.step:
                w.start_work(next_step(candidates, edges, done))
                if w.step: candidates.remove(w.step)
        second += 1
    return second


if __name__ == '__main__':
    edges = read_input()
    print(solve1(edges))
    print(solve2(edges))

