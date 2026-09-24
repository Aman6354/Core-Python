'''Function + Condition

Function banao:

check_number(number)

Function ko ek number milega.

Us number ke basis par:

Agar number positive hai → "Positive"
Agar number negative hai → "Negative"
Agar number 0 hai → "Zero"
Example
check_number(10)

Output:

Positive

Aur:

check_number(-5)

Output:

Negative
Rules
Function mein 1 parameter
if / elif / else use karo
Function ke andar result print karo
return abhi use mat karo
Kam se kam 4 different numbers test karo, including 0.'''

def check_number(number):
    if number >= 1:
        print("positive")
    elif number  < 0:
        print("negative")
    else:
        print("zero")

result = check_number(6745)
result2 = check_number(745)
result3 = check_number(-4345)
result4 = check_number(0)