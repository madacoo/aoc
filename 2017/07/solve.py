from collections import defaultdict

def puzzle_input():
    "Return puzzle input as a list of strings."
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def program_tree():
    "Return a dictionary describing the program tree."
    #  { name: { 'weight': int,
    #            'children': list of str } (empty list if no children)
    tree = {}
    for desc in puzzle_input():
        name = desc.split(" ")[0]
        weight = int(desc[desc.index('(')+1:desc.index(')')])
        try:
            children = desc.split("-> ")[1].split(", ")
        except IndexError:
            children = []
        tree[name] = { 'weight': weight, 
                       'children': children }
    return tree


def is_child(name, tree):
    for p in tree:
        if name in tree[p]['children']:
            return True
    return False
    
def program_weight(name, tree):
    return tree[name]['weight'] + \
        sum([program_weight(c, tree) 
             for c in tree[name]['children']])
        
        
def unbalanced(name, tree):
    "Return unbalanced child of name in tree."
    weight_dict = defaultdict(list)
    for child in tree[name]['children']:
        weight_dict[program_weight(child, tree)].append(child)
    for weight in weight_dict:
        if len(weight_dict[weight]) == 1:
            return weight_dict[weight][0]
    
tree = program_tree()
holders = [p for p in tree if tree[p]['children']]
bottom = [p for p in tree if not is_child(p, tree)][0]

runt = bottom
while True:
    runt = unbalanced(runt, tree)
    if not runt:
        break
    print(runt)
    
print([(child, program_weight(child, tree)) 
        for child in tree['sphbbz']['children']])

print(tree['sphbbz']['weight'])
