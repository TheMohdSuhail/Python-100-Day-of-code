'''
Inheritance in Python

When a class drives from another class. The child class will inherit all teh public and
protected properies and methods from the parent class. In addition, it can have its own
properties and methods, this is called as inheritance.



#Python Inheritance Syntax:

class BaseClass:
    Body of base class
class DerivedVlass(BaseClass):
    Body of derived class
__________________________________________________________________________________________

Derived class inherits features from the base class where new featues can be added to it.
This results in re-usability of code.

Types of inheritance:

1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical inheritance

'''


'''

Single inheritance:-

Single inheritance enables a derived class to inherit properites from single parent clas,
thus enabiling code reualbility and the addition of new featues to existing code.

'''
#Example of Single Inheritance

print("\n ::::::::: Single inheritence :::::::: \n")


class Parent:
    def func1(self):
        print("This function is in parent class.")
        
class Child(Parent):
    def func2(self):
        print("This function is in child Class.")

ref = Child()
ref.func1()
ref.func2()


'''
Multiple Inheritance:

When a class can be derived from more than one base class this type of inheritance is called
multiple inheritance. In multiple inheritances, all the features of the base classes are
inherited into the derived class.

'''
#Example :

print("\n ::::::: Multiple Inheritance ::::::: \n")

class Mother:
    MotherName = "XYZ"

    def mother(self):
        print(self.MotherName)

        
class Father:
    FatherName = "ABC"

    def Father(self):
        print(self.FatherName)

class Son(Mother,Father):
    def parents(self):
        print("Father name is :", self.FatherName)
        print("Moher name is :", self.MotherName)

s1 = Son()
s1.FatherName = "Daddy"
s1.MotherName = "Mamma"
s1.parents()
        
'''

Multilevel Inheritance:

In multilevel inheritance, features of the base class and the derived class are further
inherited into the new derived class. This is similar to a relationship representing child
and a grandfather.

'''
#Example :-

print("\n :::::: Multilevel Inheritance :::::: \n")


class Grandfather:

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername



class Father(Grandfather):
    def __init__(self,fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)



class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):

        self.sonname = sonname
        Father.__init__(self, fathername,grandfathername)

    def print_name(self):
            
            print('Grandfather name:', self.grandfathername)
            print("Father name : ", self.fathername)
            print("Son name :", self.sonname)


s1 = Son('Prince', 'Mohd ', 'Suhail')
#print(s1.grandfathername)
s1.print_name()
    
'''
Hierachical Inheritance:

When more than one drived class are created from a single base this type of inheritance is
called hierarchical inheritance. In this program, we have a parent (base) class and two
child(drived) classes

'''

#Example :

print(" \n ::::: Hierachical Inheritance :::::: \n")


class Parent:
    def func(self):
        print("This function is in parent class. ")


class Child(Parent):
    def func2(self):
        print("This function is in child 1. ")


class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

        
ref1 = Child()
ref2 = Child2()
ref1.func()
ref1.func2()
ref2.func()
ref2.func3()


'''
Hybrid Inheritance:

Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

'''

#Example :

print("\n :::::: Hybrid Inheritance :::::: \n")

class School:
    def SchInfo(self):
        print("This function is in school.")

class Student1(School):
    def std1(self):
        print("This function is in Student 1.")

class Student2(School):
    def std2 (self):
        print("This function is in Student 2.")

class Student3(Student2,Student1,School):
    def std3(self):
        print("This function is in student 3.")

obj = Student3()
obj.SchInfo()
obj.std1()
obj.std2()

    
    
    

















































































        







































