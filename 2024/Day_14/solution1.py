import re
from collections import defaultdict

# Define grid dimensions
GRID_WIDTH = 101
GRID_HEIGHT = 103

# Define the function to parse input
def parse_input(input_file):
    robots = []
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line.strip())
            if match:
                px, py, vx, vy = map(int, match.groups())
                robots.append(((px, py), (vx, vy)))
    return robots

# Simulate robots
def simulate_robots(robots, seconds):
    positions = defaultdict(int)

    for (px, py), (vx, vy) in robots:
        # Calculate new position after 'seconds' time steps with wrapping
        nx = (px + vx * seconds) % GRID_WIDTH
        ny = (py + vy * seconds) % GRID_HEIGHT
        positions[(nx, ny)] += 1

    return positions

# Calculate safety factor
def calculate_safety_factor(positions):
    # Initialize quadrants
    quadrant_counts = [0, 0, 0, 0]

    for (x, y), count in positions.items():
        if x == GRID_WIDTH // 2 or y == GRID_HEIGHT // 2:
            continue  # Exclude robots in the middle

        if x < GRID_WIDTH // 2 and y < GRID_HEIGHT // 2:
            quadrant_counts[0] += count  # Top-left quadrant
        elif x >= GRID_WIDTH // 2 and y < GRID_HEIGHT // 2:
            quadrant_counts[1] += count  # Top-right quadrant
        elif x < GRID_WIDTH // 2 and y >= GRID_HEIGHT // 2:
            quadrant_counts[2] += count  # Bottom-left quadrant
        elif x >= GRID_WIDTH // 2 and y >= GRID_HEIGHT // 2:
            quadrant_counts[3] += count  # Bottom-right quadrant

    # Calculate the product of robot counts in all quadrants
    safety_factor = 1
    for count in quadrant_counts:
        safety_factor *= count

    return safety_factor

if __name__ == "__main__":
    input_file = "Day_14/input.txt"

    # Parse input
    robots = parse_input(input_file)

    # Simulate for 100 seconds
    positions = simulate_robots(robots, 100)

    # Calculate safety factor
    safety_factor = calculate_safety_factor(positions)

    print(f"Safety Factor: {safety_factor}")
