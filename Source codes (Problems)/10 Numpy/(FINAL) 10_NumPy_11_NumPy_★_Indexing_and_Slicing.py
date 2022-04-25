import numpy as np

# A is a 2D array

def get_column_from_bottom_to_top(A, c):
    return A.T[c, ::-1]

def get_odd_rows(A):
    return A[1::2]

def get_even_column_last_row(A):
    return A[A.shape[0] - 1, ::2]

# A is a square matrix

def get_diagonal1(A):
    final = [A[i][i] for i in range(A.shape[0])]
    return np.array(final)

def get_diagonal2(A):
    final = [A[i][A.shape[0] - (i + 1)] for i in range(A.shape[0])]
    return np.array(final)

A = np.array( [[1,2,3],[4,5,6],[7,8,9]] )
print(get_diagonal2(A))