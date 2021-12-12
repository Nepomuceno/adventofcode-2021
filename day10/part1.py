import io
import logging
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


file = "day10/input.txt"


lines = []
wrong_found = [0,0,0,0]
score_weight = [3,57,1197,25137]
with open(file) as f:
    lines = [ x.strip() for x in f.readlines()]

for line in lines:
    content = []
    for char in line:
        if char in ['(' ,'[' ,'{', '<']:
            content.append(char)
        elif char == ')':
            last = content.pop()
            if last != '(':
                wrong_found[0] += 1
                break
        elif char == ']':
            last = content.pop()
            if last != '[':
                wrong_found[1] += 1
                break            
        elif char == '}':
            last = content.pop()
            if last != '{':
                wrong_found[2] += 1
                break
        elif char == '>':
            last = content.pop()
            if last != '<':
                wrong_found[3] += 1
                break

log.info(f"Wrong found: {wrong_found}")
log.info(f"Score: {wrong_found[0] * score_weight[0] + wrong_found[1] * score_weight[1] + wrong_found[2] * score_weight[2] + wrong_found[3] * score_weight[3]}")





