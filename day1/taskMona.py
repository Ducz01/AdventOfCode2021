with open('day1/inputMona.txt') as f:
    lines = f.readlines()

increaseCount = 0

for i in range(len(lines)):
    if i != 0 and int(lines[i]) > int(lines[i-1]):
        increaseCount += 1

#print(increaseCount)

increaseCountSum = 0
sum1 = 0
sum2 = 0
for i in range(len(lines)):
    if i + 3 > len(lines): 
        break
    if i == 0:
        sum1 = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        sum2 = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
    else:
        sum1 = sum2
        sum2 = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    if(sum2 > sum1):
        increaseCountSum +=1

print(increaseCountSum)
        
