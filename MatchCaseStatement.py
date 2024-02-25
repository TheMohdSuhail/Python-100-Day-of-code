'''
Match Case Statement
To implement switch-case like characteristics very simeilar to if-else functionality,we use a match case in python.

The match case consists of three main entities:
1. The match keyword
2. One or more case clauses
3. Expression for each case

We more than one Default match case with if esle statement

'''

x = int(input("Enter the number "))
match x:
    case 1:
        print("Number is 1 ")
    case 2:
        print("Number is 2 ")
    case 3:
        print("Number is 3")
    case _:
        print("This is Default Match Case ")