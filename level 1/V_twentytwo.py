"""We're introducing a new concept: elif.

🎓 Student Grade Calculator

Write a program that:

Takes marks as input.
Prints the grade based on these rules:
Marks	Grade
90–100	A
75–89	B
60–74	C
40–59	D
Below 40	Fail"""


marks = int(input("Enter the marks: "))

if marks < 0 or marks > 100:
    grade = "Invalid marks"
elif marks >= 90 and marks <= 100:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else: 
    grade = "Fail"

print("Marks: ", marks)
print("Grade: ", grade)












