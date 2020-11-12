from itertools import combinations
import math


# Return a layout of all the floors,
# key = floor number, value = contents
def get_floors():
    floors = {1: ['HM', 'LM'],
              2: ['HG'],
              3: ['LG'],
              4: []}

    return floors


# Checks if all but floor 4 is empty
def all_on_floor_four(floors):
    if floors[1] or floors[2] or floors[3]:
        return False
    else:
        return True


# Checks if there is a generator on the floor
def exists_generator(floor_layout):
    for floor_item in floor_layout:
        second_char = floor_item[1]
        if second_char == 'G':
            return True
    return False


# Check if a floor explodes
def explodes(floor_layout: list):

    for floor_item in floor_layout:
        first_char = floor_item[0]
        second_char = floor_item[1]

        # if it is a micro_controller
        if second_char == 'M':
            if (first_char + 'G') not in floor_layout and exists_generator(floor_layout):
                return True
    return False


# Return floor layout after moving the cargo to specified floor
def move_cargo_to_floor(old_layout: dict, cargo: list, previous_floor, current_floor):

    new_layout = old_layout.copy()

    # remove cargo from previous floor
    for cargo_item in cargo:
        new_layout[previous_floor].remove(cargo_item)

    # add cargo to current_floor
    new_layout[current_floor] = new_layout[current_floor] + cargo

    return new_layout


def part_one(current_floor, prev_layouts: list, current_layout, steps):

    print(current_layout)

    if current_layout in prev_layouts:
        return math.inf

    # Breaks and return steps if everything is on flour four
    if all_on_floor_four(current_layout):
        return steps

    # all combination of possible cargo
    cargo_combinations = \
        list(combinations(current_layout[current_floor], 2)) + \
        list(combinations(current_layout[current_floor], 1))
    cargo_combinations = [list(itm) for itm in cargo_combinations]

    prev_layouts.append(current_layout)

    required_steps = []

    # Going up
    if not current_floor == len(current_layout):

        for cargo in cargo_combinations:
            new_layout = move_cargo_to_floor(current_layout.copy(), cargo, current_floor, current_floor + 1)
            if new_layout not in prev_layouts and not explodes(new_layout[current_floor + 1]):
                required_steps.append(part_one(current_floor + 1, prev_layouts.copy(), new_layout, steps + 1))

    # Going down
    if not current_floor == 1:

        for cargo in cargo_combinations:
            new_layout = move_cargo_to_floor(current_layout.copy(), cargo, current_floor, current_floor - 1)
            if new_layout not in prev_layouts and not explodes(new_layout[current_floor + 1]):
                required_steps.append(part_one(current_floor - 1, prev_layouts.copy(), new_layout, steps + 1))

    # Return the minimum steps from going up or down
    return min(required_steps)


print(part_one(1, [], get_floors(), 0))

