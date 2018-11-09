#!/usr/bin/env python3

from itertools import permutations
from functools import reduce

wrapping_paper_sq_ft = 0

with open("input.txt", "r") as f:
    for d in f:
        dimensions = d.strip().split('x')
        faces_dimensions = permutations(dimensions, 2)
        face_areas = [int(d[0]) * int(d[1]) for d in faces_dimensions]
        spare = sorted(face_areas)[0]
        total_area = reduce(lambda x, y: x+y, [spare, *face_areas])
        wrapping_paper_sq_ft += total_area

print(wrapping_paper_sq_ft)
