user = int(input("Enter the number: "))
evencount = 0
oddcount = 0
evensum = 0
oddsum = 0
number_divisible3 =0

for n in range(1,user+1):
    if n % 3 == 0:
        number_divisible3 += 1
    if n % 2 == 0:
        evensum = evensum + n 
        evencount += 1
    else:
        oddsum = oddsum + n
        oddcount += 1

print("Evencount",evencount)
print("Evensum",evensum)
print("Oddcount",oddcount)
print("Oddsum",oddsum) 
print("Number divisibe by 3:",number_divisible3)   
