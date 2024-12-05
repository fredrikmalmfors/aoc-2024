with open("input", "r+") as file:
    lines: list[str] = file.read().splitlines()


mid = lines.index("")
rules = lines[:mid]
data = lines[mid + 1 :]

rules = [tuple((int(k) for k in x.split("|"))) for x in rules]
data = [list((int(k) for k in x.split(","))) for x in data]


def is_valid(seq: list[int]):
    for i, a in enumerate(seq):
        for j, b in enumerate(seq[i + 1 :], i + 1):
            if (b, a) in rules:
                return False, (i, j)

    return True, None


res = 0
for i, dd in enumerate(data):

    count = 0
    while True:

        valid, bad_pair = is_valid(dd)
        if valid:
            break

        count += 1
        a, b = bad_pair

        # swap
        dd[a], dd[b] = dd[b], dd[a]

    if count > 0:
        res += dd[int((len(dd) - 1) / 2)]

print(res)
