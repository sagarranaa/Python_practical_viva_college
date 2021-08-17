"""
4.b) Write a python program to print a specified list after removing the 0th,2nd,4th and 5th
elements
Coding:-
"""
color=["Red","Green","White","Black","Pink","Yellow"]

color1=[]

for i,x in enumerate(color):
    if i in (0,4,5):
        continue
    color1.append(x)

print(color1)

