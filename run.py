#game code is in the Persona 5 System file 
import timeit
start = timeit.default_timer() #starts timer

from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E) 
class Oppenents(E):
      def __init__(self,weakness, resistance):
        self.weakness = weakness
        self.resistance = resistance
      def __repr__(self)->str:
        return f"Oppenent({self.weakness}, {self.resistance})"
#new opponents
OppenentWeakness= {
      "Physical" :[],
      "Bullet":[],
      "Fire" :[],
      "Ice":[],
      "Electric":[],
      "Wind" :[],
      "Nuclear":[],
      "Blessed":[],
      "Curse":[],
      "Psychokinesis":[]
}
for weakness in OppenentWeakness: 
      for i in range(9):
            OppenentWeakness[weakness].append(Oppenents(weakness,i))
            
OppenentResistance= {
      "Physical" :[],
      "Bullet":[],
      "Fire" :[],
      "Ice":[],
      "Electric":[],
      "Wind" :[],
      "Nuclear":[],
      "Blessed":[],
      "Curse":[],
      "Psychokinesis":[]
}
for resistance in OppenentWeakness: 
      for i in range(9):
            OppenentResistance[resistance].append(Oppenents(resistance,i))            
    
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
@constraint.at_least_one(E)
@proposition(E)
class FancyPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

# Call your variables whatever you want
x = BasicPropositions("x")
y = BasicPropositions("y")   
o = BasicPropositions("o")

P = BasicPropositions("Physical")
B = BasicPropositions("Bullet")
F = BasicPropositions("Fire")
I = BasicPropositions("Ice")
E = BasicPropositions("Electric")
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

