from collections import Counter, deque
from itertools import islice

class FishPopulationIterator:
    def __init__(self, timers):
        fish_count = Counter(timers)
        fish = [0] * 7
        for f,c in fish_count.items():
            fish[f] = c

        self.fish = deque(fish)
        self.newborns = deque([0] * 9)

    def __iter__(self):
        return self

    def __next__(self):
        births = self.fish.popleft() + self.newborns.popleft()

        self.fish.append(births)
        self.newborns.append(births)

        return sum(self.fish) + sum(self.newborns)


def read_timers(filename):
    with open(filename) as file:
        return [int(f) for f in file.read().strip().split(',')]

timers = read_timers('input.txt')

print('solution 1:', next(islice(FishPopulationIterator(timers), 79, None)))
print('solution 2:', next(islice(FishPopulationIterator(timers), 255, None)))
