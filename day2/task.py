with open('day2/input.txt') as f:
    lines = f.readlines()
def part1():
    horizontal = 0
    depth = 0

    for line in lines:
        commands = line.split(' ')
        command = commands[0]
        value = int(commands[1])
        if command == 'forward': 
            horizontal+=value
        elif command=='up':
            depth -= value
        elif command=='down':
            depth+=value

    print(horizontal * depth)

def part2():
    horizontal = 0
    depth = 0
    aim = 0

    for line in lines:
        commands = line.split(' ')
        command = commands[0]
        value = int(commands[1])
        if command == 'forward': 
            horizontal+=value
            depth += aim*value
        elif command=='up':
            aim -= value
        elif command=='down':
            aim+=value

    print(horizontal * depth)




#part1()
part2()