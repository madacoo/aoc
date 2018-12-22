from collections import defaultdict

class Device:
    def __init__(self, rb):
        self.regs = defaultdict(int)
        self.instrs = { 'addr': self.addr, 'addi': self.addi, 
                        'mulr': self.mulr, 'muli': self.muli,
                        'banr': self.banr, 'bani': self.bani,
                        'borr': self.borr, 'bori': self.bori,
                        'setr': self.setr, 'seti': self.seti,
                        'gtir': self.gtir, 'gtri': self.gtri,
                        'gtrr': self.gtrr, 'eqir': self.eqri,
                        'eqri': self.eqri, 'eqrr': self.eqrr }
        self.ip =  0 # instruction pointer
        self.rb = rb # register than intruction pointer is bound to



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

