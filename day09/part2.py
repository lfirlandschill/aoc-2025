from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

points = [tuple(int(x) for x in line.split(',')) for line in lines]

max_area = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        rx_min = min(points[i][0], points[j][0])
        rx_max = max(points[i][0], points[j][0])
        ry_min = min(points[i][1], points[j][1])
        ry_max = max(points[i][1], points[j][1])
        area = (rx_max - rx_min + 1) * (ry_max - ry_min + 1)
        if area > max_area:
            has_segments_crossing = False
            for s in range(len(points)):
                sx_min = min(points[s][0], points[s-1][0])
                sx_max = max(points[s][0], points[s-1][0])
                sy_min = min(points[s][1], points[s-1][1])
                sy_max = max(points[s][1], points[s-1][1])
                crosses_rectangle = not (sx_min >= rx_max or sx_max <= rx_min or sy_min >= ry_max or sy_max <= ry_min)
                if (crosses_rectangle):
                    has_segments_crossing = True
                    break
            if not has_segments_crossing:
                max_area = area

print(max_area)