'''Challenge 12: Function Pipeline

Ab hum functions ko ek doosre ke output ke saath chain karenge. Ye previous questions se genuinely different hai.

Task:

Teen functions banao:

calculate_total(price, quantity)
        ↓
apply_discount(total)
        ↓
final_bill(total_after_discount)

Rules:

calculate_total() → price × quantity return kare.
apply_discount():
total >= 10,000 → 20% discount
total >= 5,000 → 10% discount
total < 5,000 → no discount
discounted amount return kare.
final_bill() → final amount par 18% tax add karke return kare.
Ek process_order(price, quantity) function banao jo teeno functions ko correct order mein call kare.
process_order() sirf final bill return kare.
At least 4 different orders test karo.
input() mat use karna.'''


def calculate_total(price,quantity):
    total = price * quantity
    return total

def apply_discount(total):
    if total >= 10000:
        discount = total * 0.20
    elif total >= 5000:
        discount = total * 0.10
    else:
        discount = 0

    total_after_discount  = total - discount
    return total_after_discount

def final_bill(total_after_discount):
    tax = total_after_discount * 0.18
    final_amount = total_after_discount + tax
    return final_amount

def process_order(price,quantity):
    total = calculate_total(price, quantity)
    total_after_discount = apply_discount(total)
    final_amount = final_bill(total_after_discount)

    return final_amount

result1 = process_order(1000,5)
result2 = process_order(3000,8)
result3 = process_order(5000,6)
result4 = process_order(4000,10)

print("Final Bill",result1)
print("Final Bill",result2)
print("Final Bill",result3)
print("Final Bill",result4)






    
      
    

    
