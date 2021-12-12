import logging
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

file = "day12/input.txt"
paths = {}

with open(file) as f:
    for line in f:
        x, y = line.split('-')
        if x not in paths:
            paths[x] = []
        paths[x].append(y)


