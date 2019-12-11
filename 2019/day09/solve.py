from intcode import Computer

with open('input') as f:
  opcodes = [int(s) for s in f.read().strip().split(',')]

def run(value):
  output = []
  cpu = Computer(opcodes)
  cpu.receive_input(value)
  while not cpu.halted:
    out = cpu.step()
    if out != None:
      output.append(out)
  return output

# part 1
print(run(1))

# part 2
print(run(2))
