'''
OS Module in Python

The os module in Python is a built-in library that provides functions for interactin with the
oprating system. It allows you to perform a wide a variety of tasks, such as reading and
writing files, interacting with the file system, and running system commands.

Here are some common tasks you can perform with os module:

Reading and writing files The os module provides functions for opening, reading, and writing
files. For example, to open a file for reading, you can use the open function:

'''

import os

f = os.open("OS_Module_test.txt", os.O_RDONLY)
#print(f)

contents = os.read(f,1024)
print(contents)
os.close(f)

#myfile = open("myfile.txt", "x")
#print(myfile)
'''
print(len(dir(os)))

a = dir(os)

for c, b in enumerate(a):
    print(c+1,b)
'''

output = os.environ['HOME']
print(output)

'''
program = "python"
arguments = ["DateTime.py"]
print(os.execvp(program, (program,) + tuple(arguments)))

fileDir = "msp.txt"
os.rename(f,'msp4.txt')
print(fileDir)
'''


'''
Interactin with the file system

The os module also provides functions for interacting with the file system. for example you
can use the os.listdir function to get a list of the files in a directory:


'''
files = os.listdir(".")

for index , file in enumerate(files):
    print(index, file)


'''
You can also use the os.mkdir function to create a new directory.
'''
#os.mkdir("msp")
#print(os.mkdir)

files1 = os.listdir("msp")
print(files1)

'''
Running system commands

Finally, the os module provides functions for running system commands.For example, you can
use the os.system function to run a commands and get the output:


'''


SystemCMD = os.system("ls")
print(SystemCMD)

f1 = os.popen("ls")
output1 = f1.read()
print(output1)
print(os.getcwd())





























