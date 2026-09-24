'''New Concept: return

print() sirf result screen par dikhata hai.

return function ka result bahar bhejta hai, jise hum variable mein store karke baad mein use kar sakte hain.

Example:

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

Yahan result ke andar 30 aa jayega.

🏆 Challenge 4 — Return + Calculation

Function banao:

calculate_bill(price, quantity)

Function ko price × quantity ka result return karna hai.

Phir:

Function ko call karo.
Returned value ko ek variable mein store karo.
Us variable ko print karo.
3 different bills calculate karo.
Rules
return compulsory
Function ke andar final result ke liye print() nahi
input() nahi
2 parameters'''


def calculate_bill(price,quantity):
    return  price * quantity

result = calculate_bill(23,75)
result1 = calculate_bill(47,75)
result2 = calculate_bill(34,56)

print(result)
print(result1)
print(result2)

