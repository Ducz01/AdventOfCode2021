with open('day7/inputDuc.txt') as f:
    lines = f.readlines()

def getFuelCount(pos):
    fuelsum = 0
    for submarine in submarines:
        fuelsum += abs(submarine-pos)
    return fuelsum

def getExponentialFuelCount(pos):
    fuelsum = 0
    for submarine in submarines:
        diff = abs(submarine - pos)
        fuelWaste = (diff*(diff+1))/2
        fuelsum += fuelWaste
    return fuelsum

submarines = [int(s) for s in lines[0].split(',')]
def part1():
    positionCounter={}
    for submarine in submarines:
        if submarine in positionCounter:
            positionCounter[submarine] = positionCounter[submarine]+1
        else:
            positionCounter[submarine] = 1
    newcounter = dict(sorted(positionCounter.items(), key=lambda item: item[1]))
    countervalues = list(newcounter.keys())
    chosenValue = countervalues[len(newcounter.values())-1]

    minFuelCount = 2390572
    minPos = 0
    for key in positionCounter:
        print(key)
        fuelUse = getFuelCount(key)
        if fuelUse < minFuelCount:
            minFuelCount = fuelUse
            minPos = key

    print(minPos)
    print(minFuelCount)

def part2():
    sum = 0
    for submarine in submarines:
        sum+=submarine
    
    middle = sum/len(submarines)
    print(middle)
    diff=1000
    pos = int(middle)
    print(pos)

    print(getExponentialFuelCount(pos))
    

part2()