'''Challenge 14 — Function-Based Transaction System

Ab repetitive grade/discount/loan type questions se ek level upar.

Tumhe 3 functions + 1 controller function banana hai.

Functions
deposit(balance, amount)
withdraw(balance, amount)
check_balance(balance)
process_account(balance, action, amount)
Rules

deposit()

amount > 0 → new balance return
otherwise → balance unchanged

withdraw()

amount > 0 AND amount <= balance → new balance return
insufficient balance → balance unchanged

check_balance()

current balance return kare

process_account()

action == "deposit" → deposit() call
action == "withdraw" → withdraw() call
action == "balance" → check_balance() call
koi unknown action → "Invalid Action" return
Test

At least 6 transactions karo, for example:

Starting balance = 10000

deposit
withdraw
withdraw
balance
deposit
unknown action
Important

Is challenge mein main dekhunga ki tum:

input → controller → correct function → return value

ka flow independently handle kar pa rahe ho ya nahi.'''


def deposit(balance, amount):
    if amount > 0:
        balance += amount

    return balance


def withdraw(balance, amount):
    if amount > 0 and amount <= balance:
        balance -= amount

    return balance


def check_balance(balance):
    return balance


def process_account(balance, action, amount=0):

    if action == "deposit":
        return deposit(balance, amount)

    elif action == "withdraw":
        return withdraw(balance, amount)

    elif action == "balance":
        return check_balance(balance)

    else:
        return balance


balance = 10000

balance = process_account(balance, "deposit", 5000)
print("Balance:", balance)

balance = process_account(balance, "withdraw", 2000)
print("Balance:", balance)

balance = process_account(balance, "withdraw", 3000)
print("Balance:", balance)

balance = process_account(balance, "withdraw", 20000)
print("Balance:", balance)

balance = process_account(balance, "balance")
print("Balance:", balance)

balance = process_account(balance, "hello", 500)
print("Balance:", balance)