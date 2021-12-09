import io
import logging
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


file = "day8/input.txt"

displays = [[]]
number_of_uniques = 0
with open(file) as f:
    displays = [ x.split("|")[1].split() for x in f.readlines()]


for digits in displays:
    for digit in digits:
        if len(digit) != 5 and len(digit) != 6:
            number_of_uniques += 1

log.info(f"Number of unique digits: {number_of_uniques}")




