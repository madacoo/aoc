
def puzzle_input():
    with open("input.txt", "r") as f:
        return f.read().strip().split('\n')

def valid(phrase):
    words = phrase.split()
    return len(words) == len(set(words))

def valid2(phrase):
    words = [''.join(sorted(w)) for w in phrase.split()]
    return len(words) == len(set(words))

def test():

    assert valid("aa bb cc dd ee") == True
    assert valid("aa bb cc dd aa") == False
    assert valid("aa bb cc dd aaa") == True

    assert valid2("adcde fghij") == True
    assert valid2("abcde xyz ecdab") == False
    assert valid2("a ab abc abd abf abj") == True
    assert valid2("iiii oiii ooii oooi oooo") == True
    assert valid2("oiii ioii iioi iiio") == False

    return True

def solve():
    passphrases = puzzle_input()
    print(len([p for p in passphrases if valid(p)]))
    print(len([p for p in passphrases if valid2(p)]))

if test():
    solve()
