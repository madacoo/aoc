from collections import defaultdict

tape = defaultdict(int)
state_dict = { "A": { 0: (1,  1, "B"),
                      1: (0, -1, "B") },
                      
               "B": { 0: (1, -1, "C"),
                      1: (0,  1, "E") },
               
               "C": { 0: (1,  1, "E"),
                      1: (0, -1, "D") },
                      
               "D": { 0: (1, -1, "A"),
                      1: (1, -1, "A") },
                      
               "E": { 0: (0,  1, "A"),
                      1: (0,  1, "F") }, 
                      
               "F": { 0: (1,  1, "E"),
                      1: (1,  1, "A") }
              }
    

state = "A" # start state
cursor = 0
ticks = 12683008

# run turing machine
for _ in range(ticks):
    value, direction, state = state_dict[state][tape[cursor]]
    tape[cursor] = value
    cursor += direction

# perform check
diagnostic_checksum = 0
for key, value in tape.items():
    if value == 1: diagnostic_checksum += 1
print(diagnostic_checksum)
