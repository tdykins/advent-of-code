# from functions import get_input

# get_input("https://adventofcode.com/2021/day/1/input", "day1_1.txt")

data = []
with open("data/day1_1.txt", "r") as input:
    for l in input:
        newline = l.rstrip()
        data.append(newline)

data = list(map(int,data))

A = 0
B = 1
C = 2
increases = []
current_sum = 0
prev_sum = 0

while C < len(data):
    current_sum = data[A] + data[B] + data[C]
    if current_sum > prev_sum: increases.append(current_sum)
    prev_sum = current_sum
    A +=1
    B +=1
    C +=1

print(len(increases)-1)
