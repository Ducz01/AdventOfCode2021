with open('day2/inputMona.txt') as f:
    lines = f.readlines()

depth = 0
horizontal = 0

for line in lines:
    number = [int(s) for s in line.split() if s.isdigit()]
    if line[0] == "f":
        horizontal += number[0]
    elif line[0] == "d":
        depth += number[0]
    else:
        depth -= number[0]

print(depth * horizontal)

depth = 0
horizontal = 0
aim = 0

for line in lines:
    number = [int(s) for s in line.split() if s.isdigit()]
    if line[0] == "f":
        horizontal += number[0]
        depth += number[0] * aim
    elif line[0] == "d":
        aim += number[0]
    else:
        aim -= number[0]

print(depth * horizontal)