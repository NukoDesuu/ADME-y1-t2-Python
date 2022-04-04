def reverse(d):
    reversed_d = {}
    for k,v in d.items(): #use method ".items()" to gather tuples of key, value pair.
        reversed_d[v] = k
    return reversed_d

def keys(d, v):
    matches = []
    for dk,dv in d.items():
        if dv == v:
            matches.append(dk)
    return matches

exec(input().strip())