"""Write a Python program that:

Asks the user to enter:
Distance traveled (in kilometers) using float
Time taken (in hours) using float
Calculates:
average_speed = distance / time
Prints:
Distance
Time
Average Speed"""

distance = float(input("Enter the distance traveled in km"))
time = float(input("Enter the time taken by distance"))

average_speed = distance / time 

print("Distance: ", distance)
print("Time: ", time)
print("Average speed: ", average_speed)
   