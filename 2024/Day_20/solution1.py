from collections import deque
from typing import List, Set, Tuple, Dict
import heapq

def read_input(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_start_end(grid: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start = end = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    return start, end

def get_neighbors(pos: Tuple[int, int], grid: List[str]) -> List[Tuple[int, int]]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dy, dx in directions:
        new_y, new_x = pos[0] + dy, pos[1] + dx
        if (0 <= new_y < len(grid) and
            0 <= new_x < len(grid[0]) and
            grid[new_y][new_x] != '#'):
            neighbors.append((new_y, new_x))
    return neighbors

def shortest_path(grid: List[str], start: Tuple[int, int], end: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
    distances = {}
    queue = [(0, start)]
    distances[start] = 0

    while queue:
        dist, current = heapq.heappop(queue)

        if dist > distances[current]:
            continue

        for next_pos in get_neighbors(current, grid):
            new_dist = dist + 1

            if next_pos not in distances or new_dist < distances[next_pos]:
                distances[next_pos] = new_dist
                heapq.heappush(queue, (new_dist, next_pos))

    return distances

def find_cheats(grid: List[str], normal_distances: Dict[Tuple[int, int], int],
                start: Tuple[int, int], end: Tuple[int, int]) -> Dict[int, int]:
    height, width = len(grid), len(grid[0])
    savings = {}

    # For each possible cheat start position
    for y1 in range(height):
        for x1 in range(width):
            if grid[y1][x1] == '#':
                continue
            pos1 = (y1, x1)
            if pos1 not in normal_distances:
                continue

            # For each possible cheat end position
            for y2 in range(height):
                for x2 in range(width):
                    if grid[y2][x2] == '#':
                        continue
                    pos2 = (y2, x2)

                    # Calculate Manhattan distance between start and end of cheat
                    manhattan_dist = abs(y2 - y1) + abs(x2 - x1)
                    if manhattan_dist > 2:  # Cheat can only last 2 moves
                        continue

                    # If we can reach both positions in normal path
                    if pos1 in normal_distances and pos2 in normal_distances:
                        # Calculate time saved
                        normal_time = normal_distances[end]
                        cheat_time = (normal_distances[pos1] +
                                    manhattan_dist +
                                    (normal_distances[end] - normal_distances[pos2]))

                        if cheat_time < normal_time:
                            saved = normal_time - cheat_time
                            savings[saved] = savings.get(saved, 0) + 1

    return savings

def solve(grid: List[str]) -> int:
    start, end = find_start_end(grid)

    # Replace S and E with . for easier processing
    grid = [row.replace('S', '.').replace('E', '.') for row in grid]

    # Find normal shortest path distances
    normal_distances = shortest_path(grid, start, end)

    # Find all possible cheats and their time savings
    savings = find_cheats(grid, normal_distances, start, end)

    # Count cheats that save at least 100 picoseconds
    return sum(count for saved, count in savings.items() if saved >= 100)

def main():
    grid = read_input("Day_20/input.txt")
    result = solve(grid)
    print(f"Number of cheats saving at least 100 picoseconds: {result}")

if __name__ == "__main__":
    main()