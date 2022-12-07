commands = [
    (lambda xs: (xs[0], xs[1:]))(x.split("\n"))
    for x in open("2022/data/7.txt").read().replace("\n$", "$").split("$ ")[1:]
]

# Build directory structure
data_structure = {"/": {}}
cs = data_structure
for c, o in commands:
    if c[:3] == "cd ":
        cs = cs[c[3:]]
        continue
    for l in o:
        if l[:4] == "dir ":
            cs[l[4:]] = {"..": cs}
            continue
        if not l:
            continue
        sz, f = l.split(" ")
        cs[f] = int(sz)

# Compute directory sizes
def dirsizes(name, data_structure, acc):
    acc[name] = sum(
        v if isinstance(v, int) else dirsizes(name + "/" + k, v, acc)[0]
        for k, v in ds.items()
        if k != ".."
    )
    return acc[name], acc


_, acc = dirsizes("", data_structure["/"], {})
sum(filter(lambda e: e <= 100000, acc.values()))  # Part 1
min(filter(lambda e: e >= acc[""] - 40000000, acc.values()))  # Part 2
