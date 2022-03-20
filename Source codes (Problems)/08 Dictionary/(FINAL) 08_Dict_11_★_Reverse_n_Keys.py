def reverse(d):
    reversed_d = {}
    for k,v in d.items():
        reversed_d[v] = k
    return reversed_d

def keys(d, v):
    matches = []
    for dk,dv in d.items():
        if dv == v:
            matches.append(dk)
    return matches

print(keys({3:33, 4:33, 5:55, 2:33}, 9999))