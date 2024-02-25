'''
Utilites in Python

Commond line utilites are programs that can be run from
the ternimal or command line interface, and they are an
essential(ضروری) part of many development workflows. In
Python, you can create your own command line utilites
using the built-in argpase module.

Syntex :


Here is the basic syntex for creating command line
utility using argpase in Python:



import argparse

parse = argparse.ArgumentParser()

# Add command line arguments

parse.add_argument("arg1", help= "description of argument 1")
parse.add_argument("arg2", help= "description of argument 2")

# Parse the arguments

args = parse.parse_args()

# Use the arguments in your code

print(args.arg1)
print(args.arg2)

'''

# Example:

'''
Here are a few examples to help you get started with
creating command line utilites in Python


Adding optional arguments

The following example shows how to add an optional
argument to your command line utility:

'''

# Example :



import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--optional", help="description of optional argument", default="default_value")

args = parser.parse_args()

print(args.optional)

'''

Adding argument with type

The following example show how to add an argument with
a specified type:

'''
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", type=int, help="description of integer argument")

args = parser.parse_args()

print(args.n)

'''
Conclusion

Creating command line utilites in Python is a
straightforward and flexible porcess thanks  to
argparse module. With a few lines of code, you an
crate powerful and customizable comman line tools that
can make your development workflow easier and more
efficient. Whether you're working on small scripts or large applications, the argparse module is a must-have tool for any Python developer.

'''





















