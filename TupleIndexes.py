'''
Tuple Indexes
Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index[0], second item has index[1], third item has index [2] and so on.

'''

# Example 1

country = ("Spain", "Italy", "India")
print(country)

'''
Accessing tuple items:

I. Positive Indexing :

As we have seen that tuple items have index, as such we can access items using these indexes. 
'''
# Example

print(country[0])
print(country[1])
print(country[2])


'''
II. Negative Indexing:

Similar to positive indexing, negative indexing is also used t acccess items, but from the end of the tuple, The last item has index[-1]
second last item has index[-2], third last item has index[-3] and so on.

'''

print("-------------------------------------------\n")
print("Negative Indexing\n\n")

print(country[-1])
print(country[-2])
print(country[-3])

'''
III. Check for item:
We can check if a given item is present in the tuple. This is done using the 'in' keyword.
'''
if "India " in country:
    print("india is present.")
else:
    print("India is absent")



'''
IV. Range of Index:
You can print a range of tuple items by specifying where do you want to start, 
where do you want to end and of you want to skip elements in between the range. 

Syntax:
Tuple [start : end : jumpIndex]

Note: ump Index is optional. We will see this in given examples.
 
'''


# Example
print("-----------------Range of Indexing-------------------\n")

animals = ("cat" ,"dog", "bat", "mouse", "pig", "horse","donkey", "goat", "cow")
print(animals)
print(animals[3:7])
print(animals[-7:-2])
print(animals.index("pig"),"Index print ")


# Range tak pad liya hai isse aage se start karna hai

'''
Here, we provide index of the element from where want to start and the index of the element till which we want to values. Note:
The element of the end index prided will not be included.

Example: 

'''
