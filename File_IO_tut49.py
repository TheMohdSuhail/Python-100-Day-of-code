'''
Python provides several ways to manipulate files. Today, we will discuss how to handle file
in Python

Opening a File

Before we can perform any operations on a file, we must first open it. Python provides the
open() function to open a file. It takes two arguments: the name of the files and the mode
in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a'
for appending.
-------------------------------------------------------------------------------------------
Here's an example of how to open a file reading:
'''
import os


f = open('msp.py','r')

re = f.read()

print(re)

'''
Create a file using Python

"x" - Create: This command will create new file if and only if there is no file already in
existence with that name or else it will return an error.

'''

#f1 = open("msp33.txt","x")


'''
Writing to a File

To write to a file, we first need to open it in write node.

'''
f2 = open('msp33.txt','r')
#f2.write("Hello, world!")
f3 = open('msp33.txt','r')
re1 = f2.read()
print(re1)

#f4 = open("msp45.py","x")
f5 = open("msp45.py",'w')
f5.write("Mohd Suhail ")
f6 = open("msp45.py",'r')
re2 = f6.read()
print(re2)

f7 = os.open("msp44.py", os.O_RDONLY)
re3 = os.read(f7,1024)
print(re3)
os.close(f7)


f8 = os.open("msp44.py",os.O_RDWR)

strg ="print(""hello"")"
line = str.encode(strg)

numBytes = os.write(f7, line)
print(numBytes)

f8 = os.open("msp44.py",os.O_RDONLY)
res4 = os.read(f8,1024)
print(res4)

os.close(f7)


'''
Keep in mnd that writing to a file will  overwrite its contents. If you want to append to a
file instead of everwriting it, you can open it i append mode.
 
'''
f9 = open('msp45.py', 'a')
f9.write('hello world!')
#res5 = f9.read()
#print(res5)

'''
Closing a File

It is important to close a file after you are done with it. This releases the resources used
by the file and allows other programs to access it.

To close a file, you can use the close() method.



'''
f.close()
 
'''
The 'with' statement

Alternatively, you can use the with statement to automaically close the file after you are
done with it.

'''
with open('msp.py','r') as f:
    res6 =  f.read()
    print(res6)
    










