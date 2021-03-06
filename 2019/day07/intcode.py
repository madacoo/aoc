

class Computer:
    def __init__(self, opcodes=[]):
        self.pc = 0
        self.opcodes = opcodes # list of ints
        self.inputs = []
        self.halted = False


    def receive(self, value):
        self.inputs.append(value)


    def next_parameter(self, mode):
        self.pc += 1
        if mode == 0: return self.opcodes[self.opcodes[self.pc]]
        if mode == 1: return self.opcodes[self.pc]


    def parse_opcode(self, opcode):
        instr = opcode % 100
        mode_one = (opcode % 1000) // 100
        mode_two = (opcode % 10000) // 1000
        mode_three = (opcode % 100000) // 10000
        return instr, mode_one, mode_two, mode_three


    def step(self):
        instr, *modes = self.parse_opcode(self.opcodes[self.pc])

        # add
        if instr == 1:
            param_one = self.next_parameter(modes[0])
            param_two = self.next_parameter(modes[1])
            self.opcodes[self.opcodes[self.pc+1]] = param_one + param_two
            self.pc += 2

        # mul
        elif instr == 2:
            param_one = self.next_parameter(modes[0])
            param_two = self.next_parameter(modes[1])
            self.opcodes[self.opcodes[self.pc+1]] = param_one * param_two
            self.pc += 2

        # inp
        elif instr == 3:
            try:
                inp = self.inputs.pop(0)
            except IndexError:
                print('waiting for input')
                return
            self.opcodes[self.opcodes[self.pc+1]] = inp
            self.pc += 2

        # out
        elif instr == 4:
            out = self.opcodes[self.opcodes[self.pc+1]]
            self.pc += 2
            return out
        
        # jump-if-true
        elif instr == 5:
            param_one = self.next_parameter(modes[0])
            param_two = self.next_parameter(modes[1])
            self.pc += 1
            if param_one != 0:
                self.pc = param_two

        # jump-if-false
        elif instr == 6:
            param_one = self.next_parameter(modes[0])
            param_two = self.next_parameter(modes[1])
            self.pc += 1
            if param_one == 0:
                self.pc = param_two

        # less than
        elif instr == 7:
            param_one = self.next_parameter(modes[0])
            param_two = self.next_parameter(modes[1])
            self.opcodes[self.opcodes[self.pc+1]] = 0
            if param_one < param_two:
                self.opcodes[self.opcodes[self.pc+1]] = 1
            self.pc += 2

        # equals
        elif instr == 8:
            param_one = self.next_parameter(modes[0])
            param_two = self.next_parameter(modes[1])
            self.opcodes[self.opcodes[self.pc+1]] = 0
            if param_one == param_two:
                self.opcodes[self.opcodes[self.pc+1]] = 1
            self.pc += 2

        # halt
        elif instr == 99:
            self.halted = True
            # self.pc += 1 // would happen if not halted

        # unimplemented
        else:
            raise NotImplementedError

