#!/usr/bin/python3

from intcode import Computer

with open('input', 'r') as f:
    opcodes = [int(s) for s in f.read().strip().split(',')]

def tilex(t):
    for row in screen:
        for x, tile in enumerate(row):
            if tile == t: 
                return x
    return 0

# part one
cpu = Computer(opcodes[:])
screen = [[0]*50 for _ in range(30)]
outs = []

while not cpu.halted:
    out = cpu.step()
    if out != None: outs.append(out)
    if len(outs) == 3:
        x, y, tile_id = outs
        if x == None: break
        screen[y][x] = tile_id
        outs = []

print(sum([row.count(2) for row in screen]))



# part two
opcodes[0] = 2
cpu = Computer(opcodes[:])
screen = [[0]*50 for _ in range(30)]
score = 0

while not cpu.halted:
    out = cpu.step()
    if out != None: outs.append(out)
    if len(outs) == 3:
        x, y, tile_id = outs
        if x == None: break
        if x == -1 and y == 0:
            score = tile_id
        else:
            screen[y][x] = tile_id
        outs = []
    if tilex(3) < tilex(4):
        cpu.input = 1
    elif tilex(3) > tilex(4):
        cpu.input = -1
    else:
        cpu.input = 0

print(score)
