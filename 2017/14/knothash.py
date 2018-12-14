from functools import reduce

def lengths(s):
	"Take a string and return the lengths used to hash it."
	return [ord(c) for c in list(s)] + [17, 31, 73, 47, 23]


def cycle_list(L, offset):
    result = []
    length = len(L)
    for i in range(length):
        index = (i + offset) % length
        result.append(L[index])
    return result


def reverse_sublist(L, i, j):
    return list(reversed(L[i:j])) + L[j:]


def dense_hash(L):
    blocks = [L[i:i+16] for i in range(0, 256, 16)]
    return [reduce(lambda a, b: a ^ b, block) for block in blocks]


def knot_hash(L, lengths):
    for length in lengths:
        L = cycle_list(L, knot_hash.pos)
        L = reverse_sublist(L, 0, length)
        L = cycle_list(L, -knot_hash.pos)
        knot_hash.pos += (length + knot_hash.skip_size)
        knot_hash.skip_size += 1
    return L


def hash(s, size=256):
	"Take a string s and return its hexadecimal knot hash."
	# as described by challenge of day 10
	lens = lengths(s)
	L = list(range(size))

	knot_hash.skip_size = 0
	knot_hash.pos = 0
	for _ in range(64):
		L = knot_hash(L, lens)

	return "".join([hex(i)[2:].zfill(2) for i in dense_hash(L)])
