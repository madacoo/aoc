#!/usr/bin/python3

def count(orbits, orbiter):
    total = 0
    while orbiter != 'COM':
        orbiter = orbits[orbiter]
        total += 1
    return total


def path(orbits, orbiter):
    result = []
    while orbiter != 'COM':
        orbiter = orbits[orbiter]
        result.append(orbiter)
    return result

def intersection(path_one, path_two):
    for place in path_one:
        if place in path_two: return place


# part 1
orbits = dict()

with open('input', 'r') as f:
    for line in f:
        orbitee, orbiter = line.strip().split(')')
        orbits[orbiter] = orbitee

total = 0
for orbiter in orbits.keys():
    total += count(orbits, orbiter)
print(total)


# part 2
you_path = path(orbits, 'YOU')
san_path = path(orbits, 'SAN')
place = intersection(you_path, san_path)
print(you_path.index(place) + san_path.index(place))

