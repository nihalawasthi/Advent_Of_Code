from itertools import product

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for num, op in zip(numbers[1:], operators):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '||':
            result = int(str(result) + str(num))
    return result

def can_match_target(target, numbers, allow_concatenation=False):
    operators = ['+', '*']
    if allow_concatenation:
        operators.append('||')
    for ops in product(operators, repeat=len(numbers) - 1):
        if evaluate_expression(numbers, ops) == target:
            return True
    return False

def calculate_total_calibration(filename, allow_concatenation=False):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            target = int(parts[0])
            numbers = list(map(int, parts[1].split()))
            if can_match_target(target, numbers, allow_concatenation):
                total += target
    return total

file_path = "day_7.txt"

part1_result = calculate_total_calibration(file_path, allow_concatenation=False)
print("Part 1 - Total Calibration Result:", part1_result)

part2_result = calculate_total_calibration(file_path, allow_concatenation=True)
print("Part 2 - Total Calibration Result:", part2_result)
