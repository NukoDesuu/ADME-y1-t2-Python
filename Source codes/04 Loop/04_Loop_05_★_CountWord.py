w = input()
s = input()

cs = s.split()

print(cs)

n = 0

for sw in cs:
    if sw == w:
        n += 1

print(n)