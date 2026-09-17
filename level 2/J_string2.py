'''Problem Statement

User se ek string input lo.

Phir:

Original string print karo.
String ki length print karo using len().
String ko uppercase mein print karo.
String ko lowercase mein print karo.
📥 Example Input
Enter a word: Python
📤 Expected Output
Original: Python
Length: 6
Uppercase: PYTHON
Lowercase: python
⚠️ Important

in case-sensitive hai.

Isliye "python" ko search karne se pehle sentence ko lowercase karna useful hoga.

Rules
input()
.upper()
.lower()
in
len()'''

user = input("Enter the input here: ")

print("Uppercase:",user.upper())
print("Lowercase:",user.lower())
print("contains Python:",("python" in user.lower()))
print("Length:", (len(user)))