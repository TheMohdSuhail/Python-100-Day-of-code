# String are immutable
# Immutable mean We can not cange after decleration
# When we manipulatin with string then python create a new string because String is immutble
a = "Hello World"
print(a.upper())

# rstrip method  removes any trailling character
# traillig character mean " Pichhe ke sabhi character ko remove kar deta hai "

alg = "python!!!!"
print(alg.rstrip("!"))

# replace method is use to replace a string
# syntex of replce string StringName.replce("thereWriteWhichYouChange", "Write a New String "

replaceEx = "Hello World"
print(replaceEx.replace("World", "MSP"))
# String split() method :-  The split() method splits the given string at the specified instace and returns the separated strings as list items.

splitEx = "Split String Example"
print(splitEx.split())

# Capitalize() :- The captalized () method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase
CapitalizeEx = "hello \'MOHD SUHAIL' how are you today"
print(CapitalizeEx.capitalize())

# Center method :- center() method aligns the string to the center as per the parameters given by the user

centerMethodEx = "Welcome to the python Programing"
print(len(centerMethodEx))
print(len(centerMethodEx.center(50)))

# Count method :- count() method return the number of times the given value has occurred within the given string.

countEx = "Mohd Suhail and Mohd Suhail"
print(countEx.count("Mohd Suhail"))

# endswith() :- The endswith()method checks if the string ends with a given value. If yes then return True, else return Flase.
endEx = "Welcome to python World with MSP"
print(endEx.endswith("MSP"))

# Note :- We can overide variable in pthon
# find() :-
# The find() method searches for the first occurrence of the given value and return the index where it is present. If given absent from the string then return -1

findEx = "He's name is Dan. He isan honest man."
print(findEx.find("is"))

# Index() :- The index() method is similar find() method. if value is not found to find() its return -1 Whereas index() method rise an exception
# The index () method searches for the occurrence of the given value and returns the index wher it is present. If given value is absent from the string raise an exception.

indexEx = "If given value is absent from the string raise an exception"
print(indexEx.index("from"))

# isalnum() :- The isalnum() method retun True only if the entire string only consists of A-Z, az, 0-9. If any other characters or punctuations are present, then it returns False
# Note :- If space in between character then return False
isalnumEx = "HelloMohdSuhailKaiseHaiApp"
isalnumEx1= "774"
print(isalnumEx.isalnum())
print(isalnumEx1.isalnum())

# islower() :- The is lower method return True if all the character in the string are lowercase, else returns False.

lowerCaseEx = " HELLO WORLD KAISE HAI APP LOG "
print(lowerCaseEx.islower())

# isprintable() :- The isprintble() method returns True if all the values within the given string are printable, if not then return False
printableEx = "returns True if all the values within the given string are printable, if not then return False"
printableEx2 = "Print backslace n \n"
print(printableEx.isprintable())

print(printableEx2.isprintable())

# isspace() :- The isspace() method returns True only and only is the string contains white spaces, else returns False.
spaceEx = "  "
print(" Is White Space : ", spaceEx.isspace())

# istitle() : The istitle() method return True only if the first letter of each word of the string is capitalized, else it returns Falsse.

title = "Mohd Suhail "
print("Istitle method :",title.istitle())

# swapcase() :- The swapcase()method changes the character casing of the string, Upper case are converted to lower case and lowercase to uppercase

swapcaseEx = "Welcome to the python programmig"
print(swapcaseEx.swapcase())
# title() :-  The title() method capitalizes each letter of the word within the string.
titleEx = "This is title method"
print(titleEx.title())


