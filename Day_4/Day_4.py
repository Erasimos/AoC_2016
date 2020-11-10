import ut


def get_room_data():
    raw_data = ut.read_file('input.txt').split()
    room_data = []
    for raw_room in raw_data:
        room = raw_room.split('-')
        sector_id = int(room[len(room)-1].split('[')[0])
        checksum = room[len(room)-1].split('[')[1].replace(']', '')
        room_name = room[0:len(room)-1]
        final_room = [room_name, sector_id, checksum]
        room_data.append(final_room)

    return room_data


def valid_room(name, checksum):
    freq_by_char = {}
    for word in name:
        for char in word:

            try:
                freq_by_char[char] = freq_by_char[char] + 1
            except KeyError:
                freq_by_char[char] = 1

    freq_by_occurrence = {}
    for char in freq_by_char.keys():

        occurrences = freq_by_char[char]

        try:
            freq_by_occurrence[occurrences].append(char)
        except KeyError:
            freq_by_occurrence[occurrences] = [char]

    occurrence_keys = sorted(freq_by_occurrence.keys(), reverse=True)

    ordered_characters = []

    for occurrence_key in occurrence_keys:
        current_characters = sorted(freq_by_occurrence[occurrence_key])
        ordered_characters.extend(current_characters)
    new_checksum = ''.join(ordered_characters[0:5])

    return new_checksum == checksum


def shift_char(char, shift):

    # 0 equals a
    alpha_order = ord(char) - 97
    shift = shift % 26
    new_alpha_order = (alpha_order + shift) % 26
    new_char = chr(new_alpha_order + 97)

    return new_char


def decrypt_room(name, sector_id):

    decrypted_name = ''

    for word in name:
        for char in word:
            new_char = shift_char(char, sector_id)
            decrypted_name += new_char
        decrypted_name += ' '

    return decrypted_name


def print_valid_rooms():
    rooms = get_room_data()

    for room in rooms:
        room_name = room[0]
        sector_id = room[1]
        checksum = room[2]
        if valid_room(room_name, checksum):
            decrypted_name = decrypt_room(room_name, sector_id)
            print('NAME:' + decrypted_name + '  ID: ' + str(sector_id))


def get_sector_id_sum():
    rooms = get_room_data()
    sector_id_sum = 0

    for room in rooms:
        room_name = room[0]
        sector_id = room[1]
        checksum = room[2]

        if valid_room(room_name, checksum):
            sector_id_sum += sector_id

    return sector_id_sum


print_valid_rooms()
