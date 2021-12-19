with open('day3/input.txt') as f:
    lines = f.readlines()

def part1():
    gammaBinary = ''
    epsilonBinary = ''
    numberlength = len(lines[0]) -1
    
    for i in range(numberlength):
        zerocount = 0
        onecount = 0
        for line in lines:
            if len(line) <= i:
                break
            if line[i] == '0':
                zerocount+=1
            else:
                onecount+=1

        if zerocount > onecount:
            gammaBinary += '0'
            epsilonBinary += '1'
        else:
            gammaBinary += '1'
            epsilonBinary += '0'

    gamma = int(gammaBinary, 2)
    epsilon = int(epsilonBinary, 2)
    print(gamma * epsilon)
    

def part2():
    # number of bits/columns
    numberlength = len(lines[0]) -1
    oxygenlist = lines
    co2list = lines

    oxygen = 0
    co2 = 0
    
    for i in range(numberlength):
        oxygenlistzero, oxygenlistone = checkLists(i, oxygenlist)
        if len(oxygenlistone) >= len(oxygenlistzero):
            oxygenlist = oxygenlistone
        else: 
            oxygenlist = oxygenlistzero

        if len(oxygenlist) == 1:
            oxygen = oxygenlist[0]

        co2listzero, co2listone = checkLists(i, co2list)
        if len(co2listzero) <= len(co2listone):
            co2list = co2listzero
        else:
            co2list = co2listone
        if len(co2list) == 1:
            co2 = co2list[0]

        if len(co2list) ==1 and len(oxygenlist) ==1:
            break
    
    oxygenResult = int(oxygen, 2)
    co2Result = int(co2, 2)
    print(oxygenResult * co2Result)

def checkLists(index, list):
    zerolist = []
    onelist = []

    for element in list:
        if element[index] == '0':
            zerolist.append(element)
        else:
            onelist.append(element)
    return zerolist, onelist
    

#part1()
part2()