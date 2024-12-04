with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_14\input.txt") as file:
    lines = file.read().split('\n')

height = len(lines)

ans = 0

for col in range(len(lines[0])):
    stop = 0
    for idx, line in enumerate(lines):
        cur = line[col]
        if cur == '#':
            stop = idx + 1
        if cur == 'O':
            ans += (height - stop)
            stop += 1

print(ans)