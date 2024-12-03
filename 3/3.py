with open("input.txt", "r+") as file:
    data = file.read()

res = [[], []]  # Part 1 and 2
enabled = True
base = 0


def get_next():
    """Get next item type (and its index)"""
    global base

    i = data.index("mul(", base)
    try:
        ido = data.index("do()", base, i + 10)
    except ValueError:
        ido = 1_000_000
    try:
        idont = data.index("don't()", base, i + 10)
    except ValueError:
        idont = 1_000_000
    return min([("mul(", i), ("do()", ido), ("don't()", idont)], key=lambda x: x[1])


while True:

    try:
        cat, index = get_next()
    except:
        break

    match cat:
        case "mul(":
            j = data.index(")", index)
            mid = data[index + 4 : j]

            # Check if valid
            try:
                assert mid.replace(",", "").isnumeric()
                assert 3 <= len(mid) <= 7
                a, b = mid.split(",")
                a, b = int(a), int(b)
                assert 0 <= a <= 999
                assert 0 <= b <= 999
                res[0].append((a, b))
                if enabled:
                    res[1].append((a, b))
                base = j - 1
            except Exception as e:
                base += 3
        case "do()":
            enabled = True
            base = index + 2
        case "don't()":
            enabled = False
            base = index + 2


for part in [0, 1]:
    tot = 0
    for a, b in res[part]:
        tot += a * b
    print(f"part {part+1}:", tot)

# 161289189
# 83595109
