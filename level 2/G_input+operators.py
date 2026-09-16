'''📋 Problem Statement

User se 2 numbers input lo.

Phir print karo:

Addition
Subtraction
Multiplication
Division
Remainder (%)
Example

Input:

Enter first number: 20
Enter second number: 6

Output:

Addition: 26
Subtraction: 14
Multiplication: 120
Division: 3.3333333333333335
Remainder: 2'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

addition = num1 + num2 
print("Addition",addition)
subtraction = num1 - num2 
print("Subtraction",subtraction)
multiplication = num1 * num2
print("Multiplication",multiplication)
division = num1 / num2
print("Division",division)
remainder = num1 % num2 
print("Remainder",remainder)