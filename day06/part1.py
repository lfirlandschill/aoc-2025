from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

lines = [line.split() for line in lines]
ops = lines.pop()
data = [list(map(int, row)) for row in zip(*lines)]
nOps = len(data)
n = len(data[0])

res = 0
for op in range(len(data)):
    multiplying = ops[op] == '*'
    opRes = 1 if multiplying else 0
    for val in data[op]:
        opRes = opRes * val if multiplying else opRes + val
    res += opRes

print(res)
