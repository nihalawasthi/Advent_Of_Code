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

def find_swapped_wires(wire_values, gates):
    from itertools import combinations

    # Determine the range of wire indices for x, y, and z
    x_wires = [key for key in wire_values.keys() if key.startswith("x")]
    y_wires = [key for key in wire_values.keys() if key.startswith("y")]
    z_wires = [key for key in wire_values.keys() if key.startswith("z")]
    max_index = max(
        max(int(wire[1:]) for wire in x_wires),
        max(int(wire[1:]) for wire in y_wires),
        max(int(wire[1:]) for wire in z_wires),
    )

    # Simulate the current system
    original_output = evaluate_gates(wire_values.copy(), gates.copy())
    original_decimal = calculate_decimal_output(original_output)

    # Identify candidate gates with z wires
    z_gates = [gate for gate in gates if " -> z" in gate]
    z_outputs = [gate.split(" -> ")[1] for gate in z_gates]

    # Test all pairs of swaps
    for swap1, swap2 in combinations(z_outputs, 2):
        # Swap the outputs in the gates
        swapped_gates = []
        for gate in gates:
            if gate.endswith(f" -> {swap1}"):
                swapped_gates.append(gate.replace(f" -> {swap1}", f" -> {swap2}"))
            elif gate.endswith(f" -> {swap2}"):
                swapped_gates.append(gate.replace(f" -> {swap2}", f" -> {swap1}"))
            else:
                swapped_gates.append(gate)

        # Simulate the swapped system
        swapped_output = evaluate_gates(wire_values.copy(), swapped_gates)
        swapped_decimal = calculate_decimal_output(swapped_output)

        # Check if the addition is correct
        x_binary = "".join(str(wire_values.get(f"x{i:02}", 0)) for i in range(max_index + 1))
        y_binary = "".join(str(wire_values.get(f"y{i:02}", 0)) for i in range(max_index + 1))
        expected_decimal = int(x_binary, 2) + int(y_binary, 2)

        if swapped_decimal == expected_decimal:
            return sorted([swap1, swap2])

    raise ValueError("No valid swaps found.")

if __name__ == "__main__":
    input_file = "Day_24/input.txt"
    wire_values, gates = parse_input(input_file)
    wire_values = evaluate_gates(wire_values, gates)
    result = calculate_decimal_output(wire_values)
    print(f"Decimal Output: {result}")

    # Part Two: Find swapped wires
    swapped_wires = find_swapped_wires(wire_values, gates)
    print(f"Swapped Wires: {','.join(swapped_wires)}")
