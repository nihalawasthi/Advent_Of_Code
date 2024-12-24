from heapq import heappop, heappush

def parse_maze(input_str):
    maze = [list(line) for line in input_str.strip().split("\n")]
    start, end = None, None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return maze, start, end

def solve_maze(input_str):
    # Parse the maze
    maze, start, end = parse_maze(input_str)
    
    # Define movement directions: (dx, dy, direction name)
    directions = [(0, -1, 'N'), (1, 0, 'E'), (0, 1, 'S'), (-1, 0, 'W')]
    direction_map = {d[2]: i for i, d in enumerate(directions)}

    # Priority queue for Dijkstra's
    pq = []
    heappush(pq, (0, start[0], start[1], 'E'))  # (cost, x, y, facing)

    # Visited set: (x, y, facing)
    visited = set()

    while pq:
        cost, x, y, facing = heappop(pq)

        # If reached the end, return the cost
        if (x, y) == end:
            return cost

        # Skip if already visited
        if (x, y, facing) in visited:
            continue
        visited.add((x, y, facing))

        # Current direction index
        current_dir_index = direction_map[facing]

        # Explore neighbors
        for i, (dx, dy, new_dir) in enumerate(directions):
            nx, ny = x + dx, y + dy

            # If moving forward
            if i == current_dir_index:
                if maze[ny][nx] != '#':  # Valid forward move
                    heappush(pq, (cost + 1, nx, ny, new_dir))

            # If turning (rotating clockwise or counterclockwise)
            else:
                turn_cost = 1000
                heappush(pq, (cost + turn_cost, x, y, new_dir))

    return float('inf')  # No solution found

# Read input from file
with open("Day_16/input.txt", "r") as file:
    input_str = file.read()

# Solve the maze
result = solve_maze(input_str)
print("Lowest score:", result)