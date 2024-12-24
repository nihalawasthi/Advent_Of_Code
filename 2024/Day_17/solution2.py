#!/usr/bin/env python3
def run_program(program, initial_a):
    registers = {'A': initial_a, 'B': 0, 'C': 0}
    ip = 0
    output = []

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1] if ip + 1 < len(program) else None
        ip += 2

        if opcode == 0:  # adv
            denom = 2 ** (operand if operand < 4 else registers["ABC"[operand - 4]])
            registers['A'] //= denom
        elif opcode == 1:  # bxl
            registers['B'] ^= operand
        elif opcode == 2:  # bst
            registers['B'] = operand % 8 if operand < 4 else registers["ABC"[operand - 4]] % 8
        elif opcode == 3:  # jnz
            if registers['A'] != 0:
                ip = operand
        elif opcode == 4:  # bxc
            registers['B'] ^= registers['C']
        elif opcode == 5:  # out
            value = operand % 8 if operand < 4 else registers["ABC"[operand - 4]] % 8
            output.append(value)
        elif opcode == 6:  # bdv
            denom = 2 ** (operand if operand < 4 else registers["ABC"[operand - 4]])
            registers['B'] = registers['A'] // denom
        elif opcode == 7:  # cdv
            denom = 2 ** (operand if operand < 4 else registers["ABC"[operand - 4]])
            registers['C'] = registers['A'] // denom

    return output

def find_initial_a(program):
    a = 35402247981593
    while True:
        output = run_program(program, a)
        if output[0:4] == program[0:4]:
            print(f"Trying with A={a} -> {output}")
        if output == program:
            return a
        a += 10000

program = [2, 4, 1, 7, 7, 5, 4, 1, 1, 4, 5, 5, 0, 3, 3, 0]
initial_a = find_initial_a(program)
print(f"The lowest positive initial value for register A is: {initial_a}")
