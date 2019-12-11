from math import sqrt, atan2, degrees, gcd
from collections import namedtuple, defaultdict

Point = namedtuple('Point', 'x y')

def integral_points(v):
    if v.x < 0 and v.y < 0:
        return [Point(-1*p.x, -1*p.y) for p in integral_points(Point(-1*v.x, -1*v.y))]
    if v.x == 0 and v.y >= 0: return [Point(0, y) for y in range(1, v.y)]
    if v.x == 0 and v.y < 0: return [Point(0, y) for y in range(-1, v.y, -1)]
    if v.y == 0 and v.x >= 0: return [Point(x, 0) for x in range(1, v.x)]
    if v.y == 0 and v.x < 0: return [Point(x, 0) for x in range(-1, v.x, -1)]
    points = []
    div = gcd(v.x, v.y)
    x, y = v.x // div, v.y // div
    p = Point(0, 0)
    for _ in range((v.x // x)-1):
        p = Point(p.x + x, p.y + y)
        points.append(p)
    return points

def can_see(a, b, asteroids):
    v = Point(b.x - a.x, b.y - a.y)
    for p in integral_points(v):
        if Point(a.x + p.x, a.y + p.y) in asteroids:
            return False
    return True

def distance(a, b):
    return sqrt(abs(a.x - b.x)**2 + abs(a.y - b.y)**2)

def angle(a, b):
    v = Point(b.x-a.x, b.y-a.y)
    return atan2(v.x, v.y)

asteroids = []
with open('input', 'r') as f:
    y = 0
    for line in f:
        for x, p in enumerate(line.strip()):
            if p == '#':
                asteroids.append(Point(x, y))
        y += 1

detection_counts = []
for a in asteroids:
    count = 0
    for b in asteroids:
        if a == b: continue
        if can_see(a, b, asteroids): count += 1
    detection_counts.append(count)

station, count = sorted(zip(asteroids, detection_counts), key=lambda t: t[1])[-1]
print(count)

angle_dict = defaultdict(list)
for a in asteroids:
    if a == station: continue
    angle_dict[angle(station, a)].append((a, distance(station, a)))

for th in angle_dict.keys(): angle_dict[th].sort(key=lambda t: t[1])

count = 0

for k in  sorted(angle_dict.keys(), reverse=True):
    if len(angle_dict[k]) > 0:
        a, d = angle_dict[k].pop(0)
        count += 1
        if count == 200:
            print(a.x*100 + a.y)

