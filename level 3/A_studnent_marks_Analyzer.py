'''Challenge 1 — Student Marks Analyzer

User se 5 students ke marks input lo aur list mein store karo.

Program ko:

Saare marks print karne hain.
Total marks calculate karne hain.
Average calculate karna hai.
Highest marks find karne hain.
Lowest marks find karne hain.
Kitne students pass hain (marks >= 40) count karo.
Kitne students fail hain count karo.
Example
Enter mark: 85
Enter mark: 32
Enter mark: 91
Enter mark: 47
Enter mark: 25

Marks: [85, 32, 91, 47, 25]
Total: 280
Average: 56.0
Highest: 91
Lowest: 25
Pass: 3
Fail: 2'''

mark1 = int(input("Enter the marks: "))
mark2 = int(input("Enter the marks: "))
mark3 = int(input("Enter the marks: "))
mark4 = int(input("Enter the marks: "))
mark5 = int(input("Enter the marks: "))

count = 0
count_f = 0

marks = [mark1,mark2,mark3,mark4,mark5]
print("Marks: ",marks)
total = mark1 + mark2 + mark3 + mark4 + mark5
print("Total: ",total)
average = total / 5
print("Average: ",average)
highest = max(marks)
print("Highest: ",highest)
low = min(marks)
print("Low: ",low)

for mark in marks:
    if mark >= 40:
        count = count + 1
    else:
        count_f = count_f + 1

print("Pass: ",count)
print("Fail: ",count_f)
