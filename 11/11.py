from functools import cache

real = [0, 27, 5409930, 828979, 4471, 3, 68524, 170]


@cache
def trav(num: int, rm: int):

    if rm == 0:
        return 1

    if num == 0:
        return trav(1, rm - 1)

    w = len(str(num))
    if w % 2 == 1:
        return trav(num * 2024, rm - 1)

    return trav(int(str(num)[: w // 2]), rm - 1) + trav(int(str(num)[w // 2 :]), rm - 1)


print("part 1:", sum(trav(x, 25) for x in real))
print("part 2:", sum(trav(x, 75) for x in real))
