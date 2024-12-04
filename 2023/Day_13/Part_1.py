with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_13\input.txt") as file:
    lines = [[list(pattern) for pattern in chunk.split('\n')]
             for chunk in file.read().split('\n\n')]


def reflection_h(pattern):
    for i in range(1, len(pattern)):
        flag = True
        for x, y in zip(pattern[:i][::-1], pattern[i:]):
            if x != y:
                flag = False
                break
        if flag:
            return i
    return 0


def reflection_v(pattern):
    pattern_columns = [[row[idx] for row in pattern] for idx in range(len(pattern[0]))]
    return reflection_h(pattern_columns)


def reflection(pattern):
    return (reflection_h(pattern) * 100) or reflection_v(pattern)


ans = 0
for pattern in lines:
    ans += reflection(pattern)
print(ans)