import ut


def get_ip_ranges():
    return [[int(elem) for elem in ip_range.split('-')] for ip_range in ut.read_file_lines('input.txt')]


def take_first(elem):
    return elem[0]


def get_sorted_ip_ranges():
    ip_ranges = get_ip_ranges()
    ip_ranges.sort(key=take_first)
    return ip_ranges


def merge_ip_ranges(merged_ip_ranges: list, ip_ranges):

    for ip_range in ip_ranges:

        # New range to be added
        low = ip_range[0]
        high = ip_range[1]

        # Previous range to be potentially merged
        previous_low = merged_ip_ranges[-1][0]
        previous_high = merged_ip_ranges[-1][1]
        if low <= previous_high + 1:
            if high > previous_high:
                merged_ip_ranges[-1] = [previous_low, high]
        else:
            merged_ip_ranges.append([low, high])
    return merged_ip_ranges


def count_allowed_ip_addresses(ip_ranges):
    # number of blocked addresses
    blocked_addresses = 0

    for blocked_range in ip_ranges:
        low = blocked_range[0]
        high = blocked_range[1]

        blocked_addresses += (high + 1)-low

    return 4294967296 - blocked_addresses


sorted_ip_ranges = get_sorted_ip_ranges()
merged_ip_ranges = merge_ip_ranges([[0, 0]], sorted_ip_ranges)
print(merged_ip_ranges)
print(count_allowed_ip_addresses(merged_ip_ranges))

