# from functions import get_input

# get_input("https://adventofcode.com/2021/day/2/input", "day2_1.txt")


data = []
with open("data/day2_1.txt", "r") as input:
    for l in input:
        newline = l.rstrip()
        line_contents = newline.split()
        data.append(line_contents)


horizontal = 0
depth = 0
aim = 0
for i in data:
    if i[0] == 'down': aim += int(i[1])
    if i[0] == 'up': aim -= int(i[1])
    if i[0] == 'forward': 
        horizontal += int(i[1])
        depth += (aim * int(i[1]))

    

print("Horizontal:", horizontal)
print("Depth:", depth)
print("H x D = ", horizontal * depth)