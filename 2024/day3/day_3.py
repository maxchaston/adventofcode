# Part 1
import re
f = open("input.txt", "r")
line = f.read()
muls = re.findall(r"mul\(\d+,\d+\)", line)
count=0
for mul in muls:
    num1 = int(mul.split(",")[0].split("(")[1])
    num2 = int(mul.split(",")[1].split(")")[0])
    count+=num1*num2
print(count)

'''
Pretty easy regex, could have used capture groups to
clean up the string formatting for the numbers, but
not really necessary apart for a quick first try.
'''

# Part 2
count = 0
# ops = re.findall(r"(?:mul\((\d+),(\d+)\))|((?:don't\(\))|(?:do\(\)))", line)
ops = re.findall(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))", line)
print(ops)
do = True
for op in ops:
    if op[0] == "do()":
        do = True
    if op[0] == "don't()":
        do = False
    if op[0].startswith('mul'):
        if do:
            num1 = int(op[1])
            num2 = int(op[2])
            count+=num1*num2
print(count)

'''
A cool use of regex.
I was thinking to write a proper parser, but it
essentially would have been a reimplementation of
regex used to iterate through the list.
That would be the way to go if there weren't such easily
available regex libraries.
'''
