'''
Given:

text = "PYTHON"
🎯 Task

Slicing ka use karke print karo:

"PYT"
"HON"
"YTH"
"PYTHON" ko reverse karo → "NOHTYP"
📤 Expected Output
PYT
HON
YTH
NOHTYP'''

word = "PYTHON"
print(word[0:3])
print(word[-3:])
print(word[1:4])
print(word[::-1]) 

# NOTE: [::1] MEANS READ THE STRING FROM RIGHT TO LEFT 
