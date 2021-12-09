import re

def read_input(filename):
    with open(filename) as file:
        pattern = re.compile(r'([a-g]+) ' * 10 + r'\|' + r' ([a-g]+)' * 4)
        return [(list(map(frozenset,s[:10])), list(map(frozenset,s[10:])))
                for s in pattern.findall(file.read())]

puzzleinput = read_input('input.txt')

fingerprints = {
    42: 0,
    17: 1,
    34: 2,
    39: 3,
    30: 4,
    37: 5,
    41: 6,
    25: 7,
    49: 8,
    45: 9
}

def decrypt(signals, output):
    return [fingerprints.get(sum(len(o & s) for s in signals)) for o in output]

def count_occurences(items, occurencesOf):
    return sum(i in occurencesOf for i in items)

def to_number(digits):
    return sum(10**i * d for d, i in zip(digits,range(3, -1, -1)))

decrypted_output = [decrypt(signals, output) for signals, output in puzzleinput]

ex1 = sum(count_occurences(o, {1,4,7,8}) for o in decrypted_output)
print('solution 1:', ex1)

ex2 = sum(to_number(o) for o in decrypted_output)
print('solution 2:', ex2)
