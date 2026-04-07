from pathlib import Path
import math

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

points = [tuple(int(x) for x in line.split(',')) for line in lines]

point_pairs = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        point_pairs.append((dist, i, j))

circuit_by_point = list(range(len(points)))
size_by_circuit = [1] * len(points)
point_pairs.sort(key = lambda x: x[0])

max_circuit_size = 1
p = 0
point_pair = []
while not max_circuit_size == len(points):
    point_pair = point_pairs[p]
    c1 = circuit_by_point[point_pair[1]]
    c2 = circuit_by_point[point_pair[2]]
    if (c1 is not c2):
        for i in range(len(points)):
            if circuit_by_point[i] == c2:
                circuit_by_point[i] = c1
                size_by_circuit[c1] += 1
                size_by_circuit[c2] -= 1
        max_circuit_size = max(max_circuit_size, size_by_circuit[c1])
    p += 1

res = points[point_pair[1]][0] * points[point_pair[2]][0]
print(res)


