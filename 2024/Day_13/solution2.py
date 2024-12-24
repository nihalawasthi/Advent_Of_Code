data = []
with open("Day_13/input.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

offset = 10000000000000
groups = '\n'.join(data).split('\n\n')
total = 0
for group in groups:
    a_str, b_str, p_str = group.split('\n')

    ax, ay = [int(x[2:]) for x in a_str[10:].split(', ')]
    bx, by = [int(x[2:]) for x in b_str[10:].split(', ')]
    px, py = [int(x[2:]) for x in p_str[7:].split(', ')]

    px += offset
    py += offset

    m = (px * by - py * bx) // (ax * by - ay * bx)
    if m * (ax * by - ay * bx) != (px * by - py * bx):
        continue
    n = (py - ay * m) // by
    if n * by != (py - ay * m):
        continue

    total += 3 * m + n

print(total)