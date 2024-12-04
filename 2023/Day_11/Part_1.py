with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_11\input.txt") as file:
    lines = file.read().split('\n')

lines = [list(l) for l in lines]

empty_lines = []
len_line = len(lines[0])
for idx, line in enumerate(lines):
    if set(line) == {'.'}:
        empty_lines.append(idx)

for i in empty_lines[::-1]:
    lines.insert(i, (['.'] * len_line))

empty_columns = []
for idx in range(len_line):
    flag = True
    for j in range(len(lines)):
        if lines[j][idx] == '#':
            flag = False
            break
    if flag:
        empty_columns.append(idx)

for column in empty_columns[::-1]:
    for line in lines:
        line.insert(column, '.')

galaxies = []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '#':
            galaxies.append((i, j))

ans = 0

for i, (x1, y1) in enumerate(galaxies):
    for (x2, y2) in galaxies[i + 1:]:
        ans += (abs(x1 - x2) + abs(y1 - y2))

print(ans)