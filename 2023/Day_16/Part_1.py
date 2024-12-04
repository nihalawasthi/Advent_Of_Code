from queue import Queue

with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_16\input.txt") as file:
    lines = file.read().split('\n')

def get_next(x, y, dir):
    d = {
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0),
        '^': (-1, 0),
    }
    a, b = d[dir]
    return ((x + a, y + b), dir)


seen = set()
q = Queue()
q.put(((0, 0), '>'))

while not q.empty():
    (x, y), dir = q.get()
    if x < 0 or y < 0 or x >= len(lines) or y >= len(lines[0]):
        continue

    if ((x, y), dir) in seen:
        continue

    seen.add(((x, y), dir))

    if lines[x][y] == '.':
        q.put(get_next(x, y, dir))
    elif lines[x][y] == '-':
        if dir in ('>', '<'):
            q.put(get_next(x, y, dir))
        else:
            q.put(get_next(x, y, '>'))
            q.put(get_next(x, y, '<'))
    elif lines[x][y] == '|':
        if dir in ('v', '^'):
            q.put(get_next(x, y, dir))
        else:
            q.put(get_next(x, y, '^'))
            q.put(get_next(x, y, 'v'))
    elif lines[x][y] == '/':
        if dir == '>':
            q.put(get_next(x, y, '^'))
        elif dir == '<':
            q.put(get_next(x, y, 'v'))
        elif dir == '^':
            q.put(get_next(x, y, '>'))
        elif dir == 'v':
            q.put(get_next(x, y, '<'))
    elif lines[x][y] == '\\':
        if dir == '>':
            q.put(get_next(x, y, 'v'))
        elif dir == '<':
            q.put(get_next(x, y, '^'))
        elif dir == '^':
            q.put(get_next(x, y, '<'))
        elif dir == 'v':
            q.put(get_next(x, y, '>'))


print(len(set(a for a, _ in seen)))