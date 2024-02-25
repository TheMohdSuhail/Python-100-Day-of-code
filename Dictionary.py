'''

Dictionaries are ordered collection of data items. They store multiple items in a single variable.
Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets{}

'''
info = {"name": "Mohd Suhail", "age":20}

print(info["name"])
print(info.get("name9"))


'''

NOTES : Run time error show karne ke liye normal key se value access kar te hai

if agar key dictionary me koi key nahi hai to or error show nahi karna for .get()methon ka use kiya jata hai

'''



for key in info.keys():
    print(f"The value corresponding to the key {key } is {info[key]}")

'''

I. Accessing single values:

Values in a dictionary can be accessed using keys. We can access dictionay
values by mentioning keys either in square brackets or by using get method. 

'''


'''

II. Accessing multiple values:
We can print all the values in the dictionaary using values() method. 

'''
print(info.values())


'''

II. Accissing keys: We can print all the keys in the dictionary using keys()method. 

'''

print(info.keys())


'''
IV. Accessing key-value pairs:

We can print all the key-value pairs in the dictionary using items() method.

'''

#Example:

print(info.items())

