import re
from collections import deque

cubes = set(
    tuple(int(x) for x in line.split(","))
    for line in open("2022/data/18.txt").read().strip().split("\n")
)

# cubes2 = set(map(eval, re.findall("\d+,\d+,\d+", open("2022/data/18.txt").read().strip())))
block = {(a, b, c) for a in range(-1, 21) for b in range(-1, 21) for c in range(-1, 21)} - cubes
delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
sides = lambda x, y, z: {
    (x + a, y + b, c + z) for a, b, c in delta if (x + a, y + b, c + z) in block
}
steam = set()
nodes = deque([(-1, -1, -1)])
while nodes:
    n = nodes.pop()
    steam.add(n)
    nodes.extend(sides(*n) - steam)
print(
    "part1", sum(sum((x + a, y + b, c + z) not in cubes for a, b, c in delta) for x, y, z in cubes)
)
print("part2", sum(sum((x + a, y + b, c + z) in steam for a, b, c in delta) for x, y, z in cubes))
