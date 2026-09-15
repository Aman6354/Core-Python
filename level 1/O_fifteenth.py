"""📋 Problem Statement

A user enters:

Their account balance
The amount they want to withdraw

Rules:

If the withdrawal amount is less than or equal to the balance, print:
Withdrawal Successful
Remaining Balance: ...
Otherwise print:
Insufficient Balance"""


account_balance = float(input("Enter your account balance"))
withdraw_amount = int(input("Enter your withdraw amount"))

remaining_balance = account_balance - withdraw_amount

if account_balance >= withdraw_amount:
    print("Withdraw Successful")
    print("Remaining Balance:", remaining_balance)
else:
    print("Insufficient Balance")