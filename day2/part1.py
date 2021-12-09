import io

with open("day2/input.txt") as file:
    horizontal = 0
    depth = 0
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    for line in lines:
        print(line)
        command = line.split(" ")[0]
        value = line.split(" ")[1]
        if command == "forward":
            horizontal += int(value)
        elif command == "up":
            depth -= int(value)
        elif command == "down":
            depth += int(value)
    print(horizontal, depth)
    print(horizontal*depth)