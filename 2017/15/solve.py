def gen(f, x, m=1):
    while True:
        x = (x * f) % 2147483647
        if x % m == 0: yield x

def solve1():
    gen_a = gen(16807, 703) # Generator A starts with 703
    gen_b = gen(48271, 516) # Generator B starts with 516

    count = 0
    for _ in range(40000000):
        a, b = next(gen_a), next(gen_b)
        if bin(a)[-16:] == bin(b)[-16:]: count += 1
    print(count)

def solve2():
    gen_a = gen(16807, 703, 4) # Generator A starts with 703, and looks for multiples of 4
    gen_b = gen(48271, 516, 8) # Generator B starts with 516, and looks for multiples of 8

    count = 0
    for _ in range(5000000):
        a, b = next(gen_a), next(gen_b)
        if bin(a)[-16:] == bin(b)[-16:]: count += 1
    print(count)

solve2()
