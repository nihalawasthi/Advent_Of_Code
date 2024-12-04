def count_word_occurrences(grid, word):
    def search_direction(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
                return False
        return True

    directions = [
        (0, 1),
        (0, -1),  
        (1, 0),   
        (-1, 0),  
        (1, 1),   
        (-1, -1),
        (1, -1), 
        (-1, 1)   
    ]

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if search_direction(x, y, dx, dy):
                    count += 1
    return count

filename = 'day_4.txt'

with open(filename, "r") as file:
    word_search = [line.strip() for line in file.readlines()]

occurrences = count_word_occurrences(word_search, "XMAS")
print(f"Occurrences of Xmas: {occurrences}")

with open(filename, 'r') as file:
    grid = {
        (x, y): c
        for y, row in enumerate(file)
        for x, c in enumerate(row.strip('\n'))
    }

max_x, max_y = max(grid.keys())

def count_mas_sam_cross(grid, max_x, max_y):
    count = 0
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            diagonal1 = "".join([
                grid.get((x - 1, y - 1), ""),
                grid.get((x, y), ""),
                grid.get((x + 1, y + 1), "")
            ])
            diagonal2 = "".join([
                grid.get((x - 1, y + 1), ""),
                grid.get((x, y), ""),
                grid.get((x + 1, y - 1), "")
            ])
            if diagonal1 in ("MAS", "SAM") and diagonal2 in ("MAS", "SAM"):
                count += 1
    return count

cross_count = count_mas_sam_cross(grid, max_x, max_y)

print(f"The cross patterns 'MAS' or 'SAM' appear {cross_count} times.")
