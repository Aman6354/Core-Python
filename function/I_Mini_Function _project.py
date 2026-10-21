'''🏆 number_analyzer(n)

Function ko ek number n milega.

1 se n tak process karke calculate karo:

Total numbers
Even count
Odd count
Even sum
Odd sum
Numbers divisible by 3
Numbers divisible by 5
Example
number_analyzer(10)

Expected values:

Total: 10
Even: 5
Odd: 5
Even Sum: 30
Odd Sum: 25
Divisible by 3: 3
Divisible by 5: 2
Rules 🔥
Function compulsory
for loop
if/elif/else
Counters
Sums
return all 7 values
Function ko 2 different numbers ke saath test karo
input() nah'''

def number_observer(n):
    
    total_numbers = 0
    even_count = 0
    odd_count = 0
    even_sum = 0
    odd_sum = 0
    number_divisible_by_3 = 0
    number_divisible_by_5 = 0

    for n in range(1,n+1):
        total_numbers += 1  
        if n % 2 == 0:
            even_count += 1
            even_sum += n
        else:
            odd_count += 1
            odd_sum += n

        if n % 3 == 0:
            number_divisible_by_3 += 1

        if n % 5 == 0:
            number_divisible_by_5 += 1


    return total_numbers, even_count, odd_count, even_sum, odd_sum, number_divisible_by_3, number_divisible_by_5

result = number_observer(25)

print("Total:",result[0])
print("Even:",result[1])
print("Odd:",result[2])
print("Even sum:",result[3])
print("Odd sum:",result[4])
print("Divisible by 3:",result[5])
print("divisible by 5:",result[6])
