
with open('day12/inputDuc.txt') as f:
    lines = f.readlines()

connections = []
for line in lines:
    cleanLine = line.strip()
    parts = cleanLine.split('-')
    connections.append((parts[0],parts[1]))

currentCave = 'start'
count = 100
connectionCount = 0
queue = []
def checkPath(caveName, visited):
    alreadyVisited = []
    for element in visited: 
        alreadyVisited.append(element)

    if caveName == 'end':
        return 1
    if caveName in alreadyVisited and not caveName[0].isupper():
        return 0
    
    alreadyVisited.append(caveName)
    possibleConnections = []
    for connect in connections:
        if connect[0] == caveName:
            if connect[1] != 'start':
                possibleConnections.append(connect[1])
        elif connect[1] == caveName:
            if connect[0] != 'start':
                possibleConnections.append(connect[0])
    numberOfConnections = 0
    print(caveName, possibleConnections)
    print('already: ', alreadyVisited)
    
    for connection in possibleConnections:
        numberOfConnections += checkPath(connection, alreadyVisited)
    return numberOfConnections

def part1():
    startCave = 'start'
    possibleConnections = []
    alreadyVisited = []
    alreadyVisited.append(startCave)
    for connect in connections:
        if connect[0] == startCave:
            possibleConnections.append(connect[1])
        elif connect[1] == startCave:
            possibleConnections.append(connect[0])
    numberOfConnections = 0
    for connection in possibleConnections:
        numberOfConnections += checkPath(connection, alreadyVisited)
    print(numberOfConnections)



def checkPath2(caveName, visited):
    alreadyVisited = []
    for element in visited: 
        alreadyVisited.append(element)

    if caveName == 'end':
        return 1
    if caveName in alreadyVisited and not caveName[0].isupper():
        cantVisit = True
        smallCaves = []
        for visited in alreadyVisited:
            if not visited[0].isupper():
                smallCaves.append(visited)
            if len(smallCaves) != len(set(smallCaves)):
                return 0
    
    alreadyVisited.append(caveName)
    possibleConnections = []
    for connect in connections:
        if connect[0] == caveName:
            if connect[1] != 'start':
                possibleConnections.append(connect[1])
        elif connect[1] == caveName:
            if connect[0] != 'start':
                possibleConnections.append(connect[0])
    numberOfConnections = 0
    
    for connection in possibleConnections:
        numberOfConnections += checkPath2(connection, alreadyVisited)
    return numberOfConnections

def part2():
    startCave = 'start'
    possibleConnections = []
    alreadyVisited = []
    alreadyVisited.append(startCave)
    for connect in connections:
        if connect[0] == startCave:
            possibleConnections.append(connect[1])
        elif connect[1] == startCave:
            possibleConnections.append(connect[0])
    numberOfConnections = 0
    for connection in possibleConnections:
        numberOfConnections += checkPath2(connection, alreadyVisited)
    print(numberOfConnections)
part2()