'''Ab sirf Even/Odd nahi. Function ko multiple calculations karwani hain.

analyze_numbers(n)

Function 1 se n tak numbers process karega.

Tumhe calculate karna hai:

Total numbers
Even numbers ki count
Odd numbers ki count
Even numbers ka sum
Odd numbers ka sum

Example:

analyze_numbers(5)

Expected:

Total numbers: 5
Even count: 2
Odd count: 3
Even sum: 6
Odd sum: 9

Because:

Even → 2, 4       → sum = 6
Odd  → 1, 3, 5    → sum = 9
Rules
Function compulsory
for loop
if/else
Counters + sums
return abhi mat use karo
Function ko 2 different values ke saath test karo.'''

def analyze_number(n):
    total_numbers = 0
    even_count = 0
    odd_count = 0
    even_sum = 0
    odd_sum = 0

    for m in range(1,n+1):
        total_numbers += 1
        if m % 2 == 0:
            even_count += 1
            even_sum += m
        else:
            odd_count += 1
            odd_sum += m

    
    return total_numbers, even_count, even_sum, odd_count, odd_sum

a,b,c,d,e = analyze_number(25)



print("Even count",b)
print("Odd count",d)
print("Even sum",c)
print("Odd sum",e)
print("Total count",a)

