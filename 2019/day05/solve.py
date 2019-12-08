from intcode import Computer

with open('input', 'r') as f:
    opcodes = [int(s) for s in f.read().strip().split(',')]

cpu = Computer(opcodes=opcodes, inp=lambda: int(input('Enter int: ')), out=print)

cpu.run()

