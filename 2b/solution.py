#!/usr/bin/env python3

from itertools import permutations
from functools import reduce

ribbon_length_ft = 0

with open("input.txt", "r") as f:
    for d in f:
        dimensions = [int(x) for x in d.strip().split('x')]
        bow_length = reduce(lambda x, y: x*y, dimensions)
        shortest_edges = sorted(dimensions)[0:2]
        shortest_distance_around_sides = reduce(lambda x, y: x+y, shortest_edges) * 2
        ribbon_length_ft += bow_length + shortest_distance_around_sides

print(ribbon_length_ft)
