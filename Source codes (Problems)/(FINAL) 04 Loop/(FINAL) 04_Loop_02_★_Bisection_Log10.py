a = float(input())

if a == 1:
    print(0.0)
else:
    L = 0
    U = a
    
    x = (L + U) / 2

    while abs(a - 10**x) > ( (10**-10) * max(a,10**x) ):
        if 10**x > a:
            U = x
        else:
            L = x
        x = (L + U) / 2
    
    out = round(x, 6)
    print(out)