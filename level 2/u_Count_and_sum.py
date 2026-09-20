'''Objective

Loop ke andar multiple variables maintain karna.

📋 Problem

User se n input lo.

1 se n tak:

Numbers ka sum calculate karo.
Even numbers kitne hain unka count karo.

Finally dono print karo.

📥 Example
Enter n: 10
📤 Expected Output
Sum: 55
Even Count: 5'''

user = int(input("Enter the number: "))
sum = 0
even = 0
for n in range(1,user+1):
    sum = sum + n
    if n % 2 == 0:
        even = even + 1


print(sum)
print(even)
    