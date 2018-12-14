
def puzzle_input():
    "Read puzzle input from 'input.txt' and return as string."
    with open("input.txt") as f:
        return f.read().strip()

        
def match_next(digits):
    "Filter a string of digits to those that match the next digit."
    "string -> list of ints"
    # The string of digits is considered circular.
    # In Python iterable[-1] is the last element in an iterable.
    return [int(d) for i, d in enumerate(digits) 
                   if digits[i-1] == d]

                     
def match_halfway(digits):
    "Filter a string of digits to those that match"
    "the next digit halfway around the string."
    "string -> list of ints"
    # The string of digits is considered circular.
    n = len(digits)
    return [int(d) for i, d in enumerate(digits) 
                   if digits[int((i+n/2) % n)] == d]


def test1():
    assert sum(match_next("1122")) == 3
    assert sum(match_next("1111")) == 4
    assert sum(match_next("1234")) == 0
    assert sum(match_next("91212129")) == 9
    print("test1 pass")
    return True
    

def test2():
    assert sum(match_halfway("1212")) == 6
    assert sum(match_halfway("1221")) == 0
    assert sum(match_halfway("123425")) == 4
    assert sum(match_halfway("123123")) == 12
    assert sum(match_halfway("12131415")) == 4
    print("test2 pass")
    return True


digits = puzzle_input()

if test1():    
    print(sum(match_next(digits)))
    
if test2():
    print(sum(match_halfway(digits)))
