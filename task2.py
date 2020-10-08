#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""
str = input("The number list is:")

numberlist = [int(n) for n in str.split()]

numberlist = sorted(numberlist, reverse = True)

print("The largest number is:",numberlist[0])