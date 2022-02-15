a = float(input())

x = a

L = 0
U = 0

if a != 1:
    while x != 0:
        x = x // 10
        U += 1

    x = (L + U) / 2

    while abs(a - 10**x) > ( (10**-10) * max(a,10**x) ):
        if 10**x > a:
            U = x
        else:
            L = x
        x = (L + U) / 2

    out = round(x, 6)
    print(out)
else:
    print(0.0)