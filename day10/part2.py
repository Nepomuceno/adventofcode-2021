import io
import logging
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


file = "day10/input.txt"


lines = []
wrong_found = [0,0,0,0]
score_weight = [3,57,1197,25137]
total_scores = []
with open(file) as f:
    lines = [ x.strip() for x in f.readlines()]

for line in lines:
    content = []
    corrupted = False
    for char in line:
        if char in ['(' ,'[' ,'{', '<']:
            content.append(char)
        elif char == ')':
            last = content.pop()
            if last != '(':
                wrong_found[0] += 1
                corrupted = True
                break
        elif char == ']':
            last = content.pop()
            if last != '[':
                wrong_found[1] += 1
                corrupted = True
                break            
        elif char == '}':
            last = content.pop()
            if last != '{':
                wrong_found[2] += 1
                corrupted = True
                break
        elif char == '>':
            last = content.pop()
            if last != '<':
                wrong_found[3] += 1
                corrupted = True
                break
    if len(content) != 0 and not corrupted:
        log.info("Autocomple: %s", content)
        total_score = 0
        while len(content) > 0:
            total_score *= 5
            value = content.pop()
            if value == '(':
                total_score += 1
            elif value == '[':
                total_score += 2
            elif value == '{':
                total_score += 3
            elif value == '<':
                total_score += 4
        total_scores.append(total_score)
total_scores = sorted(total_scores)
log.info(f"Wrong found: {wrong_found}")
log.info(f"Score: {wrong_found[0] * score_weight[0] + wrong_found[1] * score_weight[1] + wrong_found[2] * score_weight[2] + wrong_found[3] * score_weight[3]}")
log.info(f"Total scores: {total_scores}")
log.info(f"median score: {total_scores[len(total_scores)//2]}")





