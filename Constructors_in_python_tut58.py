'''
Constructors in Python :-

A constructor is a special method in a class used to create and initialize an object of a
class. There are different types of constructores. Constructor is invoked(lagu or call karta
hai) automatically when an object of a class in created.

A constructor is a unique function that gets called automatically when an object is created
of a class. The main purpose of a constructor is to initaialize or assign values to the data
members of that class. It cannot return any value other than None.

'''
#Syntax of Pythn Constructor

'''
def __init__(self):
    initializations
_________________________________


init is one of the reserved functions in Python. In Object Oriented Programming, it is known
as constructor.

Types of Constructors in Python :

1. Parameterized Constructor
2. Default Constructor

Parameterized Constructor in Python

When the constructor accepts arguments along with self, it is known as parameterized
constructor.

These arguments can be used inside the class to assign the values to the data mumbers.

'''

# Example:

class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

ref1 = Details("Crab", "Crustanceasn")
print(ref1.animal, "belongs to the ", ref1.group, "group.")

'''
Default Constructor in Python

When the constructor doesn't accept any arguments from the object and has only one argument,
self, in the constructor, it is known as Default constructor.

'''

print("\n Example of Default Constructor \n")

#Example:

class details:
    def __init__(self):
        print("animal Crab belongs to Crustaceans group")
ref2 = details()













































        
