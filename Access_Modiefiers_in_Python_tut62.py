'''
Access Specifiers/Modifiers in Python

Access specifiers or access modifiers in python programming are used to limit the access of
class variables and class methods outside of class while implementing the concepts of
inheritance.

Let us see the each one of access specifiers on detail:

Type of access specifiers

1. Public Access Modifier
2. Private Access Modifier
3. Protected Access Modifier
____________________________________________________________________________________________

Public Access Specifier In Python :-

All the varible and methods(member functions) in Python are by default public. Any instance
vaiable in a class followed by the 'self' keyword ie. self.var_name are public accessed.

'''

#Example:


print("\n :::::: Public Specifier ::::::\n")

class Student:

    #constructor is defined

    def __init__(self, age, name):
        self.age = age              #public variable
        self.name = name            #public variable

obj = Student(21,"Mohd Suhail")
print(obj.age)
print(obj.name)

'''
Private Access Modifier

By definition, Private members of a class(varibles or methods) are those members which are
only accessible inside the class. We cannot use private member outside of class.

In Python, there is no strict conscept of "private" access modifiers like in some other
programming languages. However, a convention has been established to inidcate that a vaiable
or method should be considered private by prefixing its name with a double underscore('__').
This is known as a "weak internal use indicator" and it is a convention only, not a strict
rule. Code outside the class can still access these "private" vaiables and methods, but it
is generally understood that they should not be accessed or modified.

'''

#Example :-

print(" \n ::::::: Private Specifier ::::::::\n")


class Student1:
    def __init__(self, age, name):
        self.__age = age   # An indication of private variable

        def __funName(self): # An indication of private function

            self.y = 34
            print(self.y)

class Subject(Student1):
    pass

ref = Student1(22,"MSP")
ref1 = Subject

# Calling by object of class Student1
try:
    
    print(ref.__age)
    print(ref.__funName())
except:

    print("AttributeError: 'student' object has no attribute '__age' :")

# Calling by Object of class Subject
try:
    

    print(ref1.__age)
    print(ref1.__funName())

except:
    
    print("AttributeError: 'subject' object has no attribute '__age' :")

    
'''

Private members of a class cannot be accessed or inheriten outside of class. It we try to
access or to ingerit the properties of private members to child class( Derived Class).
Then it will show the error.
___________________________________________________________________________________________


Name mangling

Name mangling in Python is a technique used to protect class-private and superclass-private
attributes from being accidentally overwritten by subclasses. Names of class-private and
superclass-class attributes are transfromed by the addition of a single leading underscore
and a double leading underscore respectively.


'''

print("\n:::: Name mangled ::::::\n")


class MyClass:
    def __init__(self):
        self._nonmangled_attribute = " I am a nonmangled Attribute"
        self.__mangled_attribute = " I am a mangled attribute"

My_Obj = MyClass()

print(My_Obj._nonmangled_attribute)  # Output : I am a nonmangled attribute

try:
    
    print(My_Obj.__mangled_attribute) # This line Throws Attribute Error Without Exception Handling
    
except:
    print("Throws an AttributeError")
print(My_Obj._MyClass__mangled_attribute) #Output : I am a mangled attribute

'''
In the example above, the attribue _nonmangled_attribute is marked as nonmangled by
convention, but can still be accessed from outside the class.
The attribute __mangled_attribute is private and its name is "mangled"
to _MyClass__mangled_attribute, so it can't be accessed directly from outside the class,
but can access it by calling _MyClass__mangled_attribute


'''
print("\n :::::::  Protected Specifier ::::::\n ")


'''
Protected Access Modifier :-

In Object-Oriented Programming (OOPs), the term "Protected" is used to describe member
(i.e., a method or Attribute) of a class that is intended to be accessed only by the class
itself and its subclasses. In Python, the convention(सम्मेलन) for indicating that a member is
protected is to prefix its name with single underscore(_). For example, if a class has a
method called _my_method, it is indicating that the method should only be accessed by the
class itself and its subclasses.

It's important to note that the single underscore is just a naming convention, and does not
actually provide any protection or restrict access to the member. The syntax we follow to
make any variable protected is to write variable name followed by a single underscore (_) ie.
_varName.


'''

#Example :-

class Student01:
    def __init__(self):
        self._name= "Mohd Suhail"

    def _funName(self):             #Protected method
        return " Mohd Suhail MSP "

class Subject01(Student01):         # inherited class

    pass


obj01 = Student01()
obj02 = Subject01()

# Calling by object of Student class

print(obj01._name)
print(obj01._funName())

# calling by object of Subject class

print(" Call By object of Subject class")
print(obj02._name)
print(obj02._funName())





    






































