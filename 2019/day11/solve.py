#!/usr/bin/python3

from intcode import Computer

from collections import defaultdict

class Robot:
    def __init__(self, pos, opcodes):
        self.cpu = Computer(opcodes)
        self.pos = pos
        self.dir = (0, 1)

    def move(self):
        self.pos = self.pos[0]+self.dir[0], self.pos[1]+self.dir[1]

    def turn_right(self):
        self.dir = self.dir[1], -1*self.dir[0]

    def turn_left(self):
        self.dir = -1*self.dir[1], self.dir[0]

    def run(self):
        while not self.cpu.halted:
            out = self.cpu.step()
            if out != None:
                return out


with open('input', 'r') as f:
    opcodes = [int(s) for s in f.read().strip().split(',')]

# part one
panels = defaultdict(int)
rob = Robot((0, 0), opcodes)
painted = set()
while not rob.cpu.halted:
    rob.cpu.receive_input(panels[rob.pos])
    col = rob.run()
    panels[rob.pos] = col
    painted.add(rob.pos)
    direction = rob.run()
    rob.turn_left() if direction == 0 else rob.turn_right()
    rob.move()
print(len(painted))


# part two
panels = []
for y in range(6):
    panels.append([0]*43)
rob = Robot((0, 5), opcodes)
panels[rob.pos[1]][rob.pos[0]] = 1
while not rob.cpu.halted:
    rob.cpu.receive_input(panels[rob.pos[1]][rob.pos[0]])
    color = rob.run()
    if color in [0, 1]: panels[rob.pos[1]][rob.pos[0]] = color
    direction = rob.run()
    rob.turn_left() if direction == 0 else rob.turn_right()
    rob.move()
for row in reversed(panels):
    for col in row:
        print('#', end='') if col == 1 else print(' ', end='')
    print('\n', end='')

