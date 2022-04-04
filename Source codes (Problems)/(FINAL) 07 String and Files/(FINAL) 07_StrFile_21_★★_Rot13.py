numArr = '0123456789'
lowerAlphaArr = 'abcdefghijklmnopqrstuvwxyz'
upperAlphaArr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

rot13A_upper = upperAlphaArr[:13]
rot13B_upper = upperAlphaArr[13:]

rot13A_lower = lowerAlphaArr[:13]
rot13B_lower = lowerAlphaArr[13:]

lines = []
l = input()
while l != 'end':
    lines.append(l)
    l = input()

rot13Lines = []

for line in lines:
    currl = ''
    for c in line:
        if c in lowerAlphaArr or c in upperAlphaArr:
            if c in rot13A_lower:
                currl += rot13B_lower[rot13A_lower.index(c)]
            elif c in rot13B_lower:
                currl += rot13A_lower[rot13B_lower.index(c)]
            elif c in rot13A_upper:
                currl += rot13B_upper[rot13A_upper.index(c)]
            elif c in rot13B_upper:
                currl += rot13A_upper[rot13B_upper.index(c)]
        else:
            currl += c
    rot13Lines.append(currl)

for l in rot13Lines:
    print(l)