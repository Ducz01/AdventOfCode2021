with open('day14/inputDuc.txt') as f:
    lines = f.readlines()
    f.close()

startingFormula = lines[0].strip()
formulaRules = {}

for line in lines:
    if lines.index(line) > 1:
        parts = line.strip().split(' -> ')
        formulaRules[parts[0]] = parts[1]


def step(formula):
    res = formula[0]
    for i in range(1, len(formula)):
        current = formula[i]
        key = formula[i-1]+current
        inbetween = formulaRules[key]
        res += inbetween
        res += current
    return res

def coolStep(formula):
    newPairs = []
    for entry in formula:
        newChar = formulaRules[entry]
        newPairs.append(entry[0]+newChar)
        newPairs.append(newChar + entry[1])
    return newPairs

def part1():
    currentFormula = startingFormula
    for i in range(40):
        print(i, len(currentFormula))
        currentFormula = step(currentFormula)
    occurencies = {}
    for char in currentFormula:
        if char in occurencies:
            occurencies[char] = occurencies[char]+1
        else:
            occurencies[char] = 1
    sortedOccurencies = dict(sorted(occurencies.items(), key=lambda item: item[1]))
    result = int(sortedOccurencies[list(sortedOccurencies)[-1]]) - int(sortedOccurencies[list(sortedOccurencies)[0]])
    print(result)


def part2():
    currentFormula=[]
    for i in range(1, len(startingFormula)):
        currentFormula.append(startingFormula[i-1]+startingFormula[i])
    for i in range(40):
        print(i)
        currentFormula = coolStep(currentFormula)
    
    print('done')
part1()