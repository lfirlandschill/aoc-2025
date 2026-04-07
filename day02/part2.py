from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    line = f.readline()

res = 0
ranges = [(int(start), int(end)) for start, end in (r.split("-") for r in line.split(","))]
for r0, r1 in ranges:
    for id in range(r0, r1 + 1):
        id = str(id)
        foundInvalidID = False
        nPattern = 1
        while nPattern <= (len(id) // 2) and not foundInvalidID:
            if len(id) % nPattern != 0:
                nPattern += 1
                continue
            pattern = id[:nPattern]
            if id == pattern * (len(id) // len(pattern)):
                foundInvalidID = True
                break
            else:
                nPattern += 1
        if foundInvalidID:
            res += int(id)

print(res)