import numpy as np

def sum_2_rows( M ):
    two_row_sums = list()
    for i in range(M.shape[0] // 2):
        m = i * 2
        a = M[m]
        b = M[m + 1]
        two_row_sums.append(a + b)
    return np.array(two_row_sums)

def sum_left_right( M ):
    nrow = M.shape[0]
    ncol = M.shape[1]
    half_col = ncol // 2
    sum_rows = list()
    for i in range(nrow):
        row = M[i]
        a = row[:half_col]
        b = row[half_col:]
        sum_rows.append(a + b)
    return np.array(sum_rows)

def sum_upper_lower( M ):
    nrow = M.shape[0]
    half_row = nrow // 2
    sum_rows = list()
    a = M[:half_row]
    b = M[half_row:]
    sum_rows = list()
    for i in range(half_row):
        sum_rows.append(a[i] + b[i])
    return np.array(sum_rows)

def sum_4_quadrants( M ):
    half_row = M.shape[0] // 2
    half_col = M.shape[1] // 2
    # you know... these are QUADRANTS right..? XD
    q1 = M[:half_row, :half_col]
    q2 = M[:half_row, half_col:]
    q3 = M[half_row:, half_col:]
    q4 = M[half_row:, :half_col]
    # Preparing the metrix with all zeros
    a = np.zeros((half_row, half_col), int)
    for i in range(half_row):
        for j in range(half_col):
            # each cell is the sum of 4 quadrants
            a[i,j] = q1[i,j] + q2[i,j] + q3[i,j] + q4[i,j]
    return a

def sum_4_cells( M ):
    cell_rows = M.shape[0] // 2
    cell_cols = M.shape[1] // 2
    p1 = M[::2, ::2]
    p2 = M[::2, 1::2]
    p3 = M[1::2, 1::2]
    p4 = M[1::2, ::2]
    s = np.zeros((cell_rows, cell_cols), int)
    for i in range(cell_rows):
        for j in range(cell_cols):
            s[i,j] = p1[i,j] + p2[i,j] + p3[i,j] + p4[i,j]
    return s

def count_leap_years( years ):
    ch_years = years - 543
    c = 0
    for y in ch_years:
        if (y % 100 != 0 and y % 4 == 0) or (y % 100 == 0 and y % 400 == 0):
            c += 1
    return c

# testcase = np.arange(36).reshape(6,6)
# testcase2 = np.array([2543, 2559, 2560])
# testcase3 = np.arange(16).reshape(4,4)

# print(sum_2_rows(testcase))
# print(sum_left_right(testcase))
# print(sum_upper_lower(testcase))
# print(sum_4_quadrants(testcase))
# print(sum_4_cells(testcase))
# print(count_leap_years(testcase2))

print(sum_4_quadrants(np.arange(-10,54).reshape(8,8)))

# exec(input().strip())