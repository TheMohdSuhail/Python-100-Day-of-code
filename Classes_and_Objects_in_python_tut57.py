'''
Python Class and Objects

Class :-
________

A Class is a blueprint or a template for creating objects, providing initial
(prelimainary = prarambhik) values for state(member variables or attributes), and
implementations of behavior (member functions or methods). The user-defined objects are
created using the class keyword.

'''

#Creating a Class:

#Let us now create class using the class keyword.

class Person:
    name = " MOhd Suhail"
    age = 20
    job = "Student"

'''
Createing an Object:

Object is the instance of the class used to access the properies of the class
Now lets create an object of the class.

'''

obj1 = Person()
#Now we can print values:

#Example:

print(obj1.name)
print(obj1.age)
print(obj1.job)

# We can modify properties on objects like this:
obj1.name = "MSP"
print(obj1.name)

'''
Self Parameter

The self parameter is a reference to the current instance of the class, and is used to
access variables that belongs to the class.

It must be provided as the extra parameter inside the method definition.

'''
#Example:

class Person :
    name = "Mohd Suhail"
    age = 20
    
    def desc(self):
        print("My name is ", self.name, "and I'm", self.age, "years old.")

ref = Person()
ref.desc()
ref.name = "MSP"
ref.age = 22

ref.desc()















































