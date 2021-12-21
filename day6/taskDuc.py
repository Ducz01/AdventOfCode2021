import numpy as np
with open('day6/inputDuc.txt') as f:
    lines = f.readlines()

fishPool = lines[0].split(',')
all_fish = []
for i in range(9):
    all_fish.append(0)
for fish in fishPool:
    all_fish[int(fish)] += 1
    
print(len(all_fish))
print(all_fish)

days = 256

for i in range(days):
    reproduceNumber = all_fish[0]

    for index in range(1,len(all_fish)):
        all_fish[index-1] = all_fish[index]
    all_fish[6] += reproduceNumber
    all_fish[8] =reproduceNumber



sum = 0
for fishrow in all_fish:
    sum+=fishrow

print(sum)