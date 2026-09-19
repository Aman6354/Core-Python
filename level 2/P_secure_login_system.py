"""Concept: not

not kisi condition ka result reverse karta hai:

not True   → False
not False  → True

Example:

if not is_verified:
    print("Not verified")
🎯 Objective

User se input lo:

username
password
is_verified (yes / no)

Rules:

Username "admin" AND password "python123" AND verified "yes" → Login Successful
Username/password correct hain but verified "no" → Please verify your account
Username ya password incorrect → Invalid credentials

Case: inputs ko lowercase mein handle karna hai, so "Admin" aur "ADMIN" bhi username admin ke equivalent hone chahiye."""

username = input("Enter the username here: ")
password = input("Enter Password here: ")
is_verified = input("Enter only yes or no: ")

if username.lower() == "admin" and password == "python123":
    
    if not is_verified == "yes":
        print("Please verify your account")
    else:
        print("Login Successful!")

else:
    print("Invalid Credentials!")







# username = input("Enter the username here: ")
# password=input("Enter PAssword here: ")
# is_verified=input("enter only yes or no: ")

# if username.lower()=="admin" and password=="python123" and is_verified=="yes":
#     print("Login SSUccessFull !")
# elif username.lower()=="admin" and password=="python123" and is_verified == 'yes':
#     print("Plese verify your acccount: ")
# else:
#     print("Invelid Credinatial !")

