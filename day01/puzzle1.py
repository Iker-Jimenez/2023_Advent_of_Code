import sys

with open('data.txt', 'r') as data_file:
    total = 0
    for line in data_file:
        first_num = None
        last_num = None
        for char in line:
            if char.isnumeric():
                if first_num is None:
                    first_num=char
                last_num=char
        line_num = int(first_num + last_num)
        total += line_num
        print("number=%d" % line_num)

print("Total is %d" % total)
