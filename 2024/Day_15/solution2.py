from collections import defaultdict

with open("Day_15/input.txt", 'r') as f:
    inp = f.read()

parts = inp.split("\n\n")
lines = parts[0].split("\n")

def expand(c):
    if c == "O":
        return "[]"
    elif c == "@":
        return "@."
    else:
        return c + c

lines = ["".join(expand(c) for c in l) for l in lines]

m = len(lines)
n = len(lines[0])

grid = defaultdict(lambda: defaultdict(lambda: "!"))
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        grid[i][j] = c

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
chardirs = {"<": 1, ">": 0, "^": 2, "v": 3}

def check_move(d, i, j, already_checked):
    if (i, j) in already_checked:
        return already_checked[(i, j)]
    already_checked[(i, j)] = True
    if grid[i][j] == "#":
        already_checked[(i, j)] = False
    elif grid[i][j] == ".":
        already_checked[(i, j)] = True
    elif grid[i][j] == "@":
        already_checked[(i, j)] = check_move(d, i + d[0], j + d[1], already_checked)
    elif grid[i][j] == "[":
        already_checked[(i, j)] = check_move(d, i + d[0], j + d[1], already_checked) and check_move(d, i, j + 1, already_checked)
    elif grid[i][j] == "]":
        already_checked[(i, j)] = check_move(d, i + d[0], j + d[1], already_checked) and check_move(d, i, j - 1, already_checked)
    return already_checked[(i, j)]

def commit_move(d, i, j, already_committed):
    if (i, j) in already_committed:
        return
    already_committed.add((i, j))
    if grid[i][j] == "#":
        return
    elif grid[i][j] == ".":
        return
    elif grid[i][j] == "[":
        commit_move(d, i + d[0], j + d[1], already_committed)
        commit_move(d, i, j + 1, already_committed)
        grid[i + d[0]][j + d[1]] = grid[i][j]
        grid[i][j] = "."
    elif grid[i][j] == "]":
        commit_move(d, i + d[0], j + d[1], already_committed)
        commit_move(d, i, j - 1, already_committed)
        grid[i + d[0]][j + d[1]] = grid[i][j]
        grid[i][j] = "."
    elif grid[i][j] == "@":
        commit_move(d, i + d[0], j + d[1], already_committed)
        grid[i + d[0]][j + d[1]] = grid[i][j]
        grid[i][j] = "."

robot_pos = (0, 0)
for i in range(m):
    for j in range(n):
        if grid[i][j] == "@":
            robot_pos = (i, j)

for dirchar in parts[1]:
    if dirchar == "\n":
        continue
    d = dirs[chardirs[dirchar]] 
    if check_move(d, robot_pos[0], robot_pos[1], {}):
        commit_move(d, robot_pos[0], robot_pos[1], set()) 
        robot_pos = (robot_pos[0] + d[0], robot_pos[1] + d[1])

result = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == "[":
            result += 100 * i + j

print("Final GPS sum:", result)