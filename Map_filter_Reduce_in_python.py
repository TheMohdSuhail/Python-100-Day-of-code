'''
Map, Filter and Reduce

In Python the map, filter,and reduce functions are built-in functions that allow you to apply
a function to a sequence of elements and return a new sequence.
These functions are known as higher-order functions, as they take other functions as arguments.


Map

The Map function applies a function to each element in a sequence and returns a new sequence
containing the transformed elements. The map function has the following syntax:

_______________________________________

    map(function, iterable)
_______________________________________

The function argument is a function that is appled to each element in the iterable argument.
The iterable argument can be a list, tuple or any other iterable object.

Here is an example of how to use the map function:



'''

numbers = [1,2,3,4,5]
#Double each number using the map function

doubled = map(lambda x: x * 2, numbers)

print(list(doubled))


'''

In the above example, the lambda fucntion lambda x: x * 2 is used to double each element in
the numbers in the numbers list. The map function applies the lambda function to each elemente
in the list and returns a new list containing the doubled numbers.

--------------------------------------------------------------------------------------------

Filter

The filter functions filters a sequence of elements based on given predicate ( a function that
returns a boolean value) and returns a new sequence containing only the elements that meet the
predicate. The filter function has teh followig syntax:

_____________________________________________________

    filter(predicate, iterable)

_____________________________________________________

The predicate argument is a function that returns boolean and is applied to each element in the
iterable argument. The iterable argument can be a list, tuple or other iterable object.

Here is an example of how to use the filter function:

'''
# Get only th even numbers using the filter function

evens = filter(lambda x: x % 2 ==0, numbers)

print(list(evens))

'''

In the above example, the lambda function lambda x: x % 2 == 0 is used to filter the numbers
list and return only the even numbers. The filter function applies the lambda function to
each element in the list and returns a new list containing only the even numbers.

--------------------------------------------------------------------------------------------

Reduce

The reduce function is a higher-order function that applies a function to a sequence and
returns a sigle value. It is a part of the funct

'''



































