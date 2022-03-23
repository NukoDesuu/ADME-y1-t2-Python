def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m

def mult_c(c, A):
    results = []
    for row in A:
        row_result = []
        for e in row:
            result = e * c
            row_result.append(result)
        results.append(row_result)
    return results

def mult(A, B):
    max_B_column = len(B[0])
    max_A_row = len(A)
    A_mult_B = []
    for rowA in A:
        B_transpost = []
        i = 0
        products_list = []
        while i < max_B_column:
            product = 0
            B_transpost = []
            for rowB in B:
                B_transpost.append(rowB[i])
            for e in range(max_A_row):
                product += rowA[e] * B_transpost[e]
            print(product)
            products_list.append(product)
            i += 1
        A_mult_B.append(products_list)
    return A_mult_B

print(mult(read_matrix(), read_matrix()))