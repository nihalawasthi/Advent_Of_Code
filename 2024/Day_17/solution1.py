def read_program(file_path):
    """Reads the program from the file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    registers = {}
    program = []

    for line in lines:
        line = line.strip()
        if line.startswith("Register A"):
            registers['A'] = int(line.split(": ")[1])
        elif line.startswith("Register B"):
            registers['B'] = int(line.split(": ")[1])
        elif line.startswith("Register C"):
            registers['C'] = int(line.split(": ")[1])
        elif line.startswith("Program"):
            program = list(map(int, line.split(": ")[1].split(",")))

    return registers, program


def get_operand_value(operand, registers):
    """Calculates the value of a combo operand."""
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']
    else:
        raise ValueError("Invalid combo operand")


def execute_program(registers, program):
    """Executes the given program."""
    instruction_pointer = 0
    output = []

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        if opcode == 0:  # adv
            divisor = 2 ** get_operand_value(operand, registers)
            registers['A'] //= divisor

        elif opcode == 1:  # bxl
            registers['B'] ^= operand

        elif opcode == 2:  # bst
            registers['B'] = get_operand_value(operand, registers) % 8

        elif opcode == 3:  # jnz
            if registers['A'] != 0:
                instruction_pointer = operand
                continue

        elif opcode == 4:  # bxc
            registers['B'] ^= registers['C']

        elif opcode == 5:  # out
            output.append(get_operand_value(operand, registers) % 8)

        elif opcode == 6:  # bdv
            divisor = 2 ** get_operand_value(operand, registers)
            registers['B'] = registers['A'] // divisor

        elif opcode == 7:  # cdv
            divisor = 2 ** get_operand_value(operand, registers)
            registers['C'] = registers['A'] // divisor

        else:
            raise ValueError("Invalid opcode")

        instruction_pointer += 2

    return ",".join(map(str, output))


if __name__ == "__main__":
    file_path = "Day_17/input.txt"

    # Read the registers and program from the file
    registers, program = read_program(file_path)

    # Execute the program and print the output
    result = execute_program(registers, program)
    print(result)
