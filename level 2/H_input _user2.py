'''Input + Type Conversion

Ab ek important real-world situation.

input() se 3 values lo:

Name
Age
Salary

Requirements:

Name → str
Age → int
Salary → float

Phir print karo:

Name: Aman
Age: 22
Salary: 45000.50
Rules
input() mandatory
Correct type conversion mandatory
if / loops / functions nahi
Salary ko float banana hai, int nahi.

No hint. First attempt.'''


name = input("Enter the name: ")
print("Name",name)
age = int(input("Enter the age: "))
print("Age",age)
salary = float(input("Enter the salary: "))
print("Salary",salary)