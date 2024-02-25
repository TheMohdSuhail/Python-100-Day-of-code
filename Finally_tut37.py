
'''
Finally Clause

The finally code block is also a part of exeption handling. When we handle exception
using the try and except block, we can include a finally
block at the end. The finally block is always exceuted, so it is generally used for doing the
concluding tasks like closing file resources or closing database connection or may be ending
the porgarm execution with a delightful message.

'''
#Example

try:
    num = int(input("Enter an interger: "))

except ValueError:
    print("Number entered is not an integer." )
else:
    print("Integer Accepted. ")
finally:
    print("This block is always executed. ")

def func1():
    try:
        l= [1,4,6,5,3,2]
        i = int(input("Enter the index: " ))
        print(l[i])
        return 1

    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed")


e = func1()
print(e)


        
