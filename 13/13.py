from itertools import batched

with open("input", "r+") as file:
    lines = file.read().splitlines()

HOI = 10000000000000

res = 0
for ll in batched(lines, 4):
    try:
        _a, _b, _c, _ = ll
    except:
        _a, _b, _c = ll
    (xa, ya), (xb, yb) = ((int(k[2:]) for k in z[10:].split(", ")) for z in (_a, _b))
    xt, yt = (HOI + int(k[2:]) for k in _c[7:].split(", "))

    # if a != 0
    b = (yt * xa - xt * ya) / (xt * yb - yt * xb)
    a = yt / (ya + b * yb)
    b = a * b

    if abs(round(a) - a) < 0.001 and abs(round(b) - b) < 0.001:
        res += a * 3 + b

print(int(res))
