from pathlib import Path
import math

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

points = [tuple(int(x) for x in line.split(',')) for line in lines]

point_pairs = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        area = (abs(y2-y1)+1)*(abs(x2-x1)+1)
        point_pairs.append((area, i, j))

point_pairs.sort(key = lambda x: x[0], reverse=True)
res = point_pairs[0][0]
print(res)


