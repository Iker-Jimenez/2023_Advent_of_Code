import re

with open('data.txt', 'r') as data_file:
    total = 0
    for line in data_file:
        print('--------------------------')
        print(line)
        first_num = None
        last_num = None
        indexes = {}
        line = line.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")
        print(line)
        numbers = re.findall("\d", line)
        line_num = int(numbers[0] + numbers[-1])
        total += line_num
        print("number=%d" % line_num)

print("Total is %d" % total)
