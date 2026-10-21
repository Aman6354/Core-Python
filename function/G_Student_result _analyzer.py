'''Student Result Analyzer

Function banao:

student_result(name, marks)

Function ko name aur marks milenge.

Function ke andar:

Marks ke basis par grade determine karo:

Marks	Grade
90–100	A
75–89	B
60–74	C
40–59	D
Below 40	F

Phir function ko name + grade return karna hai.

Example:

result = student_result("Aman", 82)
print(result)

Expected:

Aman B
Rules 🔥
Function compulsory
2 parameters
if / elif / else
return compulsory
input() nahi
Function ko at least 4 students ke saath test karo
Marks 0–100 ke andar hi rakho'''




def student_result(name,marks):
        if marks >= 90 and marks <= 100:
            return name,'A'
        elif marks  >= 75 and marks <= 89:
            return name,"B"
        elif marks >= 60 and marks <= 74:
            return name,"C"
        elif marks >= 40 and marks <= 59:
            return name,"D"
        else:
            return name,"F"

result1 = student_result("Aman",85)
result2 = student_result("Raman",97)
result3 = student_result("Mohan",75)
result4 = student_result("Sohan",35)


print(result1)
print(result2)
print(result3)
print(result4)

