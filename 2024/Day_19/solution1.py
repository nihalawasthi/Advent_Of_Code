from collections import defaultdict, deque

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')

    # Separate towel patterns and desired designs
    towel_patterns = lines[0].split(', ')
    designs = lines[2:]  # Skip the blank line and get designs
    
    return towel_patterns, designs

def can_form_design(design, towel_patterns):
    # Perform a BFS to check if we can create the design using the patterns
    queue = deque([design])
    seen = set()

    while queue:
        current = queue.popleft()

        if current == "":
            return True

        if current in seen:
            continue
        seen.add(current)

        for pattern in towel_patterns:
            if current.startswith(pattern):
                queue.append(current[len(pattern):])

    return False

def count_possible_designs(file_path):
    towel_patterns, designs = read_input(file_path)
    possible_count = 0

    for design in designs:
        if can_form_design(design, towel_patterns):
            possible_count += 1

    return possible_count

# Input file path
file_path = "Day_19/input.txt"

# Count and print the number of possible designs
result = count_possible_designs(file_path)
print(f"Number of possible designs: {result}")