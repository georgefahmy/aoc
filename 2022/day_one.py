with open("2022/data/input_data.txt","r") as input:
    data = [i.strip() for i in input.readlines()]

total_sums = []
elf_sum = 0
for item in data:
    if not item:
        total_sums.append(elf_sum)
        elf_sum = 0
    elf_sum = elf_sum + int(item)

top_three = sorted(total_sums)[-3:]
top_three_sum = sum(top_three)
