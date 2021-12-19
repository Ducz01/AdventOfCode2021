with open('01/input.txt') as f:
    lines = f.readlines()

prev = int(lines[0])
counter = 0

#part 1
for line in lines:
    current = int(line)
    if current > prev:
        counter += 1
    prev = current

print(counter)

#part 2

prev = int(lines[0]) + int(lines[1]) + int(lines[2])
part2_counter = 0
for line in range(len(lines)):
    index = int(line)
    if index+2 > len(lines)-1:
        break
    current = int(lines[index]) + int(lines[index+1]) + int(lines[index+2])
    if current > prev:
        part2_counter+=1
    prev = current

print(part2_counter)