friend = [("Rechel", 19),
          ("Monica", 18),
          ("Rana",17),
          ("Suhail", 16),
          ("Mohd", 21),
          ("MSP", 20)]


age = lambda friend: friend[1]>=18

for i in friend:
    l = []
    l.append(i[1])
    print(l>=18)
