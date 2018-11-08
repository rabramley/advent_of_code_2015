#!/usr/bin/env python3

floor = 0

with open("input.txt", "r") as f:
    for i, c in enumerate(f.readline(), 1):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        
        if floor < 0:
            print(i)
            break

