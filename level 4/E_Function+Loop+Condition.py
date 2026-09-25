'''number_analysis()

Ek function banao:

number_analysis(n)

Function ko n milega.

Function ke andar 1 se n tak loop chalao.

Har number ke liye:

Even hai → "Even"
Odd hai → "Odd"

Example:

number_analysis(5)

Expected:

1 Odd
2 Even
3 Odd
4 Even
5 Odd
Rules
Function compulsory
Parameter n
for loop use karo
if/else use karo
input() nahi
Abhi return ki zarurat nahi
Function ko 2 different values ke saath call karo.'''

def number_anlysis(n):
    for n in range(1,n+1):
        if n % 2 == 0:
            print(n," ","Even")
        else:
            print(n, " ","odd")

result = number_anlysis(25)


print(result)


# Ek important observation

# Tumne ye likha:

# result = number_anlysis(25)
# print(result)

# Output ke end mein None aayega.

# Kyun?
# Kyuki tumhare function mein return nahi hai. Python mein agar function kuch return nahi karta, to automatically None return hota hai.

# So:

# result = number_anlysis(25)

# mein result ki value None hai.