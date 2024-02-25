'''
Async IO in Python

Asynchronous I/O, or async for short, is a programming pattern that allows for
high-perfomance I/O operations in a concurrent and non-blocking manner. In Python, async
porgramming is achieved through the use of the asyncio module and asynchronous functions.

Syntax

Here is the basic syntax for creating an asynchronous function in Python :



'''
import time
import requests 
import asyncio

async def my_async_function():

    await asyncio.sleep(1)
    return "Hello, Async World!"

async def main():
    result = await my_async_function()
    print(result)



#Another way to schedule tasks concurrently is as

    L = await asyncio.gather(
        
            my_async_function(),
            my_async_function(),
            my_async_function(),
        )
    print(L)
asyncio.run(main())


'''
Async IO is a powerful programming pattern that allows for high-performance and concurrent
I/O operations in Python. With the asyncio module and asynchronous functions, you can write
efficient and scalable code that can handle large amounts of data and I/O operations without
blocking the main thread. Wheather you're working on web applications, network services, or
data processing pipelines, async IO is an essential tool for any Python developer.


'''

async def function1():
     print("func 1")
     URL ="https://images.unsplash.com/photo-1493612276216-ee3925520721?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cmFuZG9tfGVufDB8fDB8fHww&auto=format&fit=crop&w=1000&q=60"
     response = requests.get(URL)
     open("themsp.ico","wb").write(response.content)
     return "MSP"

async def function2():
    print("func 2")
    URL = "https://images.unsplash.com/photo-1508138221679-760a23a2285b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8cmFuZG9tfGVufDB8fDB8fHww&auto=format&fit=crop&w=1000&q=60"
    response = requests.get(URL)
    open("themsp2.jpg", "wb").write(response.content)

async def main():
##    await function1()
##    await function2()
##    return 2
    L = await asyncio.gather(
        function1(),
        function2(),
    )
    print(L)

asyncio.run(main())   










































     
