from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations

with open("input", "r+") as file:
    lines = file.read().splitlines()


@dataclass(frozen=True)
class P:
    y: int
    x: int

    def __add__(self, o: "P"):
        return P(self.y + o.y, self.x + o.x)

    def __sub__(self, o: "P"):
        return P(self.y - o.y, self.x - o.x)

    def in_bounds(self):
        return 0 <= self.y < len(lines) and 0 <= self.x < len(lines[0])


A = defaultdict(list[P])
for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        if ch != ".":
            A[ch].append(P(y, x))

res = set()
for ch, ants in A.items():
    for pa, pb in combinations(ants, 2):
        delta = pa - pb

        while pa.in_bounds():
            res.add(pa)
            pa += delta

        while pb.in_bounds():
            res.add(pb)
            pb -= delta

print(len(res))
