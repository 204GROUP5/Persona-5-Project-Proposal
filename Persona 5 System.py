from bauhaus import Encoding, proposition, constraint

def getInputReal(elements1,elements2): #elements is an array of valid inputs
    gotInput = False
    value1 = -1
    while not gotInput: #repeats until given valid input
        value1 = int(input(""))
        if value1 in elements1:
            gotInput = True #exits if given valid input
        else: #else tells the user that they made a mistake
            print("Dumbass stupid idiot")

    gotInput = False
    value2 = -1
    while not gotInput:
        value2 = int(input(""))
        if value2 in elements2:
            gotInput = True
        else:
            print("Whoohps")

    return value1,value2


def getInputFake(elements1,elements2):
    return 0 #doesn't work yet

def getInput(elements1,elements2,inputType):
    if inputType: #depending on elementType, uses human or computer inputs
        return getInputFake(elements1,elements2)
    return getInputReal(elements1,elements2)

def game(E, state):
    types = ["Physical", "Bullet", "Fire", "Ice", "Electric", "Wind", "Nuclear", "Blessed", "Curse", "Psychokinesis"]
    #just a list of the types in order

    teammates = state[1]

    enemies = state[0]
    numE = len(enemies)

    enemyArray = []
    enemyWeak = []
    enemyRes = []
    enemyHit = []
    for i in range(numE):
        enemyArray.append(i)
        enemyWeak.append(enemies[i][0])
        enemyRes.append(enemies[i][1])
        enemyHit.append(False)

    roundCount = 1
    allHit = False

    while not allHit: #goes until all enemies have been hit with their weakness
        print("Round {}".format(roundCount))

        for i in range(len(teammates)): #on each teammate's turn
            for j in range(numE): #print available enemies
                print("{}) Enemy {}".format(j,j+1))
            
            print(" ")
            
            for k in range(len(teammates[i])): #print available elements
                print("{}) {}".format(teammates[i][k],types[teammates[i][k]]))

            (enemyTargeted, elementUsed) = getInput(enemyArray,teammates[i],0) #gets the one chosen

            print("Targeted Enemy {} with {}".format(enemyTargeted+1,types[elementUsed]))
            #tell player which enemy they targeted with which element

            if enemyRes[enemyTargeted] == elementUsed:
                print("The enemy resisted that attack.")
                #tells the player if they hit an enemy with their resistance
                
            elif enemyWeak[enemyTargeted] == elementUsed:
                enemyHit[enemyTargeted] = True
                print("That was the enemy's weakness!")
                #tells the player if they hit an enemy with their weakness

                allHit = True #after a weakness is hit,
                    #exit if all enemies have been hit by a weakness
                for i in range(0,numE):
                    if enemyHit[i] == False:
                        allHit = False

            else:
                print("It had little effect.")
                #tells the player if they did not hit an enemy with their resistance or weakness

        roundCount += 1

if __name__ == '__main__':
    #runs the main code if you are running this directly
    game("",[1])
