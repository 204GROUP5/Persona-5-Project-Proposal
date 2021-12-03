import random
import game_system #game code is in this file
import timeit
start = timeit.default_timer() #starts timer

from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
#@proposition(E) 
#class Oppenents(E):
#      def __init__(self,weakness, resistance):
#        self.weakness = weakness
#        self.resistance = resistance
#      def __repr__(self)->str:
#        return f"Oppenent({self.weakness}, {self.resistance})"

#set up opponent weaknesses and resistances
weak_to_res = [1, 6, 5, 2, 3, 4, 9, 8, 7, 0] #all different power types

@proposition(E)
class Weakness:
    def __init__(self, opponent, element):
        self.opp = opponent
        self.elem = element
        
    def __repr__(self):
        return 'Weakness(' + self.opp + ',' + self.elem + ')'

    
@proposition(E)
class Resistance:
    def __init__(self, opponent, element):
        self.opp = opponent
        self.elem = element
        
    def __repr__(self):
        return 'Resistance(' + self.opp + ',' + self.elem + ')'

    
class Opponent:
    def __init__(self, opponent, weakness):
        self.weak = weakness
        self.res = weak_to_res[weakness]

opponents_arr = []
all_weak = []
all_res = []
num_opponents= (random.randint(1,6))
for opp in range(num_opponents):
    weaknesses = []
    resistances = []
    for elem in range(10):
        weaknesses.append(Weakness(opp, elem))
        resistances.append(Resistance(opp, elem))

    all_weak.append(weaknesses)
    all_res.append(resistances)
    
    opponents_arr.append([])
    opponents_arr[opp].append(Opponent(opp, random.randint(0,9))) #append weakness


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


@proposition(E)
class BasicPropositions:
     def build2DArray(num_rows, num_cols, format_string='({i},{j})'):
        """A helper function to build a 2D array of variables
        Inputs:
        num_rows: the number of rows in this array
        num_cols: the number of columns in this array
        format_string: a string defining the name of each variable, where
        {i} and {j} will be replaced with the row and column number respectively
        Outputs:
        array: an array with the specified number of rows and columns"""

        array = []
        for i in range(num_rows):
            row = []
            for j in range(num_cols):
                row.append(Var(format_string.format(i=i,j=j)))
            array.append(row)
        return array

     def __init__(self, data):
        self.data = data

     def __repr__(self):
        return f"A.{self.data}"


# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
#@constraint.at_least_one(E)
#@proposition(E)
#class FancyPropositions:
#
#    def __init__(self, data):
#        self.data = data
#
#    def __repr__(self):
#        return f"A.{self.data}"

# Call your variables whatever you want
x = BasicPropositions("x") #weakness
y = BasicPropositions("y") # resistances 
o = BasicPropositions("o") #oppenents 

P = BasicPropositions("Physical")
B = BasicPropositions("Bullet")
F = BasicPropositions("Fire")
I = BasicPropositions("Ice")
EL = BasicPropositions("Electric")
W = BasicPropositions("Wind")
N = BasicPropositions("Nuclear")
BB = BasicPropositions("Bless")
C = BasicPropositions("Curse")
PP = BasicPropositions("Psychokinesis")


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.

