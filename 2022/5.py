with open("2022/data/5_input_data.txt","r") as input:
    data = [i.strip() for i in input.readlines()]

stacks = {
    "stack1": ['T', 'P', 'Z', 'C', 'S', 'L', 'Q', 'N'],
    "stack2": ['L', 'P', 'T', 'V', 'H', 'C', 'G'],
    "stack3": ['D', 'C', 'Z', 'F'],
    "stack4": ['G', 'W', 'T', 'D', 'L', 'M', 'V', 'C'],
    "stack5": ['P', 'W', 'C'],
    "stack6": ['P', 'F', 'J', 'D', 'C', 'T', 'S', 'Z'],
    "stack7": ['V', 'W', 'G', 'B', 'D'],
    "stack8": ['N', 'J', 'S', 'Q', 'H', 'W'],
    "stack9": ['R', 'C', 'Q', 'F', 'S', 'L', 'V']
}

instructions = data[10:]

for i in instructions:
    num_to_move = int(i.split()[1])
    from_stack = i.split()[3]
    to_stack = i.split()[5]
    reversed_stack = stacks["stack"+from_stack]
    reversed_stack.reverse()
    stacks["stack"+to_stack] = stacks["stack"+to_stack] + reversed_stack[0:num_to_move]
    remaining_in_stack = reversed_stack[num_to_move:]
    remaining_in_stack.reverse()
    stacks["stack"+from_stack] = remaining_in_stack

final_string = ""
for key, value in stacks.items():
    final_string = final_string + value[-1]


#Part 2
for i in instructions:
    num_to_move = int(i.split()[1])
    from_stack = i.split()[3]
    to_stack = i.split()[5]
    stack = stacks["stack"+from_stack]
    stacks["stack"+to_stack] = stacks["stack"+to_stack] + stack[len(stack) - num_to_move:]
    remaining_in_stack = stack[:len(stack) - num_to_move]
    stacks["stack"+from_stack] = remaining_in_stack

final_string = ""
for key, value in stacks.items():
    final_string = final_string + value[-1]
