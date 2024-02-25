import os
import time
import platform
from plyer import notification




print(os.name)


print(platform.system())

if platform.system() == "Darwin":
    print("This is a Mac")
elif platform.system() == "Windows":
    print("This is a Windows")
elif platform.system() == "Linux":
    print("This is a lean, mean, Linux machine")

time.sleep(5)
##while True:
##    
####    time.sleep(4)
##    notification.notify(
##            title = "Drink Water ",
##            message = "For healthy individuals, the average daily water for men is about 15.5 cups and for women about 11.5 cups.",
####            app_icon = "image.ico",
##            timeout = 10,
##            )
##    break
##print("loop Break")


if platform.system() == "Linux":

    
    while True:
    
##    time.sleep(4)
        notification.notify(
            title = "Drink Water ",
            message = "For healthy individuals, the average daily water for men is about 15.5 cups and for women about 11.5 cups.",
##            app_icon = "image.ico",
            timeout = 10,
            )
        break

print("You use Different Operating System")

