a = int(input("Enter first  number : \n "))
print("Which operation you want to perform")
operation = input("Enter Operation charator : \n")
b = int(input("Enter Second number : \n "))
if(operation == "="):
    c = a+b
    print(" Your result is : ",c)
elif(operation == "-"):
    c= a-b
    print(" Your result is : ",c)
elif(operation == "*"):
    c = a*b
    print(" Your result is : ",c)
elif(operation == "/"):
    c = a/b
    print(" Your result is : ",c)
else:
    print("Invalid number")