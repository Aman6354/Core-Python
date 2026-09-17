'''Take marks as user input:

Enter marks: 72

Then use these rules:

Marks	Grade
90-100	A
75-89	B
60-74	C
40-59	D
Below 40	F'''

marks = int(input("Enter your marks here: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75 and marks <= 89:
    print("Grade B")
elif marks >= 60 and marks <= 74:
    print("Grade C")
elif marks >= 40 and marks <= 59:
    print("Grade D")
else:
    print("Grade F") 
   