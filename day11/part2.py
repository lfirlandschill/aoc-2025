from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

connections = {}
for line in lines:
    device = line.split(':')[0]
    connects_to = line.split(':')[1].strip().split()
    connections[device] = connects_to

memo = {}
def DFS(device, seen_dac, seen_fft):
    if device == "dac":
        seen_dac = True
    if device == "fft":
        seen_fft = True
    key = (device, seen_dac, seen_fft)
    if key in memo:
        return memo[key]
    if (device == 'out'):
        return 1 if seen_dac and seen_fft else 0
    paths = 0
    for connection in connections.get(device, []):
        paths += DFS(connection, seen_dac, seen_fft)
    memo[key] = paths
    return paths

res = DFS('svr', False, False)
print(res)