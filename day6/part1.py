import io
import logging
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class Pack:
    day0: int = 0
    day1: int = 0
    day2: int = 0
    day3: int = 0
    day4: int = 0
    day5: int = 0
    day6: int = 0
    day7: int = 0
    day8: int = 0

file = "day6/input.txt"

def tick_day_for_pack(pack: Pack) -> Pack: 
    new_pack = Pack()
    new_pack.day0 = pack.day1
    new_pack.day1 = pack.day2
    new_pack.day2 = pack.day3
    new_pack.day3 = pack.day4
    new_pack.day4 = pack.day5
    new_pack.day5 = pack.day6
    new_pack.day6 = pack.day7 + pack.day0
    new_pack.day7 = pack.day8
    new_pack.day8 = pack.day0
    return new_pack

pack = Pack()

with open(file) as f:
    fishes = [int(x) for x in f.readlines()[0].split(",")]
    for fish in fishes:
        if fish == 0:
            pack.day0 += 1
        elif fish == 1:
            pack.day1 += 1
        elif fish == 2:
            pack.day2 += 1
        elif fish == 3:
            pack.day3 += 1
        elif fish == 4:
            pack.day4 += 1
        elif fish == 5:
            pack.day5 += 1
        elif fish == 6:
            pack.day6 += 1
        elif fish == 7:
            pack.day7 += 1
        elif fish == 8:
            pack.day8 += 1

for i in range(0, 256):
    pack = tick_day_for_pack(pack)
    # sum all the pack days 
    print(pack.day0 + pack.day1 + pack.day2 + pack.day3 + pack.day4 + pack.day5 + pack.day6 + pack.day7 + pack.day8)


