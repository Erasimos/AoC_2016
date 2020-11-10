import hashlib
import math


def starts_with_five_zeroes(hsh):

    for i in range(0, 5):
        if not hsh[i] == str(0):

            return False
    return True


def find_password(door_id):
    password = [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf]
    index = 3231929
    password_positions = [0, 1, 2, 3, 4, 5, 6, 7]

    while len(password_positions) > 0:

        # Generate hash

        hash_input = (door_id + str(index)).encode()

        md5_hash = (hashlib.md5(hash_input)).hexdigest()

        if starts_with_five_zeroes(md5_hash):
            password_index = int(md5_hash[5], 16)
            password_char = md5_hash[6]

            if password_index in password_positions:
                password_positions.remove(password_index)
                password[password_index] = password_char
                print(password)

        index += 1

    print(password)
    return password


find_password('uqwqemis')
