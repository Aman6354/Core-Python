# BMI calculator 

weight = float(input("Enter your weight in kilogram"))
height = float(input("Enter your height in meters"))

bmi = weight / height**2

print("BMI:", bmi)
print("Weight:", weight)
print("Height:", height)