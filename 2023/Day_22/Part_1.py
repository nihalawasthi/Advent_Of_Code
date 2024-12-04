import re

with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_22\input.txt") as file:
    ls = file.read().strip().split()

ns = (map(int, re.findall("\d+", l)) for l in ls)
bricks = []
for x1, y1, z1, x2, y2, z2 in ns:
    bricks.append(
        {
            (x, y, z)
            for x in range(x1, x2 + 1)
            for y in range(y1, y2 + 1)
            for z in range(z1, z2 + 1)
        }
    )

all_locs = set.union(*bricks)
while True:
    any_dropped = False
    for i, brick in enumerate(bricks):
        all_without = all_locs - brick
        if all((x, y, z - 1) not in all_without for (x, y, z) in brick) and all(z > 1 for _, _, z in brick):
            brick = {(x, y, z - 1) for (x, y, z) in brick}
            bricks[i] = brick
            all_locs = all_without | brick
            any_dropped = True
    if not any_dropped:
        break

depends_on = [
    {
        j
        for j, brick2 in enumerate(bricks)
        if i != j and any((x, y, z - 1) in brick2 for (x, y, z) in brick1)
    }
    for i, brick1 in enumerate(bricks)
]

# Part 1
print(len(bricks) - len({list(v)[0] for v in depends_on if len(v) == 1}))