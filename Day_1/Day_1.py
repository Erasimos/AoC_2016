import ut
from enum import Enum


def get_facing(current_face, dir):

    if dir == 'R':
        return (current_face + 1) % 4
    elif dir == 'L':
        return (current_face - 1) % 4


def delta_movement(facing):
    if facing == 0:
        return 0, 1
    elif facing == 1:
        return 1, 0
    elif facing == 2:
        return 0, -1
    elif facing == 3:
        return -1, 0


def get_directions():
    raw_directions = ut.read_file('input.txt').split(', ')
    final_directions = []
    for direction in raw_directions:
        dir = direction[0]
        steps = int(direction[1:])
        final_directions.append((dir, steps))
    return final_directions


def is_visited(positions, pos):
    try:
        x = positions[pos]
        return True
    except KeyError:
        return False


def get_destination():
    directions = get_directions()
    positions = {(0, 0): 1}
    facing = 0
    x_pos = 0
    y_pos = 0

    for direction in directions:
        facing = get_facing(facing, direction[0])

        delta_mov = delta_movement(facing)
        for i in range(0,direction[1]):
            x_pos = x_pos + delta_mov[0]
            y_pos = y_pos + delta_mov[1]

            if is_visited(positions, (x_pos, y_pos)):
                return x_pos, y_pos
            else:
                positions[(x_pos, y_pos)] = 1

        
print(get_destination())