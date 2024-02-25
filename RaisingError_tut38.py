'''



Raising Custom Errors

In python, we can raise custom errors by using the raise Keyword.

'''

salary = int(input("Enter salary amount :"))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

'''

In the previous tutorial, we learned about different built-in exceptions in Python
and why it is important to handle exceptions. However, sometimes we may need to create
our own custom exceptions that serve our purpose.


Defining Custom Exceptions

In Python, we can define custom exceptions by creatin a new class that is derived from
the built-in Ecepton class.

 Here's the sybtax to define custom exceptons:

 Syntex

 class CustomError (Exception):
 #code ......
 pass

 try:
     #code ....
 except CustomError:
     code........


This is useful because sometimes we might want to do something when a particular
exception is raised. For example, sending an error report to the admin. calling an api, etc.
'''
a = int(input("Enter any value between 5 and 9 "))

if(a<5 or a>9):
    raise ValurError("Value should be between 5 and 9")



