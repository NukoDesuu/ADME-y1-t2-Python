import math as ma




##### INPUT : Receiving inputs from user, then process them to analyze the components #####
num = input()
comp = num.split(",")

# keep in mind that all of these are STRING!!
w = comp[0] # Whole number input
si = comp[1] # Static decimal input, MIGHT BE AN EMPTY STRING
r = comp[2] # Repeating decimal input




##### PROCESS : Troublesome processing zone #####

## Dealing with possible empty string...

s = str(int(bool(si))) + si # bool(si) returns True (1) if exists, False (0) if EMPTY.
# if si ISN'T empty, the string (s) will be "1???" (added "1" on the leftmost side)
# if si IS empty, the string (s) will be "0" (because si itself is empty)

## Analyzing the length and rearranging the data...

n = len(s) # Starting length value (static decimal)
s = str(int(s) % (10**(n-1))) # Fixing (originally) modified string s
# HOW...?
# Since the string s is added leftmost "1" or "0", it must be removed here before further usages.
# s is converted (from string) to an integer first, then "1" is removed by using modulus
# 10**(n-1) came from the concept that the position of removing (n)...
# ...will be one value more than the power of 10 required to do modulus on the right position
# ex. "125" -> len(s) = 3 = n -> ... % 100 == ... % (10**(2)) == ... % (10**(n-1))
## if the string is originally 0, this will return the same result

n = n - 1 # Fixed length value -> the actual length after the data is being fixed (as "1" is removed, or sometimes not)
# This also offset the member value when actually... the data arrived empty
m = len(r) #Inputted repeating decimal length



### Finding true fraction for never ending, REPEATING DECIMAL places (r) ###

r_numerator = int(r) #converts string r to integer
r_denominator = ((10**(m)) - 1) * (10**n) #based on theorem... (try writing on paper)
# for m is the length of repeating decimal and n is the length of the static decimal
# it is found that the way to eliminate the repeating section is to multiply itself (x) by ...
# ... 10 to the power of m, then when subtracting repeated section out...
# ... to be left with static number, the coefficient of x is decreased by 1
# coeffient is moved to the denominator
# in order to match integer state of r, the denominator is multiplied by the 10 to the power...
# ... of n (offsets that make both sides become integer)

r_grcmd = ma.gcd(r_numerator, r_denominator) # finds greatest common divisor for the fraction

# Simplify
r_simple_num = r_numerator // r_grcmd 
r_simple_deno = r_denominator // r_grcmd



### Finding true fraction for FIXED DECIMAL places (s) ###

s_numerator = int(s) #normal decimal compared to unit
s_denominator = 10**n #based on the location of the number from unit place (actually.. the length of input)

s_grcmd = ma.gcd(s_numerator, s_denominator) # finds greatest common divisor for the fraction

# Simplify
s_simple_num = s_numerator // s_grcmd
s_simple_deno = s_denominator // s_grcmd



### Finding the COMBINED FRACTION (r + s) ###

# This is the way we add 2 fractions with different denominators
dec_numerator = (s_simple_num * r_simple_deno) + (s_simple_deno * r_simple_num)
dec_denominator = s_simple_deno * r_simple_deno
# from... sn/sd + rn/rd = [(sn*rd) + (sd*rn)] / [sd*rd]

dec_grcmd = ma.gcd(dec_numerator, dec_denominator) # finds greatest common divisor for the fraction

# Simplify
dec_simple_num = dec_numerator // dec_grcmd
dec_simple_deno = dec_denominator // dec_grcmd

## dec_simple_num will now be numerator for decimal part
## dec_simple_deno will now be denominator for decimal part


### FINALIZE : Finding the TRUE FRACTION OF THE ENTIRE DECIMAL ###

# We have to combine the fraction from decimal part to the whole number given
# let final_num be the finalized numerator
# let final_deno be the finalized denominator

final_num = dec_simple_num + (int(w) * dec_simple_deno)
final_deno = dec_simple_deno




##### OUTPUT : Preparing appropriate outputs #####

print(str(final_num) + " / " + str(final_deno))