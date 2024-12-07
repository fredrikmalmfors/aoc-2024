with open("input.txt", "r+") as file:
    lines = file.read().splitlines()


def foo(a, b):
    return int(str(a) + str(b))


ans = 0

for ll in lines:
    a, b = ll.split(": ")
    roof = int(a)
    b = tuple(int(x) for x in b.split(" "))

    def trav(seq: tuple[int]):

        assert seq
        el = seq[-1]
        if len(seq) == 1:
            return (el,)

        rest = trav(seq[:-1])
        rest = [x for x in rest if x <= roof]
        temp = (
            [el + x for x in rest] + [el * x for x in rest] + [foo(x, el) for x in rest]
        )
        return [x for x in temp if x <= roof]

    res = trav(b)
    if roof in res:
        ans += roof

print(ans)
