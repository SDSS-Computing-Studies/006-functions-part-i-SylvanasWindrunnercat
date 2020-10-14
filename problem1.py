#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math

def hypotenuse(a, b, c):
    if c == False:
        if a > b:
            d = math.sqrt(a ** 2 - b ** 2)
            return d
        elif b > a:
            d = math.sqrt(b ** 2 - a ** 2) 
            return d
    elif c == True:
        e = math.sqrt(a ** 2 + b ** 2)
        return e

x = hypotenuse(3, 4, True)

print(x)
