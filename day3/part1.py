import io
def most_common(lst, pos):
    count = 0
    for item in lst:
        count += int(item[pos])
    if count > len(lst) / 2:
        return 1
    elif count < len(lst) / 2:
        return 0
    else:
        return 2

with open("day3/sample.txt") as file:
    content = ''
    reversed_content = ''
    has_error = False
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    for i in range(len(lines[0])):
        content_res = most_common(lines, i)
        content += str(content_res)
        reversed_content += content_res == 1 and '0' or '1'
    print(content)
    print(reversed_content)
    if not has_error:
        print(int(content, 2), int(reversed_content, 2), int(content, 2) * int(reversed_content, 2))
    else:
        print('No error')