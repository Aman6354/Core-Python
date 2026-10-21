'''Challenge 11 — Grade + Student Analysis

Do functions banao:

Function 1:

get_grade(marks)

Ye sirf grade return kare:

90+ → A
75–89 → B
60–74 → C
40–59 → D
below 40 → F

Function 2:

student_result(name, marks)

Ye get_grade(marks) ko andar se call kare aur return kare:

name, grade

Example:

student_result("Aman", 85)

Expected:

("Aman", "B")
Rules
2 functions compulsory
student_result() ke andar get_grade() call hona chahiye
return use karo
At least 5 students test karo
input() nahi'''

def get_grade(marks):
    if 90 <= marks <= 100:
        return "A"
    elif 75 <= marks <= 89:
        return "B"
    elif 60 <= marks <= 74:
        return "C"
    elif 40 <= marks <= 59:
        return "D"
    else:
        return "F"

def student_result(name,marks):
    grade = get_grade(marks)

    return ((name,grade))

result1 = student_result("Aman",97)
result2 = student_result("Rohan",52)
result3 = student_result("Mohan",45)
result4 = student_result("Sohan",45)
result5 = student_result("Kiran",14)



print(result1)
print(result2)
print(result3)
print(result4)
print(result5)




    