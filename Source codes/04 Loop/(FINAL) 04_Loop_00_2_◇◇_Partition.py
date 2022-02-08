d = [int(i) for i in input().split()]

n = len(d)
p = d[-1]
i = -1
j = 0

while j < (n - 1):
    if d[j] <= p:
        i += 1
        d[i],d[j] = d[j],d[i]
    
    j += 1

d[i+1],p = p,d[i+1]

print(d)