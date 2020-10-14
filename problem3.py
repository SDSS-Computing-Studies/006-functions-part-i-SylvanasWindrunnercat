#! python3
"""
Create a function called factors()
Input parameter is a positive integer
Output is a sorted list containing all of the factors of that number.
Note: A Factor is a positive integer that can be evenly divided
into another number.
Example: The factors of 10 are 1, 2, 5, 10
(2 points)
"""
def factor(a):
    output = []
    i = 2
    while a // i > 0:
        if a % i == 0:
            output.append(i)
            a //= i
        else: i += 1
    return(output)

print(factor(12))