def example_theory():

    for i in range(len(opponents_arr)):
        #implication, if an opponent is weak to one type it is not weak to the others 
        #E.add_constraint(x[damageType]>>~x[otherDamagetypes])
        E.add_constraint(all_weak[i][0]>>(~all_weak[i][1] &~all_weak[i][2] &~all_weak[i][3] &~all_weak[i][4] &~all_weak[i][5] &~all_weak[i][6] &~all_weak[i][7] &~all_weak[i][8] &~all_weak[i][9]))
        E.add_constraint(all_weak[i][1]>>(~all_weak[i][0] &~all_weak[i][2] &~all_weak[i][3] &~all_weak[i][4] &~all_weak[i][5] &~all_weak[i][6] &~all_weak[i][7] &~all_weak[i][8] &~all_weak[i][9]))
        E.add_constraint(all_weak[i][2]>>(~all_weak[i][0] &~all_weak[i][1] &~all_weak[i][3] &~all_weak[i][4] &~all_weak[i][5] &~all_weak[i][6] &~all_weak[i][7] &~all_weak[i][8] &~all_weak[i][9]))
        E.add_constraint(all_weak[i][3]>>(~all_weak[i][0] &~all_weak[i][1] &~all_weak[i][2] &~all_weak[i][4] &~all_weak[i][5] &~all_weak[i][6] &~all_weak[i][7] &~all_weak[i][8] &~all_weak[i][9]))
        E.add_constraint(all_weak[i][4]>>(~all_weak[i][0] &~all_weak[i][1] &~all_weak[i][2] &~all_weak[i][3] &~all_weak[i][5] &~all_weak[i][6] &~all_weak[i][7] &~all_weak[i][8] &~all_weak[i][9]))
        E.add_constraint(all_weak[i][5]>>(~all_weak[i][0] &~all_weak[i][1] &~all_weak[i][2] &~all_weak[i][3] &~all_weak[i][4] &~all_weak[i][6] &~all_weak[i][7] &~all_weak[i][8] &~all_weak[i][9]))
        E.add_constraint(all_weak[i][6]>>(~all_weak[i][0] &~all_weak[i][1] &~all_weak[i][2] &~all_weak[i][3] &~all_weak[i][4] &~all_weak[i][5] &~all_weak[i][7] &~all_weak[i][8] &~all_weak[i][9]))
        E.add_constraint(all_weak[i][7]>>(~all_weak[i][0] &~all_weak[i][1] &~all_weak[i][2] &~all_weak[i][3] &~all_weak[i][4] &~all_weak[i][5] &~all_weak[i][6] &~all_weak[i][8] &~all_weak[i][9]))
        E.add_constraint(all_weak[i][8]>>(~all_weak[i][0] &~all_weak[i][1] &~all_weak[i][2] &~all_weak[i][3] &~all_weak[i][4] &~all_weak[i][5] &~all_weak[i][6] &~all_weak[i][7] &~all_weak[i][9]))
        E.add_constraint(all_weak[i][9]>>(~all_weak[i][0] &~all_weak[i][1] &~all_weak[i][2] &~all_weak[i][3] &~all_weak[i][4] &~all_weak[i][5] &~all_weak[i][6] &~all_weak[i][7] &~all_weak[i][8]))
        
    

        #or, an opponent must have one weakness 
        E.add_constraint(all_weak[i][0] | all_weak[i][1] |all_weak[i][2] | all_weak[i][3] | all_weak[i][4] | all_weak[i][5] | all_weak[i][6] | all_weak[i][7] | all_weak[i][8] | all_weak[i][9])
    
        #implication an imponent can only have one resistance 
        #E.add_constraint(y[damageType]>>~y[otherDamagetypes])
        E.add_constraint(all_res[i][0]>>~all_res[i][1] &~all_res[i][2] &~all_res[i][3] &~all_res[i][4] &~all_res[i][5] &~all_res[i][6] &~all_res[i][7] &~all_res[i][8] &~all_res[i][9])
        E.add_constraint(all_res[i][1]>>~all_res[i][0] &~all_res[i][2] &~all_res[i][3] &~all_res[i][4] &~all_res[i][5] &~all_res[i][6] &~all_res[i][7] &~all_res[i][8] &~all_res[i][9])
        E.add_constraint(all_res[i][2]>>~all_res[i][0] &~all_res[i][1] &~all_res[i][3] &~all_res[i][4] &~all_res[i][5] &~all_res[i][6] &~all_res[i][7] &~all_res[i][8] &~all_res[i][9])
        E.add_constraint(all_res[i][3]>>~all_res[i][0] &~all_res[i][1] &~all_res[i][2] &~all_res[i][4] &~all_res[i][5] &~all_res[i][6] &~all_res[i][7] &~all_res[i][8] &~all_res[i][9])
        E.add_constraint(all_res[i][4]>>~all_res[i][0] &~all_res[i][1] &~all_res[i][2] &~all_res[i][3] &~all_res[i][5] &~all_res[i][6] &~all_res[i][7] &~all_res[i][8] &~all_res[i][9])
        E.add_constraint(all_res[i][5]>>~all_res[i][0] &~all_res[i][1] &~all_res[i][2] &~all_res[i][3] &~all_res[i][4] &~all_res[i][6] &~all_res[i][7] &~all_res[i][8] &~all_res[i][9])
        E.add_constraint(all_res[i][6]>>~all_res[i][0] &~all_res[i][1] &~all_res[i][2] &~all_res[i][3] &~all_res[i][4] &~all_res[i][5] &~all_res[i][7] &~all_res[i][8] &~all_res[i][9])
        E.add_constraint(all_res[i][7]>>~all_res[i][0] &~all_res[i][1] &~all_res[i][2] &~all_res[i][3] &~all_res[i][4] &~all_res[i][5] &~all_res[i][6] &~all_res[i][8] &~all_res[i][9])
        E.add_constraint(all_res[i][8]>>~all_res[i][0] &~all_res[i][1] &~all_res[i][2] &~all_res[i][3] &~all_res[i][4] &~all_res[i][5] &~all_res[i][6] &~all_res[i][7] &~all_res[i][9])
        E.add_constraint(all_res[i][9]>>~all_res[i][0] &~all_res[i][1] &~all_res[i][2] &~all_res[i][3] &~all_res[i][4] &~all_res[i][5] &~all_res[i][6] &~all_res[i][7] &~all_res[i][8])

        #implication, or, an imponent cannot be weak to an element and be resistance
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

    
        #if an oppent is weak to an element is resists another corresponding element 
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
    # Don't compile until you're finished adding all your constraints!
    game_system.game(T, teammates, all_weak, all_res)
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    #print("\nVariable likelihoods:")
    #for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
    #    print(" %s: %.2f" % (vn, likelihood(T, v)))
    #print()

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
