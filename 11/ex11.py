from itertools import islice

def pretty_print_map(map):
    return '\n'.join(['  '.join([str(c) for c in r]) for r in map])

def increment(map, inc = 1):
    return [[c + inc for c in r] for r in map]

def trigger_flashes(map, threshold):
    flashes = 0

    def get_neighbors(r,c):
        ds = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        return ((r + dr, c + dc)
                for dr, dc in ds
                if 0 <= r + dr < len(map) and 0 <= c + dc < len(map[r]))

    def trigger_flash(r,c,inc=0):
        flashes = 0
        if map[r][c] > 0:
            map[r][c] += inc
        if map[r][c] > threshold:
            flashes += 1
            map[r][c] = 0
            for n in get_neighbors(r,c):
                flashes += trigger_flash(*n, 1)
        return flashes

    for r in range(len(map)):
        for c in range(len(map[r])):
            flashes += trigger_flash(r,c)

    return flashes
  

class EnergyLevelIterator:
    def __init__(self, levels, threshold = 9):
        self.levels = levels
        self.threshold = threshold
        self.flashes = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.levels = increment(self.levels)
        self.flashes += trigger_flashes(self.levels, self.threshold)
        return self.levels, self.flashes


def read_input(filename):
    with open(filename) as file:
        return [[int(c) for c in r.strip()] for r in file.readlines()]



energy_levels = read_input('input.txt')

levels, flashes = next(islice(EnergyLevelIterator(energy_levels), 99, None))
print('solution 1:', pretty_print_map(levels), flashes, sep='\n')


for i, (levels, flashes) in enumerate(EnergyLevelIterator(energy_levels), 1):
    if all(c == 0 for r in levels for c in r):
        print('solution 2:', i)
        break
