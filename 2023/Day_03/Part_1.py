class EngineSchematicAnalyzer:
    DIRECTIONS = [
        (-1, -1), # Top-left
        (-1, 0),  # Up
        (-1, 1),  # Top-right
        (0, -1),  # Left
        (0, 1),   # Right
        (1, -1),  # Bottom-left
        (1, 0),   # Down
        (1, 1)    # Bottom-right
    ]

    def __init__(self, schematic):
        self.schematic = [list(line) for line in schematic.split('\n')]
        self.processed_locations = set()

    def is_valid_symbol(self, char):
        return not (char.isdigit() or char == '.')

    def is_adjacent_to_symbol(self, row, col):
        for dx, dy in self.DIRECTIONS:
            if 0 <= row + dx < len(self.schematic) and 0 <= col + dy < len(self.schematic[row + dx]):
                if self.is_valid_symbol(self.schematic[row + dx][col + dy]):
                    return True
        return False

    def calculate_sum_of_part_numbers(self):
        total_sum = 0
        for i, row in enumerate(self.schematic):
            j = 0
            while j < len(row):
                if row[j].isdigit() and (i, j) not in self.processed_locations:
                    number, init_j = row[j], j
                    while j + 1 < len(row) and row[j + 1].isdigit():
                        number += row[j + 1]
                        j += 1
                    
                    for col_index in range(init_j, j + 1):
                        self.processed_locations.add((i, col_index))
                        if self.is_adjacent_to_symbol(i, col_index):
                            total_sum += int(number)
                            break
                j += 1
            
        return total_sum


def main():
    with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_03\input.txt") as file:
        engine_schematic = file.read()

    analyzer = EngineSchematicAnalyzer(engine_schematic)
    total_sum = analyzer.calculate_sum_of_part_numbers()
    print(f"Sum of part numbers is {total_sum}")

if __name__ == "__main__":
    main()