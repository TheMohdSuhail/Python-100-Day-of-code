from gtts import gTTS

from playsound import playsound

lst =[]
while True:
    n = input("Enter Name: \n")
    name = "Shoutout to " +n
    lst.append(name)

    choice = input("Want to enter more? \n1. Yes\n2. No\n")
    if choice == "2":
        break
    elif choice == "1":
        pass
    else:
        raise ValueErro("Invalid Input Try Again")
txt = ""

for i in lst:
     txt += (i+" ")


myobj = gTTS (text = txt, lang='ur', slow= False)

myobj.save("shoutout.mp3")
source = playsound('shoutout.mp3')

x = input("Enter any key to stop:")
