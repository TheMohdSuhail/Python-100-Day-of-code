'''
Static Method :-

Static methods in Python are methods that belong to a class rather than(بجائے اس کے ) an
instance of the class. They are defined using the @staticmethod decorator and do not have
access to the instance of the class(i.e.self). They are called on the class itself, not on
an instance of the class. Static methods are often used to create utlity functions that don't
need access to instance data.

'''

#Example :-

class Math:
    @staticmethod
    def add(a, b):
        return a+b
result = Math.add(1,2)
print(result)


'''
In this example, the 'add' method is a static method of the Math Class. It takes two
parameters 'a' and 'b' and returns their sum. The method can be called on the class itself,
without the need to create an instance of the class.



'''
