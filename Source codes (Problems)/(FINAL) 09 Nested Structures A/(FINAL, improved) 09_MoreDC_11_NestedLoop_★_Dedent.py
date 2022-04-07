import string


n = int(input())

i = 0
lines = []

while i < n:
    lines.append(input())
    i += 1

leading_spaces = []

for line in lines:
    dis,k,out = 0,0,0
    while k < len(line) and out != 1:
        if line[k] == ".":
            dis += 1
        else:
            out = 1
        k += 1
    leading_spaces.append([line,dis])

modified = []

for l in leading_spaces:
    string = l[0]
    sep = l[1]
    if sep != 0:
        old = string
        mod = old[sep:]
        final = ("." * int(sep // 2)) + mod
    else:
        final = string
    modified.append(final)

for o in modified:
    print(o)