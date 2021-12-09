import io

with open("day1/input.txt") as file:
    acm = 0
    lines = file.readlines()
    lines = [float(line.rstrip()) for line in lines]
    for i in range(3, len(lines)):
        previous = lines[i - 1] + lines[i - 2] + lines[i - 3]
        current = lines[i] + lines[i - 1] + lines[i - 2]
        print(previous, current)
        if current > previous:
            acm += 1
    print(acm)