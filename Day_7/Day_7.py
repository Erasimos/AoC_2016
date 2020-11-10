import ut
import re


def get_ip_addresses():
    raw_data = ut.read_file('input.txt').split()

    ip_addresses = []
    for address in raw_data:

        new_address = []

        hyper_net_sequences = re.findall("\[([^[\]]*)\]", address)
        non_hyper_net_sequences = re.sub("[\(\[].*?[\)\]]", " ", address).split()
        new_address.append(non_hyper_net_sequences)
        new_address.append(hyper_net_sequences)
        ip_addresses.append(new_address)

    return ip_addresses


def support_abba(address_str):

    for index in range(0, len(address_str)-3):
        first_char = address_str[index]
        second_char = address_str[index + 1]

        if not first_char == second_char:
            third_char = address_str[index + 2]
            fourth_char = address_str[index + 3]

            if third_char == second_char and fourth_char == first_char:
                return True

    return False


def get_aba_or_bab(sequences):
    aba_or_babas = []

    for sequence in sequences:

        for i in range(0, len(sequence) - 2):
            first_char = sequence[i]
            second_char = sequence[i+1]
            third_char = sequence[i+2]

            if not (first_char == second_char) and (first_char == third_char):
                aba_or_babas.append(sequence[i:(i+3)])
    return aba_or_babas


def invert_aba(aba):
    first_char = aba[0]
    second_char = aba[1]

    return second_char + first_char + second_char


def support_ssl(abas, babas):

    for aba in abas:
        inverted_aba = invert_aba(aba)

        if inverted_aba in babas:
            return True


def count_tls_support():
    ip_addresses = get_ip_addresses()
    count = 0

    for address in ip_addresses:
        abas = get_aba_or_bab(address[0])
        babas = get_aba_or_bab(address[1])

        print(abas)
        print(babas)
        if support_ssl(abas, babas):
            count += 1

    print(count)
    return count


count_tls_support()