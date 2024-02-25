'''
Super kyeword in Python

The super() keyword in python used to refer to the parent class. It is especially useful
when a class inherits from multiple parent classes and you want to call a method from one
of the parent classes.

When a class inherits from a parent class, it can override or extend the methods defined in
the parent class method in the child class. This is where the super() keyword comes in handy.

Here's an example of how to use the super() keyword in a simple inhritance scenario:

'''

# Example :

class ParentClass1:
    def parent_method(self):
        print(" This is the parent method 1.")


class ParentClass2:
    def parent_method(self):
        print(" This is the parent method 2.")

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("This is child method. ")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()


# Another Example 

class Employee:
    def __init__(self, name,id):
        self.name = name
        self.id = id

class  Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name,id)
        self.lang = lang
obj = Employee("Mohd Suhail", 404)
obj2 = Programmer( "Rana", 222, "Python")

print(obj2.name)
print(obj2.id)
print(obj2.lang)
print("Address of class object = ", id(obj2))


'''
In this example, the ChildClass inherits from both ParentClass1 and ParentClass2. The
child_method calls the parent_method of the first parent class using the super() keyword.

In conclusion, the super() keyword is a useful tool in Python when you want  to all parent
class method in child class. It can be used in inhritance senarios with a single parent
class or multiple parent classes.



'''

