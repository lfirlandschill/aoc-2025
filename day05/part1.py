from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

res = 0
readRanges = True
ranges = []
for line in lines:
    line = line.strip()
    if line == "":
        readRanges = False
        continue
    if readRanges:
        ranges.append((int(line.split('-')[0]), int(line.split('-')[1])))
    else:
        val = int(line)
        for r in ranges:
            if r[0] <= val <= r[1]:
                res += 1
                break

print(res)


