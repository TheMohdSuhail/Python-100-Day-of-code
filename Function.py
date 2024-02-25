'''
Function in Python

A funtion is a block of code that performs a specific task whenever it is called.
In bigger programs, where we have large amounts of code,it is advisable to create or use existing functions that make the programs flow organized and neat.

There are two types of functons:

1. Built-in functions
2. User-defined functions

Built-in functions:

These functions are defined and pre-coded in python.Some examples of built-on functions are as follows;

min(),max(), len(), sum(),type(), range(), dict(), list(),tuple(),set(), print(),etc.

User-defined functions:

We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.
Notes:- User define funtions define by def keyword

Syntax: 

def hello():
    a = 4
    b = 5
    print(a+b)

hello() # function calling

'''

def average(*number):
    sum = 0
    # print(number)
    for i in number:
        print(i)
        sum = sum + i
        # print(sum)
    print("Lenths of number ",len(number))
    print("Average is: ", sum/len(number))

average(2,2,4,5,6)