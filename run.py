
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BasicPropositions:

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
a = BasicPropositions("a")
b = BasicPropositions("b")   
c = BasicPropositions("c")
d = BasicPropositions("d")
e = BasicPropositions("e")
# At least one of these will be true
x = FancyPropositions("x")
y = FancyPropositions("y")
z = FancyPropositions("z")


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
