import networkx


grid = [list(ln) for ln in open("2022/data/12.txt", "r").read().strip().split("\n")]
rows, cols = len(grid), len(grid[0])

start_x, start_y, end_x, end_y = 0, 0, 0, 0
for y in range(rows):
    for x in range(cols):
        if grid[y][x] == "S":
            start_x, start_y = x, y
            grid[y][x] = "a"
        elif grid[y][x] == "E":
            end_x, end_y = x, y
            grid[y][x] = "z"

G = networkx.DiGraph()
for y in range(rows):
    for x in range(cols):
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                A = ord(grid[y][x]) - 96
                B = ord(grid[ny][nx]) - 96
                if B <= A + 1:
                    G.add_edge((x, y), (nx, ny))

p = networkx.shortest_path(G, (start_x, start_y), (end_x, end_y))
print(len(p) - 1)

m = 1000000
for y in range(rows):
    for x in range(cols):
        if grid[y][x] == "a":
            try:
                p = networkx.shortest_path(G, (x, y), (end_x, end_y))
                m = min(m, len(p) - 1)
            except:
                pass

print(m)
