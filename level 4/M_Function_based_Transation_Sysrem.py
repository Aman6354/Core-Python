
privious_balance = 0

def deposit(amount):
    global privious_balance

    if amount > 0:
        privious_balance += amount
        deposite = privious_balance
        return "current Balance: ",deposit 
    else:
        deposit = privious_balance
        return "current Balance: ",deposit

def withdraw(amount):
    global privious_balance

    if 0 > amount >= privious_balance:
        privious_balance -= amount
        withdraw = privious_balance
        return "your current Balance is: ",withdraw
    else:
        withdraw = privious_balance
        return "current Balance",withdraw

def check_balance():
    global privious_balancen ra radh
    balance = privious_balance
    return "Current Balance",balance

def process_account(action, amount = 0):

    if action == "deposit":
        return deposit(amount)
    elif action == "withdraw":
        return withdraw(amount)
    elif action == "check_balance":
        return check_balance()
    else:
        return "Invalid Action"


print(process_account(deposit,1000))
print(process_account(withdraw,510))
print(process_account(check_balance))
print(process_account(deposit,1000))
print(process_account(withdraw,200))
print(process_account("hello"))   
   