'''
Dictionary Methods

Dictionary uses several built-in methods for manipulation. They are listed below


'''

'''
update():

The update() method updates the value of the key provided to it if the item already exists
in the dictionay, else it creates a new key-value pair

'''

#Example:

info= { "name": "Karan", "age":19, "eligible":True}
print(info)
print(type(info))

info.update({"age":20})
print(info)


info.update({"dob":2001})
print(info)


'''
Removing items form dictionary:

There are a few metods that we can use to remove items form dictionary.

clear():
The clear() method removes all the items from the list.

'''

#Example:

#info.clear()
print(info)

'''
pop():
The pop() method removes the key-vlaue pair whose key is passed as a paremeter. 

'''
#Example:

info.pop('eligible')
print(info)


'''
popitem():
The popitem() method removes the last key-value pair from the dictionay.

'''

#Example:

info.popitem()
print(info)


'''

del:

We can also use the keyword to remove a dictionay item.

NOTES : IF KEY IS NOT PROVIDED, THEN THE DEL KEYWORD WILL DELETE THE DICTIONAY ENTIRELY.
'''
#Example:

#del info
print(info)

del info['age']
print(info)































