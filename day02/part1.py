from pathlib import Path
import math

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    line = f.readline()

res = 0
ranges = [(int(start), int(end)) for start, end in (r.split("-") for r in line.split(","))]
for r0, r1 in ranges:
    nDigitsR0 = int(math.log10(r0)) + 1
    if (nDigitsR0 % 2 != 0): # odd
        r0even = 10 ** nDigitsR0
        nDigitsR0Even = nDigitsR0 + 1
    else:
        r0even = r0
        nDigitsR0Even = nDigitsR0
    r0evenLHS = r0even // (10 ** (nDigitsR0Even // 2))
    r0evenRHS = r0even % (10 ** (nDigitsR0Even // 2))
    if r0evenLHS >= r0evenRHS:
        first = r0evenLHS
    else:
        first = r0evenLHS + 1
    nDigitsR1 = int(math.log10(r1)) + 1
    if (nDigitsR1 % 2 != 0): # odd
        r1even = 10 ** (nDigitsR1 - 1) - 1
        nDigitsR1Even = nDigitsR1 - 1
    else:
        r1even = r1
        nDigitsR1Even = nDigitsR1
    r1evenLHS = r1even // (10 ** (nDigitsR1Even // 2))
    r1evenRHS = r1even % (10 ** (nDigitsR1Even // 2))
    if r1evenRHS >= r1evenLHS:
        last = r1evenLHS
    else:
        last = r1evenLHS - 1
    if (last - first + 1 > 0):
        for half in range(first, last + 1):
            nDigitsHalf = int(math.log10(half)) + 1
            id = half + half * (10 ** nDigitsHalf)
            res += id

print(res)