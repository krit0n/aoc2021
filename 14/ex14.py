import itertools as it
import functools as fun
import collections as col

def read_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        template = lines[0].strip()
        rules = dict(tuple(l.strip().split(' -> ')) for l in lines[2:])
        return template, rules

def pairwise(iterable):
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)

def repeat(f, n):
    def fn(x):
        for _ in range(n):
            x = f(x)
        return x
    return fn

def apply(tuplecount, rules):
    counts_new = col.Counter()
    for i,c in tuplecount.most_common():
        for r in rules.get(i):
            counts_new[r] += c
    return counts_new

def count_chars(tuplecount, extrachar):
    counts = col.Counter()
    for i,c in tuplecount.most_common():
        counts[i[0]] += c
    counts[extrachar] += 1
    return counts


template, rules = read_input('input.txt')

apply_rules = lambda cs: apply(cs, productions)
last_char = template[-1]
tuplecount = col.Counter(map(''.join, pairwise(template)))
productions = {key: [key[0] + val, val + key[1]] for key, val in rules.items()}

occurences1 = count_chars(repeat(apply_rules, 10)(tuplecount), last_char).most_common()
print('solution 1:', occurences1[0][1] - occurences1[-1][1])

occurences2 = count_chars(repeat(apply_rules, 40)(tuplecount), last_char).most_common()
print('solution 2:', occurences2[0][1] - occurences2[-1][1])
