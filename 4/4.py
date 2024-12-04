from collections import defaultdict
from dataclasses import dataclass
import numpy as np
import re

with open("input", "r+") as file:
    lines = file.read().splitlines()


@dataclass
class P:
    y: int
    x: int
    char: str


# Add (y, x) to to each char in grid --> Grid of points
grid = np.array(
    [[P(y, x, char) for x, char in enumerate(line)] for y, line in enumerate(lines)]
)


def get_match_points(seq: list[P], pattern: str):
    """find pattern in sequence and return P of the second element (crosspoint)"""
    return [
        seq[match.start() + 1]
        for match in re.finditer(f"(?={pattern})", "".join(x.char for x in seq))
    ]


counter_p1 = 0
counter_p2 = defaultdict(int)  # Freq of each crosspoint
for rotations in range(4):
    _grid = np.rot90(grid, k=rotations)

    # Part 1
    for offset in range(-len(_grid), len(_grid)):
        counter_p1 += len(get_match_points(_grid.diagonal(offset), "XMAS"))

    for seq in _grid:
        counter_p1 += len(get_match_points(seq, "XMAS"))

    # Part 2
    for offset in range(-len(_grid), len(_grid)):
        for p in get_match_points(_grid.diagonal(offset), "MAS"):
            counter_p2[(p.y, p.x)] += 1

print("part 1:", counter_p1)
print("part 2:", sum(v >= 2 for v in counter_p2.values()))
