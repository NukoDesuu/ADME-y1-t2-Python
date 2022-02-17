def make_int_list(x):
    items = [int(n) for n in x.split()]
    return items

def is_odd(e):
    if e % 2 == 1:
        return True
    return False

def odd_list(alist):
    o_list = []
    for n in alist:
        if is_odd(n) == True:
            o_list.append(n)
    return o_list

def sum_square(alist):
    sq_sum = 0
    for n in alist:
        sq_sum += (n**2)
    return sq_sum

exec(input().strip())