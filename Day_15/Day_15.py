

class Disc:

    def __init__(self, cycle, offset):
        self.cycle = cycle
        self.offset = offset

    # Returns true if this disc is open at the specified time
    def is_open(self, time):
        return (time - self.offset) % self.cycle == 0


def get_discs():
    discs = [Disc(17, 1),
             Disc(3, 2),
             Disc(19, 12),
             Disc(13, 7),
             Disc(7, 0),
             Disc(5, 4),
             Disc(11, 4)]
    return discs


def find_closest_alignment():
    discs = get_discs()
    time = 0

    # try time values until all disc are open
    while True:
        constraints = [disc.is_open(time) for disc in discs]
        if all(constraints):
            return time
        time += 1


print(find_closest_alignment())