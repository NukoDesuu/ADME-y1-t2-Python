import math as m

numerator = m.pi - (m.factorial(10) / (8**8)) + (m.log(9.7, m.e)**((7/m.sqrt(71)) - m.sin((40/360) * (2*m.pi))))
denominator = 1.2**(2.3**(1/3))

ans = numerator / denominator

out = round(ans, 6)

print(out)