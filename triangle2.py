# coding: utf8
"""
Write a program that will ask the user for an integer (the size of the triangle)
and then print an isosceles triangle composed of `*` characters of the given
size. E.g:

Enter the size of the triangle: 3
  *
 ***
*****

"""

# your code here
x=int(input("what size? "))
for i in range(1,x+1):
    print((' '*(x-i))+('*'*i)+('*'*(i-1)))
    
