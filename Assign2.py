"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

num1 = float(input("enter a number "))
num2 = float(input("enter a number "))

A = input("is one of the numbers the hypotenuse of the right triangle: ")
    
if A == "yes": 
    nmax = max(num1,num2)
    nmin = min(num1,num2)
    B = (nmax **2)
    D = (nmin **2)
    E = (B - D) **0.5
    round(E, 1)
    print(E)
elif A == "no":
    C = ((num1**2) + (num2**2)) ** 0.5
    C = round(C,1)
    print(C)

