import ut


def get_triangles():
    raw_triangles = ut.read_file('input.txt').split()
    column_1 = []
    column_2 = []
    column_3 = []

    index = 0
    while index < len(raw_triangles):
        row = raw_triangles[index:(index + 3)]

        column_1.append(row[0])
        column_2.append(row[1])
        column_3.append(row[2])

        index += 3

    return column_1, column_2, column_3


def valid(triangle):

    side_1 = int(triangle[0])
    side_2 = int(triangle[1])
    side_3 = int(triangle[2])

    if ((side_1 + side_2) > side_3) and (side_1 + side_3) > side_2 and (side_2 + side_3) > side_1:
        return True
    else:
        return False


def count_invalid_triangles():
    (column_1, column_2, column_3) = get_triangles()
    number_of_valid = 0
    index = 0
    while index < len(column_1):
        triangle_1 = column_1[index:(index + 3)]
        triangle_2 = column_2[index:(index + 3)]
        triangle_3 = column_3[index:(index + 3)]

        if valid(triangle_1):
            number_of_valid += 1

        if valid(triangle_2):
            number_of_valid += 1

        if valid(triangle_3):
            number_of_valid += 1

        index += 3

    return number_of_valid


print(count_invalid_triangles())

