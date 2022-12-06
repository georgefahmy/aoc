with open("2022/data/6_input_data.txt", "r") as input:
    data = [i.strip() for i in input.readlines()]

data = data[0]

part1 = 4
part2 = 14

i = part1  # (or part2)
for i in range(len(data)):
    substring = data[i - part1 : i]
    if len(set(substring)) == part1:
        print(i, substring)
        break
