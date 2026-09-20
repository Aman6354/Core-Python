'''Concept: continue

continue current iteration ko skip karta hai, lekin loop ko completely stop nahi karta.

Example:

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

Output:

1
2
4
5

3 skip hua, loop continue raha.

🎯 Challenge

User se n input lo.

1 se n tak numbers print karo, lekin 5 ko skip karo.

📥 Example
Enter n: 8
📤 Expected
1
2
3
4
6
7
8
'''

user = int(input("Enter the number:"))
n = 0
while n < user:
    n += 1
    if n == 5:
        continue
    print(n)