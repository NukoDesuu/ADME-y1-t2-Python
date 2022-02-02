inp = input()
d = inp.split()

n = len(d)
p = d[n - 1]
i = -1
j = 0

while j < (n - 1):
    if d[j] <= p:
        i += 1
        d[i], d[j] = d[j], d[i]

    j += 1

d[i], p = p, d[i]

print(d)