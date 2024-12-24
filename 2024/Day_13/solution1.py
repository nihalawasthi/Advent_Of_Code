from itertools import product
import math

def parse_input(file_path):
    """Parse the input file and extract button configurations and prize locations."""
    machines = []
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n\n')
        for machine in lines:
            lines = machine.split('\n')
            button_a = tuple(map(int, [v.split('+')[1] for v in lines[0].split(':')[1].strip().split(',')]))
            button_b = tuple(map(int, [v.split('+')[1] for v in lines[1].split(':')[1].strip().split(',')]))
            prize = tuple(map(int, [v.split('=')[1] for v in lines[2].split(':')[1].strip().split(',')]))
            machines.append((button_a, button_b, prize))
    return machines

def find_min_tokens(button_a, button_b, prize, max_presses=100):
    """Find the minimum tokens required to win the prize for a single machine."""
    x_target, y_target = prize
    a_x, a_y = button_a
    b_x, b_y = button_b

    min_tokens = math.inf

    for a_presses, b_presses in product(range(max_presses + 1), repeat=2):
        total_x = a_presses * a_x + b_presses * b_x
        total_y = a_presses * a_y + b_presses * b_y

        if total_x == x_target and total_y == y_target:
            tokens = a_presses * 3 + b_presses * 1
            min_tokens = min(min_tokens, tokens)

    return min_tokens if min_tokens != math.inf else None

def solve(file_path):
    """Solve the problem and return the minimum tokens to win the maximum prizes."""
    machines = parse_input(file_path)
    total_tokens = 0
    prizes_won = 0

    for button_a, button_b, prize in machines:
        min_tokens = find_min_tokens(button_a, button_b, prize)
        if min_tokens is not None:
            total_tokens += min_tokens
            prizes_won += 1

    return prizes_won, total_tokens

if __name__ == "__main__":
    input_file = "Day_13/input.txt"
    prizes_won, total_tokens = solve(input_file)
    print(f"Maximum prizes won: {prizes_won}")
    print(f"Minimum tokens spent: {total_tokens}")
