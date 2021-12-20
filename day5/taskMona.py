import numpy as np

with open('day5/inputMona.txt') as f:
    lines = f.readlines()

values = []
coordinates = np.empty((0, 2), int)
maxX = 0
maxY = 0
for line in lines:
    valueHolder = line.split(' ')
    value1 = [int(s) for s in valueHolder[0].split(',')]
    value2 = [int(s) for s in valueHolder[2].split(',')]
    coordinates = np.append(coordinates, np.array([value1,value2]), axis=0)
    if coordinates[0][0] > maxX:
        maxX = coordinates[0][0]
    if coordinates[1][0] > maxX:
        maxX = coordinates[1][0]
    if coordinates[0][1] > maxY:
        maxY = coordinates[0][1]
    if coordinates[1][1] > maxY:
        maxY = coordinates[0][1]
    values.append(coordinates)

map = np.full((maxY, maxX), 0)

for value in values:
    x1 = value[0][0]
    x2 = value[1][0]

    y1 = value[0][1]
    y2 = value[1][1]

    if x1 == x2:
        if y2 < y1:
            holder = y1
            y1 = y2
            y2 = holder
        for i in range(y1,y2):
            map[i][x1] += 1
    if  y1 == y2:
        if x2 < x1:
            holder = x1
            x1 = x2
            x2 = holder
        for i in range(x1,x2):
            map[y1][i] += 1
sum = map[map >= 2]
print(sum)
   