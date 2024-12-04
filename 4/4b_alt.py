""" Another way of solving part 2 """

with open("input", "r+") as file:
    grid = file.read().splitlines()

counter = 0
for y, ll in enumerate(grid[1:-1], 1):
    for x, ch in enumerate(ll[1:-1], 1):
        try:
            assert ch == "A"
            assert set(grid[y + 1][x + 1] + grid[y - 1][x - 1]) == set("MS")
            assert set(grid[y + 1][x - 1] + grid[y - 1][x + 1]) == set("MS")
            counter += 1
        except:
            continue

print("part 2:", counter)
