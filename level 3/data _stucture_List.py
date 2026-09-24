#  A LIST IS A DATA STUCTURE USE TO STORE MULTIPLE VALUES IN ONE VARIABLE 
# 
# EXAMPLE 
list_name = [10, 20, "RAHUL"  "ROHIT"  "ROHINI" , 67, 9.6]
print(list_name)

# EXPLANATION 
# LIST ARE WRITTEN USING SQUARE BRACKETS[].
# LIST ITEM ARE SEPRATED BY COMMAS.
# LIST ARE ORDER SO EVERY ITEM HAS AN INDEX.
# LISTS ARE MUTABLE, MEANNG WE CAN CHANGE THEM AFTER CREATATION.
# LIST CAN STORE DUPLICATE VALUES.
# LIST CAN STORE DIFFERENT DATA TYPE TOGETHER.

# CREATING LIST 
list_name = [12, 5.6, "king", "aman", 53234, 758.875 ]

# A LIST CAN BE STORE STRINGS, VALUE, NUMBERS, BOOLEAN, OR MIXED VALUES 
# AN EMPTY LIST CAN ALSO BE CREATED 
# LIST ARE USEFUL WHEN MANY RELATE VALUED NEED TO BE STORE TOGETHER 

# ACCESSING VALUES 
 
student = [ "Aman","Rohit","Sunderam","shukla"]
print(student[0])
print(student[2])
print(student[3])
print(student[-1])

# LIST ITEMS ARE ACCESSED USING INDES NUMBER 
# INDEX STATRS FORM 0
# POSITIVE NDEX STARTS FROM LEFT SIDE  WHILE NEGETIVE INDEX STRATS FROM RIGHT SIDE.
  
# UPDATING VALUES 

numbers = [12, 23, 34, 4545, 56.5, 45]
numbers[0:5:1] = [78,57,75,75,4,7,4.87]
print(numbers)

# LIST METHODS
# append()
# Adds one item at the end 
numbers.append(40)
# adds 40

# extend()
# Adds mutiple items 
numbers.extend([50,60])
# adds 50, 60

# insert()
# Adds items at specific index
numbers.insert(1,15)
# adds 15 at index 1

# remove()
# Removes first matching value
numbers.remove(78)
# removes 23

# pop()
# Remove item by index 
numbers.pop(2)
# removes item at index 1

# index()
# Return index of value 
numbers.index(4)
# gives position

# count
# count occurrences 
numbers.count(6)
# count of 5

# sort()
# sorts list 
numbers.sort()
# ascending order

# reverse()
# reverse list 
numbers.reverse()
# reverse order

# copy()
# creates shallow copy 
new = numbers.copy()
# new list copy 

# clear()
# removes all items 
numbers.clear()
# empty list 

