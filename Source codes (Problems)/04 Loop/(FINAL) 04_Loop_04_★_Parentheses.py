inp = str(input())

r = ""

for e in inp:
    if e not in "()[]":
        r += e
    else:
        if e == "(":
            r += "["
        if e == "[":
            r += "("
        if e == ")":
            r += "]"
        if e == "]":
            r += ")"

print(r)