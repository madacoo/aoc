from collections import defaultdict

class Device:
    def __init__(self):
        self.regs = defaultdict(int)
        self.instrs = [self.addr, self.addi, self.mulr, self.muli,
                       self.banr, self.bani, self.borr, self.bori,
                       self.setr, self.seti, self.gtir, self.gtri,
                       self.gtrr, self.eqir, self.eqri, self.eqrr]

    def addr(self, A, B, C):
        self.regs[C] = self.regs[A] + self.regs[B]

    def addi(self, A, b, C):
        self.regs[C] = self.regs[A] + b

    def mulr(self, A, B, C):
        self.regs[C] = self.regs[A] * self.regs[B]

    def muli(self, A, b, C):
        self.regs[C] = self.regs[A] * b

    def banr(self, A, B, C):
        self.regs[C] = self.regs[A] & self.regs[B]

    def bani(self, A, b, C):
        self.regs[C] = self.regs[A] & b

    def borr(self, A, B, C):
        self.regs[C] = self.regs[A] | self.regs[B]

    def bori(self, A, b, C):
        self.regs[C] = self.regs[A] | b

    def setr(self, A, _, C):
        self.regs[C] = self.regs[A]

    def seti(self, a, _, C):
        self.regs[C] = a

    def gtir(self, a, B, C):
        if a > self.regs[B]:
            self.regs[C] = 1 
        else:
            self.regs[C] = 0

    def gtri(self, A, b, C):
        if self.regs[A] > b:
            self.regs[C] = 1 
        else:
            self.regs[C] = 0

    def gtrr(self, A, B, C):
        if self.regs[A] > self.regs[B]:
            self.regs[C] = 1 
        else:
            self.regs[C] = 0

    def eqir(self, a, B, C):
        if a == self.regs[B]:
            self.regs[C] = 1 
        else:
            self.regs[C] = 0

    def eqri(self, A, b, C):
        if self.regs[A] == b:
            self.regs[C] = 1 
        else:
            self.regs[C] = 0

    def eqrr(self, A, B, C):
        if self.regs[A] == self.regs[B]: 
            self.regs[C] = 1 
        else:
            self.regs[C] = 0

    def set_registers(self, L):
        for i, n in enumerate(L):
            self.regs[i] = n

    def compare_registers(self, L):
        for i, n in enumerate(L):
            if self.regs[i] != n: return False
        return True


def read_input():
    with open('input') as f:
        section_a, section_b = f.read().split('\n\n\n')
    samples = section_a.split('\n\n')
    return samples, None


def parse_sample(s):
    before, instr, after = s.strip().split('\n')
    before = before.split(': ')[1]
    after = after.split(':  ')[1]
    before = [int(c) for c in before[1:-1].split(', ')]
    instr  = [int(c) for c in  instr.split(' ')]
    after  = [int(c) for c in  after[1:-1].split(', ')]
    return before, instr, after



d = Device()

samples, program = read_input()
total = 0
for s in samples:
    before, instr, after = parse_sample(s)
    count = 0
    for i in d.instrs:
        d.set_registers(before)
        i(*instr[1:])
        if d.compare_registers(after): count += 1
    if count >= 3: total += 1
print(total)

