'''
dir(), __dict__ and help() attribute/methods in python. They make it easy for us to
understand how classes resolve various functions and executes code. In Python, there are
three built-in functions that are commonly used to get information about objects: dir(),
dict, and help()>


The dir() method :

dir(): The dir() function returns a list of all the attributes and methods (including
dunger methods) available for an objecct. It is useful tool for discovering what you can do
with an object. Example:

'''
x = [1,2,3]
print(dir(x))
print("\n ____________________________________________________________\n")

'''
The __dict__ attribute

__dict__ : The __dict__ attribute returns a dictionary representation of an object's
attributes. It is a useful tool for introspection.

'''

# Example :

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

p = Person("Mohd Suhail", 21)

print("\n ____________________________________________________________\n")
print(p.__dict__)
print("\n ____________________________________________________________\n")
print(dir(p))
print("\n ____________________________________________________________\n")
print(p.__class__)
print(p.__delattr__)


'''
The help() method :

help(): The help() function is used to get help documentation for an object, including a
description of its attrubutes and methods. Example:

'''

print("\n ____________________________________________________________\n")

print(help(Person))

'''
In conclusion, dir(), dict, and help() are useful built-in functions in Python that can be
used to get information about objects. They are valuable tools for introspection and
discovery.




'''









































