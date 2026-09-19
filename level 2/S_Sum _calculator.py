'''Problem

User se n input lo aur 1 se n tak ke numbers ka total sum calculate karke print karo.

📥 Example
Enter n: 5
📤 Expected Output
Sum: 15

Because:

1 + 2 + 3 + 4 + 5 = 15'''

user = int(input("Enter the number: "))
sum = 0
for n in range(1,user+1):
    sum = sum + n

print("result: ",sum)        
    

     
    
