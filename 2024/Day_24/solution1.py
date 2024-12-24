#!/usr/bin/env python3

def parse_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    wire_values = {}
    gates = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if ":" in line:  # Initial wire values
            wire, value = line.split(": ")
            wire_values[wire] = int(value)
        else:  # Gate operations
            gates.append(line)

    return wire_values, gates

def evaluate_gates(wire_values, gates):
    def get_value(wire):
        if wire.isdigit():
            return int(wire)
        return wire_values.get(wire, None)

    while gates:
        remaining_gates = []

        for gate in gates:
            parts = gate.split(" -> ")
            operation, output = parts[0], parts[1]

            if " AND " in operation:
                a, b = operation.split(" AND ")
                a_val, b_val = get_value(a), get_value(b)
                if a_val is not None and b_val is not None:
                    wire_values[output] = a_val & b_val
                else:
                    remaining_gates.append(gate)
            elif " OR " in operation:
                a, b = operation.split(" OR ")
                a_val, b_val = get_value(a), get_value(b)
                if a_val is not None and b_val is not None:
                    wire_values[output] = a_val | b_val
                else:
                    remaining_gates.append(gate)
            elif " XOR " in operation:
                a, b = operation.split(" XOR ")
                a_val, b_val = get_value(a), get_value(b)
                if a_val is not None and b_val is not None:
                    wire_values[output] = a_val ^ b_val
                else:
                    remaining_gates.append(gate)
            else:
                raise ValueError(f"Unsupported operation: {operation}")

        gates = remaining_gates

    return wire_values

def calculate_decimal_output(wire_values):
    binary_result = ""
    z_wires = {key: value for key, value in wire_values.items() if key.startswith("z")}
    for key in sorted(z_wires.keys()):
        binary_result = str(z_wires[key]) + binary_result

    return int(binary_result, 2)

if __name__ == "__main__":
    input_file = "Day_24/input.txt"
    wire_values, gates = parse_input(input_file)
    wire_values = evaluate_gates(wire_values, gates)
    result = calculate_decimal_output(wire_values)
    print(f"Decimal Output: {result}")
