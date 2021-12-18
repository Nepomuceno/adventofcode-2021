import logging
from typing import List, Tuple
from functools import reduce

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

from collections import defaultdict

package_types = {
    "000": "operator"
    , "001": "operator"
    , "010": "operator"
    , "011": "operator"
    , "100": "literal"
    , "101": "operator"
    , "110": "operator"
    , "111": "operator"
}

def get_bin_from_hex(hex_str: str) -> str:
    result = ""
    for i in range(len(hex_str)):
        char = hex_str[i]
        if char == "0":
            result += "0000"
        elif char == "1":
            result += "0001"
        elif char == "2":
            result += "0010"
        elif char == "3":
            result += "0011"
        elif char == "4":
            result += "0100"
        elif char == "5":
            result += "0101"
        elif char == "6":
            result += "0110"
        elif char == "7":
            result += "0111"
        elif char == "8":
            result += "1000"
        elif char == "9":
            result += "1001"
        elif char == "A":
            result += "1010"
        elif char == "B":
            result += "1011"
        elif char == "C":
            result += "1100"
        elif char == "D":
            result += "1101"
        elif char == "E":
            result += "1110"
        elif char == "F":
            result += "1111"
        else:
            raise Exception("Invalid character")
    return result


file = "day16/sample.txt"
content = open(file).read().split()

def execute_operation(operator: str, numbers: List[int]) -> int:
    if operator == "000":
        return sum(numbers)
    elif operator == "001":
        return reduce(lambda a, b: a * b, numbers,1)
    elif operator == "010":
        return min(numbers)
    elif operator == "011":
        return max(numbers)
    elif operator == "101":
        return 1 if numbers[0] > numbers[1] else 0
    elif operator == "110":
        return 1 if numbers[0] < numbers[1] else 0
    elif operator == "111":
        return 1 if numbers[0] == numbers[1] else 0

def parse_literal(literal: str) -> Tuple[int,int,str]:
    version = int(literal[:3],2)
    content = literal[6:]
    number_bin = ""
    while True:
        number_bin += content[1:5]
        if content[0] == "0":
            break
        content = content[5:]
    content = content[5:]
    return (version, int(number_bin,2), content)


def parse_operator(operator: str) -> Tuple[int,int,str]:
    version = int(operator[:3],2)
    operator_type = operator[3:6]
    legth_type = operator[6]
    content = operator[7:]
    number_of_packages = -1
    if legth_type == "0":
        length = int(content[:15],2)
        package_numbers = []
        package_content = content[15:length+15]
        while len(package_content.rstrip("0")) > 0:
            package_version, number, package_content = process_package(package_content)
            version += package_version
            package_numbers.append(number)
        content = content[length+15:]
    else:
        length = int(content[:11],2)
        content = content[11:]
        package_numbers = []
        for i in range(length):
            package_version, number, content = process_package(content)
            version += package_version
            package_numbers.append(number)
    value = execute_operation(operator_type, package_numbers)
    return (version, value, content)

def process_package(content: str) -> Tuple[int,int,str]:
    package_type = package_types[content[3:6]]
    if package_type == "literal":
        version, number, content = parse_literal(content)
    else:
        version, number, content = parse_operator(content)
    return version, number, content


for instruction in content:
    bin_instruction = get_bin_from_hex(instruction)
    sum_versions = 0
    while len(bin_instruction.rstrip("0")) > 0:
        version, number, bin_instruction = process_package(bin_instruction)
        sum_versions += version
        break
    print(f"{instruction}: {number}")