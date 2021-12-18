import logging
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def get_insertion(polimer: str, instructions: dict) -> List[str]:
    insertion = []
    for i in range(len(polimer) - 1):
        key = polimer[i] + polimer[i + 1]
        if key in instructions:
            insertion.append(instructions[key])
        else:
            insertion.append("")
    return insertion

# get count or each char in a string and return a dict
def get_count(string: str) -> dict:
    return {char: string.count(char) for char in string}

file = "day14/test.txt"
polimerer = ""
insertion = []
instructions = {}



with open(file) as f:
    lines = [line.strip() for line in f.readlines()]
    polimerer = lines[0]
    for i in range(2, len(lines)):
        key, value = lines[i].split(" -> ")
        instructions[key] = value



log.info(f"Polimerer: {polimerer}")
log.info(f"Instructions: {instructions.keys()}")


for i in range(10):
    insertion = get_insertion(polimerer, instructions)
    new_polimer = ""
    for j in range(len(polimerer)-1):
        new_polimer += polimerer[j] + insertion[j]
    new_polimer += polimerer[-1]
    polimerer = new_polimer
    log.debug(f"Polimer: {new_polimer} - {len(new_polimer)}")
    log.info("Step: %s", i)

log.info(f"Polimer: {polimerer}")
log.info(f"Polimer length: {len(polimerer)}")
count = get_count(polimerer)
log.info(f"Count: {count}")
# get max and min from count dict
max_count = max(count.values())
min_count = min(count.values())
log.info(f"Max: {max_count}")
log.info(f"Min: {min_count}")
log.info(f"Diff: {max_count - min_count}")
