"""Write a Python program that:

Takes input for:
length (float)
width (float)
cost_per_square_meter (float)
Calculates:
area = length * width
total_cost = area * cost_per_square_meter
Prints:
Length
Width
Area
Cost Per Square Meter
Total Cost"""

length = float(input("Enter the length"))
width = float(input("Enter the width "))
cost_per_square_meter = float(input("Enter the cost per square meter"))

area = length * width 
total_cost = area * cost_per_square_meter

print("Length: ", length)
print("Width: ", width)
print("Cost Per Square Meter: ", cost_per_square_meter)
print("Area: ", area)
print("Total Cost: ", total_cost)
