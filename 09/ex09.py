from functools import reduce

def read_input(filename):
    with open(filename) as file:
        return [[int(c) for c in line.strip()] for line in file.readlines()]

def pad_map(map, pad = 9):
    padding_horizontal = [(len(map[0]) + 2) * [pad]]
    return padding_horizontal + [[pad] + m + [pad] for m in map] + padding_horizontal

def pretty_print_map(map):
    print('\n'.join(['  '.join([str(c) for c in r]) for r in map]))

def neighbors(x, y):
    return (x-1,y), (x,y-1), (x,y+1), (x+1,y)

def floodfill(map, coord, mark=9):
    r = coord[0]
    c = coord[1]
    if map[r][c] == mark:
        return 0
    else:
        map[r][c] = mark
        return 1 + sum(floodfill(map, c) for c in neighbors(*coord))

heightmap = read_input('input.txt')
padded_map = pad_map(heightmap)

# exercise 1

low_points = 0
for r in range(1, len(padded_map) - 1):
    for c in range(1, len(padded_map[r]) - 1):
        if padded_map[r][c] < min(padded_map[x][y] for x,y in neighbors(r,c)):
            low_points += padded_map[r][c] + 1
print('solution 1:', low_points)


# exercise 2

basin_sizes = []
for r in range(1, len(padded_map) - 1):
    for c in range(1, len(padded_map[r]) - 1):
        basin_size = floodfill(padded_map, (r, c))
        if basin_size > 0:
            basin_sizes.append(basin_size)

print('solution 2:', reduce((lambda x, y: x*y), sorted(basin_sizes)[-3:]))


