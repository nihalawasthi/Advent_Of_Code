import collections
import sys

fname =  "Day_12/input.txt" if len(sys.argv) < 2 else sys.argv[1]

out = 0

grid = []
total = 0

for line in open(fname):
  line = line.strip()
  grid += [line]
  total += len(line)

used = set()

def p(a, b):
  return (a[0] + b[0], a[1] + b[1])

def invert(a):
  return (a[1], a[0])

def neg(a):
  return (-1 * a[0], -1 * a[1])

while len(used) < total:
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if (i,j) not in used:
        current_region = set()
        borders = []
        num_borders = 0
        queue = [(i,j)]
        while queue:
          n = queue.pop()
          current_region.add(n)
          ii = n[0]
          jj = n[1]
          for d in [(0,1), (1,0), (-1,0), (0,-1)]:
            iii = ii + d[0]
            jjj = jj + d[1]
            if iii < 0 or iii >= len(grid) or jjj < 0 or jjj >= len(grid[iii]) or grid[iii][jjj] != grid[i][j]:
              borders += [((iii, jjj), d)]
            elif (iii, jjj) not in queue and (iii, jjj) not in current_region:
              queue += [(iii, jjj)]
        while borders:
          pt, d = borders.pop()
          flipped = invert(d)
          pt2 = pt
          while True:
            pt2 = p(pt2, flipped)
            if (pt2,d) in borders:
              borders.remove((pt2, d))
            else:
              break
          pt2 = pt
          while True:
            pt2 = p(pt2, neg(flipped))
            if (pt2,d) in borders:
              borders.remove((pt2, d))
            else:
              break
          num_borders += 1

        out += len(current_region) * num_borders
        for n in current_region:
          used.add(n)

print(out)