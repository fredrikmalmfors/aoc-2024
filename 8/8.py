from collections import defaultdict
from itertools import combinations


with open("input", "r+") as file:
    lines = file.read().splitlines()


def in_bounds(y, x):
    return 0 <= y < len(lines) and 0 <= x < len(lines[0])


A = defaultdict(list)
for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        if ch != ".":
            A[ch].append((y, x))

res = set()
for ch, ants in A.items():
    for ta, tb in combinations(ants, 2):
        ay, ax = ta
        by, bx = tb
        day, dax = ay - by, ax - bx

        while in_bounds(ay, ax):
            res.add((ay, ax))
            ay, ax = ay + day, ax + dax

        while in_bounds(by, bx):
            res.add((by, bx))
            by, bx = by - day, bx - dax

print(len(res))
