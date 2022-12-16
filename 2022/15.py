import re

def distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
def abcd2abr(a,b,c,d): return (a,b,distance((a,b),(c,d)))

max_n = 4000000
raw_data = open("2022/data/15.txt").read().split("\n")
data = [abcd2abr(*map(int,re.findall(r'[-]*\d+', line))) for line in raw_data[:-1]]

def line_intervals(line):
    return sorted([ (x - d, x + d) for x, y, r in data for d in [r-abs(line-y)] if d >= 0])


intervals = line_intervals(max_n//2)
start, stop, holes = *intervals[0], 0

for nstart, nstop in intervals:
    holes, stop = max(0, nstart-stop-1), max(stop, nstop)

print("Part1:", stop - start - holes)

a = set(x-y+r+1 for x,y,r in data).intersection(x-y-r-1 for x,y,r in data).pop()
b = set(x+y+r+1 for x,y,r in data).intersection(x+y-r-1 for x,y,r in data).pop()

print("Part2:", (a+b)*max_n//2+(b-a)//2)
