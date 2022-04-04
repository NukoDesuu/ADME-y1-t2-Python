numArr = '0123456789'
lowerAlphaArr = 'abcdefghijklmnopqrstuvwxyz'
upperAlphaArr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def SpecialRemoveString(s):
    removed = []
    temp = ''
    for c in s:
        if c in numArr or c in lowerAlphaArr or c in upperAlphaArr:
            temp += c
        else:
            removed.append(temp)
            temp = ''
    if temp != '':
        removed.append(temp)
    return removed

def emptyElementRemove(l):
    nonEmpty = []
    for e in l:
        if e != '':
            nonEmpty.append(e)
    return nonEmpty

def ShiftLetter(c, f):
    if f == 'lower' and c not in lowerAlphaArr:
        cout = lowerAlphaArr[upperAlphaArr.index(c)]
    elif f == 'upper' and c not in upperAlphaArr:
        cout = upperAlphaArr[lowerAlphaArr.index(c)]
    else:
        cout = c
    return cout

phrase = input()
normalWords = SpecialRemoveString(phrase)
polishedWords = emptyElementRemove(normalWords)

wordn = len(polishedWords)

camelWords = []

for k in range(wordn):
    cword = polishedWords[k]
    cwordl = len(cword)
    fl = cword[0]
    rest = cword[1:cwordl]
    restLower = ''
    
    out = ''
    if fl not in numArr:
        for c in rest:
            restLower += ShiftLetter(c, 'lower')
        if k == 0:
            for c in cword:
                out += ShiftLetter(c, 'lower')
        elif fl not in upperAlphaArr:
            fl = ShiftLetter(fl, 'upper')
            out = fl + restLower
        else:
            fl = ShiftLetter(fl, 'lower')
            out = fl + restLower
    else:
        out = fl + rest
    camelWords.append(out)

camelPhrase = ''.join(camelWords)

print(camelPhrase)