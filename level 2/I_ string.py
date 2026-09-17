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
Lowercase: python'''

user = input("Enter your string: ")

print("Original:", user)
print("Length:", len(user))
print("Uppercase:", user.upper())
print("Lowercase:", user.lower())