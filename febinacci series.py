a = 0
b = 1
c = 0
n = int(input("Enter number  :"))
if n<0:
    print("Invalid number")
elif n==0:
    print(a)
elif n ==1:
    print(b)
else:
    for i in range(0,n):
        a=b
        b= c
        c= a+b
        print(c)