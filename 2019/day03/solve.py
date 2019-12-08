

def direction(s): return s[0]
def magnitude(s): return int(s[1:])
def manhattan(coords): return abs(coords[0]) + abs(coords[1])

def increment(coords, direction):
  if direction == 'R':
    return coords[0]+1, coords[1]
  if direction == 'D':
    return coords[0], coords[1]-1
  if direction == 'U':
    return coords[0], coords[1]+1
  if direction == 'L':
    return coords[0]-1, coords[1]


def map_wire(wire, name, wire_map):
  intersections = []
  coords = 0, 0
  for s in wire:
    d, m = direction(s), magnitude(s)
    while m:
      if coords in wire_map and wire_map[coords] != name:
        intersections.append(coords)
      wire_map[coords] = name
      m -= 1
      coords = increment(coords, d)
  return intersections[1:] # first value is just central port

def steps(wire, goal_coords):
  result = 0
  coords = 0, 0
  for s in wire:
    d, m = direction(s), magnitude(s)
    while m:
      coords = increment(coords, d)
      result += 1
      m -= 1
      if coords == goal_coords:
        return result



wire_map = dict()

with open('input', 'r') as f:
  wire_one = f.readline().strip().split(',')
  wire_two = f.readline().strip().split(',')

map_wire(wire_one, 'a', wire_map)
intersections = map_wire(wire_two, 'b', wire_map)
print(sorted([manhattan(coords) for coords in intersections])[0])

print(sorted([steps(wire_one, coords) + steps(wire_two, coords) for coords in intersections])[0])

"""
This is a correct but currently very inefficient solution.

It could be improved by tallying total steps of taken along each wire while looking for intersections and making a note of the total steps each time an intersection is found. In this way we could solve part one and two simultaneously.

"""

