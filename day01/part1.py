from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

dial = 50
res = 0
for line in lines:
    num = int(line[1:])
    turningLeft = line[0] == 'L'
    if turningLeft:
        dial -= num
    else:
        dial += num
    dial = dial % 100
    if dial == 0:
        res += 1

print(res)