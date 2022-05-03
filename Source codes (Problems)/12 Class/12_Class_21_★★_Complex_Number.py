class Complex():
    def __init__(self,a,b):
        self.real = a
        self.imaginary = b

    def __str__(self):
        a = self.real
        b = self.imaginary
        if b == 0:
            sign = ""
            b = ""
        elif b < 0:
            sign = "-"
        else:
            sign = "+"
        return str(a) + sign + str(b) + "i"

    def __add__(self, rhs):
        a1 = self.real
        b1 = self.imaginary
        a2 = rhs.real
        b2 = rhs.imaginary
        return Complex(a1 + a2, b1 + b2)

    def __mul__(self, rhs):
        a1 = self.real
        b1 = self.imaginary
        a2 = rhs.real
        b2 = rhs.imaginary
        
        r = a1 * a2
        
        if b1 != 0 and b2 != 0:
            i = b1 * b2
            r += (i * -1)
            i = (a1 * b2) + (b1 * a2)
        elif not(b1 == 0 and b2 == 0):
            if b1 == 0:
                i = a1 * b2
            else:
                i = b1 * a2
        return Complex(r,i)

    def __truediv__(self, rhs):
        pass

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1: print(c1)
elif t == 2: print(c2)
elif t == 3: print(c1 + c2)
elif t == 4: print(c1 * c2)
else: print(c1 / c2)