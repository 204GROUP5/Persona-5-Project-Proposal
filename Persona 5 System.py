import random

def getInputReal(elements): #elements is an array of valid inputs
    gotInput = False
    value = -1
    while not gotInput: #repeats until given valid input
        value = int(input(""))
        if value in elements:
            gotInput = True #exits if given valid input
        else: #else tells the user that they made a mistake
            print("Dumbass stupid idiot")

    return value


def getInputFake(elements):
    return 0 #doesn't work yet

def getInput(elements,inputType):
    if inputType: #depending on elementType, uses human or computer inputs
        return getInputFake(elements)
    return getInputReal(elements)

def game():
    types = ["Physical", "Bullet", "Fire", "Ice", "Electric", "Wind", "Nuclear", "Blessed", "Curse", "Psychokinesis"]
    #just a list of the types in order
    
    numE = random.randint(1,5) #picks a random number of enemies
    enemyArray = []
    enemyWeak = []
    enemyHit = []
    
    for i in range(numE): #for each enemy
        enemyArray.append(i) #puts their number into an array
        enemyWeak.append(random.randint(1,10)) #randomly gives them a weakness
        enemyHit.append(False) #adds that they haven't been hit

    #teammate values
    teammates = [[],[],[],[]] #2d array of teammates + their available elements
    ceiling = 7
    
    for i in range(len(teammates)-1): #determines first 3 party members types
        teammates[i].append(0) #physical and gun
        teammates[i].append(1)
        
        newElement = (random.randint(0,ceiling) + 2)
        for j in range(i): #get a random element not already taken by another teammate
            if newElement == teammates[j][2]:
                newElement += 1
        
        teammates[i].append(newElement)
        ceiling -= 1

    for j in range(10): #give fourth teammate all elemental types
        teammates[3].append(j)

    roundCount = 1
    allHit = False

    while not allHit: #goes until all enemies have been hit with their weakness
        print("Round {}".format(roundCount))

        for i in range(len(teammates)): #on each teammate's turn
            for j in range(numE): #print available enemies
                print("{}) Enemy {}".format(j,j+1))
            enemyTargeted = getInput(enemyArray,0) #gets the one chosen
            
            for k in range(len(teammates[i])): #print available elements
                print("{}) {}".format(teammates[i][k],types[teammates[i][k]]))
            elementUsed = getInput(teammates[i],0) #gets the one chosen

            print("Targeted Enemy {} with {}".format(enemyTargeted+1,types[elementUsed]))
            #tell player which enemy they targeted with which element

            if enemyWeak[enemyTargeted] == elementUsed:
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
                #tells the player if they did not hit an enemy with their weakness

        roundCount += 1

if __name__ == '__main__':
    #runs the main code if you are running this directly
    game()
