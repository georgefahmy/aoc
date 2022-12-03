with open("2022/data/3_input_data.txt","r") as input:
    data = [i.strip() for i in input.readlines()]


def letter_map(letter):
    if letter.isupper():
        point = ord(letter) - 38
    else:
        point = ord(letter) - 96
    return point

#part 1
total = 0
for rucksack in data:
    rl = len(rucksack)
    common_letter = list(set(rucksack[:int(rl/2)]).intersection(rucksack[int(rl/2):]))[0]
    total += letter_map(common_letter)
print(total)

#part 2
total = 0
groups = list(zip(*[iter(data)]*3))
for group in groups:
    rucksack1 = group[0]
    rucksack2 = group[1]
    rucksack3 = group[2]
    common_letter = list(set(rucksack1).intersection(rucksack2).intersection(rucksack3))[0]
    total += letter_map(common_letter)
