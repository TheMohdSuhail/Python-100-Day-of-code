'''
readlines() method

The readline() method reads a single line from the file. If we want to read multiple lines,
we can use a loop

'''

#f = open ('msp.py', 'r')
#while True:
 #   line = f.readline()
#    if not line:
        #break
  #  print(line)
    

f = open('myfile.txt','r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in Maths is: {m1}")
    print(f"Marks of student {i} in English is: {m2}")
    print(f"Marks of student {i} in SST is : {m3}")

    print(line)
          


    
'''
The readlines() method reads all the lines of the file and returns them as a list of strings.
---------------------------------------------------------------------------------------------

writelines() method

The writelines() method in Python writes a sequence of strings to a file. The Sequence can
be any iterable object, such as a list or a tuple.

Here's an example of how to use the writelines() method:


'''

#f= open('myfile.txt','w')
#lines = ['line 3\n', 'line 2\n', 'line 3\n']
#f.writelines(lines)
#f.close()


'''
This will write the strings in the lines list to the file myfile.txt. The \n characters are
used to add newline characters to the end of each string.

Keep in mind that the writelines() method does not add newline characters between the strings\
in the sequence. If you want to add newlines between the strings, you can use a loop to
write each string separately:


'''
f1 = open('myfile2.txt', 'w')
lines1 = ['line 1 ', 'line 2', 'line 3']
for line in lines1:
    f1.write(line +'\n')

f2 = open('myfile2.txt', 'r')
print(f2.read())
f1.close()

# It is also a good practice to close the file after you are done with it.









































