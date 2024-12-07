from copy import deepcopy


with open("input.txt", "r+") as file:
    lines = file.read().splitlines()

DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


def find_start():
    for y, ll in enumerate(lines):
        for x, ch in enumerate(ll):
            if ch == "^":
                return y, x


def in_bounds(y, x):
    return 0 <= y < len(lines) and 0 <= x < len(lines)


def is_obs(y, x):
    return lines[y][x] == "#"


# State
loop_count = 0

SY, SX = find_start()
initial_visit_set = set()

for ky in range(len(lines)):
    for kx in range(len(lines)):
        if initial_visit_set and (ky, kx) not in initial_visit_set:
            continue

        cy, cx = SY, SX
        visited = set()
        tot_steps = 0
        cdir = 0

        is_loop = False
        while True:
            visited.add((cy, cx))

            dy, dx = DIRS[cdir]
            ny, nx = cy + dy, cx + dx

            if not in_bounds(ny, nx):
                if not initial_visit_set:
                    initial_visit_set = deepcopy(visited)
                break

            if is_obs(ny, nx) or (ny == ky and nx == kx):
                cdir = (cdir + 1) % 4
                continue

            tot_steps += 1
            cy, cx = ny, nx

            if (tot_steps > 1000) and ((tot_steps / 10) > len(visited)):
                print("LOOP")
                is_loop = True
                break

        if is_loop:
            loop_count += 1


print(loop_count)
