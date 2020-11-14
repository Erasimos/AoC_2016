

def invert_bit(bit):
    if bit == '0':
        return '1'
    elif bit == '1':
        return '0'


def invert_data(data):
    return ''.join([invert_bit(bit) for bit in data])


def extend_data(data):
    return data + '0' + invert_data(data[::-1])


def generate_data(data_input, size):

    data = data_input
    while len(data) < size:
        data = extend_data(data)
    return data[0:size]


def calc_checksum_2(checksum):
    new_checksum = ''
    index = 0
    while index < len(checksum) - 1:
        pair = checksum[index:index+2]
        if pair[0] == pair[1]:
            new_checksum += '1'
        else:
            new_checksum += '0'
        index += 2
    return new_checksum


def calc_checksum(data):
    checksum = data
    while True:
        checksum = calc_checksum_2(checksum)
        if not len(checksum) % 2 == 0:
            return checksum


input_data = '11100010111110100'
generated_data = generate_data(input_data, 35651584)
print(calc_checksum(generated_data))