def example_theroy():
    
    #implication, if an opponent is weak to one type it is not weak to the others 
    #E.add_constraint(x[damageType]>>~x[otherDamagetypes])
    E.add_constraint(x["Physical"]>>~x["Bullet"] &~x["Fire"] &~x["Ice"]  &~x["Electric"]  &~x["Wind"]  &~x["Nuclear"]  &~x["Bless"] &~x["Curse"] &~x["Psychokinesis"])
    E.add_constraint(x["Bullet"]>>~x["Physical"] &~x["Fire"] &~x["Ice"]  &~x["Electric"]  &~x["Wind"]  &~x["Nuclear"]  &~x["Bless"] &~x["Curse"] &~x["Psychokinesis"])
    E.add_constraint(x["Fire"]>>~x["Physical"] &~x["Bullet"] &~x["Ice"]  &~x["Electric"]  &~x["Wind"]  &~x["Nuclear"]  &~x["Bless"] &~x["Curse"] &~x["Psychokinesis"])
    E.add_constraint(x["Ice"]>>~x["Physical"] &~x["Bullet"] &~x["Fire"]  &~x["Electric"]  &~x["Wind"]  &~x["Nuclear"]  &~x["Bless"] &~x["Curse"] &~x["Psychokinesis"])
    E.add_constraint(x["Electric"]>>~x["Physical"] &~x["Bullet"] &~x["Fire"]  &~x["Ice"]  &~x["Wind"]  &~x["Nuclear"]  &~x["Bless"] &~x["Curse"] &~x["Psychokinesis"])
    E.add_constraint(x["Wind"]>>~x["Physical"] &~x["Bullet"] &~x["Fire"]  &~x["Ice"]  &~x["Electric"]  &~x["Nuclear"]  &~x["Bless"] &~x["Curse"] &~x["Psychokinesis"])
    E.add_constraint(x["Nuclear"]>>~x["Physical"] &~x["Bullet"] &~x["Fire"]  &~x["Ice"]  &~x["Electric"]  &~x["Wind"]  &~x["Bless"] &~x["Curse"] &~x["Psychokinesis"])
    E.add_constraint(x["Bless"]>>~x["Physical"] &~x["Bullet"] &~x["Fire"]  &~x["Ice"]  &~x["Electric"]  &~x["Wind"]  &~x["Nuclear"] &~x["Curse"] &~x["Psychokinesis"])
    E.add_constraint(x["Curse"]>>~x["Physical"] &~x["Bullet"] &~x["Fire"]  &~x["Ice"]  &~x["Electric"]  &~x["Wind"]  &~x["Nuclear"] &~x["Bless"] &~x["Psychokinesis"])
    E.add_constraint(x["Psychokinesis"]>>~x["Physical"] &~x["Bullet"] &~x["Fire"]  &~x["Ice"]  &~x["Electric"]  &~x["Wind"]  &~x["Nuclear"] &~x["Bless"] &~x["Curse"])
    

    #or, an opponent must have one weakness 
    E.add_constraint(x["Physical"] | x["Bullet"] | x["Fire"] | x["Ice"] | x["Electric"] | x["Wind"] | x["Nuclear"] | x["Bless"] | x["Curse"] | x["Psychokinesis"])
    
    #implication an imponent can only have one resistance 
    #E.add_constraint(y[]>>~y[])
    E.add_constraint(y["Physical"]>>~y["Bullet"] &~y["Fire"] &~y["Ice"]  &~y["Electric"]  &~y["Wind"]  &~y["Nuclear"]  &~y["Bless"] &~y["Curse"] &~y["Psychokinesis"])
    E.add_constraint(y["Bullet"]>>~y["Physical"] &~y["Fire"] &~y["Ice"]  &~y["Electric"]  &~y["Wind"]  &~y["Nuclear"]  &~y["Bless"] &~y["Curse"] &~y["Psychokinesis"])
    E.add_constraint(y["Fire"]>>~y["Physical"] &~y["Bullet"] &~y["Ice"]  &~y["Electric"]  &~y["Wind"]  &~y["Nuclear"]  &~y["Bless"] &~y["Curse"] &~y["Psychokinesis"])
    E.add_constraint(y["Ice"]>>~y["Physical"] &~y["Bullet"] &~y["Fire"]  &~y["Electric"]  &~y["Wind"]  &~y["Nuclear"]  &~y["Bless"] &~y["Curse"] &~y["Psychokinesis"])
    E.add_constraint(y["Electric"]>>~y["Physical"] &~y["Bullet"] &~y["Fire"]  &~y["Ice"]  &~y["Wind"]  &~y["Nuclear"]  &~y["Bless"] &~y["Curse"] &~y["Psychokinesis"])
    E.add_constraint(y["Wind"]>>~y["Physical"] &~y["Bullet"] &~y["Fire"]  &~y["Ice"]  &~y["Electric"]  &~y["Nuclear"]  &~y["Bless"] &~y["Curse"] &~y["Psychokinesis"])
    E.add_constraint(y["Nuclear"]>>~y["Physical"] &~y["Bullet"] &~y["Fire"]  &~y["Ice"]  &~y["Electric"]  &~y["Wind"]  &~y["Bless"] &~y["Curse"] &~y["Psychokinesis"])
    E.add_constraint(y["Bless"]>>~y["Physical"] &~y["Bullet"] &~y["Fire"]  &~y["Ice"]  &~y["Electric"]  &~y["Wind"]  &~y["Nuclear"] &~y["Curse"] &~y["Psychokinesis"])
    E.add_constraint(y["Curse"]>>~y["Physical"] &~y["Bullet"] &~y["Fire"]  &~y["Ice"]  &~y["Electric"]  &~y["Wind"]  &~y["Nuclear"] &~y["Bless"] &~y["Psychokinesis"])
    E.add_constraint(y["Psychokinesis"]>>~y["Physical"] &~y["Bullet"] &~y["Fire"]  &~y["Ice"]  &~y["Electric"]  &~y["Wind"]  &~y["Nuclear"] &~y["Bless"] &~y["Curse"])

    #implication, or, an imponent cannot be weak to an element and be resistance
    E.add_constraint(~(x["Physical"] | y["Physical"])
    E.add_constraint(~(x["Bullet"] | y["Bullet"])
    E.add_constraint(~(x["Fire"] | y["Fire"])
    E.add_constraint(~(x["Ice"] | y["Ice"])
    E.add_constraint(~(x["Electric"] | y["Electric"])
    E.add_constraint(~(x["Wind"] | y["Wind"])
    E.add_constraint(~(x["Nuclear"] | y["Nuclear"])
    E.add_constraint(~(x["Bless"] | y["Bless"])
    E.add_constraint(~(x["Curse"] | y["Curse"])
    E.add_constraint(~(x["Psychokinesis"] | y["Psychokinesis"])
                     

    return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()

#stops timer and prints length of time program took to run
stop = timeit.default_timer()
print("Time: ", stop - start)