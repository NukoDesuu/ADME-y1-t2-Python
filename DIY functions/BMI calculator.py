h = float(input("Please input your height in cm. : "))
w = float(input("Please input your weight in kg. : "))

bmi = round(w / (h / 100)**2, 2)

print("Your BMI is :", bmi)