# the coordinates of a hex grid can be treated as three dimensional
# https://www.redblobgames.com/grids/hexagons/

cord_dict = { "n":  (0, 1, -1), 
              "ne": (1, 0, -1),
			  "se": (1, -1, 0),
			  "s":  (0, -1, 1),
			  "sw": (-1, 0, 1),
			  "nw": (-1, 1, 0) }


def puzzle_input():
	"Return puzzle input as list of strings describing steps taken by child."
	with open("input.txt", "r") as f:
		return f.read().strip().split(',')


def move(a, b):
	return (a[0] + b[0], 
			a[1] + b[1], 
			a[2] + b[2])


def distance(a, b):
	dx = a[0] + b[0]
	dy = a[1] + b[1]
	dz = a[2] + b[2]
	return (abs(dx) + abs(dy) + abs(dz)) / 2


def solve(steps):
	position = (0,0,0)
	for step in steps:
		position = move(position, cord_dict[step])
	return distance((0,0,0), position)


def solve2(steps):
	position = (0,0,0)
	max_distance = 0
	for step in steps:
		position = move(position, cord_dict[step])
		max_distance = max(max_distance, distance((0, 0, 0), position))
	return max_distance


print(solve(puzzle_input()))
print(solve2(puzzle_input()))
