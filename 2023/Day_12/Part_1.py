with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_12\input.txt") as file:
    lines = file.read().split('\n')
    

def get_options(springs):
    ops = []

    def solve(substr, idx):
        if idx == len(springs):
            ops.append(substr)
            return

        if springs[idx] in '.#':
            solve(f'{substr}{springs[idx]}', idx + 1)
        else:
            solve(f'{substr}.', idx + 1)
            solve(f'{substr}#', idx + 1)
    solve('', 0)

    return ops


def _check_spring(opt, m):
    tmp = [len(k) for k in opt.split('.') if k]
    return tmp == m


ans = 0
for line in lines:
    springs, m = line.split()
    m = [int(x) for x in m.split(',')]
    opts = get_options(springs)
    for opt in opts:
        if _check_spring(opt, m):
            ans += 1

print(ans)