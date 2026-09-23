'''Challenge — Smart Number Analyzer
🎯 Objective

Ek hi loop mein classification + counters + sums + special conditions handle karni hain.

📋 Problem

User se n input lo.

1 se n tak har number ke liye:

Even/Odd identify karo.
Agar number 3 aur 5 dono se divisible hai → FizzBuzz
Sirf 3 se divisible → Fizz
Sirf 5 se divisible → Buzz
Otherwise → number print karo.

Saath mein calculate karo:

Even count
Odd count
Even sum
Odd sum
Divisible by 3 count
Divisible by 5 count
Divisible by both count
FizzBuzz numbers ka sum
Normal numbers ka sum — jo 3 ya 5 se divisible nahi hain
📥 Example

Input:

15
📤 Expected classification
1 - Odd
2 - Even
3 - Odd Fizz
4 - Even
5 - Odd Buzz
6 - Even Fizz
7 - Odd
8 - Even
9 - Odd Fizz
10 - Even Buzz
11 - Odd
12 - Even Fizz
13 - Odd
14 - Even
15 - Odd FizzBuzz
📊 Final output
Even Count: 7
Odd Count: 8

Even Sum: 56
Odd Sum: 64

Divisible by 3: 5
Divisible by 5: 3
Divisible by both: 1

FizzBuzz Sum: 15
Normal Numbers Sum: 45'''

user = int(input("Enter the number: "))
evencount = 0 
oddcount = 0
evensum = 0 
oddsum = 0 
div_by_3 = 0
div_by_5 = 0 
div_by_both = 0
fizzbuzz_sum = 0
nor_sum = 0

for i in range (1,user+1):
    if i % 2 == 0:
        evensum += i
        evencount += 1
        result = " " "Even"
      
       
    else:           
        oddsum += i
        oddcount += 1
        result =  " " "Odd"
       
      
    if i % 3 == 0:
        div_by_3 += 1
        result += " " "Fizz" 


    if i % 5 == 0:
        div_by_5 += 1
        result += " " "Buzz"

    if (i % 3 == 0) and (i % 5 == 0):
        fizzbuzz_sum  += i
        div_by_both += 1

    if (i % 3 != 0) and (i % 5 != 0):
        nor_sum = nor_sum + i

    print(i , "-" , result )


print("Even count",evencount)
print("oddcount",oddcount)
print("Even sum",evensum)
print("Odd sum",oddsum)
print("divisible by 3 count",div_by_3)
print("divisible by 5 count",div_by_5)
print("divisible by both count",div_by_both)
print("FizzBuzz number's sum",fizzbuzz_sum)
print("Normal Sum",nor_sum)