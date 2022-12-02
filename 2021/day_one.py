from itertools import pairwise, islice

with open("2021/data/day_one_input_data.txt","r") as input:
    data = [int(i.strip()) for i in input.readlines()]

paired_data = list(pairwise(data))

increases = 0
for val1, val2 in paired_data:
    if int(val2) > int(val1):
        increases += 1

triple_vals = []
for i, val in enumerate(data):
    triple_vals.append(sum(islice(data[i:],3)))

increases = 0
for val1, val2 in list(pairwise(triple_vals)):
    if int(val2) > int(val1):
        increases += 1
