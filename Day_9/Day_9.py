import ut


def get_compressed_message():
    return ut.read_file('input.txt')


def get_decompressed_length(compressed_message, marker_length, marker_reps, message_index):

    decompressed_length = 0
    start_index = message_index

    while message_index < (start_index + marker_length):

        current_char = compressed_message[message_index]
        if current_char == '(':

            # Read the marker instructions
            message_index += 1
            new_marker_length = ''
            while not compressed_message[message_index] == 'x':
                new_marker_length += compressed_message[message_index]
                message_index += 1

            message_index += 1
            new_marker_reps = ''
            while not compressed_message[message_index] == ')':
                new_marker_reps += compressed_message[message_index]
                message_index += 1

            message_index += 1

            # Count the marker
            new_marker_length = int(new_marker_length)
            new_marker_reps = int(new_marker_reps)

            decompressed_length += \
                get_decompressed_length(compressed_message, new_marker_length, new_marker_reps, message_index)

            message_index += new_marker_length
        else:
            decompressed_length += 1
            message_index += 1

    return decompressed_length * marker_reps


def decompress_message():
    compressed_message = get_compressed_message()
    decompressed_message = ''

    message_index = 0

    while message_index < len(compressed_message):

        current_char = compressed_message[message_index]

        if current_char == '(':
            message_index += 1
            repeat_length = ''
            while not compressed_message[message_index] == 'x':
                repeat_length += compressed_message[message_index]
                message_index += 1

            message_index += 1
            repeats = ''
            while not compressed_message[message_index] == ')':
                repeats += compressed_message[message_index]
                message_index += 1

            message_index += 1
            repeat_string = compressed_message[message_index:(message_index + int(repeat_length))]
            repeated_string = repeat_string * int(repeats)
            decompressed_message += repeated_string
            message_index += int(repeat_length)

        else:
            decompressed_message += current_char
            message_index += 1

    print(decompressed_message)
    print('Length: ' + str(len(decompressed_message)))
    return decompressed_message


a_compressed_message = get_compressed_message()
print(get_decompressed_length(a_compressed_message, len(a_compressed_message), 1, 0))
