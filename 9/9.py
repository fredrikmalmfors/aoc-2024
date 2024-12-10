from collections import deque


with open("sample", "r+") as file:
    line = file.read().strip()

data = deque()
for i, ch in enumerate(line):
    data.extend([i // 2 if i % 2 == 0 else None] * int(ch))

res = deque()
while data:
    el = data.popleft()
    if el is not None:
        res.append(el)
    else:
        try:
            while (oth := data.pop()) is None:
                pass
            res.append(oth)
        except IndexError:
            continue

# print("".join(str(x) if x is not None else "." for x in res))
print(res)
print(sum(i * x for i, x in enumerate(res)))
