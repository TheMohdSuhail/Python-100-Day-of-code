'''
Function Argumrnts and return statement

There are four types of argumrnts that we can provide in a function:
. Default Arguments
. Keyword Arguments
. Variable length Arguments
. Required Argument

Default arguments:

We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

Example:

def name(fname, mname = "jhon", lname = "Whatson"):
    print("Hello, ", fname mname, lname)
name("MSP")

:KEYWORD ARGUMENTS:

We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the order in which the arguments are passed does not matter.

Example:

def name2(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name2(mname = "Peter", lname = "Wesker", fname - "Jade")


: REQUIRED ARGUMENTS:

In case we don't pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match woth actual function definition.

Example 1: When number of arguments passed does not match to the actual function definition.

def name3(fname, mname,lname):
    print("Hello,", fname, mname, lname)
name3("peter", Quill")

Example2:

def name4(fname, mname, lname):
    print("Hello, ", fname, mname, lname)

name4("Peter", Ego", Quill")

:: Variable-length arguments:

Sometimes we may need to pass more arguments than those defined in the actual function.
This can be done using variable-length arguments.

There are two ways to achieve this:

Arbitrary Arguments:

While creating a function, pass a * before the parameter name while defining the function, The function acesses the arguments by processing them in the form of tuple.

Example:
    def name5(*name):
    print("Hello,", name[0], name[1], name[2])

name5("James", Bucchanan", "Barnes")


Keyword Arbitrary Arguments:

While creating a function, pass a ** before the parameter name while defining the function. The function accesses the arguments by processing the in the form of dictionary.

Example :

def name6 (**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name6(mname = "Buchanan", lname = "Barnes", fname = "James")



 Return Statement

The return statement is used to return the value of the expression back to the calling function.

Example:

def name7(fname, mname, lname):
     return "hello, " + fname + "  " + mname  + " " + lname
print(name("James", "Buchanan", Barnes"))

'''