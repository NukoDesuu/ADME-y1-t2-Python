import math as m

w = float(input())
h = float(input())

Hc_Const = 0.024265
Hc_Wp = 0.5378
Hc_Hp = 0.3964

Boyd_Const = 0.0333
Boyd_Wp = 0.6157 - (0.0188 * m.log10(w))
Boyd_Hp = 0.3

Mosteller_BSA = m.sqrt(w*h) / 60
Haycock_BSA = Hc_Const * (w ** Hc_Wp) * (h ** Hc_Hp)
Boyd_BSA = Boyd_Const * (w ** Boyd_Wp) * (h ** Boyd_Hp)

print(Mosteller_BSA)
print(Haycock_BSA)
print(Boyd_BSA)