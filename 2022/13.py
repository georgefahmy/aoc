import sys
import json
from functools import cmp_to_key

sys.setrecursionlimit(3000000)

pairs = open("2022/data/13.txt", "r").read().split("\n\n")


def compare(a, b):
    if type(a) == int:
        if type(b) == int:
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0
        else:
            a = [a]
    if type(b) == int:
        if type(a) == int:
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0
        else:
            b = [b]
    for i in range(min(len(a), len(b))):
        res = compare(a[i], b[i])
        if res != 0:
            return res
    if len(a) < len(b):
        return -1
    if len(a) > len(b):
        return 1
    return 0


s = 0
for j, pair in enumerate(pairs):
    x = pair.split("\n")
    left = json.loads(pair[0])
    right = json.loads(pair[1])
    if compare(left, right) < 0:
        s += j + 1

print(s)

# part2
w = []
for i, l in enumerate(pairs):
    ps = l.split("\n")
    if len(ps) >= 2:
        try:
            l1 = json.loads(ps[0])
            l2 = json.loads(ps[1])
            w.append(l1)
            w.append(l2)
        except json.decoder.JSONDecodeError:
            pass

w.append([[2]])
w.append([[6]])
w.sort(key=cmp_to_key(compare))

print((w.index([[2]]) + 1) * (w.index([[6]]) + 1))
