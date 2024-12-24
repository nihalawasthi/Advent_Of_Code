from collections import defaultdict, deque

def parse_map(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

def calculate_area_and_perimeter(garden_map):
    rows = len(garden_map)
    cols = len(garden_map[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    def bfs(start_row, start_col, plant_type):
        queue = deque([(start_row, start_col)])
        visited[start_row][start_col] = True
        area = 0
        perimeter = 0
        
        while queue:
            row, col = queue.popleft()
            area += 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if garden_map[nr][nc] == plant_type and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                    elif garden_map[nr][nc] != plant_type:
                        perimeter += 1
                else:
                    perimeter += 1
        
        return area, perimeter

    regions = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant_type = garden_map[r][c]
                area, perimeter = bfs(r, c, plant_type)
                regions[plant_type].append((area, perimeter))

    return regions

def calculate_total_cost(regions):
    total_cost = 0
    for plant_type, details in regions.items():
        for area, perimeter in details:
            total_cost += area * perimeter
    return total_cost

def main(file_path):
    garden_map = parse_map(file_path)
    regions = calculate_area_and_perimeter(garden_map)
    total_cost = calculate_total_cost(regions)
    print(f"Total price of fencing: {total_cost}")

# Example usage
if __name__ == "__main__":
    input_file =  "Day_12/input.txt"
    main(input_file)