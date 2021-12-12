import itertools as it
from collections import Counter

def read_input(filename):
    with open(filename) as file:
        return [tuple(line.strip().split('-'))
                for line in file.readlines()
                if line]

def group_by(s, groupby = None, mapvalue = None):
    return {k: mapvalue(v) for k, v in it.groupby(sorted(s, key=groupby), groupby)}

def make_symmetric(edges):
    symmetric_edges = set(edges)
    for (f, t) in edges:
        symmetric_edges.add((t, f))
    return symmetric_edges

edges = make_symmetric(read_input('input.txt'))
node_to_edges = group_by(edges, lambda x: x[0], lambda ls: set(map(lambda l: l[1], ls)))


def get_paths(nodes, f, t, valid, path = []):
    if not valid(path):
        return []
    if f == t:
        return [path + [f]]

    neighbors = nodes.get(f, [])
    next_path = path + [f]

    return (p for n in neighbors for p in get_paths(nodes, n, t, valid, next_path) if p)
        
def valid_path_1(path):
    most_common = Counter(p for p in path if p.islower()).most_common(1)
    return not most_common or most_common[0][1] <= 1

def valid_path_2(path):
    c = Counter(p for p in path if p.islower())
    return all(i <= j for i, j in zip([mc[1] for mc in c.most_common()], (2,1))) and c.get('start', 0) <= 1

print(len(list(get_paths(node_to_edges, 'start', 'end', valid_path_1))))
print(len(list(get_paths(node_to_edges, 'start', 'end', valid_path_2, []))))
