"""Write a Python program that:

Asks the user to enter:
Number of tickets (int)
Price per ticket (float)
Calculates:
total_cost = number_of_tickets * ticket_price
Prints:
Number of Tickets
Ticket Price
Total Cost"""

ticket = int(input("Enter the number of tickets"))
price = float(input("Enter the price per ticket"))
total_cost = ticket * price 

print("Ticket: ", ticket)
print("Price: ", price)
print("Total_cost: ", total_cost)  