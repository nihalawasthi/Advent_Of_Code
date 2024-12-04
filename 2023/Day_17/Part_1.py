from queue import PriorityQueue

with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_17\input.txt") as file:
    lines = file.read().split('\n')

grid = [
    [int(x) for x in list(l)]
    for l in lines
]
height = len(grid)
width = len(grid[0])
d = {
    '>': (0, 1),
    '<': (0, -1),
    'v': (1, 0),
    '^': (-1, 0),
}


def _get_next(x, y, dir):
    a, b = d[dir]
    return x + a, y + b


def dijkstra(grid):
    pq = PriorityQueue()
    seen = set()
    pq.put((0, 0, 0, 1, '>'))

    while not pq.empty():
        loss, x, y, steps, dir = pq.get()

        if x == height - 1 and y == width - 1:
            return loss

        if (x, y, steps, dir) in seen:
            continue

        seen.add((x, y, steps, dir))

        to_go = []
        if steps < 3:
            to_go.append(dir)
        if dir in ('>', '<'):
            to_go.extend(['v', '^'])
        if dir in ('v', '^'):
            to_go.extend(['>', '<'])

        for new_dir in to_go:
            nx, ny = _get_next(x, y, new_dir)
            if nx < 0 or nx >= height or ny < 0 or ny >= width:
                continue
            new_steps = steps + 1 if new_dir == dir else 1
            pq.put((loss + grid[nx][ny], nx, ny, new_steps, new_dir))


print(dijkstra(grid))