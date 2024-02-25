'''
Getters :-

Getters in Python are methods that are used to access the values of an object's properties.
They are used to return the value of a specific property, and are typically defined using
the @propety decorator. Here is an example of a simple class with getter method:

'''

class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    
'''
In this example, the MyClass class has single property, _value, which is initialized in the
init method. The value method is defined as a getter using the @property decorator, and is
used to return the value of the _vlaue property.

To use the getter, we can create an instance of the MyClass class, and then access the value
property as if it were an attribute:


>>> ref = MyClass(10)
>>> ref.value

'''

'''
Setters :-

It is important to note that the getter do not take any parameters and we cannot set the
value through getter method. For that we need setter method which can be added by decorating
method with @property_name.setter

Here is example of a class with both getter and setter:

'''
class MyClass:
    def  __init__(self, value):
        self._value = value

        @property
        def value(self):
            return self._value
        @value.setter
        def value(sefl, new_value):
            sefl._value = new_value

'''
For Run Type These line in sell

>>> obj = MyClass(10)
>>> obj.value = 20
>>> obj.value
____________________________________________________________________________________________

In Conclusion, getter are a convenient way to access the values of an object's properties,
while keeping the internal represintation of the property hidden. This can be useful for
encapsulation and data validation.


'''













            
