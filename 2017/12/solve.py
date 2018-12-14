def puzzle_input():
	pipes = {}
	with open("input.txt", "r") as f:
		for line in f.readlines():
			ID, programs = line.strip().split(" <-> ")
			pipes[ID] = programs.split(", ")
	return pipes


def trace_pipes(pipes, ID="0", seen=[]):
	for child in pipes[ID]:
		if not child in seen:
			seen.append(child)
			trace_pipes(pipes, child, seen)
	return seen


def solve(pipes):
	group = trace_pipes(pipes, "0", [])
	return len(group)


def solve2(pipes):
	groups = set()
	for ID in range(2000):
		group = trace_pipes(pipes, str(ID), [])
		groups.add(",".join(sorted(group))) # hashable string
	return len(groups)


pipes = puzzle_input()
print(solve(pipes))
print(solve2(pipes))


