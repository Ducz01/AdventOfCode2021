with open('day6/inputMona.txt') as f:
    lines = f.readlines()

#Save numbers to draw in array
drawString = lines[0]
drawPool = drawString.split(',')
initialLength = len(drawPool)
print(len(drawPool))

for i in range(80):
    for i in range(len(drawPool)):
        #print(drawPool[i])
        if int(drawPool[i]) == 0:
            drawPool[i] == 6
            drawPool.append(8)
        else:
            drawPool[i] = int(drawPool[i]) - 1
           
