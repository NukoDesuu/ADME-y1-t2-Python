import numpy as np

def toCelsius(f):
    return (f - 32) * (5 / 9)

def BMI( wh ):
    rows = wh.shape[0]
    bmis = [(wh[i][0] / (wh[i][1] / 100)**2) for i in range(rows)]
    return np.array(bmis)

def distanceTo(p, Points):
    p_counts = Points.shape[0]
    dis_list = [ ( (Points[i][0] - p[0])**2 + (Points[i][1] - p[1])**2 )**0.5 for i in range(p_counts)]
    return np.array(dis_list)

exec("x=toCelsius(np.array([-100, 0, 32, 50.5, 212]))\nprint(type(x))\nfor e in x:\n print(round(e,6))")