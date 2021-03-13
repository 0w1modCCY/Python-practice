import re
hand = open('regex_sum_1035094.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)

    for num in stuff:
        n = int(num)
        numlist.append(n)

print("Maximum: ", sum(numlist))
