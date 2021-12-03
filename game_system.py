from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

def getInput(num, elements1,elements2):
    i = num % len(elements1)
    j = (num//(len(elements1))) % len(elements2)
        
    return (elements1[i], elements2[j])

#def getInput(elements1,elements2, weak, E):
#    indexes = (0,0)
#    tempE = E
#    tempSolutions = -1
#    numSolutions = -1
#    for i in elements1:
#        for j in elements2:
#            tempE = E
#            tempE.add_constraint(weak[i][j])
#            tempE = tempE.compile()
#            tempSolutions = count_solutions(tempE)
#            if tempSolutions >= numSolutions:
#                numSolutions = tempSolutions
#                indexes = (i,j)
#    return indexes

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

            (enemyTargeted, elementUsed) = getInput(roundCount-1, enemyId,teammates[i]) #gets the one chosen

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
                        
                if allHit == True:
                    break

            else:
                print("It had little effect.")
                #tells the player if they did not hit an enemy with their resistance or weakness
                #E.add_constraint(~weaknesses[enemyTargeted][elementUsed])
                #E.add_constraint(~resistances[enemyTargeted][elementUsed])

        roundCount += 1

    return E
