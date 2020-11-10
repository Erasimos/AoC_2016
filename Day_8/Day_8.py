import ut


def get_instructions():
    raw_data = ut.read_file_lines('input.txt')
    instructions = [item.split() for item in raw_data]
    print(instructions)
    return instructions


def rect(w, h, display):

    for row in range(0, h):
        for column in range(0, w):
            display[row][column] = '#'
    return display


def rotate_row(row, offset, display):

    show_display(display)

    pixel_row = display[row].copy()

    for i in range(0, len(pixel_row)):
        index = (i + offset) % len(pixel_row)
        display[row][index] = pixel_row[i]

    show_display(display)
    return display


def rotate_column(column, offset, display):

    show_display(display)
    pixel_column = [display[row][column] for row in range(0, len(display))]

    for i in range(0, len(display)):
        index = (i + offset) % len(display)
        display[index][column] = pixel_column[i]

    show_display(display)
    return display


def do_instr(instruction, display):

    operation = instruction[0]

    if operation == 'rect':
        dimensions = instruction[1].split('x')
        display = rect(int(dimensions[0]), int(dimensions[1]), display)

    elif operation == 'rotate':

        offset = int(instruction[4])

        if instruction[1] == 'row':
            row = int(instruction[2].split('y=')[1])
            display = rotate_row(row, offset, display)

        elif instruction[1] == 'column':
            column = int(instruction[2].split('x=')[1])
            display = rotate_column(column, offset, display)

    return display


def count_lit_pixels(display):
    count = 0

    for row in range(0, len(display)):
        for column in range(0, len(display[0])):
            if display[row][column] == '#':
                count += 1
    print('COUNT: ' + str(count))


def show_display(display):

    for row in range(0, len(display)):
        for column in range(0, len(display[0])):
            print(display[row][column], end='')
        print()
    print()
    return


def part_one():
    instructions = get_instructions()
    height = 6
    width = 50
    display = [['.' for j in range(width)] for i in range(height)]

    # Do all instructions
    for instruction in instructions:
        display = do_instr(instruction, display)

    # Display the display
    show_display(display)
    count_lit_pixels(display)





part_one()