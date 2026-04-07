from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

data = [list(line.rstrip('\n')) for line in lines]
ops = ''.join(data[len(data) - 1]).replace(' ', '')
data.pop()

ops = ops[::-1]
rotData = [list(row) for row in zip(*data)][::-1]
rotData = [''.join(row).strip() for row in rotData]
nums = [int(s) if s else None for s in rotData]

res = 0
op = 0
multiplying = ops[op] == '*'
opRes = 1 if multiplying else 0
for num in nums:
    if num == None:
        res += opRes
        op += 1
        multiplying = ops[op] == '*'
        opRes = 1 if multiplying else 0
    else:
        opRes = opRes * num if multiplying else opRes + num
res += opRes

print(res)
