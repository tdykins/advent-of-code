
# from functions import get_input

# get_input("https://adventofcode.com/2021/day/1/input", "day1_1.txt")

data = []
with open("data/day1_1.txt", "r") as input:
    for l in input:
        newline = l.rstrip()
        data.append(newline)

data = list(map(int,data))

diffs = []
it = 0
for i in data:
    if it == 0:
        prev = i
        it +=1
    else:
        if i > prev: diffs.append(i)
        prev = i
        it +=1


print("Total measurements:", len(data))
print("Total increases:", len(diffs))


