'''
Shutil Module in Python

Shutil is a Python module that provides a higher level interface for working with file and
directories. The name "shutil" is short for shell utility. It provides a convenient(آسان )
and efficient way to automate tasks that are commonly performed on files ad directories. In
this repl, we'll take a closer look at the shutil module and its various functions and how
they can be used in Python.


'''
import shutil
import os


'''
Functions

The following are some of the most commonly used functions in the shutil module:



● shutil.copy(src, dst): This function copies the file located at src to a new location
specified by dst. If the destination location already existes, the original file will be
overwritten

● shutil.copy2(src, dst): This function is similar to shutil.copy but it also preserves
(محفوظ کرتا ہے ) more
metadata about the original file, such as the timestamp.

● shutil.copytree(src, dst): This function recursively copies the directory located at src
to a new location specified by dst. If the destination location already exists, the original
directory will be merged with it.

● shutil.move(src, dst) : This function moves the file located at src to a new location
specified by dst. This function is equivalent ot renaming a file in most cases.

● shutil.rmtree(path): This function recursively deletes the directory located at path,
along with all of its contents. This function is similar to using the rm -rf command in a
shell.


'''

# Examples :

'''
Here are some examples of how you can use the shutil module in your Python code:
'''

#Copying a file

shutil.copy("shutil.txt","dest_test.txt")





cwd = os.getcwd()

print("Current working directory: ", cwd)







def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()

current_path()

os.chdir('../')
current_path()







import sys

##print(sys.version)
##
##for line in sys.stdin:
##    if 'q' == line.rstrip():
##        break
##    print(f'Input : {line}')
##
##print("Exit")




##sys.stdout.write('MOhd Suhail')



##def print_to_stderr(*a):
##    print(*a, file = sys.stderr)

##
##print_to_stderr("Mohd Suhail")


##print(sys.path)

##for index , i in enumerate(sys.modules):
##    print(index, i)



print(os.getlogin())




##file = os.open('shutil.txt','O_RDONLY')
##
##print(file)



import platform

print(platform.machine())

print(platform.node())



##for index , i in  enumerate(dir(platform)):
##
##    print(index, i)

##print(platform.re)

##print(os.path)

##fd = os.open('msp.txt', os.O_RDONLY)
##
##
##n = 50
##
##read = os.read(fd,n)
##print(read)
##os.close(fd)
##             



'''
As you can see, the shutil module provies a simple and efficient way to perform common file
and directory- reated tasks in Python. Whether you need to copy, move, delete, or preserve
metadata about files and directories, the shutil moduel has you covered.

In conclusion, the shutil module is a powerful tool for automating file and directory-related
tasks in Python. Whether you are beginner or an experienced Python developer, the shutil
module is an essential toool to have in your toolbox.


'''

# shutil.copy("main.py", "main2.py")
# shutil.copytree(".tutorial", "mytutorial")
# shutil.move(".tutorial/file.file", "file.file")
# shutil.rmtree("mytutorial")
# os.remove("file.file")
































