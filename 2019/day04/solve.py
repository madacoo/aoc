
# part 1 and 2

def has_lonely_double(s):
    checked = []
    for a, b, c in zip(s, s[1:], s[2:]+'_'):
        if not a in checked and a == b and a != c:
            return True
        checked.append(a)
    return False

def has_double(s):
    for a, b in zip(s, s[1:]):
        if a == b:
            return True
    return False

count_one = count_two = 0
for n in range(146810, 612565):
    if ''.join(sorted(str(n))) == str(n) and has_double(str(n)):
        count_one += 1
    if ''.join(sorted(str(n))) == str(n) and has_lonely_double(str(n)):
        count_two += 1
print(count_one, count_two)
