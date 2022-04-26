import numpy as np

def p(x):
    return np.array([1 / (1 + np.e**-( -3.98 + (0.1 * x[i][0]) + (0.5 * x[i][1]) ) ) for i in range(x.shape[0])])

exec(input().strip())