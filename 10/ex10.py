from statistics import median

def read_input(filename):
    with open(filename) as file:
        return (line.strip() for line in file.readlines())

opening_parantheses = ['(', '[', '{', '<']
closing_parantheses = [')', ']', '}', '>']
    
def get_matching_paranthesis(p):
    if p in opening_parantheses:
        return closing_parantheses[opening_parantheses.index(p)]
    else:
        return opening_parantheses[closing_parantheses.index(p)]

def check(line):
    stack = []
    for p in line:
        if p in opening_parantheses:
            stack.append(p)
        else:
            last_opening_paranthesis = stack.pop()
            expected = get_matching_paranthesis(last_opening_paranthesis)
            if p != expected:
                print(f'Expected {expected}, but found {p} instead')
                return p, None

    missing_parantheses = [get_matching_paranthesis(p) for p in reversed(stack)]
    if missing_parantheses:
        print(f'Complete by adding', ''.join(missing_parantheses))
                
    return None, missing_parantheses

points1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

points2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


lines = read_input('input.txt')

result1 = 0
scores2 = []
for line in lines:
    illegal, missing = check(line)
    if illegal:
        result1 += points1.get(illegal)
    else:
        score = 0
        for m in missing:
            score *= 5
            score += points2.get(m)
        scores2.append(score)

print('solution 1:', result1)
print('solution 2:', median(sorted(scores2)))
