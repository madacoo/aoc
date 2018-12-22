from device import Device

def read_input():
    with open('input') as f:
        rb = int(f.readline().strip().split()[1])
        program = []
        for line in f:
            instr, *args = line.strip().split()
            args = [int(a) for a in args]
            program.append((instr, args))
        return rb, program


def solve(d):
    while True: 
        if d.ip < 0 or d.ip >= len(program): break
        istr, args = program[d.ip]
        d.regs[d.rb] = d.ip
        d.instrs[i](*args)
        d.ip = d.regs[d.rb]
        d.ip += 1
    return d.regs[0]

if __name__ == '__main__':
    rb, program = read_input()
    d = Device(rb)
    print(solve(d))
    # it seems for part two we need to reverse engineer the program...

