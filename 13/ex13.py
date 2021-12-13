import itertools as it
import functools as func

def read_input(filename):
    with open(filename) as file:
        lines = [l.strip() for l in file.readlines()]
        coordinates = {
            tuple(map(int, line.strip().split(',')))
            for line in it.takewhile(lambda l: l.strip(), lines)
        }
        folds = [(l.split('=')[0][-1], int(l.split('=')[1]))
                 for l in lines[(len(coordinates) + 1):]]
        return coordinates, folds

def fold(coords, fold):
    (dim, height) = fold
    if dim == 'y':
        return { (x, min(y, 2*height - y)) for (x,y) in coords }
    elif dim == 'x':
        return { (min(x, 2*height - x), y) for (x,y) in coords }

def print_paper(paper):
    max_x = max(x for x,y in paper)
    max_y = max(y for x,y in paper)

    for y in range(max_y + 1):
        s = []
        for x in range(max_x + 1):
            if (x,y) in paper:
                s.append('#')
            else:
                s.append('.')
        print(''.join(s))

if (__name__ == '__main__'):
    coords, folds = read_input('input.txt')
    print('solution 1:', len(fold(coords, folds[0])))
    print('solution 2:')
    print_paper(func.reduce(fold, folds, coords))
