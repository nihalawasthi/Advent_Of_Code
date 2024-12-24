
import datetime
import re

# Read the input from 'input.txt' file
def read_input(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data

# Part a: Solving the puzzle
def a(data):
    grid, moves = data.split("\n\n")
    wall = set()
    boxes = set()
    pos = None
    for i, line in enumerate(grid.splitlines()):
        width = len(line)
        for j, c in enumerate(line):
            if c == "#":
                wall.add(j + i*1j)
            elif c == "O":
                boxes.add(j + i*1j)
            elif c == "@":
                pos = j + i*1j
    height = i + 1
    move2dir = {
        ">": 1,
        "^": -1j,
        "<": -1,
        "v": 1j,
    }
    for move in moves.replace("\n", ""):
        dir = move2dir[move]
        if pos + dir in wall:
            continue
        if pos + dir not in boxes:
            pos += dir
            continue
        boxes_to_move = 0
        pos_to_check = pos + dir
        while True:
            if pos_to_check in boxes:
                boxes_to_move += 1
                pos_to_check += dir
            elif pos_to_check in wall:
                boxes_to_move = 0
                break
            else:
                break
        if boxes_to_move > 0:
            pos += dir
            box_to_move = pos
            boxes.remove(pos)
            boxes.add(pos + boxes_to_move * dir)
    s = 0
    for box in boxes:
        s += box.real + 100 * box.imag
    return s

# Part b: (example placeholder for part b, you can add the logic as needed)
def b(data):
    print("Part B is not implemented yet.")
    return 0

# Main execution function
def main():
    # Read the input from the file
    input_data = read_input("Day_15/input.txt")

    # Solve part a
    answer_a = a(input_data)
    print("Part A:", answer_a)

   

    # Optionally, print the results to a text file or store them
    # For example, puzzle.answer_a = answer_a, puzzle.answer_b = answer_b, etc.

if __name__ == '__main__':
    main()

 