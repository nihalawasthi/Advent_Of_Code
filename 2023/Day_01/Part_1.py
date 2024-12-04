def cal_value(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line:
                a = next((char for char in line if char.isdigit()), None)
                b = next((char for char in reversed(line) if char.isdigit()), None)

                if a is not None and b is not None:
                    calibration_value = int(a + b)
                    total_sum += calibration_value

    return total_sum

file_path = 'D:\My\Advent_of_code_2023\Day_01\input.txt'

sum = cal_value(file_path)
print("Sum of calibration values:", sum)