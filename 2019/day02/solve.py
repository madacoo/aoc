#!/usr/bin/python3

from intcode import Computer

# part 1
with open('input') as f:
    opcodes = [int(n) for n in f.read().strip().split(',')]

opcodes[1] = 12
opcodes[2] = 2
cpu = Computer(list(opcodes))
cpu.run()
print(cpu.opcodes[0])

# part 2
def test(noun, verb, opcodes):
    opcodes[1] = noun
    opcodes[2] = verb
    cpu = Computer(list(opcodes))
    cpu.run()
    return cpu.opcodes[0]

for noun in range(100):
    for verb in range(100):
        if test(noun, verb, opcodes) == 19690720:
            print(100 * noun + verb)
            break
    else:
        continue
    break




