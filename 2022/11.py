import re
import math


class Monkey:
    def __init__(self, s):
        lines = s.split("\n")
        self.items = [int(i) for i in [n.split(",") for n in lines[1].split(": ")[1:]][0]]
        if not re.search("\d", lines[2]):
            self.op = (lambda x: x * x) if "*" in lines[2] else (lambda x: x + x)
        else:
            y = int(re.findall("\d+", lines[2])[0])
            self.op = (lambda x: x * y) if "*" in lines[2] else (lambda x: x + y)
        self.test = int(lines[3].split()[-1])
        self.if_true = int(lines[4].split()[-1])
        self.if_false = int(lines[5].split()[-1])
        self.inspections = 0

    def turn(self, monkeys, lcm):
        for item in self.items:
            self.inspections += 1
            item = self.op(item)
            item = item % lcm if lcm else item // 3
            monkeys[self.if_false if item % self.test else self.if_true].items.append(item)
        self.items = []


def run_sim(monkeys, rounds, lcm):
    for _ in range(rounds):
        for m in monkeys:
            m.turn(monkeys, lcm)


def monkey_business(monkeys):
    x = sorted([m.inspections for m in monkeys], reverse=True)
    return x[0] * x[1]


def part1():
    monkeys = [Monkey(s) for s in open("2022/data/11.txt", "r").read().split("\n\n")]
    run_sim(monkeys, 20, 0)
    print(monkey_business(monkeys))


def part2():
    monkeys = [Monkey(s) for s in open("2022/data/11.txt", "r").read().split("\n\n")]
    run_sim(monkeys, 10_000, math.lcm(*[m.test for m in monkeys]))
    print(monkey_business(monkeys))
