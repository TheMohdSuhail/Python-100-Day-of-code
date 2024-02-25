'''
Multiple Inheritance in Python

Multiple inheritance is a powerful feature in object-oriented programming that allows a
class to inherit attributes and methods from multiple parent classes. This can be useful
in situations where a class needs to inherit functionality from multiple sources.

Syntax

In Python, multiple inheritance is implemented by specifying multiple parent classes in the
class definition, separated by commas.

class ChildClass(ParentClass1, ParentClass2, ParentClass3):
    # Class body


it's important to note that, in case of multiple inheritance, Python follows a method
resolution order(MRO) to resovle coflicts between methods or attributes for different parent
classes. The MRO determines the order in which parent classes are searched from attributes
and methods.


'''

# Example :
'''
class Animal1:
    def __init__(self, name1, species1):

        self.name1 = name1
        self.species1 = species1


    def make_sound1(self):
        print("Sound made by the animal")

class Mammal1:

    def __init__(self, name1, fur_color1):

        self.name1 = name1
        self.fur_color1 = fur_sound1


class Dog1(Animal1 , Mammal1):

    def __init__(self, name1, breed, for_color1):

        Animal1.__init__(self, name1, species="Dog1")

        Mammal1.__init__(self, name1, fur_color1)
        self.breed1 = breed1


    def make_sound1(self):
        print("Bark!")


d = Dog1()'''


class Employee:

    def __init__(self,name):
        self.name = name

    def show (self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):

        self.dance = dance


    def show (self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):

    def __init__(self, dance, name):

        self.dance = dance
        self.name = name



o = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())












































        
