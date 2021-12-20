with open('day3/inputMona.txt') as f:
    lines = f.readlines()

gamma = ''
epsilon = ''
for i in range(len(lines[0])-1):
    ones = 0
    zeros = 0
    for line in lines:
        if int(line[i]) == 1:
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)