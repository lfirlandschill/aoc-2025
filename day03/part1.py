from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

res = 0
for bank in lines:
    bank = bank.strip()
    max_digit1 = -1
    max_index1 = -1
    for i, c in enumerate(bank[:-1]):
        digit = int(c)
        if digit > max_digit1:
            max_digit1 = digit
            max_index1 = i
    max_digit2 = -1
    max_index2 = -1
    for i, c in enumerate(bank[max_index1 + 1:]):
        digit = int(c)
        if digit > max_digit2:
            max_digit2 = digit
            max_index2 = i
    res += 10*max_digit1 + max_digit2

print(res)
        