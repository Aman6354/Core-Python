password = input("Enter the password:")
print("password should contain at least one uppercase,one lowercase,one special character,numbers,underscore and at least it's length >= 8 ")
length: 0
uppercase: 0
lowercase: 0
digits: 0
spaces: 0
special_character: 0

for ch in password:
    if ch >= "A" and ch <= "Z":
        print(password.upper())
    elif ch >= "a" and ch <= "z":
        print(password.lower())
    elif ch >= "0" and ch <= "9":
        digits += 1
    else:
        print(ch)
    
    



