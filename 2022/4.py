with open("2022/data/4_input_data.txt", "r") as input:
    data = [i.strip() for i in input.readlines()]


def elf_range(elf):
    return list(range(int(elf.split("-")[0]), int(elf.split("-")[1]) + 1))


fully_contains = 0
for pairs in data:
    elf1, elf2 = pairs.split(",")[0], pairs.split(",")[1]
    elf1_range = elf_range(elf1)
    elf2_range = elf_range(elf2)
    elf1_min, elf1_max = min(elf1_range), max(elf1_range)
    elf2_min, elf2_max = min(elf2_range), max(elf2_range)
    if elf1_min <= elf2_min and elf1_max >= elf2_max:
        print(pairs)
        fully_contains += 1
    elif elf2_min <= elf1_min and elf2_max >= elf1_max:
        print(pairs)
        fully_contains += 1


# part2
overlap_total = 0
for pairs in data:
    elf1, elf2 = pairs.split(",")[0], pairs.split(",")[1]
    elf1_range = elf_range(elf1)
    elf2_range = elf_range(elf2)
    overlap = set(elf1_range).intersection(elf2_range)
    if len(overlap):
        overlap_total += 1
