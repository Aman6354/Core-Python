'''Objective

for + range() + calculation ko combine karna.

📋 Problem

User se ek number lo aur uska 1 se 10 tak multiplication table print karo.

📥 Example Input
Enter number: 7
📤 Expected Output
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70 '''

user = int(input("Enter the number: "))
for n in range(1,11):
    
    print(user, "*" ,n, "=",  user * n)
