# inheritanc provides you "is a" relation

class Animal:
    pass
# dog is a animal
class Dog(Animal):
    pass
# tiger is a animal
class Tiger(Animal):
    pass



class Furniture:
    pass

# chair is a furniture
class Chair(Furniture):
    pass
# chair is a table
class Table(Furniture):
    pass
# chair is a bed
class Bed(Furniture):
    pass

