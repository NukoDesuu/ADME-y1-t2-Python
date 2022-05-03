h = float(input("Please input your height in cm. : "))
b = float(input("Your desired BMI value : "))

w = round(((h / 100)**2 ) * b, 2)

print("Your weight (kg.) for this BMI value is :", w)