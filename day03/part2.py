from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

res = 0
nDigits = 12
for bank in lines:
    bank = bank.strip()
    joltage = 0
    last_index = -1
    for d in range(nDigits):
        max_digit = -1
        max_index = -1
        for i, c in enumerate(bank[last_index + 1 : len(bank) - nDigits + d + 1], start = last_index + 1):
            digit = int(c)
            if digit > max_digit:
                max_digit = digit
                max_index = i
        last_index = max_index
        joltage += max_digit * 10 ** (nDigits - d - 1)
    res += joltage

print(res)
        