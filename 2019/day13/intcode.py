from collections import defaultdict

class Computer:
  def __init__(self, opcodes=[]):
    self.memory = defaultdict(int)
    for i, val in enumerate(opcodes):
      self.memory[i] = val
    self.pc = 0
    self.relbase = 0
    self.halted = False
    self.input = 0

  def decode(self, instruction):
    opcode = instruction % 100
    instruction //= 100
    modes = []
    for _ in range(3):
      modes.append(instruction % 10)
      instruction //= 10
    return opcode, modes


  def receive_input(self, value):
    self.inputs.append(value)


  def read(self, mode):
    self.pc += 1
    if mode == 0: # position
      return self.memory[self.memory[self.pc]]
    elif mode == 1: # immediate
      return self.memory[self.pc]
    elif mode == 2: # relative
      return self.memory[self.memory[self.pc] + self.relbase]


  def store(self, mode, value):
    self.pc += 1
    if mode == 0: # position
      self.memory[self.memory[self.pc]] = value
    elif mode == 1: # immediate
      raise ValueError
    elif mode == 2: # relative
      self.memory[self.memory[self.pc] + self.relbase] = value


  def step(self):
    opcode, modes = self.decode(self.memory[self.pc])

    # add
    if opcode == 1:
      self.store(modes[2], self.read(modes[0]) + self.read(modes[1]))

    # multiply
    elif opcode == 2:
      self.store(modes[2], self.read(modes[0]) * self.read(modes[1]))

    # input
    elif opcode == 3:
      self.store(modes[0], self.input)

    # output
    elif opcode == 4:
      out = self.read(modes[0])
      self.pc += 1
      return out

    # jump if not zero
    elif opcode == 5:
      first, second = self.read(modes[0]), self.read(modes[1])
      if first != 0:
        self.pc = second
        return

    # jump if zero
    elif opcode == 6:
      first, second = self.read(modes[0]), self.read(modes[1])
      if first == 0:
        self.pc = second
        return

    # less than
    elif opcode == 7:
      first, second = self.read(modes[0]), self.read(modes[1])
      if first < second:
        self.store(modes[2], 1)
      else:
        self.store(modes[2], 0)
    
    # equals
    elif opcode == 8:
      first, second = self.read(modes[0]), self.read(modes[1])
      if first == second:
        self.store(modes[2], 1)
      else:
        self.store(modes[2], 0)

    # add to relative base
    elif opcode == 9:
      self.relbase += self.read(modes[0])
    
    # halt
    elif opcode == 99:
      self.halted = True
      return

    else:
      raise NotImplementedError
    
    self.pc += 1

