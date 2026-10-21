'''🏆 analyze_student_marks(marks)

Function ko marks ki list milegi.

Example:

analyze_student_marks([85, 42, 91, 67, 30])

Function ko calculate karke return karna hai:

Total students
Pass students → marks >= 40
Fail students → marks < 40
Highest marks
Lowest marks

Expected:

Total: 5
Pass: 4
Fail: 1
Highest: 91
Lowest: 30
Rules
Function compulsory
Parameter: marks
Loop compulsory
if/else compulsory
return compulsory
Multiple values return karo
Built-in max() / min() use mat karna
Function ko 2 different lists ke saath test karo'''

def analyze_student_marks(marks):

    pass_count = 0
    fail_count = 0
    highest_mark = marks[0]
    lowest_mark = marks[0]

    for mark in marks:

        if mark >= 40:
            pass_count += 1

        elif mark < 40:
            fail_count += 1

        if mark > highest_mark:
            highest_mark = mark
        
        if mark < lowest_mark:
            lowest_mark = mark
    
    return len(marks),pass_count,fail_count,highest_mark,lowest_mark



result = analyze_student_marks([85, 42, 91, 67, 30])


print("Total numbers",result[0])
print("Pass student",result[1])
print("Fail student",result[2])
print("Highest Marks",result[3])
print("lowest Marks",result[4])
     
    
       
    
    
    