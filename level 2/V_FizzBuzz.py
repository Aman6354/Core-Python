'''Problem

1 se n tak loop chalao.

Har number ke liye:

Number 3 aur 5 dono se divisible → print "FizzBuzz"
Sirf 3 se divisible → print "Fizz"
Sirf 5 se divisible → print "Buzz"
Otherwise → number print karo
📥 Example
Enter n: 15
📤 Expected Output
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz'''

user = int(input("Enter the number: "))
for n in range(1,user+1):
    if (n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz") 
    elif n % 3 == 0:
        print("Fizz")       
    else:
        print(n)