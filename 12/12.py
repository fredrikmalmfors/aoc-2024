with open("input", "r+") as file:
    lines = file.read().splitlines()

D = {}

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def seek(y, x, ch, cati):
    global D
    D[(y, x)] = cati
    for dy, dx in DIRS:
        ny, nx = y + dy, x + dx
        if (
            0 <= ny < len(lines)
            and 0 <= nx < len(lines[0])
            and lines[ny][nx] == ch
            and (ny, nx) not in D
        ):
            seek(ny, nx, ch, cati)


cati = 0
for y, ll in enumerate(lines):
    for x, ch in enumerate(ll):
        if (y, x) not in D:
            seek(y, x, ch, cati)
            cati += 1


p1 = []
p2 = []

for cat in range(cati):

    poses = [k for k, v in D.items() if v == cat]
    area = len(poses)

    # Part 1
    perimiter = 4 * area - sum(
        D.get((y + dy, x + dx), None) == cat for y, x in poses for dy, dx in DIRS
    )
    p1.append(area * perimiter)

    # Part 2
    oppos = []
    for y, x in poses:
        for dy, dx in DIRS:
            ny, nx = y + dy, x + dx
            opp = D.get((ny, nx), "oob")
            if opp != cat:
                oppos.append(((y, x), (ny, nx)))

    sides = 0
    while oppos:
        (ya, xa), (yb, xb) = oppos.pop()
        for dy, dx in [(xa - xb, ya - yb), (xb - xa, yb - ya)]:
            k = 1
            while 1:
                try:
                    oppos.remove(
                        ((ya + dy * k, xa + dx * k), (yb + dy * k, xb + dx * k))
                    )
                    k += 1
                except ValueError:
                    break

        sides += 1

    p2.append(area * sides)

print("part 1:", sum(p1))
print("part 2:", sum(p2))

assert sum(p1) == 1457298
assert sum(p2) == 921636
