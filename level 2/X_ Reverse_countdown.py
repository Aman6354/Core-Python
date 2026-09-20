'''Concept: Negative Step

range() mein step negative ho sakta hai:

range(10, 0, -1)

Ye generate karega:

10
9
8
...
1
📋 Problem

User se n input lo aur n se 1 tak reverse order mein numbers print karo.

📥 Example
Enter n: 5
📤 Expected Output
5
4
3
2
1'''

user = int(input("Enter the number: "))
for n in range(user,0,-1):
    print(n)