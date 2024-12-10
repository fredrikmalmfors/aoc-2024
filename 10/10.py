from itertools import product


with open("input", "r+") as file:
    lines = file.read().splitlines()

D = [[int(ch) for ch in ll] for ll in lines]
heads = [(y, x) for y, x in product(range(len(D)), range(len(D[0]))) if D[y][x] == 0]


def trav(y, x):

    if D[y][x] == 9:
        return [(y, x)]

    nines = []
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(D) and 0 <= nx < len(D[0]) and D[ny][nx] == D[y][x] + 1:
            nines.extend(trav(ny, nx))

    return nines


print("part 1:", sum(len(set(trav(y, x))) for y, x in heads))
print("part 2:", sum(len(trav(y, x)) for y, x in heads))
