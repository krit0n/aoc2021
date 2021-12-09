with open('input.txt') as file:
    data = [int(line) for line in file]

solution1 = sum(x < y for x, y in zip(data, data[1:]))
solution2 = sum(x < y for x, y in zip(data, data[3:]))

print('solution 1: ', solution1)
print('solution 2: ', solution2)
