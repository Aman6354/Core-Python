
privious_balance = 0

def deposit(amount):
    global privious_balance

    if amount > 0:
        privious_balance += amount
        deposite = privious_balance
        return "New Balance: ",deposit 
    else:
        privious_balance += amount
        deposit = privious_balance
        return "Unchanged Balance: ",deposit

def withdraw(amount):
    global privious_balance

    if amount >= 0:
        privious_balance -= amount
        withdraw = privious_balance
        return "New Balance",withdraw
    else:
        withdraw = privious_balance
        return "New Balance",withdraw

def check_balance():
    global privious_balance

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
   