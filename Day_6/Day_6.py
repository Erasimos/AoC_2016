import ut
from collections import Counter


def get_corrupted_message():
    message_in_rows = ut.read_file('input.txt').split()
    message_in_columns = [[], [], [], [], [], [], [], []]

    rows = len(message_in_rows)
    cols = len(message_in_rows[0])

    for row in range(0, rows):
        for col in range(0, cols):
            message_in_columns[col].append(message_in_rows[row][col])

    return message_in_columns


def get_most_occurring(char_list):
    occurrence_count = Counter(char_list)
    return occurrence_count.most_common()[-1][0]


def error_correct_message():
    corrupted_message_in_columns = get_corrupted_message()
    corrected_message = ''
    for message_col in corrupted_message_in_columns:
        next_char = get_most_occurring(message_col)
        corrected_message += next_char
    print(corrected_message)


error_correct_message()