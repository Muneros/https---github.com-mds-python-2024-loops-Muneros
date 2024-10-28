# coding: utf8
"""
Write a program that prompts user to enter some text and prints the number
of CAPITAL LETTERS on the screen. E.g:

Enter text: Data Science is SUPER!
7

"""

# your code here
num=0
st=input("enter your message ")
nap=list(st)
i=0
for i in range(len(nap)):
    if nap[i]>='A' and nap[i]<='Z':
        num+=1
        i+=1
        continue
    else:
        i+=1
        continue
print (num)
