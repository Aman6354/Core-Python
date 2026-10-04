def calculate_total(price,quantity):
    total = price * quantity
    return total

def apply_discount(total):

    if total >= 5000:
        discount = total * 0.15
        return discount 
    elif total >= 2000:
        discount = total * 0.10
        return discount
    else:
        print("no discount")


total = calculate_total(1250,5)
final = apply_discount(total)