import re

blueprints = open("2022/data/19.txt").read().strip().split("\n")


class Bot:
    def __init__(self, type, ore_cost, clay_cost, obsidian_cost):
        self.type = type
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_cost = obsidian_cost


class Supplies:
    def __init__(self, ore=0, clay=0, obsidian=0, geodes=0):
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geodes = geodes


for blueprint in blueprints:
    ore = 0
    clay = 0
    obsidian = 0
    geodes = 0
    id = blueprint.split(":")[0]
    costs = [x.strip() for x in blueprint.split(":")[1].split(".") if x]
    for minute in range(1, 24):
        for bot in costs:
            for n, type in bot.split("costs ")[-1].split():
                print(type, n)
            if "ore robot" in bot:
                ore_bot_ore_cost = bot.split("costs ")[-1].split()
            elif "clay robot" in bot:
                clay_bot_ore_cost = bot.split("costs ")[-1]
            elif "obsidian robot" in bot:
                obsidian_bot_ore_cost = bot.split("costs ")[-1].split(" and ")[0]
                obsidian_bot_clay_cost = bot.split("costs ")[-1].split(" and ")[1]
            elif "geode robot" in bot:
                geode_bot_ore_cost = bot.split("costs ")[-1].split(" and ")[0]
                geode_bot_obsidian_cost = bot.split("costs ")[-1].split(" and ")[1]


def theirs():

    import sys
    import math
    from copy import deepcopy
    from collections import defaultdict, deque

    infile = "2022/data/19.txt"
    data = open(infile).read().strip()
    lines = [x for x in data.split("\n")]

    def solve(Co, Cc, Co1, Co2, Cg1, Cg2, T):
        best = 0
        # state is (ore, clay, obsidian, geodes, r1, r2, r3, r4, time)
        S = (0, 0, 0, 0, 1, 0, 0, 0, T)
        Q = deque([S])
        SEEN = set()
        while Q:
            state = Q.popleft()
            # print(state)
            o, c, ob, g, r1, r2, r3, r4, t = state
            best = max(best, g)
            if t == 0:
                continue
            Core = max([Co, Cc, Co1, Cg1])
            if r1 >= Core:
                r1 = Core
            if r2 >= Co2:
                r2 = Co2
            if r3 >= Cg2:
                r3 = Cg2
            if o >= t * Core - r1 * (t - 1):
                o = t * Core - r1 * (t - 1)
            if c >= t * Co2 - r2 * (t - 1):
                c = t * Co2 - r2 * (t - 1)
            if ob >= t * Cg2 - r3 * (t - 1):
                ob = t * Cg2 - r3 * (t - 1)
            state = (o, c, ob, g, r1, r2, r3, r4, t)
            if state in SEEN:
                continue
            SEEN.add(state)
            if len(SEEN) % 1000000 == 0:
                print(t, best, len(SEEN))
            assert o >= 0 and c >= 0 and ob >= 0 and g >= 0, state
            Q.append((o + r1, c + r2, ob + r3, g + r4, r1, r2, r3, r4, t - 1))
            if o >= Co:  # buy ore
                Q.append((o - Co + r1, c + r2, ob + r3, g + r4, r1 + 1, r2, r3, r4, t - 1))
            if o >= Cc:
                Q.append((o - Cc + r1, c + r2, ob + r3, g + r4, r1, r2 + 1, r3, r4, t - 1))
            if o >= Co1 and c >= Co2:
                Q.append((o - Co1 + r1, c - Co2 + r2, ob + r3, g + r4, r1, r2, r3 + 1, r4, t - 1))
            if o >= Cg1 and ob >= Cg2:
                Q.append((o - Cg1 + r1, c + r2, ob - Cg2 + r3, g + r4, r1, r2, r3, r4 + 1, t - 1))
        return best

    p1 = 0
    p2 = 1
    for i, line in enumerate(lines):
        words = line.split()
        id_ = int(words[1][:-1])
        ore_cost = int(words[6])
        clay_cost = int(words[12])
        obsidian_cost_ore, obsidian_cost_clay = int(words[18]), int(words[21])
        geode_cost_ore, geode_cost_clay = int(words[27]), int(words[30])
        s1 = solve(
            ore_cost,
            clay_cost,
            obsidian_cost_ore,
            obsidian_cost_clay,
            geode_cost_ore,
            geode_cost_clay,
            24,
        )
        p1 += id_ * s1
        if i < 3:
            s2 = solve(
                ore_cost,
                clay_cost,
                obsidian_cost_ore,
                obsidian_cost_clay,
                geode_cost_ore,
                geode_cost_clay,
                32,
            )
            p2 *= s2
    print(p1)
    print(p2)
