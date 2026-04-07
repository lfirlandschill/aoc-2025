from pathlib import Path
import re

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

res = 0
for line in lines:
    target = line.split(']')[0][1:].replace('[','').replace('.','0').replace('#','1')
    buttons = [
    [int(x.strip()) for x in part.split(',')]
    for part in re.findall(r'\((.*?)\)', line)
    ]
    min_presses = float('inf')
    n = len(buttons)
    for mask in range(2**n):
        bits = format(mask, f'0{n}b')
        subset = [buttons[i] for i in range(n) if bits[i] == '1']
        subset_res = '0' * len(target)
        for button in subset:
            for toggle in button:
                subset_res = subset_res[:toggle] + str(int(subset_res[toggle]) ^ 1) + subset_res[toggle+1:]
        if subset_res == target:
            min_presses = min(min_presses, len(subset))
    res += min_presses

print(res)
