import ut


def get_instructions():
    return ut.read_file('input.txt').splitlines()


def get_digits_map():
    digit_map = {(2, 4): 1,
                 (1, 3): 2,
                 (2, 3): 3,
                 (3, 3): 4,
                 (0, 2): 5,
                 (1, 2): 6,
                 (2, 2): 7,
                 (3, 2): 8,
                 (4, 2): 9,
                 (1, 1): 'A',
                 (2, 1): 'B',
                 (3, 1): 'C',
                 (2, 0): 'D'}
    return digit_map


def get_delta_movement(direction):
    if direction == 'U':
        return 0, 1
    elif direction == 'R':
        return 1, 0
    elif direction == 'D':
        return 0, -1
    elif direction == 'L':
        return -1, 0


def out_of_bounds(position, digit_map):
    try:
        digit = digit_map[position]
        return False
    except KeyError:
        return True


def move(instruction, position, digit_map):
    current_pos = position
    for direction in instruction:
        delta_movement = get_delta_movement(direction)
        new_x = current_pos[0] + delta_movement[0]
        new_y = current_pos[1] + delta_movement[1]
        if not out_of_bounds((new_x, new_y), digit_map):
            current_pos = (new_x, new_y)
    return current_pos


def get_bathroom_code():
    code = []
    current_pos = (0, 2)
    digit_map = get_digits_map()
    instructions = get_instructions()

    for instruction in instructions:
        new_pos = move(instruction, current_pos, digit_map)
        new_digit = digit_map[new_pos]
        current_pos = new_pos
        code.append(new_digit)
    return code


print(get_bathroom_code())