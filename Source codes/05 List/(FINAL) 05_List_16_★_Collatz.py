n = int(input())

steps = []
steps.append(n)

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = (3 * n) + 1
    
    steps.append(n)

steps = [str(e) for e in steps]

limit = steps[-15:]

out = '->'.join(limit)

print(out)