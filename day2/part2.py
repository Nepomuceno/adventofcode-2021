import io

with open("day2/input.txt") as file:
    horizontal = 0
    depth = 0
    aim = 0
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    for line in lines:
        print(line)
        command = line.split(" ")[0]
        value = int(line.split(" ")[1])
        if command == "forward":
            horizontal += value
            depth += (aim * value)
        elif command == "up":
            aim -= value
        elif command == "down":
            aim += value
        print(horizontal, depth, aim)
    print(horizontal, depth)
    print(horizontal*depth)

