import numpy as np


with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_18\input.txt") as file:
    lines = [l.split() for l in file.read().strip().split("\n")]
    
dirs = {"R": 1j, "L": -1j, "U": -1, "D": 1}


def solve(instructions):
    vs = np.array([dirs[d] * dist for d, dist in instructions])
    return abs(np.sum(np.cumsum(vs.real) * vs.imag)) + np.sum(np.abs(vs)) / 2 + 1


# Part 1
print(solve((d, int(length)) for d, length, _ in lines))