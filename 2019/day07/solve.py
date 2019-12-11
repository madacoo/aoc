#!/usr/bin/python3

from itertools import permutations
from intcode import Computer


with open('input', 'r') as f:
    opcodes = [int(s) for s in f.read().strip().split(',')]

def amplification(phase_setting, opcodes):
    vals = [0]
    for setting in phase_setting:
        def inp():
            yield setting
            yield vals[-1]
        def out(x):
            vals.append(x)
        gen = inp()
        cpu = Computer(opcodes.copy(), inp=lambda: next(gen), out=out)
        cpu.run()
    return vals[-1]



"""
# part 1
signal = 0
for phase_setting in permutations(range(5)):
    signal = max(signal, amplification(phase_setting, opcodes))
print(signal)
"""

# part 2
max_signal = 0
for phase_setting in permutations(range(5, 10)):

    # create amplifiers
    amplifiers = []
    for amp in range(5):
        cpu = Computer(opcodes.copy())
        cpu.receive(phase_setting[amp])
        amplifiers.append(cpu)
    amplifiers[0].receive(0)

    i = 0
    while not all([amp.halted for amp in amplifiers]):
        out = amplifiers[i].step()
        if type(out) == int:
            i = (i+1)%5
            amplifiers[i].receive(out)
        elif amplifiers[i].halted:
            i = (i+1)%5

    max_signal = max(max_signal, amplifiers[0].inputs[0])
print(max_signal)


