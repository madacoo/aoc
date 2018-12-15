from collections import namedtuple

Vector = namedtuple('Vector', 'x y')

def vadd(va, vb):
    return Vector(va.x + vb.x,
                  va.y + vb.y)


class Kart:
    def __init__(self, pos, d, track):
        self.track = track
        self.pos = pos
        self.dir = d


    def collides(self, karts):
        for k in karts:
            if k == self: continue
            if k.pos == self.pos:
                return True
        return False


    def move(self):
        self.pos = vadd(self.pos, self.d)
        if track[self.pos] in '\/+':
            self.turn()

    def turn(self, d=1):
        # 1 = left, -1 = right
        a = self.dir.x + (self.dir.y)j
        b = 0 + d*1j
        c = a * b
        self.pos = Vector(int(c.real), int(c.imag))


def read_input():
    track = []
    kart_poss = []


def solve():
    karts = read_input()
    for k in karts:
        k.move()
        if k.collides(karts):
            return k.pos
