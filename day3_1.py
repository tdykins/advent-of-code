# from functions import get_input

# get_input("https://adventofcode.com/2021/day/3/input", "day3_1.txt")

import pandas as pd

data = pd.read_csv("data/day3_1.txt", header=None, dtype=str, names=["Report"])
#print(data.head())

for i in range(1,13):
    data[f"bit_{i}"] = data['Report'].str[i-1]
#print(data.head())

for i in range(1,13):
    data[f"bit_{i}"] = pd.to_numeric(data[f"bit_{i}"])
# print(data.head())

gamma = ''
for i in range(1,13): 
    gamma += str((sum(data[f"bit_{i}"].mode())))
# print(gamma)
# print(type(gamma))

epsilon = ''
for i in gamma:
    nxt_bit = 1 - int(i)
    epsilon += str(nxt_bit)
# print(epsilon)
# print(type(epsilon))

print("Gamma:",gamma)
print("Epsilon:",epsilon)
print("Power consumption:",(int(gamma,2)) * (int(epsilon,2)))




