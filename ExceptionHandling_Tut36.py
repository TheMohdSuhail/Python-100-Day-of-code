'''
Exception Handling

Exception handling is the process of responding to unwanted or unexpected events
when a computer program runs. Excption handling deals with these events to avoid
the program or system crashing, and without this process, exceptions would disrupt
the normal operation of a program.



Exceptions in Python

Python has many built-exceptions that are raised when your prograam uncounters
an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process
and passess it to the calling process untill it is handled. If not handled, the
program will crash.


Python try.. except

try ..except blocks are used in python to handle error and exceptions.
The code in try block runs when there is no error. If the try block catches
the error, then the except block is executed. 


'''

#Example:

try:
    num = int(input("Enter an integer: "))
    print(f"Your number is {num} ")
except:
    print("Invalid Input!")

#try:
 #   for i in range(1,11):
  #      print(f"{num}  X {i} = {num*i}")

#except:
 #s   print("Invalid Input!")


try:
    a = [6,3]
    print(a[num])

except ValueError:

    print("Number enterred is not an integer:")

except IndexError:
    print("index Error")

    
