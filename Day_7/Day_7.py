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


def count_tls_support():
    ip_addresses = get_ip_addresses()
    count = 0

    for address in ip_addresses:
        address_names = address[0]
        hyper_net_sequences = address[1]

        hyper_net_ok = True

        for hyper_net_sequence in hyper_net_sequences:
            if support_abba(hyper_net_sequence):
                hyper_net_ok = False

        if hyper_net_ok:

            non_hyper_ok = False

            for non_hyper_net_sequence in address_names:
                if support_abba(non_hyper_net_sequence):
                    non_hyper_ok = True
        if non_hyper_ok:
            count += 1

    print(count)
    return count


count_tls_support()