with open("input", "r+") as file:
    lines: list[str] = file.read().splitlines()


mid = lines.index("")
rules = lines[:mid]
data = lines[mid + 1 :]

rules = [tuple((int(k) for k in x.split("|"))) for x in rules]
data = [tuple((int(k) for k in x.split(","))) for x in data]


def is_valid(seq: list[int]):
    for i, a in enumerate(seq):
        for b in seq[i + 1 :]:
            if (b, a) in rules:
                return False

    return True


ans = sum(nums[int((len(nums) - 1) / 2)] for nums in data if is_valid(nums))
print(ans)
