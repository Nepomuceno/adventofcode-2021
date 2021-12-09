import io
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

file = "day4/input.txt"

def check_win(board):
    won = False
    for row in board:
        if all(char == '#' for char in row):
            won = True
    ## check if the the any column is all '#'
    for i in range(len(board[0])):
        if all(row[i] == '#' for row in board):
            won = True
    return won

def mark_number(board, number):
    for row in board:
        for i, char in enumerate(row):
            if char == number:
                row[i] = '#'
    return board

def load_boards(filename):
    result = []
    with open(filename) as f:
        lines = [lines.strip() for lines in f.readlines()]
        for i in range(2, len(lines), 6):
            rows = lines[i:i+5]
            rows = [row.split() for row in rows]
            result.append(rows)
            log.debug(f"Loaded board {i}")
            log.debug(f"{result[-1]}")
    return result

def load_game(filename):
    with open(filename) as f:
        lines = [lines.strip() for lines in f.readlines()]
        return lines[0].split(',')

boards = load_boards(file)
game = load_game(file)
log.info(f"Loaded {len(boards)} boards")
log.info(f"Loaded {len(game)} numbers")
winning_board = []
winning_number = -1
# mark every nymber until there is a winnign board
for i in range(len(game)):
    log.info(f"Marking {game[i]}")
    for j in range(len(boards)):
        log.debug(f"Checking board {j}")
        log.debug(f"{boards[j]}")
        boards[j] = mark_number(boards[j], game[i])
        if check_win(boards[j]):
            winning_board = boards[j]
            winning_number = int(game[i])
            log.info(f"Board {j} is winning")
            log.info(f"{boards[j]}")
            break
    else:
        continue
    break

# sum all the numbers on the winning board
sum = 0
for row in winning_board:
    for char in row:
        if char != '#':
            sum += int(char)

print(f"The winning number is {winning_number}")
print(f"The sum of the winning board is {sum}")
print(f"the result is {winning_number * sum}")

# with open("day3/sample.txt") as file:
#     content = ''
#     reversed_content = ''
#     has_error = False
#     lines = file.readlines()
#     lines = [line.rstrip() for line in lines]
#     for i in range(len(lines[0])):
#         content_res = most_common(lines, i)
#         content += str(content_res)
#         reversed_content += content_res == 1 and '0' or '1'
#     print(content)
#     print(reversed_content)
#     if not has_error:
#         print(int(content, 2), int(reversed_content, 2), int(content, 2) * int(reversed_content, 2))
#     else:
#         print('No error')