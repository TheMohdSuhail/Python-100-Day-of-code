'''
Recursion in python

Recursion is the process of defining something terms of itself.

A physical world example would be to place two parallel mirrors facing each other. Any object in between
them would be reflected recursively.

Python Recursive function

In Python, we know that a function can call other functions. It is even possible for the function to call itself.
These types of construct are termed as recursive functions.

'''
#Example

def factorial(num):
    if(num== 1 or num ==0):
        return 1
    else:
         return(num* factorial(num-1))

inp = int(input("Enter number :"))

print(factorial(inp))




