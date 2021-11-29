from bauhaus import Encoding, proposition, constraint

#def getInputReal(elements1,elements2): #elements is an array of valid inputs
#    gotInput = False
#    value1 = -1
#    while not gotInput: #repeats until given valid input
#        value1 = int(input(""))
#        if value1 in elements1:
#            gotInput = True #exits if given valid input
#        else: #else tells the user that they made a mistake
#            print("Dumbass stupid idiot")
#
#    gotInput = False
#    value2 = -1
#    while not gotInput:
#        value2 = int(input(""))
#        if value2 in elements2:
#            gotInput = True
#        else:
#            print("Whoohps")
#
#    return value1,value2
# from a version of the code where we tested it with user input
# just to see that the underlying code didn't have any errors


def getInputFake(elements1,elements2, weak, E):
    indexes = (0,0)
    tempE = E
    tempSolutions = -1
    numSolutions = -1
    for i in range(elements1):
        for j in range(elements2):
            tempE = E
            tempE.add_constraint(weak[i][j])
            tempSolutions = count_solutions(tempE)
            if tempSolutions >= numSolutions:
                numSolutions = tempSolutions
                indexes = (i,j)
    return indexes

def getInput(elements1,elements2,inputType, weak, E):
    #if inputType: #depending on elementType, uses human or computer inputs
    #now only uses computer input since it's the only one that could be reached anyways
    return getInputFake(elements1,elements2, weak, E)
    #return getInputReal(elements1,elements2)

def game(E, teammates, enemies, weaknesses, resistances):
    types = ["Physical", "Bullet", "Fire", "Ice", "Electric", "Wind", "Nuclear", "Blessed", "Curse", "Psychokinesis"]
    #just a list of the types in order

    numE = len(enemies)
    enemyHit = []
    enemyId = []
    for i in range(numE):
        enemyHit.append([False])
        enemyId.append(i)

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

            (enemyTargeted, elementUsed) = getInput(enemyId,teammates[i],weaknesses,E) #gets the one chosen

            print("Targeted Enemy {} with {}".format(enemyTargeted+1,types[elementUsed]))
            #tell player which enemy they targeted with which element

            if enemies[enemyTargeted].res == elementUsed:
                print("The enemy resisted that attack.")
                #tells the player if they hit an enemy with their resistance
                E.add_constraint(resistances[enemyTargeted][elementUsed])
                #updates the constraints
                
            elif enemies[enemyTargeted].weak == elementUsed:
                enemyHit[enemyTargeted] = True
                print("That was the enemy's weakness!")
                #tells the player if they hit an enemy with their weakness
                E.add_constraint(weaknesses[enemyTargeted][elementUsed])
                #updates the constraints

                allHit = True #after a weakness is hit,
                    #exit if all enemies have been hit by a weakness
                for i in range(0,numE):
                    if enemyHit[i] == False:
                        allHit = False

            else:
                print("It had little effect.")
                #tells the player if they did not hit an enemy with their resistance or weakness
                E.add_constraint(~weaknesses[enemyTargeted][elementUsed])
                E.add_constraint(~resistances[enemyTargeted][elementUsed])

        roundCount += 1

        return E

if __name__ == '__main__':
    #runs the main code if you are running this directly
    game()
