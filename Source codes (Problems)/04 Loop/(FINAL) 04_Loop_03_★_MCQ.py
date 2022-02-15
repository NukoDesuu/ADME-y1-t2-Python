c = [a for a in input()]
s = [b for b in input()]

cn = len(c)
sn = len(s)

if sn < cn:
    print("Incomplete answer")
else:
    p = 0
    for i in range(cn):
        if s[i] == c[i]:
            p += 1
    
    print(p)