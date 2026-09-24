'''Problem

User se n input lo.

1 se n tak:

Even numbers ka sum
Odd numbers ka sum
Even numbers ka count
Odd numbers ka count
3 se divisible numbers ka count
5 se divisible numbers ka count
3 aur 5 dono se divisible numbers ka count
1 se n tak ka total sum

End mein sab print karo.

Example

Input:

15

Expected:

Even Sum: 56
Odd Sum: 64
Even Count: 7
Odd Count: 8
Divisible by 3: 5
Divisible by 5: 3
Divisible by both 3 and 5: 1
Total Sum: 120'''

user = int(input("Enter the number: "))
count_divisible_by_3 = 0
count_divisible_by_5 = 0
count_divisible_by_3_5 = 0
oddcount = 0
evencount = 0
evensum = 0
oddsum = 0
total_sum = 0

for n in range(1,user+1):
    if n % 2 == 0:
        evencount += 1
        evensum = evensum + n 
    else: 
        oddcount += 1 
        oddsum = oddsum + n 


    if n % 3 == 0:
        count_divisible_by_3 += 1

    if n % 5 == 0:
        count_divisible_by_5 += 1

    if (n % 3 == 0) and (n % 5 == 0):
        count_divisible_by_3_5 += 1


    total_sum = total_sum + n

print("Even sum: ",evensum)
print("Odd sum: ",oddsum)
print("Even count: ",evencount)
print("Odd count: ",oddcount)
print("Divisible by 3: ",count_divisible_by_3)
print("Divisible by 5: ",count_divisible_by_5)
print("Divisible by 3 and 5: ",count_divisible_by_3_5)
print("Total sum",total_sum)