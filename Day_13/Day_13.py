import math


# Returns the valid neighbours, that are not out of bounds, to a current position
def get_neighbours(position):
    old_x = position[0]
    old_y = position[1]
    neighbours = []
    delta_movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for delta_movement in delta_movements:
        d_x = delta_movement[0]
        d_y = delta_movement[1]
        new_x = old_x + d_x
        new_y = old_y + d_y
        # A long as both are positive then it is a valid position
        if new_x > -1 and new_y > -1:
            neighbours.append((new_x, new_y))

    return neighbours


# Returns True if specified position is not a wall
def is_open_pos(position):
    x = position[0]
    y = position[1]

    favourite_number = 1364
    wall_sum = x*x + 3*x + 2*x*y + y + y*y + favourite_number
    binary_sum = str(bin(wall_sum))
    # Count the number of 1's
    one_count = 0
    for bit in binary_sum:
        if bit == '1':
            one_count += 1
    # Check if number of 1's is even
    if one_count % 2 == 0:
        return True
    else:
        return False


# Returns true if a position is visited
def is_visited(position, visited: dict):
    return visited.get(position, False)


def print_maze(x_size, y_size):
    for x_pos in range(0, x_size):
        for y_pos in range(0, y_size):
            if is_open_pos((x_pos, y_pos)):
                print('.', end='')
            else:
                print('#', end='')
        print()


# Shortest path through the maze, from (0, 0) to a specified position
def shortest_path(current_pos, destination_pos, visited: dict, steps):

    if steps > 50:
        return math.inf

    # if current position is destination, return steps
    elif current_pos == destination_pos:
        return steps

    # Otherwise keep searching

    # Add current position to visited
    visited[current_pos] = True

    neighbours = get_neighbours(current_pos)
    next_steps = []

    # Move in every direction
    for neighbour in neighbours:
        if is_open_pos(neighbour) and not is_visited(neighbour, visited):
            next_steps.append(shortest_path(neighbour, destination_pos, visited.copy(), steps + 1))
    # If you moved to a dead end, return infinity
    if not next_steps:
        return math.inf
    # Return the minimum steps from moving in any direction
    else:
        return min(next_steps)


count = 0
for x in range(0, 52):
    for y in range(0, 52):
        new_destination = (x, y)
        if is_open_pos(new_destination):
            the_steps = shortest_path((1, 1), new_destination, {}, 0)
            if the_steps <= 50:
                count += 1
                print("COUNT:" + str(count))
print(count)


