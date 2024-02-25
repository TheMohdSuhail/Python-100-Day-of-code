'''
Operator Overloading in Python:

An Introduction

Operator Overlading is a feature in Python that allows developer to redefine the behavior
of mathematical and comparison operators for custom data types. This means that you can use
the standard mathematical operators (+,-,*,/, etc) and comparison operators(>,<,==, etc.)
in your own classes, just as you  would for built-in data types like int, float, and str.

Why do we need operator overloaading?

Operator overloading allows you to create more readable and intuitive code. For instance,
consider a custom class that represent a point in 2D space. You could define a method called
'add' to add two points together, but using the + operator makes the code more concise(مختصر)
and readable:

p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1 + p2
print(p3.x, p3.y)

How to overload an operator In Python?

You can overlaod an operator in Python by defining special methods in your class. These
methods are identified by their names, which start and end with double underscore(__).
Here are some of the most commonly overloaded operators and their corresponding special
methods:

+ : __add__
- : __sub__
* : __mul__
/ : __truediv__
< : __lt__
> : __gt__
== : __eq__

For example, if you want ot overload the + opeator to add two instances of custom class,
you would define the add method:

'''
# Example :

class Point:
    def __init__(self, x):
        self.x = x
        #self.y = y
    def __add__ (self, other):
        return Point(self.x + other.x)
    

p1 = Point(1)
p2 = Point(4)
p3 = p1+p2


print(p3.x)


class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f" {self.i}i + {self.j}j + {self.k}k"
    def __add__(self,x):
        return Vector(self.i + x.i, self.j+x.j, self.k+x.k)
v1 = Vector(3,5,6)
print(v1)

v2 = Vector(1,2,9)
print(v2)


print(v1+v2)
print(type(v1+ v2))



































