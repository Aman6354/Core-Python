''' tke input from user and print
Even numbers ka sum ✅
Odd numbers ka sum ✅
Even numbers ka count ✅
Odd numbers ka count ✅

'''

user = int(input("Enter the input: "))
evensum = 0
oddsum = 0
evencount = 0
oddcount = 0

for n in range(1,user+1):
    if n % 2 == 0:
        evensum = evensum + n
    else:
        oddsum = oddsum + n
    if n % 2 == 1:
        oddcount += 1
    else:
        evencount += 1       
                

print("Evencount",evencount)
print("Evensum",evensum) 
print("Oddcount",oddcount)
print("Oddsum",oddsum)       
        

# improvement 
# if n % 2 == 0:
#     evensum += n
#     evencount += 1
# else:
#     oddsum += n
#     oddcount += 1