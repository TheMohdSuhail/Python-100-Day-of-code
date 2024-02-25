import platform
import schedule
import time
from  plyer import notification

system = platform.system()


title = "This is notification form msp"
message = " This message form Mohd Suhail, im persuring b.tech in DBUU dehradun and completed diploma in CSE "
notification.notify(
    title= title,
    message = message,
    timeout = 5
    )

for index ,a in enumerate(dir(notification)):
    print(index, a)
