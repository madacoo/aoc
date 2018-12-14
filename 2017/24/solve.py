def puzzle_input():
    with open('input.txt', 'r') as f:
        return f.read().strip().split('\n')

def strength(bridge):
    split_parts = [p.split('/') for p in bridge.split('--')]
    return sum([int(part) for split_part in split_parts 
                          for part in split_part])

def connects(bridge, part):
    """Return the orientation of part needed to connect it to bridge.
       Or if it can't be connected return False.
    """
    a, b = part.split('/')
    socket = bridge.split('--')[-1].split('/')[-1] if bridge else '0'
    if a == socket: return '/'.join((a, b))
    if b == socket: return '/'.join((b, a))
    return False

def build_bridges(bridge, components, bridges):
    for part in components:
        orient = connects(bridge, part)
        if not orient: continue
        new_bridge = "{}--{}".format(bridge, orient) if bridge else orient
        new_components = [p for p in components if not p == part]
        build_bridges(new_bridge, new_components, bridges)
    if bridge: bridges.append(bridge)

def key(bridge):
    split_parts = [p.split('/') for p in bridge.split('--')]
    parts = [int(part) for split_part in split_parts 
                       for part in split_part]
    return len(parts), sum(parts)
    
components = puzzle_input()
# test: components = "0/2,2/2,2/3,3/4,3/5,0/1,10/1,9/10".split(',')

# part a
bridges = []
build_bridges("", components, bridges)
print(max([strength(b) for b in bridges]))

# part b
print(strength(sorted(bridges, key=key, reverse=True)[0]))



