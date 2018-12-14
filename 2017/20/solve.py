from collections import namedtuple


Vector = namedtuple('Vector', 'x y z')
Particle = namedtuple('Particle', 'pos vel acc')


def puzzle_input():
    "Return a list of Particles."
    particles = []
    with open('input.txt', 'r') as f:
       for line in f:
           pva = [s[3:-1] for s in line.strip().split(', ')]
           pos, vel, acc = [Vector(*map(int, s.split(','))) for s in pva]
           particles.append(Particle(pos, vel, acc))
    return particles


def add_vectors(v1, v2):
    return Vector(v1.x + v2.x,
                  v1.y + v2.y,
                  v1.z + v2.z)


def manhatten_distance(v):
    return abs(v.x) + abs(v.y) + abs(v.z)


def update_particle(p):
    vel = add_vectors(p.vel, p.acc)
    pos = add_vectors(p.pos, vel)
    return Particle(pos, vel, p.acc)


def find_collisions(particles):
    """Return a list of indices (in reverse order)
       of particles in a state of collision."""
    indices = []
    for i, pi in enumerate(particles):
        for j, pj in enumerate(particles):
            if i == j: continue
            if pi.pos == pj.pos:
                if not i in indices: indices.append(i)
    return sorted(indices, reverse=True)


def solve():
    # find index of smallest acceleration vector
    particles = puzzle_input()
    smallest_acc_vec = manhatten_distance(particles[0].acc)
    min_index = 0
    for i, p in enumerate(particles[1:]):
        m = manhatten_distance(particles[i].acc)
        if m < smallest_acc_vec:
            smallest_acc_vec = m
            min_index = i
    return min_index


def solve2():
    particles = puzzle_input()
    for tick in range(100000):
        for index in find_collisions(particles):
            del particles[index]
        particles = [update_particle(p) for p in particles]
        if tick % 100 == 0: print(len(particles))
    return(len(particles))
        
print(solve())
print(solve2())

"""
The solution to part b is very dirty. I basically just have the program tick along, printing out the number of particles still remaining and once I see some repetition in the amount of particles, I try that as an answer.

I'm also not at all happy with my find_collisions function, which is clearly slow and ugly.

There is probably a much better way of figuring out whether any two given particles will collide and when, and using that information to figure out how many particles will be left altogether. Of course if any two given particles will collide, this will only actually occur if they don't collide with other particles before then.
"""
