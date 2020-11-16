import ut

def get_tile_type(triplet):
    if triplet[0] == triplet[1] and not triplet[0] == triplet[2]:
        return '^'
    elif triplet[1] == triplet[2] and not triplet[0] == triplet[1]:
        return '^'
    else:
        return '.'


def get_triplet(row, row_index):
    triplet = [row[index] if len(row) > index >= 0 else '.' for index in range(row_index-1, row_index+2)]
    return triplet


def get_triplets(row):
    return [get_triplet(row, row_index) for row_index in range(0, len(row))]


def get_next_row(current_row):
    triplets = get_triplets(current_row)
    return ''.join([get_tile_type(triplet) for triplet in triplets])


def generate_map(current_row, rows):
    trap_map = [current_row]
    while len(trap_map) < rows:
        current_row = get_next_row(current_row)
        trap_map.append(current_row)
    return trap_map


def count_safe_tile(trap_map: list[list]):

    return sum([row.count('.') for row in trap_map])


first_row = ut.read_file('input.txt')
tr_map = generate_map(first_row, 400000)
print('Safe tiles: ' + str(count_safe_tile(tr_map)))


