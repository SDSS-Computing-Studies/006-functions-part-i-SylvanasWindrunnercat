#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""
str = input("The number list is:")

perimeterlist = [int(n) for n in str.split()]

total = sum(perimeterlist)

print(total)