import ut


def get_instructions():
    return [str.split(instruction) for instruction in ut.read_file_lines('input.txt')]


class AssembunnyComputer:

    def __init__(self):
        self.registers = {}
        self.pointer = 0

    def reset_register(self):
        self.registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

    def copy(self, value, register):

        # if the value is numeric, do not read from register
        if str.isnumeric(value):
            self.registers[register] = int(value)
        # if the value is not numeric, then copy value from register
        else:
            self.registers[register] = self.registers[value]

        # Increment the program pointer
        self.pointer += 1

    def jump(self, value, offset):
        # if the value is numeric, do not read from register
        if str.isnumeric(value) and not int(value) == 0:
            self.pointer += int(offset)

        elif not self.registers[value] == 0:
            self.pointer += int(offset)

        # If not zero jump to next instruction
        else:
            self.pointer += 1

    def execute_instruction(self, instruction):
        # The operation to be executed
        operation = instruction[0]

        # The copy operation
        if operation == 'cpy':
            value = instruction[1]
            register = instruction[2]
            self.copy(value, register)

        # The increment operation
        elif operation == 'inc':
            register = instruction[1]
            self.registers[register] += 1
            # Increment the program pointer
            self.pointer += 1

        # The decrement operation
        elif operation == 'dec':
            register = instruction[1]
            self.registers[register] -= 1
            # Increment the program pointer
            self.pointer += 1

        # The jump operation
        elif operation == 'jnz':
            value = instruction[1]
            offset = instruction[2]
            self.jump(value, offset)

    def run_program(self, instructions):

        # Reset the pointer at start of program
        self.pointer = 0
        # Reset the register at the start of the program
        self.reset_register()

        # Run program until pointer is outside of instruction range
        while self.pointer < len(instructions):

            # Execute next instruction
            instruction = instructions[self.pointer]
            self.execute_instruction(instruction)


computer_instructions = get_instructions()
assembunny_computer = AssembunnyComputer()
assembunny_computer.run_program(computer_instructions)
print(assembunny_computer.registers['a'])

