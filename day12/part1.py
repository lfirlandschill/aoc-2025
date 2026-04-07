from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

gifts = []
gift_sizes = []
regions = []
for line in lines:
    if 'x' in line:
        area = [int(x) for x in line.split(':')[0].split('x')]
        counts = [int(x) for x in line.split(':')[1].split()]
        regions.append((area, counts))
    elif ':' in line:
        gifts.append([])
        gift_sizes.append(0)
    elif line.strip():
        l = [1 if c == '#' else 0 for c in line]
        gift_sizes[-1] += l.count(1)
        gifts[-1].append(l)

n_trivial_positive = 0
n_trivial_negative = 0
for region in regions:
    region_area = region[0][0] * region[0][1]
    side_by_side_gift_area = 9*sum(region[1])
    minimum_gift_area = sum(x * y for x, y in zip(region[1], gift_sizes))
    if side_by_side_gift_area <= region_area:
        n_trivial_positive += 1
    if minimum_gift_area > region_area:
        n_trivial_negative += 1

print(f'{len(regions)} regions')
print(f'{n_trivial_positive} trivial positive')
print(f'{n_trivial_negative} trivial negative')
print(f'{len(regions) - n_trivial_negative - n_trivial_positive} unknown')