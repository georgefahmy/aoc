from itertools import pairwise, islice

with open("2021/data/day_two_input_data.txt","r") as input:
    data = [i.strip() for i in input.readlines()]

forward_total = 0
depth_total = 0
for direction in data:
    if direction.split()[0] == "forward":
        forward_total += int(direction.split()[-1])
    if direction.split()[0] == "down":
        depth_total += int(direction.split()[-1])
    if direction.split()[0] == "up":
        depth_total -= int(direction.split()[-1])

part_1_total = depth_total * forward_total

forward_total = 0
depth_total = 0
aim = 0
for direction in data:
    if direction.split()[0] == "forward":
        forward_total += int(direction.split()[-1])
        depth_total += aim * int(direction.split()[-1])
    if direction.split()[0] == "down":
        aim += int(direction.split()[-1])
    if direction.split()[0] == "up":
        aim -= int(direction.split()[-1])

part_2_total = depth_total * forward_total
