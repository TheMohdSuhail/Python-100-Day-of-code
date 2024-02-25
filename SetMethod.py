'''

Joining Sets

Sets in python more or less work in the same way as sets in mathematics.
We can perform operations like union and intersection on the sets just like
in mathematics.



I. union() and update():

The union() and update() methods prints all items that are present in the two
sets. The union() method returns new whereas update() method adds item into the
 existing set from another set.

'''

# Example:

cities = {"Tokyo", "Madrid","Berlin","Delhi"}
cities2 = {"Tokyo", "Seoul","Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)
#
# cities.update(cities2)
# print(cities)


'''
II. Intersection and intersection_update():

The intersection() and intersection_update()methods prints only items that are similar to both the sets. 
The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

'''
num = { 4,5,6,8,9}
num2 = {1,2,3,4,5,6,7}


num3 = num.intersection(num2)
print(num3)


num.intersection_update(num2)
print(num)

'''
III. Symmetric_difference and summetric__differece_update():

The symmetric_diffrence() and symmetric_diffrenceUpdate() methods prints only
items that are not similar to both the sets. The symmetric_differebce() method returns a new set where
as  symmetic_difference_update() method updates into existig set from anoter set. 

'''
#Example

num5 = {2,4,6,7,8,8,9,55,88,55}
num6 = {1,2,4,6,7,8,9,35,75,44}
num7 = num5.symmetric_difference(num6)
print("Symmetric Difference ", num7)
num5.symmetric_difference_update(num6)
print("Symmetric Difference Update ", num5)


'''
IV. Difference() and difference_update():

The difference() and differnce_update() methods prints only items that are only present in both the sets.
The difference() method returns a new set whereas difference_update() mehod updates into
the existing set from anothe set.


'''
num8 = num6.difference(num5)
print("Difference Mehtods ",num8)


'''
Ther are several in-built methods used for the manipulation of set. They are explainde below


isdisjoint():

The isdisjoint() method checks if items of given set are present in another set, This method return 
False if items are present, else it returns True.

'''

print( " Disjoint side ",num5.isdisjoint(num6))

'''
issuperset():

The issuperset(0 method checks if all the items of a partucular set are present in the original set. It returns True if all the items are present, slse it returns False.

'''

print(" This form SuperSet ",num5.issuperset(num6))


'''
issubset():

The issubset() method checks if all the items of the original set are present in the present in the particular set. It returns True if all the items are present, else it returns False.


'''
# Example
print(" This is Subset ",num5.issubset(num6))



'''
add()

If you want to add a single item to the set use the add() method.

'''
Shahar = {"MuzaffarNagar ", "Meerut", "SaharanPur"}
print(Shahar)
Shahar.add("Shamli")
print(Shahar)


'''

update()

If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary),
and use the update() method to add it into the existing set.

'''


Shahar.update(cities)
print("Update Method ",Shahar)


'''
remove()/discard()
We can use remove() and discard() methods to remove items form list.
'''

Shahar.remove("Shamli")
print('Remove',Shahar)
#Shahar.remove("Shamli")
#print(Shahar)

Shahar.discard("Shamli")
print(Shahar)

'''
pop()

This method removes the last item of the set but the catch is that we don't know which item gets popped as sets are unordered.
However, you can access the popped item if you assign the pop() method to a variable.
'''
#Example
item = Shahar.pop()
print("POP Method ",item)
print(Shahar)

'''
del

del is not a method, rather it is a keyword which deletes the set entirely.

What if we don't want to delete the entire set, we just want to delete all items within that set?

'''
#del Shahar
print(Shahar)

'''
clear():

This method clears all items in the set and prints an empty set. 
'''
#Example

Shahar.clear()
print(Shahar)

