#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""
a = float(input("The number is:"))

s = str(a).split('.')

if float(s[1]) == 0:
    print("True")
else:
    print("False")
