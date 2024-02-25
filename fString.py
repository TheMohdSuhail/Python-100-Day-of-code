'''
String formatting in python

String formatting can be done in python using the format method.


'''
#example

txt = "For only {price:.2f} dollars!"
print(txt.format(price =49.555))

'''
f-sting in python 

It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal string Interpolation or more commonly as F-strings (f character preceding the string literal )/
The primary focus of this mechanism is to make the interpolation easier.

When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format(). If 


'''

name = " Mohd Suhail "
country = "INDIA"
print(f"We use f-string like this :Hey my name is {name} and i am from {country}")
print(f"We use f-string like this :Hey my name is {{name}} and i ama from {{country}}")

