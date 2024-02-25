'''
Lambda Function in Python

In Python, a lambda function is a small anonymous function without a name. It is defined
using lambda keyoword and has the following syntax:


lambda arguments: expression
--------------------------------------------------------------------------------------

Lambda functions are often used in situations where a small function is required for a short
period of time. They are commonly used as arguments to higher-order functions, such as map,
filter, reduce.

Here is an example of how to use a lambda function:

'''
def double(x):
    return x *2
print(double(5))

#lambda function to double the input

a = lambda y: y*2

print("This is lambda function :",a(5))

'''
Lambda function to calculate the product of two numbers
'''
b = lambda j,k: j*k
print(b(55,4))


'''
Lambda functions can include multiple statements, but they are limited to a single expression.
For example:


'''

lambda x, y : print(f'{x} * {y} = {x * y}')

'''
In the above example, the lambda function includes a print statement, but it is still
limited to single expression.

Lambda functions are often used in conjunction with higher-order functions, such as map,
filter, and reduce which we will look into later.



'''


# We can use lambda function as an argument in  normal function

def appl(fx, value):
    return 6 + fx(value)
print('this is lambda argument', appl(a,2))






























