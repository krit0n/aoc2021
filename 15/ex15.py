import heapq

class PriorityQueue:
    def __init__(self):
        self._data = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self._data, (priority, self.index, item))
        self.index += 1

    def pop(self):
        priority, _, item = heapq.heappop(self._data)
        return item, priority

    def isEmpty(self):
        return not bool(self._data)

    def __repr__(self):
        return str(self._data)


class Graph:
    def __init__(self, map):
        self.map = [r[:] for r in map]
        self.len_y = len(map)
        self.len_x = len(map[0])

    def getNode(self, x, y):
        return Node(self, x, y)

    def __repr__(self):
        return str(self.map)


class Node:
    def __init__(self, graph, x, y):
        self.graph = graph
        self.x = x
        self.y = y

    @property
    def neighbors(self):
        graph, x, y = self.graph, self.x, self.y
        return [Node(graph, x+dx,y+dy)
                for dx, dy in [(-1, 0), (1, 0), (0,-1), (0, 1)]
                if 0 <= x+dx < graph.len_x
                and 0 <= y+dy < graph.len_y]

    @property
    def cost(self):
        return self.graph.map[self.y][self.x]

    def __repr__(self):
        return f'{(self.x, self.y)}: {self.cost}'

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

def get_path(predecessors, end):
    r_path = [end]
    next = predecessors[end]
    while(next):
        r_path.append(next)
        next = predecessors.get(next)
    return list(reversed(r_path))


def a_star(graph, start, end):
    fringe = PriorityQueue()
    closed = set()
    best = {}
    predecessors = {}

    fringe.push(start, 0)
    best[start] = 0

    steps = 0
    while True:
        steps += 1
        current, _ = fringe.pop()
        g = best[current]

        if current == end:
            print('steps:', steps)
            return g, get_path(predecessors, current)

        for successor in current.neighbors:
            if successor in closed:
                continue

            g_succ = g + successor.cost

            if g_succ >= best.get(successor, float('Inf')):
                continue

            predecessors[successor] = current
            best[successor] = g_succ

            f_succ = g_succ # + (end.y - successor.x) + (end.y - successor.y)

            fringe.push(successor, f_succ)

        closed.add(current)

        if fringe.isEmpty():
            break

    return None


def read_input(filename):
    with open(filename) as file:
        return [[int(c) for c in r.strip()]
                for r in file.readlines()]

map = read_input('input.txt')
graph = Graph(map)
start = graph.getNode(0,0)
end = graph.getNode(graph.len_x-1, graph.len_y-1)
print('solution1:', a_star(graph, start, end)[0])

dimX = len(map[0])
dimY = len(map)
repetitions = 5
map2 =  [[0] * dimX * repetitions for _ in range(dimY * repetitions)]

for y in range(dimY * repetitions):
    for x in range(dimX * repetitions):
        map2[y][x] = ((map[y % dimY][x % dimX] + (y // dimY) + (x // dimX) - 1) % 9) + 1

graph2 = Graph(map2)
start2 = graph2.getNode(0,0)
end2 = graph.getNode(graph2.len_x-1, graph2.len_y-1)
print('solution2:', a_star(graph2, start2, end2)[0])
