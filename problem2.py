#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math
def distance(a,b,c,d):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = (a ** 2 - c ** 2)
    e = math.sqrt(math.sqrt(e ** 2))
    f = (b ** 2 - d ** 2)
    f = math.sqrt(math.sqrt(f ** 2))
    g = math.sqrt(e ** 2 + f ** 2)
    return g

i = input("The number1 is:")
j = input("The number2 is:")
k = input("The number3 is:")
l = input("The number4 is:")

x = distance(i,j,k,l)

round(x, 3)

print(x)
