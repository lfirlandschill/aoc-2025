from pathlib import Path

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

connections = {}
for line in lines:
    device = line.split(':')[0]
    connects_to = line.split(':')[1].strip().split()
    connections[device] = connects_to

def DFS(device):
    if (device == 'out'):
        return 1
    paths = 0
    for connection in connections[device]:
        paths += DFS(connection)
    return paths

res = DFS('you')
print(res)