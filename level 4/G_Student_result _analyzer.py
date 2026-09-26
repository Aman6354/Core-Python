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

