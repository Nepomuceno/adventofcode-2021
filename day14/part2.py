import logging
from types import new_class
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def get_polimeter_count(polimeters: dict) -> dict:
    result = {}
    for key, value in polimeters.items():
        if key[0] not in result:
            result[key[0]] = value
        else:
            result[key[0]] += value
        if key[1] not in result:
            result[key[1]] = value
        else:
            result[key[1]] += value
    return result
    

file = "day14/sample.txt"
polimerer = ""
insertion = []
instructions = {}



with open(file) as f:
    lines = [line.strip() for line in f.readlines()]
    polimerer = f"#{lines[0]}#"
    for i in range(2, len(lines)):
        key, value = lines[i].split(" -> ")
        instructions[key] = [key[0]+value[0], key[1]+value[0]]

log.info(f"Polimerer: {polimerer}")
log.info(f"Instructions: {instructions.keys()}")

polimerer_pairs = {}
for i in range(len(polimerer) - 1):
    key = polimerer[i] + polimerer[i + 1]
    if key in instructions:
        polimerer_pairs[key] = 1

# print(polimerer_pairs)

for i in range(10):
    new_pairs = {}
    for key, value in polimerer_pairs.items():
        if key in instructions:
            for instruction in instructions[key]:
                if instruction in new_pairs:
                    new_pairs[instruction] += 1 * value
                else:
                    new_pairs[instruction] = 1 * value
        else:
            if key in new_pairs:
                new_pairs[key] += 1 * value
            else:
                new_pairs[key] = 1 * value
    print(new_pairs)
    polimerer_pairs = new_pairs
    char_count = get_polimeter_count(polimerer_pairs)
    print(char_count)
    total_chars = sum(char_count.values())
    print(f"Total chars: {total_chars/2+1}")

max_count = max(char_count.values())
min_count = min(char_count.values())
log.info(f"Max: {max_count}")
log.info(f"Min: {min_count}")
log.info(f"Diff: {max_count/2 - min_count/2}")


# for i in range(2):
#     insertion = get_insertion(polimerer, instructions)
#     new_polimer = ""
#     for j in range(len(polimerer)-1):
#         new_polimer += polimerer[j] + insertion[j]
#     new_polimer += polimerer[-1]
#     polimerer = new_polimer
#     log.debug(f"Polimer: {new_polimer} - {len(new_polimer)}")
#     log.info("Step: %s", i)

# log.info(f"Polimer: {polimerer}")
# log.info(f"Polimer length: {len(polimerer)}")
# count = get_count(polimerer)
# log.info(f"Count: {count}")
# # get max and min from count dict
