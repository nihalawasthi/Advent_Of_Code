with open( "Day_14/input.txt", 'r') as file:
    lines = file.readlines()

x_max = 101
y_max = 103
lines = [line.strip() for line in lines]

positions = []
velocities = []
for i in range(len(lines)):
    line = lines[i]
    p = line.split(' ')[0].split('=')[1]
    v = line.split(' ')[1].split('=')[1]
    px = int(p.split(',')[0])
    py = int(p.split(',')[1])
    vx = int(v.split(',')[0])
    vy = int(v.split(',')[1])
    positions.append((px, py))
    velocities.append((vx, vy))

T = 0
while True:
    distint_positions = set(positions)
    if len(distint_positions) == len(positions):
        break

    for i in range(len(positions)):
        px, py = positions[i]
        vx, vy = velocities[i]
        positions[i] = ((px + vx) % x_max, (py + vy) % y_max)

    T += 1

print(T)