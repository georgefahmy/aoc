data = [x.strip() for x in open("2022/data/25.txt").readlines()]

smap = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
dmap = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}

dec = sum([sum([smap[c] * (5 ** (len(n) - (i + 1))) for i, c in enumerate(n)]) for n in data])

s = dmap[(dec % 5) - 2]
while dec := (dec - ((dec + 2) % 5) + 2) // 5:
    s += dmap[((dec + 2) % 5) - 2]

ans = s[::-1]
print(ans)
