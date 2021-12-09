from statistics import median, mean
from math import comb, floor, ceil

def read_positions(filename):
    with open(filename) as file:
        return [int(p) for p in file.read().strip().split(',')]

def fuel_part1(positions):
    optimum = round(median(positions))
    return sum(abs(p - optimum) for p in positions)

def fuel_part2(positions):
    m = mean(positions)
    possible_optimums = range(floor(m), ceil(m))
    return min(sum(delta(opt,p) for p in positions) for opt in possible_optimums)

def delta(a, b):
    return comb(abs(a-b)+1, 2)

positions = read_positions('input.txt')
print('solution 1:', fuel_part1(positions))
print('solution 2:', fuel_part2(positions))
