with open("input", "r+") as file:
    lines = file.read().splitlines()


def is_safe(elems: list[int]):

    cond = (elems == list(sorted(elems))) or (
        elems == list(sorted(elems, reverse=True))
    )
    if not cond:
        return False

    for i in range(len(elems) - 1):
        diff = abs(elems[i] - elems[i + 1])
        if not (1 <= diff <= 3):
            return False

    return True


p1_count = 0
p2_count = 0

for ll in lines:
    elems = [int(x) for x in ll.split(" ")]

    if is_safe(elems):
        p1_count += 1

    variants = [elems] + [(elems[0:i] + elems[i + 1 :]) for i in range(len(elems))]
    if any(is_safe(v) for v in variants):
        p2_count += 1

print("part 1:", p1_count)
print("part 2:", p2_count)
