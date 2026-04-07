from pathlib import Path
path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

ranges = []
for line in lines:
    line = line.strip()
    if line == "":
        break
    n0 = int(line.split('-')[0])
    n1 = int(line.split('-')[1])
    newRanges = []
    placed = False
    for r0, r1 in ranges:
        if n0 > r1:
            newRanges.append((r0, r1))
        elif n1 < r0:
            if not placed:
                newRanges.append((n0, n1))
                placed = True
            newRanges.append((r0, r1))
        else:
            n0 = min(n0, r0)
            n1 = max(n1, r1)
    if not placed:
        newRanges.append((n0, n1))
    ranges = newRanges

res = 0
for range in ranges:
    res += range[1] - range[0] + 1

print(res)