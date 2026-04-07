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
        dialR = (100 - dial) % 100
        res += int( (dialR + num) / 100 )
    else:
        res += int( (dial + num) / 100 )
    if turningLeft:
        dial -= num
    else:
        dial += num
    dial = dial % 100

print(res)