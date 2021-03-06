import random
import game_system #game code is in this file
import timeit
start = timeit.default_timer() #starts timer

from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()

#set up opponent weaknesses and resistances
weak_to_res = [1, 6, 5, 2, 3, 4, 9, 8, 7, 0] #all different power types

@proposition(E)
class Weakness:
    def __init__(self, opponent, element):
        self.opp = opponent
        self.elem = element
        
    def __repr__(self):
        return 'Weakness(' + str(self.opp) + ',' + str(self.elem) + ')'

    
@proposition(E)
class Resistance:
    def __init__(self, opponent, element):
        self.opp = opponent
        self.elem = element
        
    def __repr__(self):
        return 'Resistance(' + str(self.opp) + ',' + str(self.elem) + ')'

    
class Opponent:
    def __init__(self, weakness):
        self.weak = weakness
        self.res = weak_to_res[weakness]

opponents_arr = []
all_weak = []
all_res = []
num_opponents= (random.randint(1,5))
for opp in range(num_opponents):
    weaknesses = []
    resistances = []
    for elem in range(10):
        weaknesses.append(Weakness(opp, elem))
        resistances.append(Resistance(opp, elem))

    all_weak.append(weaknesses)
    all_res.append(resistances)
    
    opponents_arr.append(Opponent(random.randint(0,9))) #append weakness


#set up teammate power types
teammates = [[], [], [], []]
ceiling = 7
for i in range(len(teammates)-1):
    teammates[i].append(0)   #physical and gun
    teammates[i].append(1)

    new_elem = (random.randint(0, ceiling) + 2)
    for j in range(i):   #get random elem not already taken by another teammate
        if new_elem == teammates[j][2]:
            new_elem += 1
    teammates[i].append(new_elem)
    ceiling -= 1
for j in range(10):    #give fourth teammate all types
    teammates[3].append(j)

# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.

