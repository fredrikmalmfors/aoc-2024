from collections import deque


with open("input", "r+") as file:
    line = file.read().strip()

data = deque(
    [(int(ch), i // 2 if i % 2 == 0 else None) for i, ch in enumerate(line) if int(ch)]
)
to_place = deque([x for x in data if x[1] is not None])


def pdd(prefix):
    global data
    print(
        prefix
        + " | "
        + "".join(str(x[1]) * x[0] if x[1] is not None else "." * x[0] for x in data)
    )


while to_place:
    el_count, el_ch = to_place.pop()
    for i, (count, ch) in enumerate(data):
        if ch == el_ch:
            break
        if ch is None and el_count <= count:
            ii = data.index((el_count, el_ch))
            data[ii] = (el_count, None)

            if ii + 1 < len(data):
                if data[ii + 1][1] is None:
                    be_count = data[ii + 1][0]
                    del data[ii]
                    del data[ii]
                    data.insert(ii, (be_count + el_count, None))

            if data[ii - 1][1] is None:
                tot_count = data[ii - 1][0] + data[ii][0]
                del data[ii - 1]
                del data[ii - 1]
                data.insert(ii - 1, (tot_count, None))

            del data[i]
            data.insert(i, (el_count, el_ch))
            rest = count - el_count
            if rest:
                data.insert(i + 1, (rest, None))

            break

i = 0
res = 0
for count, ch in data:
    for _ in range(count):
        if ch is not None:
            res += int(ch) * i
        i += 1

print(res)
