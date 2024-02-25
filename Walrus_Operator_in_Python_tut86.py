'''
The Walrus Operator in Python

The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a
variable within an expression. This can be useful when you need to use a value multiple times
in a loop, but don't want to repeat the calcutlation.

The Walrus Operator is represented by the := syntax and can be use in a variety of contexts
including while loops and if statements.

Here's an example of how you can use the Walrus Operator in a while loop:


'''

#Eample :

numbers = [1,2,3,4,5]

while (n := len (numbers)) >0:
    print(numbers.pop())

print(numbers)



'''
In this exmample, the length of the numbers list is assigned to the variable n is then used
in the condition of the while loop, so that the loop will continue to execute until the
numbers list is empty.

Another example of using the Walrus Operator in an if statement:

'''
# Example :

names = [ "John", "Jane", "Jim"]

if ( name := input ("Enter a name:")) in names:

    print(f"Hello, {name}!")
else:
    print("Name not found.")


# Here is another example :

# Using only while loop

##foods = list()
##
##while True :
##    food = input("What food do you like? :")
##    if food == "quit":
##        break
##    foods.append(food)
##print(foods)

# Another Eample using while loop with Walrus Operator

foods = list()

while (food := input("What food do you like?: ")) != "quit":

    foods.append(food)
for i in enumerate(foods):
    print(i)

'''
In this example, the user input is assigned to the variable name using the Walrus Operator.
The value of name is then use in the if statement to deternime whether it is in the names
list. If it is, the corresponding message is  printed, otherwise, a different message is
printed.



It is important to note that the Walrus Operator should be used sparingly ( تھوڑا سا ) as it
can make code less readableif overused (ضرورت سے زیادہ استعمال ).


In conclusion, the Walrus Operator is a useful tool for Python developers to have in their
toolkit. It can help streamline (ہموار or कारगर ) code and reduce duplication, but it should
be used with care to  ensure code readbiliy and 


'''




 

































