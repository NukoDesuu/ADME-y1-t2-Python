w = input()
s = input()

cs = ""

for c in s:
    if c.lower() in "abcdefghijklmnopqrstuvwxyz ":
        cs += c
    if c == ".":
        cs += " "

cs = cs.split()

n = 0

for sw in cs:
    if sw == w:
        n += 1

print(n)