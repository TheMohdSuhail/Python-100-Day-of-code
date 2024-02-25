'''if-else Statements
Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or Falsse. If the expression evaluate to
False, then the program executd to True.
Based on this the conditional statements are further clssified into following types:
if
of-else
id-else-elif
nested if-else-elif

'''


a = int(input("Enter your age : "))
print("Your age is : ",a)

if(a>18 and a<=50):
    print("You can drive car")
elif(a<=17):
    print("You can not drive a car ")
elif(a>50):
    print("Your age is\'",a,"\'Please stay home")

else:
    print("Enter a valid number")

