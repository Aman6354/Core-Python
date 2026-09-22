user = int(input("Enter the number: "))
total_count = user
evencount = 0
oddcount = 0 
divisible_by_3 = 0
divisible_by_5 = 0
for n in range(1,user+1):  
    if n % 2 == 0:
        evencount += 1
    else: 
        oddcount += 1

    if n % 3 == 0:
        divisible_by_3 += 1

    if n % 5 == 0:
        divisible_by_5 += 1

    if (n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else: 
        print(n)

print("Evencount",evencount)
print("Oddcount",oddcount)
print("Divisible by 3: ",divisible_by_3)
print("Divisible by 5: ",divisible_by_5)
print("Total count",total_count)