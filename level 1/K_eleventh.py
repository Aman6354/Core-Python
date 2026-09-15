# salary calculator 

monthly_salary = float(input("Enter your monthly salary"))

annual_salary = monthly_salary * 12
bonus = annual_salary * 0.10
total_income = annual_salary + bonus

print("Monthly Salary:", monthly_salary)
print("Annual Salary:", annual_salary)
print("Total Income:", total_income)
print("Bonus:", bonus)