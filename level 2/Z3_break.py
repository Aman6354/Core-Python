'''Concept: break

break loop ko immediately stop kar deta hai.

Example:

while ...:
    if condition:
        break

Jaise hi break execute hota hai, loop khatam.

🎯 Challenge

User se n input lo.

1 se n tak numbers print karo, lekin jaise hi 5 aaye, loop stop ho jaye.

Example

Input:

10

Output:

1
2
3
4
5

Agar input 3 ho:

1
2
3'''

user = int(input("Enter the number: "))
n = 0
while n <= user:
    n += 1 
    print(n)
    if n == 5:
        break
