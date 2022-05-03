age = int(input("Please input your age : "))
weight = float(input("Please input your weight in kg. (decimal is optional) : "))

kg_per_pound = 0.45359237

a = 2.2

if age > 55:
    b = 30
elif 30 <= age <= 55:
    b = 35
else:
    b = 40

c = 28.3

water_required_ounces = (( (weight / kg_per_pound) / a) * b) / c

ml_per_ounce = 29.5735296

water_required_ml = water_required_ounces * ml_per_ounce

ml = round(water_required_ml)
l = round(ml / 1000, 1)

print()
print("You required {0} ml of water (about {1} liters.)".format(ml, l))
