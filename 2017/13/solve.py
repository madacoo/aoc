def puzzle_input():
	"Return puzzle input as list of tuples with integers describing depth and range."
	firewall = []
	with open("input.txt") as f:
		for line in f.readlines():
			d, r = line.split(": ")
			firewall.append((int(d), int(r)))
	return firewall


def solve(firewall):
	severity = 0
	for d, r in firewall: # depth, range
		if (d) % (2*r-2) == 0:
			severity += d*r
	return severity

def solve2(firewall):
	delay = 0
	while True:
		caught = False
		delay += 1
		for d, r in firewall: # depth, range
			if (d+delay) % (2*r-2) == 0:
				caught = True
				break
		if not caught:
			return delay


firewall = puzzle_input()
print(solve(firewall))
print(solve2(firewall))
