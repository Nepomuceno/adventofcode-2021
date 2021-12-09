import io
import logging
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


file = "day9/input.txt"

def get_neighbours(i, j, points):
    neighbours = []
    height = len(points)
    width = len(points[0])
    if i > 0:
        neighbours.append(int(points[i - 1][j]))
    if i < height - 1:
        neighbours.append(int(points[i + 1][j]))
    if j > 0:
        neighbours.append(int(points[i][j - 1]))
    if j < width - 1:
        neighbours.append(int(points[i][j + 1]))
    return neighbours

points = [[]]
danger_level = 0
with open(file) as f:
    points = [ list(x.strip()) for x in f.readlines()]

height = len(points)
width = len(points[0])


for i in range(height):
    for j in range(width):
        neighbours = get_neighbours(i, j, points)
        log.debug(f"{i},{j} neighbours: {neighbours}")
        if int(points[i][j]) < min(neighbours):
            log.info(f"{i},{j} is a low point of value {points[i][j]}")
            danger_level += (int(points[i][j]) + 1)
log.info(f"Danger level: {danger_level}")





