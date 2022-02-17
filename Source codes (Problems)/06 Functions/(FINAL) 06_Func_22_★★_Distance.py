import math as m

def distance1(x1, y1, x2, y2):
    d = m.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    return d

def distance2(p1 ,p2):
    d = m.sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )
    return d

def distance3(c1, c2):
    ctr1 = c1[:2]
    rd1 = c1[2]
    ctr2 = c2[:2]
    rd2 = c2[2]
    ovl = False
    cd = m.sqrt( (ctr2[0] - ctr1[0])**2 + (ctr2[1] - ctr1[1])**2 )
    if (rd1 + rd2) >= cd:
        ovl = True
    return cd, ovl

def perimeter(points):
    vrtx = len(points)
    peri = 0
    xi = points[0][0]
    yi = points[0][1]
    xb = xi
    yb = yi
    for i in range(1,vrtx):
        xf = points[i][0]
        yf = points[i][1]
        peri += distance1(xb, yb, xf, yf)
        xb = xf
        yb = yf
    peri += distance1(xi, yi, xb, yb)
    return peri

print(perimeter([[0,0], [0,2], [2,2], [2,0]]))        