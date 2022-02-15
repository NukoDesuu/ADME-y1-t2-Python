import math as m

n = int(input())

points = []
dists = []

for i in range(n):
    inp = input().split()
    
    x_plot = float(inp[0])
    y_plot = float(inp[1])
    
    square = (x_plot ** 2) + (y_plot ** 2)
    dist = m.sqrt(square)

    points.append(str(i+1) + " " + str(x_plot) + " " + str(y_plot))
    dists.append(str(dist))

dists = [float(d) for d in dists]
dists_sorted = sorted(dists)

_3rd = points[dists.index(dists_sorted[2])].split()
_id = _3rd[0]
_x = _3rd[1]
_y = _3rd[2]

out = "#" + str(_id) + ": (" + str(_x) + ", " + str(_y) + ")"
print(out)