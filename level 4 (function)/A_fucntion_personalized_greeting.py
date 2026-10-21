'''Function with Parameters

Parameter ka matlab: function ko bahar se data dena.

Example:

def greet(name):
    print("Hello", name)

greet("Aman")
greet("Ravi")

Yahan name parameter hai, aur "Aman" / "Ravi" arguments hain.

🏆 Challenge 2 — Personalized Greeting

Ek function banao:

greet_user(name, age)

Function ko call karne par output kuch aisa ho:

Hello Aman
You are 22 years old

Phir 2 different users ke liye function call karo.

Rules
input() use nahi karna.
Function mein 2 parameters hone chahiye.
Dono parameters ko output mein use karna.'''

def greet_USER(name,age):
    print("Hello",name)
    print("you are",age,"year old")

greet_USER("Aman",21)
greet_USER ("Rohit",21)   