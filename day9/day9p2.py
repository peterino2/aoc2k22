f = [ x.split() for x in [line.strip('\n') for line in open("day9.input").readlines()]]
f = [ (x[0], int(x[1])) for x in f]
d = {
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0)
}
positions_visited = [(0,0)]
heads = [(0,0) for i in range(10)]
tail = (0,0)

head_positions = []
tail_positions = []

from operator import add, sub
from math import ceil
for line in f:
    # move head position
    move = d[line[0]]
    for j in range(line[1]):
        heads[0] = tuple(map(add, heads[0], move))
        for i in range(0, len(heads)-1):
            head = heads[i]
            tail = heads[i + 1]
            isTouching = (abs(head[0] - tail[0]) < 2) and (abs(head[1] - tail[1]) < 2)
            dist = tuple(map(sub, head, tail))
            if not isTouching:
                travel = (
                    int(dist[0] / (abs(dist[0]))) if abs(dist[0]) > 0 else 0,
                    int(dist[1] / (abs(dist[1]))) if abs(dist[1]) > 0 else 0
                )
                tail = tuple(map(add, tail, travel))
            heads[i + 1] = tail
                
        should_add = True
        for pos in positions_visited:
            if heads[-1][0] == pos[0] and heads[-1][1] == pos[1]:
                should_add = False

        if should_add:
            positions_visited.append(tail)

print(head)
print(len(positions_visited))