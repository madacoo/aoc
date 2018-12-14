from collections import defaultdict

class Program():
	def __init__(self, program_num):
		self.program_num = program_num
		self.registers = defaultdict(int)
		self.registers['p'] = program_num
		self.program_counter = 0
		self.message_queue = []
		self.messages_sent = 0
		
		with open('input.txt', 'r') as f:
		    self.instructions = f.strip().split('\n')
		
		
	
	def execute(self, instr, x, y):
		def evaluate(value):
			try:
				return int(value)
			except ValueError:
				return self.registers[value]
				
		if instr == 'set':
			self.registers[x] = evaluate(y)
			
		elif instr == 'add':
			self.registers[x] += evaluate(y)
			
		elif instr == 'mul':
			self.registers[x] *= evaluate(y)
			
		elif instr == 'mod':
			self.registers[x] %= evaluate(y)
			
		elif instr == 'jgz':
			if evaluate(x) > 0: self.program_counter += (evaluate(y)-1)
			
		elif instr == 'snd':
			self.partner.message_queue.append(evaluate(x))
			self.messages_sent += 1
			print(self.program_num, ' sent messages: ', self.messages_sent)
			
		elif instr == 'rcv':
			try:
				self.registers[x] = self.message_queue.pop(0)
			except IndexError:
				self.program_counter -= 1
			
	def step(self):
		try:
			instruction = self.instructions[self.program_counter]
		except IndexError:
			print('no instruction at ', 
				  self.program_counter,
				  ' for ',
				  self.program_num)
				  
		try:
			instr, x, y = instruction.split(' ')
		except ValueError:
			instr, x = instruction.split(' ')
			y = None
			
		self.execute(instr, x, y)
		self.program_counter += 1
		
				
program_0 = Program(0)
program_1 = Program(1)
program_0.partner = program_1
program_1.partner = program_0

while True:
	program_0.step()
	program_1.step()
