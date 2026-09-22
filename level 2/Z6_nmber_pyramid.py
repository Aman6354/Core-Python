'''Number Pyramid

User se n input lo aur nested loops se ye pattern generate karo.

Input:

Enter n: 5

Output:

1
12
123
1234
12345'''

user = int(input("Enter the number: "))
for i in range(user+1):
    for j in range(1,i+1):
        
        print(j, end = " ")
        
    print()      