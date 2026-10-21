'''Challenge 16 — Shopping Cart Flow

2 functions banao:

calculate_total(price, quantity)
apply_discount(total)

Rules:

calculate_total()

price × quantity return kare.

apply_discount()

total >= 5000 → 15% discount
total >= 2000 → 10% discount
otherwise → no discount
final discounted amount return kare.

Phir:

total = calculate_total(...)
final = apply_discount(total)

At least 4 different orders test karo.'''

def calculate_total(price,quantity):
    total = price * quantity
    return total

def apply_discount(total):

    if total >= 5000:
        print("15% Discount")
        discount = total * 0.15
        final = total - discount
        return final
    elif total >= 2000:
        print("10% Discount")
        discount = total * 0.10
        final = total - discount
        return final
    else:
        print("no discount")
        return total
        


total = calculate_total(510,5)
final = apply_discount(total)

print("Total: ",total)
print("Final: ",final)