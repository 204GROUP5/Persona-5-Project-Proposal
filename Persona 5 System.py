import random

def getInputReal(elements):
    gotInput = False
    value = -1
    while not gotInput:
        value = int(input(""))
        if value in elements:
            gotInput = True
        else:
            print("Dumbass stupid idiot")

    return value


def getInputFake(elements):
    return 0 #doesn't work yet

def getInput(elements,inputType):
    if inputType:
        return getInputFake(elements)
    return getInputReal(elements)

def game():
    types = ["Physical", "Bullet", "Fire", "Ice", "Electric", "Wind", "Nuclear", "Blessed", "Curse", "Psychokinesis"]
    
    numE = random.randint(1,5)
    enemyArray = []
    enemyWeak = []
    enemyHit = []
    
    for i in range(numE):
        enemyArray.append(i)
        enemyWeak.append(random.randint(1,10))
        enemyHit.append(False)

    #teammate values
    teammates = [[],[],[],[]]
    element = 2
    
    for i in range(len(teammates)-1):
        teammates[i].append(0)
        teammates[i].append(1)
        teammates[i].append(element)
        element += 1

    for j in range(10):
        teammates[3].append(j)

    roundCount = 1
    allHit = False

    while not allHit:
        print("Round {}".format(roundCount))

        for i in range(len(teammates)):
            for j in range(numE):
                print("{}) Enemy {}".format(j,j+1))
            enemyTargeted = getInput(enemyArray,0)
            
            for k in range(len(teammates[i])):
                print("{}) {}".format(k,types[j]))
            elementUsed = getInput(teammates[i],0)

            if enemyWeak[enemyTargeted] == elementUsed:
                enemyHit[enemyTargeted] = True

                allHit = True #after a weakness is hit,
                    #exit if all enemies have been hit by a weakness
                for i in range(0,numE):
                    if numE[i] == False:
                        allHit = False

if __name__ == '__main__':
    game()
