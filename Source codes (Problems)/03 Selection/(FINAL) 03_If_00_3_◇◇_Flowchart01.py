inp = input()
ints = inp.split(" ")

a = int(ints[0])
b = int(ints[1])
c = int(ints[2])
d = int(ints[3])

if a > b:
    a,b = b,a
    if d >= a:
        if c > d:
            c = c - a
    else:
        c = c + a
    b = a + c + d

else:
    
    if c > a >= b:
        d = d + a
    
    if d > c:
        b = b + 2
    else:
        b = 2 * b

print(str(a) + " " + str(b) + " " + str(c) + " " + str(d))