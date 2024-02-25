'''
Loops in python
Sometimes we wents to execute a group of statement a certain number of times. This can be done using loops. Based on this loops are furture classfied into following types.
1. for loop
2. while loop
3. nested loop'

For loops :- for loop is used whenever we know the number of iterations

While loops :- while loop is used whenever we don't know the of iterations.
But we know the know the stoping condtion.
'''

for i in range(1,11):
    print(i)

while True:
    username = input("Enter username: \n")
    password = (input("Enter password: \n"))
    if(username == "themsp" and password == 8650 ):
        print("Login successfully")
        break
    else:
        print("Incorrect user id or password try again!")