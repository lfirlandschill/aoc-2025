from pathlib import Path

path = Path(__file__).parent / "input.txt"
data = [list(line.strip()) for line in open(path)]
nr = len(data)
nc = len(data[0])
map = [["."] * (nc + 2)] + [["."] + list(row) + ["."] for row in data] + [["."] * (nc + 2)]

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

res = 0
converged = False
while not converged:
    nRemoved = 0
    for i in range(1, nr + 1):
        for j in range(1, nc + 1):
            if map[i][j] == "@":
                nRollsAdjacent = 0
                for dir in dirs:
                    if (map[i + dir[0]][j + dir[1]] == "@"):
                        nRollsAdjacent += 1
                if nRollsAdjacent < 4:
                    map[i][j] = "."
                    nRemoved += 1
    res += nRemoved
    if nRemoved == 0:
        converged = True

print(res)