

class Computer:
    def __init__(self, opcodes=[]):
        self.pc = 0
        self.opcodes = opcodes # list of ints

    def step(self):
        instr = self.opcodes[self.pc]

        if instr == 1:
            # add
            self.opcodes[self.opcodes[self.pc+3]] = self.opcodes[self.opcodes[self.pc+1]] + self.opcodes[self.opcodes[self.pc+2]] 
            self.pc += 4
        elif instr == 2:
            # mul
            self.opcodes[self.opcodes[self.pc+3]] = self.opcodes[self.opcodes[self.pc+1]] * self.opcodes[self.opcodes[self.pc+2]] 
            self.pc += 4
        elif instr == 99:
            # halt
            return False
            # self.pc += 1 // would happen if not halted
        else:
            raise NotImplementedError

        return True

    def run(self, verbose=False):
        if verbose: print(self.pc, self.opcodes)
        while self.step():
            if verbose: print(self.pc, self.opcodes)



