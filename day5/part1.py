import io
import logging
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class Vent:
    def __init__(self, startx : int, endx : int, starty : int, endy: int):
        self.startx = startx
        self.endx = endx
        self.starty = starty
        self.endy = endy
        self.minx = startx if startx < endx else endx
        self.maxx = endx if startx < endx else startx
        self.miny = starty if starty < endy else endy
        self.maxy = endy if starty < endy else starty

file = "day5/input.txt"

def load_vent(filename):
    result: List[Vent]= []
    with open(filename) as f:
        lines = [lines.strip() for lines in f.readlines()]
        for line in lines:
            start,end = [x.strip() for x in line.split("->")]
            startx,starty = [int(x) for x in start.split(",")]
            endx,endy = [int(x) for x in end.split(",")]
            result.append(Vent(startx,endx,starty,endy))
    log.info("Loaded %d vents", len(result))
    return result

# Print a number matrix to a file
def print_matrix(matrix):
    with open("day5/output.txt", "w") as f:
        for row in matrix:
            f.write("".join(["{:1}".format(x) for x in row]))
            log.debug("".join(["{:1}".format(x) for x in row]))
            f.write("\n")

vents = load_vent(file)

cols , rows = 0,0
for vent in vents:
    if vent.maxx > cols:
        cols = vent.maxx
    if vent.maxy > rows:
        rows = vent.maxy

matrix = [[0 for x in range(cols+1)] for x in range(rows+1)]

for vent in vents:
    if vent.startx == vent.endx or vent.starty == vent.endy:
        for x in range(vent.minx, vent.maxx+1):
            for y in range(vent.miny, vent.maxy+1):
                log.debug("{},{}".format(x,y))
                matrix[y][x] = matrix[y][x] + 1
    else:
        if vent.startx < vent.endx and vent.starty < vent.endy:
            for x in range(vent.maxx-vent.minx+1):
                matrix[vent.miny+x][vent.minx+x] = matrix[vent.miny+x][vent.minx+x] + 1
        elif vent.startx > vent.endx and vent.starty > vent.endy:
            for x in range(vent.maxx-vent.minx+1):
                matrix[vent.maxy-x][vent.maxx-x] = matrix[vent.maxy-x][vent.maxx-x] + 1
        elif vent.startx > vent.endx and vent.starty < vent.endy:
            for x in range(vent.maxx-vent.minx+1):
                matrix[vent.miny+x][vent.maxx-x] = matrix[vent.miny+x][vent.maxx-x] + 1
        elif vent.startx < vent.endx and vent.starty > vent.endy:
            for x in range(vent.maxx-vent.minx+1):
                matrix[vent.maxy-x][vent.minx+x] = matrix[vent.maxy-x][vent.minx+x] + 1
                    


print_matrix(matrix)

# Count the points in the matrix with value grater than one
count = 0
for row in matrix:
    for point in row:
        if point > 1:
            count = count + 1

print("Count: {}".format(count))

# def load_game(filename):
#     with open(filename) as f:
#         lines = [lines.strip() for lines in f.readlines()]
#         return lines[0].split(',')

# boards = load_boards(file)
# game = load_game(file)
# log.info(f"Loaded {len(boards)} boards")
# log.info(f"Loaded {len(game)} numbers")
# winning_board = []
# winning_number = -1
# # mark every nymber until there is a winnign board
# for i in range(len(game)):
#     log.info(f"Marking {game[i]}")
#     for board in boards:
#         log.debug(f"{board}")
#         board = mark_number(board, game[i])
#     for board in boards:
#         if check_win(board):
#             boards.remove(board)
#             log.info(f"Found winning board {board}")
#             if(len(boards) == 0):
#                 winning_board = board
#                 winning_number = int(game[i])
#                 break
#     else:
#         continue
#     break

# # sum all the numbers on the winning board
# sum = 0
# for row in winning_board:
#     for char in row:
#         if char != '#':
#             sum += int(char)

# print(f"The winning number is {winning_number}")
# print(f"The sum of the winning board is {sum}")
# print(f"the result is {winning_number * sum}")