'''
Python Lists

Lists are ordered collection of data items.
They store multuple items in a single variable.
List items are separated by commas and enclosed within square brackets [].
Lists are changeable meaning we can after them creation.

Examaple 1:
'''

lst1 = [1,23,4,5,6,7]
lst2 = ["Red","Green", "Blue"]
print(lst1)
print(lst2)

# Example 2


details = ["Abhijeet", 18 , "FYBScIT", 9.8]
print(details)

'''
List Index

Each item / element in a list has its own unique index. This index can be used to access any particular item from the list.  The first item has ide
particular item from the list. The first item has index[0], second item has index [1] ,third item has index [2] and so on. 
'''

#Example 3

colors = ["Red", "Green", "Blue", "Yellow", "Green"]

print(colors)

'''
Accessing list items

We can access list items by using its index with the square bracket syntax[].
For example colors[0] will give "Red", colors [1] give "Green" and so on...
'''
#Positive Indexing:

#As we have seen that list items have index, as such we can access items using these indexes,

#Example:

colors = ["Red", "Green", "Blue", "Yellow", "Green"]

print(colors[2])
print(colors[4])
print(colors[0])


'''

Negative Indexing:

Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

Example 
'''
colors = ["Red", "Green", "blue", "yellow", "Green"]
print(colors[-1])
print(colors[-2])
print(colors[-5])

'''
Check whetger an item in present in the list
We can check if a given item is present in the list. This is done using the in keyword.

'''

colors = ["Red", "Green", "Blue","Yellow","Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")

'''
Range if Index:

You can print a range of list items by specifying where you want to start, when do you want to end and if you want to skip elements to skip elements in between the range.

Syntax:
listName[start : end : jumpIndex]

Note: jump Index is optional. We will see this in later examples.

Example: printing elements within a particular range:

'''
animals = ["cat","dog", "bat", "mouse","pig","horse", "donkey","goat","cow"]
print(animals[3:7])
print(animals[-7:-2])

'''
List Comprehension 

List Comprehensions are used  for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

Syntax: 
List = [Expression(item) for item in iterable if Condition]
Expression: It is the item which is being iterated. 
Iterable: It can be list, tuples, dictionaries, sets,and even in arrays and strings.

Condition: Condition checks if the item should be added to the new list or not.

Example :
'''

print("Comprehensions List")

names = ["Milo", "Sarah", "Bruno", "Anastasia","Rosa"]
namesWith_0 = [item for item in names if "o" in item]
print(namesWith_0)





