"""Movie Ticket Booking System

Rules:

Ticket price = ₹200
If age is below 12, give 50% discount.
Otherwise, charge full price.
Print:
Ticket Price
Discount
Final Price

⚠️ Challenge Rule: Try to solve it without asking for hints first."""


ticket_price = 200

age = int(input("Enter your age"))

if age < 12:
    print(" 50 percent discount")
    discount = 50/100 * ticket_price
    final_price = ticket_price - discount
else:
    print("full payment")
    final_price  = ticket_price
    discount = 0
print("Ticket Price: ", ticket_price)
print("Discount: ", discount)
print("Final price: ",final_price)