"""
Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print("\r")
for i in range(4,0,-1):
    for j in range(0,i):
        print("*",end="")
    print("\r")