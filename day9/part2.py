import io
import logging
from typing import List
import pprint

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
pp = pprint.PrettyPrinter(indent=2)

file = "day8/input.txt"
all_wires = list("abcdefg")

def load_basic_digits(all_10: List[str]):
    digits = {}
    for digit in all_10:
        if len(digit) == 2:
            digits["1"] = digit
        if len(digit) == 4:
            digits["4"] = digit
        if len(digit) == 3:
            digits["7"] = digit
        if len(digit) == 7:
            digits["8"] = digit
    return digits

def discover_a(discovered_wires: dict, discovered_digits: dict):
    seven = discovered_digits["7"]
    one = discovered_digits["1"]
    seven = [value for value in seven if value not in one]
    discovered_wires["a"] = seven[0]
    return discovered_wires

def discover_9_and_e(discovered_wires: dict, discovered_digits: dict, all_10: List[str]):
    four = discovered_digits["4"]
    for digit in all_10:
        if len(digit) != 6:
            continue
        intersection = [value for value in digit if value in four]
        if len(intersection) == 4:
            discovered_digits["9"] = digit
            e_wire = [value for value in all_wires if value not in digit]
            discovered_wires["e"] = e_wire[0]
    return discovered_wires, discovered_digits

def discover_3(discovered_digits: dict, discovered_wires: dict, all_10: List[str]):
    one = discovered_digits["1"]
    for digit in all_10:
        if len(digit) != 5:
            continue
        intersection = [value for value in digit if value in one]
        if len(intersection) == 2:
            discovered_digits["3"] = digit
    return discovered_digits

def discover_6_and_0(discovered_wires: dict, discovered_digits: dict, all_10: List[str]):
    remaining_digits = [value for value in all_10 if value not in discovered_digits.values()]
    one = discovered_digits["1"]
    for digit in remaining_digits:
        if len(digit) != 6:
            continue
        intersection = [value for value in digit if value in one]
        if len(intersection) == 2:
            discovered_digits["0"] = digit
        else:
            discovered_digits["6"] = digit
    six = discovered_digits["6"]
    zero = discovered_digits["0"]
    nine = discovered_digits["9"]
    seven = discovered_digits["7"]
    tree = discovered_digits["3"]
    four = discovered_digits["4"]
    c_wire = [value for value in zero if value not in six] 
    discovered_wires["c"] = c_wire[0]
    d_wire = [value for value in nine if value not in zero]
    discovered_wires["d"] = d_wire[0]
    a_c = [discovered_wires["a"], discovered_wires["c"]]
    f_wire = [value for value in seven if value not in a_c]
    discovered_wires["f"] = f_wire[0]
    a_c_d_f = [discovered_wires["a"], discovered_wires["c"], discovered_wires["d"], discovered_wires["f"]]
    g_wire = [value for value in tree if value not in a_c_d_f]
    discovered_wires["g"] = g_wire[0]
    b_wire = [value for value in four if value not in a_c_d_f]
    discovered_wires["b"] = b_wire[0]
    discovered_digits["5"] = sorted([discovered_wires["a"], discovered_wires["b"], discovered_wires["d"], discovered_wires["f"], discovered_wires["g"]])
    remaining_digits = [value for value in all_10 if value not in discovered_digits.values()]
    discovered_digits["2"] = remaining_digits[0]
    return discovered_wires, discovered_digits

def calculate_display(display: str):
    all_10 =[sorted(x) for x in display.split("|")[0].split()]
    output = [sorted(x) for x in display.split("|")[1].split()]
    discovered_wires = {}
    discovered_digits = load_basic_digits(all_10)
    discovered_wires = discover_a(discovered_wires, discovered_digits)
    discovered_wires, discovered_digits = discover_9_and_e(discovered_wires, discovered_digits, all_10)
    discovered_digits = discover_3(discovered_digits, discovered_wires, all_10)
    discovered_wires, discovered_digits = discover_6_and_0(discovered_wires, discovered_digits, all_10)
    # log.debug(pp.pprint(discovered_wires))
    # log.debug(pp.pprint(discovered_digits))
    content = ""
    for value in output:        
        number_value = list(discovered_digits.keys())[list(discovered_digits.values()).index(value)]
        content += number_value
    return content
displays = []
total = 0
with open(file) as f:
    displays = [ x for x in f.readlines()]

for display in displays:
    content = calculate_display(display)
    total += int(content)
    log.info(int(content))

log.info(total)




