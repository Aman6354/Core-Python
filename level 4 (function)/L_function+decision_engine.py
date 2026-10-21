'''Challenge 13 — Functions + Decision Engine

Ab thoda tagda karte hain. Isme sirf calculation nahi, functions ko decision-making ke liye use karna hai.

Ek system banao:

check_eligibility(age, salary)
        ↓
calculate_loan_amount(salary)
        ↓
process_loan(age, salary)

Rules:

check_eligibility(age, salary):
age < 21 → "Not Eligible"
salary < 25000 → "Not Eligible"
otherwise → "Eligible"
calculate_loan_amount(salary):
salary >= 100000 → salary × 5
salary >= 50000 → salary × 3
otherwise → salary × 2
process_loan(age, salary):
pehle eligibility check karo
agar eligible hai → loan amount calculate karo
agar eligible nahi hai → loan amount calculate mat karo
return appropriate result

At least 5 test cases.'''

def check_eligibility(age,salary):
    if age < 21:
        return "Not Eligible"
    elif salary < 25000:
        return "Not Eligible"
    else:
        return "Eligible"

def calculate_loan_amount(salary):
    if salary >= 100000:
        loan = salary * 5
    elif salary >= 50000:
        loan = salary * 3 
    else:
        loan = salary * 2
    return loan


def process_loan(age,salary):
    Eligibility = check_eligibility(age,salary)
    if Eligibility == "Eligible": 
        loan_approval = calculate_loan_amount(salary)
    else:
        loan_approval = 0

    return Eligibility,loan_approval

result1 = process_loan(17,100000)
result2 = process_loan(21,15555)
result3 = process_loan(25,50000)
result4 = process_loan(29,14778546)
result5 = process_loan(36,25642)

print("How much loan you can take",result1)
print("How much loan you can take",result2)
print("How much loan you can take",result3)
print("How much loan you can take",result4)
print("How much loan you can take",result5)


