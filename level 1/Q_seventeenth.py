"""Write a Python program that:

Asks the user to enter the prices of 3 items using float.
Calculates:
subtotal = sum of all three prices
gst = 18% of subtotal
grand_total = subtotal + gst
Prints:
Item 1 Price
Item 2 Price
Item 3 Price
Subtotal
GST
Grand Total"""

item_1 = float(input("Enter the price of first item"))
item_2 = float(input("Enter the price of second item"))
item_3 = float(input("Enter the price of third item"))


subtotal = item_1 + item_2 + item_3 
gst = 18/100 * subtotal 
grand_total = subtotal + gst 

print("Item 1: ", item_1)
print("Item 2: ", item_2)
print("Item 3: ", item_3)
print("Gst ", gst)
print("Sub Total ", subtotal)
print("Grand Total: ", grand_total)  