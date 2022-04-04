def row_number(t, e):
    t_rows = len(t)
    row = 0
    while row < t_rows:
        for item in t[row]:
            if item == e:
                return row
        row += 1

def flatten(t):
    flattened = []
    for row in t:
        for e in row:
            if e != 0:
                flattened.append(e)
    return flattened

def inversions(x):
    items = len(x)
    pairs = []
    for left in range(items):
        for right in range(left+1,items):
            pairs.append([x[left], x[right]])
    counts = 0
    for pair in pairs:
        a = pair[0]
        b = pair[1]
        if a > b:
            counts += 1
    return counts

def solvable(t):
    num_of_rows = len(t)
    num_of_inversions = inversions(flatten(t))
    row_with_zero = row_number(t, 0)

    def isEven(n): return n % 2 == 0
    def isOdd(n): return not(isEven(n))
    
    if ( isOdd(num_of_rows) and isEven(num_of_inversions) ) or ( isEven(num_of_rows) and ( ( isOdd(num_of_inversions) and isEven(row_with_zero) ) or ( isEven(num_of_inversions) and isOdd(row_with_zero) ) ) ):
        return True
    return False

exec(input().strip())