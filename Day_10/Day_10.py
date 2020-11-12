import ut


class Bot:

    instruction = 0

    def __init__(self):
        self.data_chips = []

    def give_data_chip(self, data_chip):
        self.data_chips.append(data_chip)

    def give_instruction(self, instruction):
        self.instruction = instruction

    def print_bot_data(self):
        print(self.instruction)
        print(self.data_chips)


def get_bot_data():

    # Keys are bot ID
    bots = {}

    raw_instructions = ut.read_file_lines('input.txt')
    raw_instructions = [raw_instruction.split() for raw_instruction in raw_instructions]

    for raw_instruction in raw_instructions:

        # Raw instruction is either 'value' or 'bot'
        instruction_type = raw_instruction[0]

        if instruction_type == 'value':
            data_chip_value = int(raw_instruction[1])
            bot_to_give = int(raw_instruction[5])

            if bot_to_give in bots:
                bots[bot_to_give].give_data_chip(data_chip_value)
            else:
                new_bot = Bot()
                new_bot.give_data_chip(data_chip_value)
                bots[bot_to_give] = new_bot

        elif instruction_type == 'bot':
            bot_to_give = int(raw_instruction[1])
            low_give = int(raw_instruction[6])
            high_give = int(raw_instruction[11])
            low_to_bin = False
            high_to_bin = False

            # if output or not
            if raw_instruction[5] == 'output':
                low_to_bin = True
            if raw_instruction[10] == 'output':
                high_to_bin = True

            if bot_to_give in bots:
                bots[bot_to_give].give_instruction((low_give, high_give, low_to_bin, high_to_bin))
            else:
                new_bot = Bot()
                new_bot.give_instruction((low_give, high_give, low_to_bin, high_to_bin))
                bots[bot_to_give] = new_bot

    return bots


def get_bots_with_two_chips(bots : dict):

    bots_with_2 = []

    for bot_id in bots.keys():
        current_bot = bots[bot_id]
        if len(current_bot.data_chips) > 1:
            bots_with_2.append(bot_id)
    return bots_with_2


def run_bots():
    bots = get_bot_data()
    bots_with_two_chips = get_bots_with_two_chips(bots)
    output_bin = []

    while bots_with_two_chips:
        bot_id = bots_with_two_chips[0]

        # Let a bot give its chips
        bot = bots[bot_id]
        low_bot = bot.instruction[0]
        high_bot = bot.instruction[1]
        bot.data_chips.sort()
        data_chips = bot.data_chips

        if data_chips == [17, 61]:
            print(bot_id)

        # Give data chip to low
        if bot.instruction[2]:
            output_bin.append((low_bot, data_chips[0]))
        else:
            bots[low_bot].give_data_chip(data_chips[0])
            if len(bots[low_bot].data_chips) > 1:
                bots_with_two_chips.append(low_bot)

        if bot.instruction[3]:
            output_bin.append((high_bot, data_chips[1]))
        else:

            # Give data chip to high
            bots[high_bot].give_data_chip(data_chips[1])
            if len(bots[high_bot].data_chips) > 1:
                bots_with_two_chips.append(high_bot)

        # Remove data chips from bots
        bot.data_chips = []
        bots_with_two_chips.remove(bot_id)

    for waste in output_bin:
        if waste[0] == 0:
            print(waste)
        if waste[0] == 1:
            print(waste)
        if waste[0] == 2:
            print(waste)


run_bots()


