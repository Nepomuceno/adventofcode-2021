import logging
from os import path
from typing import List, TextIO
from pprint import pprint
import sys

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def fold_acording_to_instruction(points: set, instruction):
    to_remove = set()
    to_add = set()
    if instruction[0] == 'x':
        for point in points:
            if point[0] > instruction[1]:
                new_x = point[0] - ((point[0] - instruction[1]) * 2)
                if (new_x, point[1]) not in points:
                    to_add.add((new_x, point[1]))
                to_remove.add(point)
    if instruction[0] == 'y':
        for point in points:
            if point[1] > instruction[1]:
                new_y = point[1] - ((point[1] - instruction[1]) * 2)
                if (point[0], new_y) not in points:
                    to_add.add((point[0], new_y))
                to_remove.add(point)
    for point in to_remove:
        points.remove(point)
    for point in to_add:
        points.add(point)

file = "day13/input.txt"
points = set()
instructions = []

with open(file) as f:
    for line in f:
        line = line.strip()
        if line == '':
            continue
        if line.startswith("fold along "):
            line = line.replace("fold along ", "").strip().split("=")
            if line[0] == "x":
                instructions.append(("x", int(line[1])))
            elif line[0] == "y":
                instructions.append(("y", int(line[1])))
            continue
        line = line.strip().split(",")
        points.add((int(line[0]), int(line[1])))

for instruction in instructions:
    fold_acording_to_instruction(points, instruction)
print(len(points))
x_min = min(points, key=lambda x: x[0])[0]
x_max = max(points, key=lambda x: x[0])[0]
y_min = min(points, key=lambda x: x[1])[1]
y_max = max(points, key=lambda x: x[1])[1]
with open("day13/output.txt", "w") as f:
    for i in range(y_min, y_max + 1):
        result = ""
        for j in range(x_min, x_max + 1):
            if (j, i) in points:
                result += "#"
            else:
                result += "."
        f.write(result + "\n")
    
print()