with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_15\input.txt") as file:
    lines = file.read().split('\n')


ans = 0
for seq in lines[0].split(','):
    tmp = 0
    for c in seq:
        tmp += ord(c)
        tmp *= 17
        tmp %= 256
    ans += tmp

print(ans)