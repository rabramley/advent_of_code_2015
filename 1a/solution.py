#!/usr/bin/env python3

floor = 0

with open("input.txt", "r") as f:
    for c in f.readline():
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1

print(floor)

