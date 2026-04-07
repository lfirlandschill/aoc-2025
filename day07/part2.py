from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

beams = [0] * len(lines[0])
nTimeslines = 1
for line in lines:
    for i in range(len(line)):
        c = line[i]
        if c == 'S':
            beams[i] = 1
        if c == '^' and beams[i] > 0:
            beams[i - 1] += beams[i]
            beams[i + 1] += beams[i]
            beams[i] = 0

print(sum(beams))