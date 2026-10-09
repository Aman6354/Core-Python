# program to understand byte type arrary
# create a list of byte numbers 
elements = [10,20, 0, 40 ,15]

#convert the list into bytes type array
x = bytes(elements)

# Retrive elements from x using for loop and display
for i in x: print(i)