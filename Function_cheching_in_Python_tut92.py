'''
Function Caching in Python 

Function caching is a technique for improving the performance of a program by storing the
results of a function call so that you can reuse the results instead of recomputing them
every time the function is called. This can be particularly useful when a function is
computationally expensive, or when the inputs to the function are unlikely to change
frequently.


In Python, function caching can be achieved using the functools.lru_cashe decorator. The
functools.lru_cache decorator is used to cache the results of a function so that you can
reuse the results instead of recomputing them every time the function is called.
Here's an example:



'''

import functools


@functools.lru_cache(maxsize=None)
def fib(n):
    if n<2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(20))
               
                            
##def my_decorator(func):
##    def wrapper():
##        print("Something is happening before the function is called.")
##        func()
##        print("Something is happening after the function is called.")
##    return wrapper
##
##@my_decorator
##def say_hello():
##    print("Hello!")
##
### Calling the decorated function
##say_hello()


'''
As you can see, the 'functools. lru_cache' decorator is used to cache the results of the
fib function. the maxsize parameter is used to speicify the maximum number of results to
cache. If maxsize is set to None, the  cache will have an unlimited size.


Benefits of Function Caching

Function caching can have a significat impact on the performance of program, paticularly
for computationally expensive functions. By caching the results of a function, you can
avoid having to recompute the results every time the function is called, which can save a
significant amount of time and computational resources.


Another benefit of function caching is that it can simplify the code of a program by
removing the need to manually cache the results of a function. With the
'functools.lru_cache' decorator, the caching is handled automatically, so you can focus
on writing the core logic of your program.


Conclusion

Function caching is a technique for improving the perfomance of a program by storing the
results of function so that you can reuse the results instead of recomputing them every
time the function is called. In Python 3, function caching can be achieved using the
'functools.lru_cache' decorator, which provides an easy and efficient way to cache the
results of a function. Whether you're writing a computationally expensive program, or
just want ot simplify your code, function caching is a great technique to have in your
toolbox.



'''


from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
  time.sleep(5)
  return n*5
    

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
print(fx(61))
print("done for 61")





















































































