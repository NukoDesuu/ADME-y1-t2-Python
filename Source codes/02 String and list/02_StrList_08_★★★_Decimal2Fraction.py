import math as ma

##### INPUT : Receiving inputs from user, then process them to analyze the components #####
num = input()
comp = num.split(",")

w = comp[0] # Whole number input
di = comp[1] # Static decimal input, MIGHT BE AN EMPTY STRING
r = comp[2] # Repeating decimal input

##### PROCESS : Troublesome processing zone #####

## Dealing with possible empty string...

d = str(int(bool(di))) + di # bool(di) returns True (1) if exists, False (0) if EMPTY.
# if di ISN'T empty, the string (d) will be "1???" (added "1" on the leftmost side)
# if di IS empty, the string (d) will be "0" (because di itself is empty)

print("***Start of the program***\n")

## Analyzing the length and rearranging the data...

n = len(d) # Starting length value
d = str(int(d) % (10**(n-1))) # Fixing (originally) modified string d
# HOW...?
# Since the string d is added leftmost "1" or "0", it must be removed here before further usages.
# d is converted (from string) to an integer first, then "1" is removed by using modulus
# 10**(n-1) came from the concept that the position of removing (n)...
# ...will be one value more than the power of 10 required to do modulus on the right position
# ex. "125" -> len(d) = 3 = n -> ... % 100 == ... % (10**(2)) == ... % (10**(n-1))
## if the string is originally 0, this will return the same result

n = n - 1 # Fixed length value -> the actual length after the data is being fixed (as "1" is removed, or sometimes not)
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

### OUTPUT : Preparing appropriate outputs ###