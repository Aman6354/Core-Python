'''Problem

User se n input lo.

while loop use karke 1 se n tak ke even numbers print karo.

📥 Example
Enter n: 10
📤 Expected Output
2
4
6
8
10'''

user = int(input("Enter the number: "))
n = 0
while n < user:
    n += 1
    if n % 2 == 0:
        print(n)


