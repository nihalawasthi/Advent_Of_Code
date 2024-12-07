from time import time

def simulate_guard_path(file_path):
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0  # Start facing up
    visited_positions = set()
    
    # Read the map from the file
    with open(file_path, 'r') as file:
        map_lines = file.readlines()
    
    guard_position = None
    
    # Find the guard's starting position
    for r in range(len(map_lines)):
        map_lines[r] = map_lines[r].rstrip('\n')  # Remove newline characters
        for c in range(len(map_lines[r])):
            if map_lines[r][c] == '^':
                guard_position = (r, c)
                map_lines[r] = map_lines[r][:c] + '.' + map_lines[r][c+1:]  # Replace guard with empty space
                break
        if guard_position:
            break
    
    # Start simulation
    while True:
        r, c = guard_position
        visited_positions.add(guard_position)
        
        # Check the next position in the current direction
        next_r = r + directions[direction_index][0]
        next_c = c + directions[direction_index][1]
        
        # Check if the next position is within bounds
        if 0 <= next_r < len(map_lines) and 0 <= next_c < len(map_lines[0]):
            # Check if there's an obstacle
            if map_lines[next_r][next_c] == '#':
                # Turn right (change direction)
                direction_index = (direction_index + 1) % 4
            else:
                # Move forward
                guard_position = (next_r, next_c)
        else:
            # The guard has left the mapped area
            break
    
    return len(visited_positions)

Loc = tuple[int, int]
Direction = tuple[int, int]

START_MARKER = "^"
WALL = "#"
OPEN = "."

DIRECTIONS = [  # order matters
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
]


class OffGrid(Exception):
    """Raised when the guard goes off the grid."""


class InfiniteLoop(Exception):
    """Raised when the guard stays on the grid infinitely."""


def parse_grid_from_file(file_path: str) -> tuple[list[list[str]], Loc]:
    """Parses the input grid from a text file."""
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == START_MARKER:
                return grid, (r, c)
    raise ValueError(f"Start marker {START_MARKER!r} not found in the grid.")


class GuardSim:
    def __init__(self, grid: list[list[str]], start_loc: Loc):
        if not grid or not grid[0]:
            raise ValueError("Grid must be a non-empty 2D list.")
        self.grid = grid
        self.start_loc = start_loc
        self.current_loc = self.start_loc
        self._direction_index = 0  # Starts facing 'up'

    @property
    def n_rows(self) -> int:
        return len(self.grid)

    @property
    def n_cols(self) -> int:
        return len(self.grid[0])

    def direction(self) -> Direction:
        return DIRECTIONS[self._direction_index]

    def turn_right(self):
        self._direction_index = (self._direction_index + 1) % len(DIRECTIONS)

    def step_forward(self) -> bool:
        direction = self.direction()
        next_loc = self.current_loc[0] + direction[0], self.current_loc[1] + direction[1]
        if not (0 <= next_loc[0] < self.n_rows and 0 <= next_loc[1] < self.n_cols):  # Out of bounds
            raise OffGrid
        if self.grid[next_loc[0]][next_loc[1]] != WALL:  # Can step forward
            self.current_loc = next_loc
            return True
        return False  # Hit a wall

    def walk(self) -> set[Loc]:
        history: set[tuple[Loc, Direction]] = set()
        history.add((self.current_loc, self.direction()))
        while True:
            try:
                could_step = self.step_forward()
            except OffGrid:
                return {loc for loc, _ in history}
            if not could_step:  # Hit a wall
                self.turn_right()
            new_history_entry = (self.current_loc, self.direction())
            if new_history_entry in history:  # Infinite loop detected
                raise InfiniteLoop
            history.add(new_history_entry)


def count_valid_positions(file_path: str):
    grid, start_loc = parse_grid_from_file(file_path)
    # Initial simulation
    initial_guard_sim = GuardSim(grid, start_loc)
    locs_visited = initial_guard_sim.walk()
    
    # Try adding obstacles
    locs_to_modify = locs_visited - {start_loc}
    infinite_loops_count = 0
    for loc_modification in locs_to_modify:
        modified_grid = [row[:] for row in grid]  # Deep copy of the grid
        modified_grid[loc_modification[0]][loc_modification[1]] = WALL  # Place an obstacle
        modified_guard_sim = GuardSim(modified_grid, start_loc)
        try:
            modified_guard_sim.walk()
        except InfiniteLoop:
            infinite_loops_count += 1
    return infinite_loops_count


def main(file_path: str):
    start_time = time()
    infinite_loops_count = count_valid_positions(file_path)
    print(f"Number of valid positions to create infinite loops: {infinite_loops_count}")
    print(f"Execution time: {time() - start_time:.2f} seconds")


if __name__ == "__main__":
    file_path = "C:/My/Problem_Solutions/Advent_Of_Code/2024/Day_06/day_6.txt"  # Replace with your input file path
    distinct_positions_count = simulate_guard_path(file_path)
    print(distinct_positions_count)
    main(file_path)
