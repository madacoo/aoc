from collections import namedtuple


Track = dict()
Vector = namedtuple('Vector', 'x y')

def vadd(va, vb):
    return Vector(va.x + vb.x, va.y + vb.y)


class Kart:
    def __init__(self, position, direction):
        self.pos = position
        self.cross = 0
        self.alive = True

        if direction == '>':
            self.dir = Vector(1, 0)
        elif direction == 'v':
            self.dir = Vector(0, 1)
        elif direction == '<':
            self.dir = Vector(-1, 0)
        elif direction == '^':
            self.dir = Vector(0, -1)
        else:
            raise ValueError

    
    def __repr__(self):
        return "kart at ({},{}) heading ({},{})".format(self.pos.x, self.pos.y,
                                                        self.dir.x, self.dir.y)



    def collides(self, karts):
        for k in karts:
            if k == self or not k.alive: continue
            if k.pos == self.pos:
                k.alive = False
                self.alive = False
                return True
        return False


    def move(self):
        self.pos = vadd(self.pos, self.dir)

        part = Track[self.pos]

        if part == '\\':
            if self.dir.x == 0:
                self.turn('left')
            else:
                self.turn('right')
        elif part == '/':
            if self.dir.x == 0:
                self.turn('right')
            else:
                self.turn('left')
        elif part == '+':
            if self.cross == 0:
                self.turn('left')
            elif self.cross == 2:
                self.turn('right')
            self.cross = (self.cross + 1) % 3


    def turn(self, direction='right'):
        d = 1
        if direction == 'left': d = -1
        new_dir = (self.dir.x + self.dir.y*1j) * (0 + d*1j)
        self.dir = Vector(int(new_dir.real), int(new_dir.imag))


def read_input():
    karts = []
    x = y = 0
    kart_shapes = '>v<^'
    track_beneath = '-|'
    with open('input') as f:
        for line in f:
            x = 0
            for c in line[:-1]:
                v = Vector(x, y)
                if c in kart_shapes:
                    karts.append(Kart(v, c))
                    Track[v] = track_beneath[kart_shapes.index(c)%2]
                else:
                    Track[v] = c
                x += 1
            y += 1
    return karts


def print_track(karts):
    grid = []
    for y in range(HEIGHT+1):
        row = []
        for x in range(WIDTH+1):
            row.append(Track[Vector(x, y)])
        grid.append(row)

    for k in karts:
        grid[k.pos.y][k.pos.x] = '*'

    for row in grid:
        print(''.join(row))


def solve():
    karts = read_input()
    first_blood = False
    while len([k for k in karts if k.alive]) > 1:
        karts = sorted(karts, key=lambda k: (k.pos.y, k.pos.x))
        #print_track(karts)
        for k in karts:
            if not k.alive: continue
            k.move()
            if k.collides(karts) and not first_blood:
                print(str(k.pos.x) + ',' + str(k.pos.y))
                first_blood = True
    k = [k for k in karts if k.alive][0]
    print(str(k.pos.x) + ',' + str(k.pos.y))


if __name__ == '__main__':
    solve()