def example_theory():

    for i in range(len(opponents_arr)):
        #implication, if an opponent is weak to one type it is not weak to the others 
        #E.add_constraint(x[damageType]>>~x[otherDamagetypes])
        E.add_constraint(all_weak[i][0]>>((~all_weak[i][1]) &(~all_weak[i][2]) &(~all_weak[i][3]) &(~all_weak[i][4]) &(~all_weak[i][5]) &(~all_weak[i][6]) &(~all_weak[i][7]) &(~all_weak[i][8]) &(~all_weak[i][9])))
        E.add_constraint(all_weak[i][1]>>((~all_weak[i][0]) &(~all_weak[i][2]) &(~all_weak[i][3]) &(~all_weak[i][4]) &(~all_weak[i][5]) &(~all_weak[i][6]) &(~all_weak[i][7]) &(~all_weak[i][8]) &(~all_weak[i][9])))
        E.add_constraint(all_weak[i][2]>>((~all_weak[i][0]) &(~all_weak[i][1]) &(~all_weak[i][3]) &(~all_weak[i][4]) &(~all_weak[i][5]) &(~all_weak[i][6]) &(~all_weak[i][7]) &(~all_weak[i][8]) &(~all_weak[i][9])))
        E.add_constraint(all_weak[i][3]>>((~all_weak[i][0]) &(~all_weak[i][1]) &(~all_weak[i][2]) &(~all_weak[i][4]) &(~all_weak[i][5]) &(~all_weak[i][6]) &(~all_weak[i][7]) &(~all_weak[i][8]) &(~all_weak[i][9])))
        E.add_constraint(all_weak[i][4]>>((~all_weak[i][0]) &(~all_weak[i][1]) &(~all_weak[i][2]) &(~all_weak[i][3]) &(~all_weak[i][5]) &(~all_weak[i][6]) &(~all_weak[i][7]) &(~all_weak[i][8]) &(~all_weak[i][9])))
        E.add_constraint(all_weak[i][5]>>((~all_weak[i][0]) &(~all_weak[i][1]) &(~all_weak[i][2]) &(~all_weak[i][3]) &(~all_weak[i][4]) &(~all_weak[i][6]) &(~all_weak[i][7]) &(~all_weak[i][8]) &(~all_weak[i][9])))
        E.add_constraint(all_weak[i][6]>>((~all_weak[i][0]) &(~all_weak[i][1]) &(~all_weak[i][2]) &(~all_weak[i][3]) &(~all_weak[i][4]) &(~all_weak[i][5]) &(~all_weak[i][7]) &(~all_weak[i][8]) &(~all_weak[i][9])))
        E.add_constraint(all_weak[i][7]>>((~all_weak[i][0]) &(~all_weak[i][1]) &(~all_weak[i][2]) &(~all_weak[i][3]) &(~all_weak[i][4]) &(~all_weak[i][5]) &(~all_weak[i][6]) &(~all_weak[i][8]) &(~all_weak[i][9])))
        E.add_constraint(all_weak[i][8]>>((~all_weak[i][0]) &(~all_weak[i][1]) &(~all_weak[i][2]) &(~all_weak[i][3]) &(~all_weak[i][4]) &(~all_weak[i][5]) &(~all_weak[i][6]) &(~all_weak[i][7]) &(~all_weak[i][9])))
        E.add_constraint(all_weak[i][9]>>((~all_weak[i][0]) &(~all_weak[i][1]) &(~all_weak[i][2]) &(~all_weak[i][3]) &(~all_weak[i][4]) &(~all_weak[i][5]) &(~all_weak[i][6]) &(~all_weak[i][7]) &(~all_weak[i][8])))
        
    

        #or, an opponent must have one weakness 
        E.add_constraint(all_weak[i][0] | all_weak[i][1] | all_weak[i][2] | all_weak[i][3] | all_weak[i][4] | all_weak[i][5] | all_weak[i][6] | all_weak[i][7] | all_weak[i][8] | all_weak[i][9])
    
        #implication an opponent can only have one resistance 
        #E.add_constraint(y[damageType]>>~y[otherDamagetypes])
        E.add_constraint(all_res[i][0]>>((~all_res[i][1]) &(~all_res[i][2]) &(~all_res[i][3]) &(~all_res[i][4]) &(~all_res[i][5]) &(~all_res[i][6]) &(~all_res[i][7]) &(~all_res[i][8]) &(~all_res[i][9])))
        E.add_constraint(all_res[i][1]>>((~all_res[i][0]) &(~all_res[i][2]) &(~all_res[i][3]) &(~all_res[i][4]) &(~all_res[i][5]) &(~all_res[i][6]) &(~all_res[i][7]) &(~all_res[i][8]) &(~all_res[i][9])))
        E.add_constraint(all_res[i][2]>>((~all_res[i][0]) &(~all_res[i][1]) &(~all_res[i][3]) &(~all_res[i][4]) &(~all_res[i][5]) &(~all_res[i][6]) &(~all_res[i][7]) &(~all_res[i][8]) &(~all_res[i][9])))
        E.add_constraint(all_res[i][3]>>((~all_res[i][0]) &(~all_res[i][1]) &(~all_res[i][2]) &(~all_res[i][4]) &(~all_res[i][5]) &(~all_res[i][6]) &(~all_res[i][7]) &(~all_res[i][8]) &(~all_res[i][9])))
        E.add_constraint(all_res[i][4]>>((~all_res[i][0]) &(~all_res[i][1]) &(~all_res[i][2]) &(~all_res[i][3]) &(~all_res[i][5]) &(~all_res[i][6]) &(~all_res[i][7]) &(~all_res[i][8]) &(~all_res[i][9])))
        E.add_constraint(all_res[i][5]>>((~all_res[i][0]) &(~all_res[i][1]) &(~all_res[i][2]) &(~all_res[i][3]) &(~all_res[i][4]) &(~all_res[i][6]) &(~all_res[i][7]) &(~all_res[i][8]) &(~all_res[i][9])))
        E.add_constraint(all_res[i][6]>>((~all_res[i][0]) &(~all_res[i][1]) &(~all_res[i][2]) &(~all_res[i][3]) &(~all_res[i][4]) &(~all_res[i][5]) &(~all_res[i][7]) &(~all_res[i][8]) &(~all_res[i][9])))
        E.add_constraint(all_res[i][7]>>((~all_res[i][0]) &(~all_res[i][1]) &(~all_res[i][2]) &(~all_res[i][3]) &(~all_res[i][4]) &(~all_res[i][5]) &(~all_res[i][6]) &(~all_res[i][8]) &(~all_res[i][9])))
        E.add_constraint(all_res[i][8]>>((~all_res[i][0]) &(~all_res[i][1]) &(~all_res[i][2]) &(~all_res[i][3]) &(~all_res[i][4]) &(~all_res[i][5]) &(~all_res[i][6]) &(~all_res[i][7]) &(~all_res[i][9])))
        E.add_constraint(all_res[i][9]>>((~all_res[i][0]) &(~all_res[i][1]) &(~all_res[i][2]) &(~all_res[i][3]) &(~all_res[i][4]) &(~all_res[i][5]) &(~all_res[i][6]) &(~all_res[i][7]) &(~all_res[i][8])))

        #implication, or, an opponent cannot be weak to an element and be resistance
        E.add_constraint(~(all_weak[i][0] & all_res[i][0]))
        E.add_constraint(~(all_weak[i][1] & all_res[i][1]))
        E.add_constraint(~(all_weak[i][2] & all_res[i][2]))
        E.add_constraint(~(all_weak[i][3] & all_res[i][3]))
        E.add_constraint(~(all_weak[i][4] & all_res[i][4]))
        E.add_constraint(~(all_weak[i][5] & all_res[i][5]))
        E.add_constraint(~(all_weak[i][6] & all_res[i][6]))
        E.add_constraint(~(all_weak[i][7] & all_res[i][7]))
        E.add_constraint(~(all_weak[i][8] & all_res[i][8]))
        E.add_constraint(~(all_weak[i][9] & all_res[i][9]))

    
        #if an opponent is weak to an element is resists another corresponding element 
        E.add_constraint(all_weak[i][0]>>all_res[i][2])
        E.add_constraint(all_weak[i][1]>>all_res[i][6])
        E.add_constraint(all_weak[i][2]>>all_res[i][5])
        E.add_constraint(all_weak[i][3]>>all_res[i][2])
        E.add_constraint(all_weak[i][4]>>all_res[i][3])
        E.add_constraint(all_weak[i][5]>>all_res[i][4])
        E.add_constraint(all_weak[i][6]>>all_res[i][9])
        E.add_constraint(all_weak[i][7]>>all_res[i][8])
        E.add_constraint(all_weak[i][8]>>all_res[i][7])
        E.add_constraint(all_weak[i][9]>>all_res[i][0])

                     

    return E


if __name__ == "__main__":

    T = example_theory()
    game_system.game(T, teammates, opponents_arr, all_weak, all_res)
    T = T.compile()

    print("\nSatisfiable: %s" % T.satisfiable())
    #print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    types_list = ["Physical",
                  "Bullet",
                  "Fire",
                  "Ice",
                  "Electric",
                  "Wind",
                  "Nuclear",
                  "Bless",
                  "Curse",
                  "Psychokinesis"]

    for i in range(num_opponents):
        print("Enemy {} was resistant to {} and weak to {}".format(i+1, types_list[opponents_arr[i].res], types_list[opponents_arr[i].weak]))
    
#stops timer and prints length of time program took to run
stop = timeit.default_timer()
print("Time: ", stop - start)
