import math as ma

di = ""
d = str(int(bool(di))) + di

r = "0"

print("***Start of the program***\n")

n = len(d)
d = str(int(d) % (10**(n-1)))
n = n - 1
m = len(r)

print("Static decimal length : " + str(n) + " (" + d + ")")
print("Repeating decimal length : " + str(m) + " (" + r + ")")

r_numerator = int(r)
r_denominator = ((10**(m)) - 1) * (10**n)

r_grcmd = ma.gcd(r_numerator, r_denominator)

r_simple_num = r_numerator // r_grcmd
r_simple_deno = r_denominator // r_grcmd

print("\nFraction numerator for repeating decimal : " + str(r_numerator))
print("Fraction denominator for repeating decimal : " + str(r_denominator))
print("\nThe greatest common devisor for both of them : " + str(r_grcmd))
print("\nSimplified repeating decimal numerator : " + str(r_simple_num))
print("Simplified repeating decimal denominator : " + str(r_simple_deno))

d_numerator = int(d)
d_denominator = 10**n

d_grcmd = ma.gcd(d_numerator, d_denominator)

d_simple_num = d_numerator // d_grcmd
d_simple_deno = d_denominator // d_grcmd

print("\nFraction numerator for static decimal : " + str(d_numerator))
print("Fraction denominator for static decimal : " + str(d_denominator))
print("\nThe greatest common devisor for both of them : " + str(d_grcmd))
print("\nSimplified static decimal numerator : " + str(d_simple_num))
print("Simplified static decimal denominator : " + str(d_simple_deno))

dec_numerator = (d_simple_num * r_simple_deno) + (d_simple_deno * r_simple_num)
dec_denominator = d_simple_deno * r_simple_deno

dec_grcmd = ma.gcd(dec_numerator, dec_denominator)

dec_simple_num = dec_numerator // dec_grcmd
dec_simple_deno = dec_denominator // dec_grcmd

print("\nCombined decimal numerator : " + str(dec_numerator))
print("Combined decimal denominator : " + str(dec_denominator))
print("\nthe greatest common devisor for both of them : " + str(dec_grcmd))
print("\nSimplified combined numerator : " + str(dec_simple_num))
print("Simplified combined denominator : " + str(dec_simple_deno))


