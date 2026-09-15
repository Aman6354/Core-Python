marks = int(input("Enter the marks"))

if marks < 0 and marks > 100:
    grade = "Invalid grade"

elif marks >= 90 and marks <= 100:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else marks < 40:
    grade = "Fail"

print("Marks: ", marks)
print("Grade: ", grade)

