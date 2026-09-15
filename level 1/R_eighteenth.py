"""Write a Python program that:

Asks the user to enter marks (out of 100) for 5 subjects.
Calculates:
total_marks
percentage = (total_marks / 500) * 100
Prints:
Marks of all 5 subjects
Total Marks
Percentage"""

print("Enter your marks of all 5 subjects")

subject1 = float(input("Enter the marks of first subject"))
subject2 = float(input("Enter the marks of second subject"))
subject3 = float(input("Enter the marks of third subject"))
subject4 = float(input("Enter the marks of fourth subject"))
subject5 = float(input("Enter the marks of fifth subject"))

print("Subject 1:", subject1)
print("Subject 2:", subject2)
print("Subject 3:", subject3)
print("Subject 4:", subject4)
print("Subject 5:", subject5)

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks * 100) / 500

print("Total Marks:", total_marks)
print("Percentage:", percentage)