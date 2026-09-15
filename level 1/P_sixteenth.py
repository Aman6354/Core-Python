"""Write a Python program that:

Asks the user to enter:
Units of electricity consumed (float)
Assume:
Rate per unit = ₹7.5
Fixed charge = ₹100
Calculate:
energy_charge = units * 7.5
total_bill = energy_charge + 100
Print:
Units
Energy Charge
Fixed Charge
Total Bill"""

units = float(input("Enter the units of electricity consumed"))

rate_per_unit = 7.5 
fixed_charge = 100 

energy_charge = units * 7.5 
total_bill = energy_charge + fixed_charge 

print("Units: ", units)
print("Fixed Charge:", fixed_charge)
print("Energy Charge: ", energy_charge)
print("Total Bill ", total_bill)
