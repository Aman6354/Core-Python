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

