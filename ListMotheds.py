'''

List Method

list.sort()
This method sorts the list in ascending order. The original list is updated

'''

colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

'''
What if you want to print the list in descending order?
Er must give reverse = True as a parameter in the sort method.

colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

'''
print(" -------------------------------")

colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)

'''
The reverse parameter is set to False by default. 

Note: Do not mistake the reverse parameter with the reverse method.

'''

'''
reverse()
This method reverses the order of the list. 

'''

print("Reverse Method")
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)


'''
index()

The method returns the index of the first occurrence of the list item.

'''

print("Index Method")
num = [4,2,5,3,6,1,2,1,2,8,9,7]
print(num.index(3))


'''
count()

Rrturms the count of the number of items with the given value. 


'''

print("Count Method")

num = [4,2,5,3,6,1,2,1,2,8,9,7]
print(num.count(2))


'''
copy()

Returns copy of the list. This can be done to perform operation on the list without modifying the original
the list.

'''
print("Copy Method ")

num = [4,2,5,3,6,1,2,1,2,8,9,7]
newlist = num.copy()
print(num)
print(newlist)

'''
append():

This method appends items to the end of the existing list.

'''
print("Append Method ")
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.append("MSP")
print(num)

'''
insert():
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

'''
print("Insert Method")

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.insert(5,"Insert Method")
print(num)

'''
extend():

This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

'''

print("Extend Method ")
num = [4,2,5,3,6,1,2,1,2,8,9,7]
newlist1 = [2,5,6,"Extend Method"]
num.extend(newlist1)
print(num)

'''
Concatenating two lists:

You can simply concatenate two lists to join two lists.

'''

print("This is Concatenating two lists:")
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num2 = ["new","list","this list","name","is","num2"]
print(num + num2)