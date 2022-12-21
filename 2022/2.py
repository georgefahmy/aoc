with open("2022/data/2_input_data.txt","r") as input:
    data = [i.strip() for i in input.readlines()]

def win_part1(opponent, me):
    moves = {
        "A": {"X": 4, "Y": 8, "Z": 3},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 7, "Y": 2, "Z": 6},
    }
    return moves[opponent][me]


def win_part2(opponent, me):
    moves = {
        "A": {"X": 3, "Y": 4, "Z": 8},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 2, "Y": 6, "Z": 7},
    }
    return moves[opponent][me]

points_pt1 = sum([win_part1(round.split()[0], round.split()[1]) for round in data])
points_pt2 = sum([win_part2(round.split()[0], round.split()[1]) for round in data])
