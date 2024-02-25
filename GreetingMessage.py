import time
# from datetime import datetime


#
# msp = datetime.msp()
#
# currentTime = msp.strf("%h",t)
# print(currentTime)

# now = datetime.now()
#
# current_time = now.strftime("%H:%M:%S")
# print("Currrnt Timr = ", current_time)


t = time.localtime()
l = int(time.strftime("%H"))
print(l)
if(l>=5 and l<=11):
    print("Good Morning MSP")
elif(l>12 and l <17):
    print("Good Afternoon Sir")
elif(l>=17 and l<= 22):
    print("Good Evining")
elif(l>22 & l >=24 & l==1 & l<=4):
    print("Good Night")
else:
    print("Hello Sir")


