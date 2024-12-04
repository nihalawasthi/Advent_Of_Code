with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_04\input.txt") as file:
        lines = file.read().split('\n')

ans = 0

for line in lines:
    _, numbers = line.split(':')
    winner, ours = numbers.split('|')
    ws = set(winner.split())
    os = set(ours.split())
    matches = ws & os
    if matches:
        ans += 2 ** (len(matches) - 1)

print(ans)