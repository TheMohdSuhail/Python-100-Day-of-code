'''
Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png


'''
# Solution

import os

files = os.listdir("images")
i = 1 
for file in files:

    if file.endswith(".png"):
        
        print("Before Rename :",file)
        

        #print(os.path.abspath(file)) print path
        os.rename(f"images\{file}", f"images\{i}.png")
        i = i + 1
        print("After Rename : ",file)
