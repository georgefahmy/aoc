import sympy

data = open("2022/data/21.txt").read().strip()
monkeys = {l.split(":")[0].strip(): l.split(":")[1].strip() for l in data.split("\n")}
x = sympy.symbols("x")


def get_monkey_pt1(monk):
    monkey_val = monkeys[monk]
    try:
        val = int(monkey_val)
        return val
    except:
        m1, op, m2 = monkey_val.split(" ")
        m1_val = get_monkey_pt1(m1)
        m2_val = get_monkey_pt1(m2)
        return int(eval(f"{m1_val} {op} {m2_val}"))


def get_monkey_pt2(monk):
    if monk == "humn":
        return x
    monkey_val = monkeys[monk]
    try:
        val = int(monkey_val)
        return val
    except:
        m1, op, m2 = monkey_val.split(" ")
        m1_val = get_monkey_pt2(m1)
        m2_val = get_monkey_pt2(m2)
        if monk == "root":
            return sympy.solve_linear(m1_val, m2_val)
        if op == "+":
            return m1_val + m2_val
        if op == "-":
            return m1_val - m2_val
        if op == "*":
            return m1_val * m2_val
        if op == "/":
            return m1_val / m2_val


get_monkey_pt1("root")
get_monkey_pt2("root")
