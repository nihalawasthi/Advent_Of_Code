with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_08\input.txt") as file:
    lines = file.read().split('\n')

seq = lines[0]
d = {}
for line in lines[2:]:
    src, dst = line.split(' = ')
    d[src] = dst[1:-1].split(', ')

ans = 0
i = 0
cur = 'AAA'
while True:
    ans += 1
    if seq[i] == 'L':
        cur = d[cur][0]
    else:
        cur = d[cur][1]

    if cur == 'ZZZ':
        break

    i += 1
    i %= len(seq)

print(ans)