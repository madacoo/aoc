from collections import defaultdict
from math import ceil, floor


def ore(fuel):
    surplus = defaultdict(int)
    total = 0
    quantity, ingredients = reactions['FUEL']
    ingredients = list(map(lambda t: (fuel * t[0], t[1]), ingredients))
    while ingredients:
        n, chem = ingredients.pop(0)

        if chem == 'ORE':
            total += n
            continue

        if n < surplus[chem]:
            surplus[chem] = abs(n - surplus[chem])
            continue
        else:
            n -= surplus[chem]
            surplus[chem] = 0

        base_amount, chems = reactions[chem]
        batches = ceil(n / base_amount)
        surplus[chem] += base_amount * batches - n

        ingredients += [(q * batches, chem) for q, chem in chems]

    return total


reactions = dict()

with open('input', 'r') as f:
    for line in f:
        chems, out = line.strip().split(' => ')
        quantity, out = out.split(' ')
        chems.split(', ')
        ingredients = [tuple(chem.split(' ')) for chem in chems.split(', ')]
        ingredients = list(map(lambda t: (int(t[0]), t[1]), ingredients))
        reactions[out] = (int(quantity), ingredients)



# part one
print(ore(1))

# part two
lo, hi = 1, 1e12
while hi - lo >= 2:
    half = lo + (hi - lo) // 2
    total = ore(half)
    if total > 1e12:
        hi = half
    elif total <= 1e12:
        lo = half
    else:
        break
print(int(half))
