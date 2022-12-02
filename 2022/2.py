
#rock = 1 point
#paper = 2 points
#scissors = 3 points

with open("2022/data/day_two_input_data.txt","r") as input:
    data = [i.strip() for i in input.readlines()]


win_with_rock = 1
win_with_paper = 2
win_with_scissors = 3
win = 6
tie = 3
loss = 0

#X = Lose
#Y = Tie
#Z = Win

#Rock = A, X
#Paper = B, Y
#Scissors = C, Z

def win(opponent, me):
    if opponent == "A":
        #op_shape = "Rock"
        if me == "X":
            #Lose
            #my_shape = "Scissors"
            return 0 + 3
        if me == "Y":
            #Tie
            #my_shape = "Rock"
            return 3 + 1
        if me == "Z":
            #Win
            #my_shape = "Paper"
            return 6 + 2

    if opponent == "B":
        #op_shape = "Paper"
        if me == "X":
            #Lose
            #my_shape = "Rock"
            return 0 + 1
        if me == "Y":
            #Tie
            #my_shape = "Paper"
            return 3 + 2
        if me == "Z":
            #Win
            #my_shape = "Scissors"
            return 6 + 3
    if opponent == "C":
        #op_shape = "Scissors"
        if me == "X":
            #Lose
            #my_shape = "Paper"
            return 0 + 2
        if me == "Y":
            #Tie
            #my_shape = "Scissors"
            return 3 + 3
        if me == "Z":
            #Win
            #my_shape = "Rock"
            return 6 + 1
total = []
for round in data:
    total.append(win(round.split()[0],round.split()[1]))
