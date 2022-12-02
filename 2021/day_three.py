from collections import Counter

#gamma rate
#epsilon rate
#power = gamma * epsilon

#gamma rate = most common bit in the corresponding position of all the numbers
#epsilon rate = least common bit in the corresponding position of all the numbers

with open("2021/data/day_three_input_data.txt","r") as input:
    data = [i.strip() for i in input.readlines()]

# Initialize the two values we want
gamma_rate = ""
epsilon_rate = ""
for bit in range(len(data[0])):
    c = Counter()
    for val in data:
        c.update([val[bit]])
    gamma_rate = gamma_rate + str(max(c, key=c.get))
    epsilon_rate = epsilon_rate + str(min(c, key=c.get))

part_1_answer = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(part_1_answer)

### Part 2 ###

# iterate through each bit for each remaining value in the data
ind = 0
while len(data) > 1:
    #initialize the counter
    c = Counter()
    #count how many of each 1/0 and identify the one that has more
    for val in data:
        c.update([val[ind]])

    #if the count of 1s and 0s is the same, the val to keep is 1 otherwise pick the max
    vals_to_keep = "1" if list(c.values())[0] == list(c.values())[1] else str(max(c, key=c.get))

    #only keep the values of the data set where that bit index is equal to the value to keep
    data = [val for val in data if val[ind] == vals_to_keep]

    #cycle through the bit values until left with one value in the dataset, that is the result.
    ind+= 1

oxygen_generator_rating = data[0]

#Reload the original dataset
with open("2021/data/day_three_input_data.txt","r") as input:
    data = [i.strip() for i in input.readlines()]

# iterate through each bit for each remaining value in the data
ind = 0
while len(data) > 1:
    #initialize the counter
    c = Counter()

    #count how many of each 1/0 and identify the one that has more
    for val in data:
        c.update([val[ind]])

    #if the count of 1s and 0s is the same, the val to keep is 0 otherwise pick the min
    vals_to_keep = "0" if list(c.values())[0] == list(c.values())[1] else str(min(c, key=c.get))

    #Only keep the values of the data set where that bit index is equal to the value to keep
    data = [val for val in data if val[ind] == vals_to_keep]

    #cycle through the bit values until left with one value in the dataset, that is the result.
    ind+= 1

co2_scrubber_rating = data[0]

part_2_answer = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)

print(part_2_answer)
