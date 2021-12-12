import logging
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

file = "day11/input.txt"


def add_one_to_octopus_neighbours(octopuses, i, j):
    if i > 0:
        octopuses[i-1][j] += 1
    if i < len(octopuses) - 1:
        octopuses[i+1][j] += 1
    if j > 0:
        octopuses[i][j-1] += 1
    if j < len(octopuses[i]) - 1:
        octopuses[i][j+1] += 1
    if i > 0 and j > 0:
        octopuses[i-1][j-1] += 1
    if i > 0 and j < len(octopuses[i]) - 1:
        octopuses[i-1][j+1] += 1
    if i < len(octopuses) - 1 and j > 0:
        octopuses[i+1][j-1] += 1
    if i < len(octopuses) - 1 and j < len(octopuses[i]) - 1:
        octopuses[i+1][j+1] += 1


def get_flashes(step, octopuses, last_flash):
    flashes = []
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            if octopuses[i][j] > 9 and last_flash[i][j] < step:
                last_flash[i][j] = step
                flashes.append((i, j))
    return flashes


def do_step(step, octopuses, last_flash):
    total_flashes = 0
    all_flashes = True
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            octopuses[i][j] += 1
    flashes = get_flashes(step, octopuses, last_flash)
    while len(flashes) > 0:
        for i, j in flashes:
            add_one_to_octopus_neighbours(octopuses, i, j)
        flashes = get_flashes(step, octopuses, last_flash)
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            if last_flash[i][j] == step:
                total_flashes += 1
                octopuses[i][j] = 0
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            if octopuses[i][j] != 0:
                all_flashes = False
                break
    return total_flashes, all_flashes


def print_octopuses(octopuses):
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            print(octopuses[i][j], end="")
        print()


octopuses = []
with open(file) as f:
    octopuses_string = [x.strip() for x in f.readlines()]
    for i in range(len(octopuses_string)):
        octopuses.append([])
        for j in range(len(octopuses_string[i])):
            octopuses[i].append(int(octopuses_string[i][j]))
height = len(octopuses)
width = len(octopuses[0])
last_flash = [[-1 for x in range(width)] for y in range(height)]
print(height, width)
total_flashes = 0
for step in range(900):
    flashes, all_flash = do_step(step, octopuses, last_flash)
    total_flashes += flashes
    print(f"--------{flashes}----------")
    print_octopuses(octopuses)
    if all_flash:
        print(f"all flash at step {step + 1}")
        break
print("------------------")
print(total_flashes)
