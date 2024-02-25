from datetime import datetime
import time



now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Currrnt Timr = ", current_time)
t = time.localtime()
localtimeEx = time.strftime("%I:%M:%p",t)
localtimeEx2 = time.strftime("%d/%m/%y")
print(localtimeEx)
print(localtimeEx2)

