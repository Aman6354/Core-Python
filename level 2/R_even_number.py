"""Objective

for + range() ke saath step parameter practice karna.

range(start, stop, step) mein step batata hai ki har iteration mein kitna jump karna hai.

Example:

range(2, 11, 2)

→ 2, 4, 6, 8, 10

📋 Problem

User se n input lo aur 1 se n ke beech saare even numbers print karo.

📥 Example
Enter n: 10
📤 Expected Output
2
4
6
8
10"""

user = int(input("Enter the number: "))
for n in range(2,user+1,2):
    print(n)