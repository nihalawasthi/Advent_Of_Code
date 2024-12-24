def find_unique_antinodes_from_file(file_path):
    from collections import defaultdict
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    antenna_positions = defaultdict(list)
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            char = grid[r][c]
            if char.isalnum():
                antenna_positions[char].append((r, c))
    unique_antinodes = set()
    for freq, positions in antenna_positions.items():
        n = len(positions)
        if n < 2:
            continue
        for i in range(n):
            for j in range(i + 1, n):
                r1, c1 = positions[i]
                r2, c2 = positions[j]
                dr = r2 - r1
                dc = c2 - c1
                r_antin1, c_antin1 = r1 - dr, c1 - dc
                r_antin2, c_antin2 = r2 + dr, c2 + dc
                if 0 <= r_antin1 < rows and 0 <= c_antin1 < cols:
                    unique_antinodes.add((r_antin1, c_antin1))
                if 0 <= r_antin2 < rows and 0 <= c_antin2 < cols:
                    unique_antinodes.add((r_antin2, c_antin2))
    return len(unique_antinodes)

def find_all_antinodes(file_path):
    from collections import defaultdict
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    antenna_positions = defaultdict(list)
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            char = grid[r][c]
            if char.isalnum():  # Antennas are letters or digits
                antenna_positions[char].append((r, c))
    unique_antinodes = set()
    for freq, positions in antenna_positions.items():
        n = len(positions)
        if n < 2:
            continue
        unique_antinodes.update(positions)
        for i in range(n):
            for j in range(i + 1, n):
                r1, c1 = positions[i]
                r2, c2 = positions[j]
                dr = r2 - r1
                dc = c2 - c1
                for k in range(-max(rows, cols), max(rows, cols) + 1):
                    r_antin = r1 + k * dr
                    c_antin = c1 + k * dc
                    if 0 <= r_antin < rows and 0 <= c_antin < cols:
                        unique_antinodes.add((r_antin, c_antin))
    return len(unique_antinodes)

file_path = "input.txt"
unique_count1 = find_unique_antinodes_from_file(file_path)
print(f"Number of unique antinode locations: {unique_count1}")

unique_count2 = find_all_antinodes(file_path)
print(f"Number of unique antinode locations: {unique_count2}")