from collections import Counter
import re

def read_file(filename):
    with open(filename) as file:
        pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
        return [((int(x1),int(y1)),(int(x2),int(y2)))
                for x1,y1,x2,y2
                in pattern.findall(file.read())]

def sgn(x):
    return (x > 0) - (x < 0)

def get_line(start, end):
    x1,y1 = start
    x2,y2 = end
    if (x1 == x2):
        return ((x1,y) for y in range(min(y1,y2),max(y1,y2)+1))
    elif (y1 == y2):
        return ((x,y1) for x in range(min(x1,x2),max(x1,x2)+1))
    else:
        kx = sgn(x2-x1)
        ky = sgn(y2-y1)
        return ((x,y) for x,y in zip(range(x1,x2+kx,kx),range(y1,y2+ky,ky)))

# exercise 1

lines = read_file('input.txt')

counter = Counter()
counter_diag = Counter()
for (x1,y1),(x2,y2) in lines:
    line = get_line((x1,y1),(x2,y2))
    if x1 == x2 or y1 == y2:
        counter.update(line)
    else:
        counter_diag.update(line)

print('solution 1:', len([(k,c) for k, c in counter.items() if c > 1]))

# exercise 2

counter.update(counter_diag)
print('solution 2:', len([(k,c) for k, c in counter.items() if c > 1]))
            
