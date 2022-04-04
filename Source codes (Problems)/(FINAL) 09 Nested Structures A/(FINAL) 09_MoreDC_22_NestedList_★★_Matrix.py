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
    max_A_columns = len(A[0])
    max_B_columns = len(B[0])
    
    i = 0
    B_transpost = []
    while i < max_B_columns:
        eachTpRow = []
        for rowB in B:
            eachTpRow.append(rowB[i])
        B_transpost.append(eachTpRow)
        i += 1
    
    A_mult_B = []

    for rowA in A:
        rBT = 0
        row_product_element = []
        while rBT < max_B_columns:
            product, e = 0, 0
            while e < max_A_columns:
                product += rowA[e] * B_transpost[rBT][e]
                e += 1
            row_product_element.append(product)
            rBT += 1
        A_mult_B.append(row_product_element)
    
    return A_mult_B

exec(input().strip())