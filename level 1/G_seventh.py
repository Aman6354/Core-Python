'''Problem Statement

Write a Python program that:

Asks the user to enter the total number of seconds.
Converts the input using int().
Calculates:
hours
minutes
remaining_seconds
Prints all three values.'''

seconds = int(input("Enter the total no of seconds"))

hours = seconds // 3600
remaining_seconds_after_removing_hours = seconds % 3600

minutes = remaining_seconds_after_removing_hours // 60
remaining_seconds = remaining_seconds_after_removing_hours % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Remaining Seconds:", remaining_seconds)