import re

filename = "2022/data/14.txt"

with open(filename) as f:
    input_lines = [line.rstrip() for line in f]


def process_input(lines):
    s_map = {(500, 0): "x"}

    for this_line in lines:
        # Start from the 2nd set and look back at the previous
        x_index = 2
        y_index = 3

        rock_coords = [int(y) for y in re.split(",| -> ", this_line)]
        # Example result: [498, 4, 498, 6, 496, 6]

        while y_index < len(rock_coords):
            # Starting with the 2nd set and looking back at the previous set, figure out their
            # difference and whether we are moving horizontal or vertical, and positive or negative
            current_x, current_y = [rock_coords[x_index - 2], rock_coords[y_index - 2]]
            end_x, end_y = [rock_coords[x_index], rock_coords[y_index]]

            x_diff = end_x - current_x
            y_diff = end_y - current_y
            x_inc = y_inc = 0  # By default we increase by zero to avoid div/0 in this if block
            if x_diff:
                x_inc = x_diff // abs(
                    x_diff
                )  # Gets direction of change (1 if positive, -1 if negative)
                end_x += x_inc  # Prevents off-by-one error where final coord isn't added
            if y_diff:
                y_inc = y_diff // abs(y_diff)
                end_y += y_inc

            # Add lines from current (start) to end
            while current_x != end_x or current_y != end_y:
                s_map[(current_x, current_y)] = "#"
                current_x += x_inc
                current_y += y_inc

            x_index += 2
            y_index += 2
    return s_map


def pour_sand(s_map: dict, c_floor: int, part2: bool):
    # Drops a single unit of sand and adds its resting position to the map
    # Returns the updated sand map (s_map) and a bool indicating whether we
    # should continue dropping sand. True = continue; False = stop
    origin = (500, 0)
    sand_x, sand_y = origin
    max_y = max([k[1] for k in s_map])

    while True:
        # If part 2, check if we are just above the floor
        if sand_y + 1 == c_floor and part2:
            s_map[(sand_x, sand_y)] = "o"
            return sand_map, True
        # If part 1, check if we are falling into the abyss
        elif sand_y > max_y and not part2:
            return s_map, False
        # Check the 3 possible locations in order of preference
        elif (sand_x, sand_y + 1) not in s_map:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in s_map:
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in s_map:
            sand_x += 1
            sand_y += 1
        # If the sand can't move and is at the origin, Part 2 is done.
        elif (sand_x, sand_y) == origin:
            s_map[(sand_x, sand_y)] = "o"
            return sand_map, False
        # The sand has stopped moving so we add it to the map and stop looping
        else:
            s_map[(sand_x, sand_y)] = "o"
            break

    return sand_map, True


def display_map(s_map):
    min_x = min([k[0] for k in s_map]) - 1
    max_x = max([k[0] for k in s_map]) + 2
    min_y = min([k[1] for k in s_map]) - 1
    max_y = max([k[1] for k in s_map]) + 2

    for this_row in range(min_y, max_y):
        row_print = ""
        for this_col in range(min_x, max_x):
            if (this_col, this_row) not in s_map.keys():
                row_print += "???"
            elif s_map[(this_col, this_row)] == "#":
                row_print += "???"
            elif s_map[(this_col, this_row)] == "o":
                row_print += "????"
            elif s_map[(this_col, this_row)] == "x":
                row_print += "???"
        print(row_print)


# Change to False to do part 1
do_part_2 = True  # FYI part 2 takes about 10 seconds to run :(

sand_map = process_input(input_lines)
cave_floor = max([k[1] for k in sand_map]) + 2

keep_going = True

while keep_going:
    sand_map, keep_going = pour_sand(sand_map, cave_floor, do_part_2)

if not do_part_2:
    # Part 2 map is too big and kind of boring
    display_map(sand_map)

sand_count = len([sand_map[f] for f in sand_map if sand_map[f] == "o"])
print(f"Result: {sand_count}")
