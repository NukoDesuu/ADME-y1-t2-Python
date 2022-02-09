inp = input()

ini = inp[0]
out = ""
n = 0

for c in inp:
    if c == ini:
        n += 1
    else:
        out += (str(ini) + " " + str(n))
        n = 0
        ini = c
        n += 1
        out += " "

out += (str(ini) + " " + str(n))

print(out)

#I'll explain later...