import io
import logging
import os
from typing import List, Tuple

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


file = "day9/input.txt"

def local_low(i, j, points, basins) -> bool:
    height = len(points)
    width = len(points[0])
    response = False
    if i > 0:
        if (i-1, j) not in basins:
            response = True
            if int(points[i-1][j]) <= int(points[i][j]):
                return False 
    if i < height - 1:
        if (i+1,j) not in basins:
            response = True
            if int(points[i+1][j]) <= int(points[i][j]):
                return False
    if j > 0:
        if (i,j-1) not in basins:
            response = True
            if int(points[i][j-1]) <= int(points[i][j]):
                return False
    if j < width - 1:
        if (i,j+1) not in basins:
            response = True
            if int(points[i][j+1]) <= int(points[i][j]):
                return False
    if response == True and int(points[i][j]) == 9:
        log.error("Found a local low at %s,%s" % (i,j))
    return response

def get_basin(i: int, j: int, points:List[List[int]], basins:List) -> List:
    height = len(points)
    width = len(points[0])
    if i > 0:
        if (i-1, j) not in basins:
            if local_low(i-1,j,points,basins):
                basins.append((i-1,j))
                basins = get_basin(i-1,j,points,basins)
    if i < height - 1:
        if (i+1,j) not in basins:
            if local_low(i+1,j,points,basins):
                basins.append((i+1,j))
                basins = get_basin(i+1,j,points,basins)
    if j > 0:
        if (i,j-1) not in basins:
            if local_low(i,j-1,points,basins):
                basins.append((i,j-1))
                basins = get_basin(i,j-1,points,basins)
    if j < width - 1:
        if (i,j+1) not in basins:
            if local_low(i,j+1,points,basins):
                basins.append((i,j+1))
                basins = get_basin(i,j+1,points,basins)
    return basins

def get_lowest_neighbours_coordinates(i, j, points):
    value = int(points[i][j])
    lower_value = (float("inf"), (0,0))
    if i > 0:
        if int(points[i - 1][j]) < value and int(points[i - 1][j]) < lower_value[0]:
            lower_value = (int(points[i - 1][j]), (i - 1, j))
    if i < height - 1:
        if int(points[i + 1][j]) < value and int(points[i + 1][j]) < lower_value[0]:
            lower_value = (int(points[i + 1][j]), (i + 1, j))
    if j > 0:
        if int(points[i][j - 1]) < value and int(points[i][j - 1]) < lower_value[0]:
            lower_value = (int(points[i][j - 1]), (i, j - 1))
    if j < width - 1:
        if int(points[i][j + 1]) < value and int(points[i][j + 1]) < lower_value[0]:
            lower_value = (int(points[i][j + 1]), (i, j + 1))
    return lower_value[1]

# Calculate distance between two points in a Matrix including diagonals
def caculate_distance(point_a: Tuple[int,int], point_b: Tuple[int,int]):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

# Get the closest low point to the given point
# def get_closest_low(i, j, lowest_points:dict):
#     distances = [(caculate_distance((i,j), point),point) for point in lowest_points.keys()]
#     log.info("Distances: %s" % distances) 
#     min_distance = min(distances)
#     log.info("Min distance: %s, %s" % min_distance)
#     return min_distance[1]

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
low_points = {}
danger_level = 0
with open(file) as f:
    points = [ list(x.strip()) for x in f.readlines()]

height = len(points)
width = len(points[0])
basins_legth_collection = []


for i in range(height):
    for j in range(width):
        neighbours = get_neighbours(i, j, points)
        log.debug(f"{i},{j} neighbours: {neighbours}")
        if int(points[i][j]) < min(neighbours):
            log.debug(f"{i},{j} is a low point of value {points[i][j]}")
            danger_level += (int(points[i][j]) + 1)
            low_points[(i,j)] = []

for i in range(height):
    for j in range(width):
        if points[i][j] != '9':
            if (i,j) in low_points.keys():
                low_points[(i,j)].append((i,j))
                continue
            lowest_neigbour = get_lowest_neighbours_coordinates(i,j,points)
            while lowest_neigbour not in low_points:
                lowest_neigbour = get_lowest_neighbours_coordinates(lowest_neigbour[0],lowest_neigbour[1],points)
            log.info(f"{i},{j} is a low point of value {lowest_neigbour}")
            low_points[lowest_neigbour].append((i,j))

log.debug(f"{low_points}")
basins = sorted([len(basins) for basins in low_points.values()])
log.debug(f"Basins: {basins}")
log.info(f"Danger level: { basins[-1] * basins[-2] * basins[-3] }")
