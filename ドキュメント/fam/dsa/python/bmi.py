def cal_bmi(weight, height):
    return round(weight / height**2, 2)

w = float(input("Enter weight (kg): "))
h = float(input("Enter height (m): "))

print("BMI Calculator:")
bmi = cal_bmi(w, h)
print("Your BMI is:", bmi)

if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 25:
    print("You are normal weight")
elif 25 <= bmi < 30:
    print("You are overweight")
else:
    print("You are obese")
