# from functions import get_input

# get_input("https://adventofcode.com/2021/day/3/input", "day3_1.txt")

import pandas as pd

data = pd.read_csv("data/day3_1.txt", header=None, dtype=str, names=["Report"])

for i in range(1,13):
    data[f"bit_{i}"] = data['Report'].str[i-1]

for i in range(1,13):
    data[f"bit_{i}"] = pd.to_numeric(data[f"bit_{i}"])


oxygen_filter = data
co2_filter = data

count1 = 1
while len(oxygen_filter) > 1:
    oxygen_filter = oxygen_filter[oxygen_filter[f"bit_{count1}"] == max(oxygen_filter[f"bit_{count1}"].mode().values)]
    count1 +=1

count2 = 1
while len(co2_filter) > 1:
    co2_filter = co2_filter[co2_filter[f"bit_{count2}"] != max(co2_filter[f"bit_{count2}"].mode().values)]
    count2 +=1

oxygen = oxygen_filter['Report'].iloc[0]
co2 = co2_filter['Report'].iloc[0]
life_support = (int(oxygen,2) * int(co2,2))
print("Oxygen:",oxygen)
print("co2:",co2)
print("Life support:",life_support)