'''Objective

1 se n tak numbers analyze karo.

Har number ke liye:

Agar even hai → Even
Agar odd hai → Odd
Agar 3 se divisible hai → DivBy3
Agar 5 se divisible hai → DivBy5
Agar 3 aur 5 dono se divisible hai → DivByBoth

Saath mein calculate karo:

Even sum
Odd sum
Divisible-by-3 count
Divisible-by-5 count
Divisible-by-both count
Total sum
📥 Example Input
10
📤 Expected classification
1 - Odd
2 - Even
3 - Odd DivBy3
4 - Even
5 - Odd DivBy5
6 - Even DivBy3
7 - Odd
8 - Even
9 - Odd DivBy3
10 - Even DivBy5
Final output
Even Sum: 30
Odd Sum: 25
Divisible by 3: 3
Divisible by 5: 2
Divisible by both 3 and 5: 0
Total Sum: 55'''

user = int(input("Enter the number: "))
evensum = 0
oddsum = 0
div_by_3 = 0
div_by_5 = 0
div_by_both = 0
total_sum = 0
evencount = 0
oddcount = 0
for n in range(1,user+1):
    if n % 2 == 0:
        evensum = evensum + n
        evencount += 1
        print(n,"-","Even",end=" ")
        if (n % 3 == 0) and (n % 5 == 0):
            print("div_by_both") 
        elif n % 3 == 0:
            print("div_by_3")
        elif n % 5 == 0:
            print("div_by_5")
        else:
            print()

    else:
        oddsum = oddsum + n
        oddcount += 1
        print(n,"-","Odd",end=" ")
        if (n % 3 == 0) and (n % 5 == 0):
            print("div_by_both") 
        elif n % 3 == 0:
            print("div_by_3")
        elif n % 5 == 0:
            print("div_by_5")
        else:
            print()
       
        

    if n % 3 == 0:
        div_by_3 += 1 

    if n % 5 == 0:
        div_by_5 += 1
        

    if (n % 3 == 0) and (n % 5 == 0):
        div_by_both += 1
      
    total_sum = total_sum + n
    
print("Oddcount",oddcount)
print("Evencount",evencount)
print("Even sum: ",evensum)
print("Odd sum: ",oddsum)
print("Divisible-by-3 count: ",div_by_3)
print("Divisible-by-5 count: ",div_by_5)
print("Divisible-by-both count: ",div_by_both)
print("Total sum: ",total_sum)


# optimize_code

# n = int(input("Enter n: "))

# even_sum = 0
# odd_sum = 0

# div3_count = 0
# div5_count = 0
# both_count = 0

# total_sum = 0

# for i in range(1, n + 1):

#     total_sum += i

#     # Even / Odd
#     if i % 2 == 0:
#         result = "Even"
#         even_sum += i
#     else:
#         result = "Odd"
#         odd_sum += i

#     # Divisibility
#     if i % 3 == 0 and i % 5 == 0:
#         result += " DivByBoth"
#         both_count += 1

#     elif i % 3 == 0:
#         result += " DivBy3"
#         div3_count += 1

#     elif i % 5 == 0:
#         result += " DivBy5"
#         div5_count += 1

#     print(i, "-", result)


# print("\nFinal Output")
# print("Even Sum:", even_sum)
# print("Odd Sum:", odd_sum)
# print("Divisible by 3:", div3_count)
# print("Divisible by 5:", div5_count)
# print("Divisible by both 3 and 5:", both_count)
# print("Total Sum:", total_sum)