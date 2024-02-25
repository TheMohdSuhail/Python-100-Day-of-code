'''
Tut 40 & 47 


Write a python progaram to transtlate a message into secret code language.

Wse the rules below to translate normal English into secret code language


Coding :

If the word conatains atleast 3 characters, remove the first letter and append
it at the end now append three random characters at the starting and the end else:
simply reverse the string


Decoding:

if the word contains less then 3 characters, reverse it else: remove  random characters
from start and end. Now remove the last letter and append it to the beginning


Your program should ask whether you want to code or decode



'''

import string
import random
'''
res2 = ''.join(list(map(chr, [random.randint(65,122) for _  in range(3)])))

N=3
res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

print(str(res))


st = input("Enter message \n ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding\n")
coding = True if(coding=="1")else False
print(coding)
if (coding):
    nwords = []
    for word in words:
        if (len(word)>=3):
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            res2 = ''.join(list(map(chr, [random.randint(65,122) for _  in range(3)])))

            stnew = res+ word[1:]+ word[0] +res2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
        print(''.join(nwords))

else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(''.join(nwords))





'''

N=3
res = ''.join(random.choices(string.ascii_letters ,k=N))

M=3
res2 = ''.join(random.choices(string.ascii_letters, k=M))
print(res,res2)

st = input("Enter message\n")
words = st.split(" ")
coding = input(" 1 for Coding or ) for Deoding \n")
coding = True if (coding == "1") else False
if(coding):
    nwords = []
    for word in words:
        
        if(len(st)>=3):
           st = st[1:] + st[0]
           #print(st)
          # r1 = "dsf"
          # r2 = "jkr"
          # st = res + st[1:] + st[0] + res2
           #print(st)
           stnew = res+ word[1:] + word[0] + res2
           nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" " .join(nwords))
            


else:
    nwords = []
    for word in words:
        if(len(word)>=3):
           stnew = word[3:-3]
           stnew = stnew[-1] + stnew[:-1]
           nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
        






            
