'''Objective

if / elif / else + comparison + logical operators ko combine karna.

📋 Problem

User se:

age
is_member — "yes" ya "no"
is_verified — "yes" ya "no"

input lo.

Rules:

Age 18 or above AND member yes AND verified yes → "Access Granted"
Age 18 or above, but membership/verification incomplete → "Limited Access"
Age below 18 → "Access Denied"
📥 Example Input
Enter age: 22
Are you a member? yes
Are you verified? yes
📤 Expected Output
Access Granted'''

age = int(input("Enter the age hare: "))
if age < 18:
    print("Access Denied")

else:
    is_member = input("Are you member:")
    is_verified = input("Are you verified:")
        
    if is_member == "yes" and is_verified == "yes":
           print("Access Granted")
    else: 
        print("Limited Access")                 
       
    