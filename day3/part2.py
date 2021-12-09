import io

def most_common(lst, pos):
    count = 0
    for item in lst:
        count += int(item[pos])
    if count > len(lst) / 2:
        return '1'
    elif count < len(lst) / 2:
        return '0'
    else:
        return '2'

with open("day3/input.txt") as file:
    has_error = False
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    oxigen = lines
    co2 = lines
    for i in range(len(lines[0])):
        content_o2 = most_common(oxigen, i)
        content_co2 = most_common(co2, i)
        print("most common: ", content_o2, content_co2)
        if len(oxigen) > 1:
            if content_o2 == '2' or content_o2 == '1':
                oxigen = [line for line in oxigen if line[i] == '1']
            else:
                oxigen = [line for line in oxigen if line[i] == '0']
        if len(co2) > 1:
            if content_co2 == '1' or content_co2 == '2':
                co2 = [line for line in co2 if line[i] == '0']
            else:
                co2 = [line for line in co2 if line[i] == '1']
        print("O2",oxigen)
        print("CO2",co2)
    co2_result = co2[0]
    o2_result = oxigen[0]
    print(int(co2_result, 2), int(o2_result, 2), int(co2_result, 2) * int(o2_result, 2))
