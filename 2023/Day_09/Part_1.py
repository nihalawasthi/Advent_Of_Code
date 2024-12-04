with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_09\input.txt") as file:
    lines = file.read().split('\n')

ans = 0

for line in lines:
    cur = [int(x) for x in line.split()]
    tmp = [list(cur)]
    while set(tmp[-1]) != {0}:
        cur = [
            cur[i] - cur[i - 1]
            for i in range(1, len(cur))
        ]
        tmp.append(list(cur))

    tmp[-1].append(0)
    for i in range(len(tmp) - 2, -1, -1):
        tmp[i].append(tmp[i + 1][-1] + tmp[i][-1])

    ans += tmp[0][-1]

print(ans)