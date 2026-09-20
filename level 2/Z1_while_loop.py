'''Concept

while loop tab tak chalta hai jab tak condition True hoti hai.

Example:

count = 1

while count <= 5:
    print(count)
    count += 1

Output:

1
2
3
4
5

⚠️ while mein condition ko eventually False banana zaroori hai, warna infinite loop ho sakta hai.

🎯 Challenge

User se n input lo.

while loop use karke 1 se n tak numbers print karo.

📥 Example
Enter n: 5
📤 Expected
1
2
3
4
5'''

user = int(input("Enter the number:"))
n = 1
while n <= user:
    print(n)
    n += 1