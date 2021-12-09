import io
import logging
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


file = "day7/input.txt"

def calculate_needed_fuel(crabs: List[int], position) -> int:
    return sum([abs(crab-position) for crab in crabs])



max_value = 0
with open(file) as f:
    crabs = [int(x) for x in f.readlines()[0].split(",")]
    max_value = max(crabs)
    log.info(f"Max value: {max_value}")

min_value = 99999999999999999999999


for i in range(max_value):
    needed_fuel = calculate_needed_fuel(crabs, i)
    if needed_fuel < min_value:
        min_value = needed_fuel
        log.info(f"New min value: {i}, {min_value}")
