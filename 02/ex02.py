with open('input.txt') as file:
    data = ((dir, int(delta)) for dir, delta in (line.split() for line in file))

    x1, y1 = 0, 0
    x2, y2, aim = 0, 0, 0
    for dir, delta in data:
        if dir == 'forward':
            x1 += delta
            x2 += delta
            y2 += aim * delta
        if dir == 'up':
            y1 -= delta
            aim -= delta
        if dir == 'down':
            y1 += delta
            aim += delta

    print('solution 1: ', x1, '*', y1, '=', x1*y1)
    print('solution 2: ', x2, '*', y2, '=', x2*y2)
