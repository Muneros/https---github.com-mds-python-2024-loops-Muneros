# coding: utf8
"""
Write a program that prompts the user to enter a password, and then prints
exactly one of the following messages: ‘The password is secure.’ or
‘The password is insecure!’. A secure password must meet the following
conditions:

* have at least one lowercase letter,
* have at least one capital letter,
* have at least one digit.

Examples:

Enter the password: Katar7yna
The password is secure.
Enter the password: catastrophe01
The password is insecure!

"""

# your code here
haslo=input("write your password here")
haslist=list(haslo)
upper=False
lower=False
num=False
i=0
for i in range(len(haslist)):
    if haslist[i]>'a' and haslist[i] <'z':
        lower=True
        continue
    if haslist[i]>'A' and haslist[i] <'Z':
        upper=True
    if haslist[i]>'1' and haslist[i]<'9':
        num=True
if (num==True and upper==True and lower==True):
    print("The password is secure!")
else:
    print("This password insecure")



